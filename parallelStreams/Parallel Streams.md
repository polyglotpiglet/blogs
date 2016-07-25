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
        state.longs.parallelStream()
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

The results are in the following tables. 


***

n = 10\_000\_000

| | min | avg  | max |  stdev |
| ------------- | ------------- | ------------- | ------------- | ------------- | 
| **stream()** | 162.489 | 174.841 | 202.039 | 8.740
| **parallelStream()** | 140.750 | 148.792 | 155.405 | 3.693

Yay, as expected the parallel stream performs better. 

***

n = 1\_000\_000


| | min | avg | max |  stdev |
| ------------- | ------------- | ------------- | ------------- | ------------- | 
| **stream()** | 8.021 | 8.684 | 9.400 | 0.427
| **parallelStream()** |  8.010 | 8.075 | 8.246 | 0.058

Parallel stream is a still definitely faster. 

***

n = 100\_000 

| | min | avg | max |  stdev |
| ------------- | ------------- | ------------- | ------------- | ------------- | 
| **stream()** | 0.761 | 0.846 | 0.955 | 0.055
| **parallelStream()** | 0.746 | 0.772| 0.854 | 0.028

Still looking good

***

n = 10\_000 

| | min | avg | max |  stdev |
| ------------- | ------------- | ------------- | ------------- | ------------- | 
| **stream()** | 0.062 | 0.065 | 0.071 | 0.003
| **parallelStream()** | 0.071 | 0.081 | 0.092 | 0.007

Uh oh - for 10_000 longs the parallel stream is slower. 

***


n = 1\_000 

| | min | avg | max |  stdev |
| ------------- | ------------- | ------------- | ------------- | ------------- | 
| **stream()** | 0.005 | 0.006 | 0.007 | 0.001
| **parallelStream()** | 0.023 | 0.024 | 0.026 | 0.001

Now with only 1000 elements using the parallel stream takes about x4 as long as the sequential execution. 

***
  
## Type of the underlying collection

## ForkJoinPool

 
  
  
