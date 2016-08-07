# Parallel Streams

We have been trying to analyse and improve performance in our application and as part of that we have been considering the use of parallel streams in Java. 

This post will discuss some of the things to be wary of when using parallel streams. 

## Contents
1. What is a parallel stream?
2. Potential issues with parallel streams:
	* Size of the underlying collection
	* Type of the underlying collection
	* ForkJoinPool

## What is a parallel stream?

A parallel stream is just like a normal stream in java except that is uses the fork join framework to divide the stream into chunks and operate on the chunks concurrently. Often using a parallel stream can improve performance of your stream operations but, as we will see in the following examples, it's not as simple as switching every `stream()` in your code to `parallelStream()`. 

## 1. Size of the underlying collection

Intuitively, it's clear that if we have a very small collection, eg two elements, and we split it into chunks and submit these chunks to a fork join pool (or let a parallelStream submit it to a fork join pool for us) than it is likely to perform more slowly than if we had just executed our operation twice sequentilaly, due to the overhead of assigning the work to threads etc.

Let's see this in a concrete example:

``` java
public class StreamDoc {

    @State(Scope.Thread)
    public static class StreamState {

        int n = 1000000;

        List<Long> longs;
        @Setup
        public void setup() {
            Supplier<List<Long>> supplier = LinkedList::new;
            this.longs = LongStream.range(0, n)
            	.boxed()
            	.collect(Collectors.toCollection(supplier));
        }
    }

    @Benchmark
    @BenchmarkMode(Mode.AverageTime)
    @OutputTimeUnit(TimeUnit.MILLISECONDS)
    public void cat(StreamState state) {
        return state.longs.parallelStream()
       	 	.map(x -> x * x)
       	 	.mapToLong(x -> x)
       	 	.sum();
    }

    public static void main(String... args) throws RunnerException {

        Options opt = new OptionsBuilder()
                .forks(1)
                .warmupIterations(5)
                .measurementIterations(20)
                .build();

        new Runner(opt).run();

    }
}
```


I have executed this benchmark several times with different values of n, and for each n I have run it with longs.stream() and longs.parallelStream(). 

The results are in the following tables. All the times are in seconds. 


***

n = 100\_000 

| | min | avg | max |  stdev |
| ------------- | ------------- | ------------- | ------------- | ------------- | 
| **stream()** | 1.460 | 1.826 | 2.028 | 0.149
| **parallelStream()** | 0.559 | 0.680| 0.796 | 0.060

Woohoo, parallel stream behaves as it should and improves the performance. 

***

n = 10\_000 

| | min | avg | max |  stdev |
| ------------- | ------------- | ------------- | ------------- | ------------- | 
| **stream()** | 0.125 | 0.151 | 0.203 | 0.022
| **parallelStream()** | 0.082 | 0.094 | 0.107 | 0.007

Still got a definite performance benefit with the parallel stream. 

***


n = 1\_000 

| | min | avg | max |  stdev |
| ------------- | ------------- | ------------- | ------------- | ------------- | 
| **stream()** | 0.014 | 0.015 | 0.018 | 0.001
| **parallelStream()** | 0.023 | 0.024 | 0.026 | 0.001

Now with only 1000 elements using the parallel stream is a bit slower than with the sequential stream. 

***


n = 100 

| | min | avg | max |  stdev |
| ------------- | ------------- | ------------- | ------------- | ------------- | 
| **stream()** | 0.002 | 0.002 | 0.002 | 0.001
| **parallelStream()** | 0.017 | 0.019 | 0.020 | 0.001

Wow it's about x10 slower!

***

  
## 2. Type of the underlying collection

I ran the n = 1\_000\_000 test again twice. Both times with the parallelStream. The difference between the two runs was that the first time was like the original where the underlying collection is a `LinkedList` but for the second run I changed to an `ArrayList`.  

| | min | avg | max |  stdev |
| ------------- | ------------- | ------------- | ------------- | ------------- | 
| **LinkedList** | 8.073 | 8.186 | 8.427 | 0.098
| **ArrayList** | 2.988 | 3.245 | 3.994 | 0.248

 As we can see, the `ArrayList` is considerably quicker. This is mostly because splitting an `ArrayList` into chunks can be done with _O(1)_ time complexity, but splitting a `LinkedList` is _O(n)_.

## 4. ForkJoinPool

Parallel stream execution use the default forkJoinPool which means that unless you do something about it all your `.parallelStream()` usages within an application will use the same underlying thread pool. Imagine if you were to do the following? 

```java
blah.parallelStream().map(v -> longBlockingCall(v))
```

You will block the threads and potentially slow down some completely different part of your application!

A way round it is described in [this](http://stackoverflow.com/questions/21163108/custom-thread-pool-in-java-8-parallel-stream) stack overflow thread. 
  
  
