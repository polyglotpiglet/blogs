# Dropwizard Metrics Timers Deep Dive

## Contents

## Introduction

Dropwizard metrics offers a number of different measuring tools: gauges, counters, histograms, meters and timers. A timer is simply a histogram of the duration of a particular operation and a meter of the rate at which the operation is called. This post will focus on timers (and by extension histograms and meters). 

## Theory

### Quick Recap of Percentiles

The nth percentile is the value below which n% of the numbers fall. 

Let's say that we have ten numbers:

```
[5,5,3,7,7,8,9,2,1,2]
```
To calculate the 90th percentile of the numbers we first sort them: 

```
[1,2,2,3,5,5,7,7,8,9]
```

Then we can see that the numbers up to 8 are within the 90th percentile. 

### Selective Samping with Dropwizard

With small examples like the one above we can easily compute percentiles but in the real world we cannot hope to store and analyse our entire data collection. Therefore, as timer values are generated, we store only a subset of the total data set that is representative of the whole. This subset is known as a reservoir and in dropwizard metrics there are a number of strategies for choosing the reservoir. We will examine these in turn and look at how our metrics differ when using different reservoir sampling techniques. 

## Setting up our example

I have created one endpoint using dropwizard:

> dropwizard code

Eg

> output from get in browser/curl

Importantly, we want to generate some load for our http service and run the same fixed load for n minutes with each metric configuration. The load test is written in gatling:

> gatling

## Reservoir sampling with Dropwizard

1. **Exponentially Decaying Reservoir**
	



### Uniform Reservoir

**What**

If you use a uniform reservoir to generate your samples for a histogram, then the data that is sampled is representative of the data as a whole. It is probably the most intuative reservoir sampling algorithm. 

For example, consider the set we saw earlier:

```
Set S = [1,2,2,3,5,5,7,7,8,9]
```
Now take a uniformly sampled subset of S

```
Subset S' = [1,2,5,7,9]
```

In both of these sets: 

* Min = 1
* Median = 5
* 90th Percentile = 9
* Max = 9

**How**

There are several straightforward algorithms for uniformly sampling from a dataset which are trivial when the size of the dataset is known upfront. Of course, our metrics are being generated over time and we don't want to wait until we have stopped our application before we can see our percentiles etc! 

JS Vitter of Brown University in the US developed an algorithm in 1985 for exactly this case - optimal uniform sampling of a dataset when its total size, N, is not known upfront. The paper on this algorithm can be found [here](http://www.cs.umd.edu/~samir/498/vitter.pdf).

**Example**



**When to use it**

A Uniform Reservoir is suitable when you want to understand your how your application performed in general over a period of time. It is not suitable for production support and monitoring because it doesn't show recent changes, but would be very useful if you wanted to report on your application's general performance. 





