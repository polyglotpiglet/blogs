# GC

## Throughput GC

- parallel not concurrent
- major and minor gcs (ie all of them) are stop the world
- uses adaptive sizing to meet performance goals

### Adaptive Sizing

`-XX:MaxGCPauseMillis`

By default this flag isn't set. It applies to both major and minor GCs. 

`-XX:GCTimeRatio`

In terms of GC, throughput is the amount of time spent executing application code. 1-throughput is the time spent in GC. 

<div style="text-align:center"><img src ="throughputgoalEquals.png" /></div>

GCTimeRatio's default value is 19. This means that the application will spend x19 the amount of time in application code as it does running gc (ie 95% throughput). 



## CMS

There are 3 main CMS acitivies in the GC process: 

1. Stop-the-world young gen collection
2. Concurrent old gen GC (with a couple of little phases where it needs to stop-the-world)
3. Full GC (hopefully don't have to do this much)

By default permgen collection requires a full GC. This can be changed with `XX:+CMSPermGenSweepingEnabled`. Note that by default unreferenced classes aren't GC'd from permgen and given that class metadata is most of what is in permgen, you probably want to override that behaviour. Use the flag `-XX:+CMSClassUnloadingEnabled`. 

### Concurrent Mode Failure

When this happens, the garbage collector has to switch from doing a concurrent GC to a stop-the-world GC. It occurs when the tenured space is full (ie concurrent GC failed to collect objects quickly enough from the old gen).   

### Promotion Failure

This happens when tenured space has enough memory for objects, but because of fragmentation they cannot be moved there. Therefore a full GC with compaction occurs. 

To get around these failures, you could make the heap bigger, or make the CMS process trigger more frequently. There are two flags to consider: `-XX:UseCMSInitiatingOccupancyOnly` and `-XX:CMSInitiatingOccupancyFraction`

By default `-XX:UseCMSInitiatingOccupancyOnly` is false. When it is true `-XX:CMSInitiatingOccupancyFraction` is 70 which means that the concurrent old gen GC is triggered when the old gen is 70% full. Reducing this threshold means that the GC starts earlier so had more time to GC the tenured space, hopefully making concurrent mode failures less probable. 

You can tune the `-XX:CMSInitiatingOccupancyFraction` by turning off  `-XX:UseCMSInitiatingOccupancyOnly` and checking when concurrent mode failures occur. The GC log contains all of this information. 


## G1

G1 has a lot of regions (by default 2048). Some of them are eden, some survivor spaces, some old generation. Empty regions aren't assigned to any particular GC space. The general idea is that the garbage collector will prioritise clearning out regions with a lot of garbage. 

Four main operations: 

1. Young gen collection: triggered when eden is full. After a young GC, none of the regions are assigned to eden (ie eden is empty). 
2. A background concurrent scan which marks regions containing lots of garbage. 
3. Mixed GS: This does both normal young gen collections and collects some of the marked old gen regions.  
4. 	Full GC which is triggered when bad things that happen. 

### Bad things that might happen which result in full GC

1. Concurrent mode failure: when the GC starts a marking phase to decide what regions are full and need to be emptied, but the old gen fills up before the marking is finished. 
2. Promotion failure: Marking is done and the mixed GC is in progress. However during the mixed GC lots of stuff is moved from young to old gen and the old gen fills up faster than the mixed GC can empty it. 
3. Evacuation failure: During a young GC, there isn't enough space for the promoted stuff in the surivor spaces and old gen. 
4. Humongous allocation failure: When a really big object is allocated. If a full GC is triggered randomly, this is probably the cause. It's not logged clearly in the GC log. 

Tune G1 with `-XX:MaxGCPauseMillis=N` and let it decide all the complicated stuff itself (ratio of size of young gen to size of old gen, frequency of G1 collections). By default this flag is set to 200ms. 

To set number of GC threads use `ParallelGCThreads` and `ConcGCThreads`. 

To make the GC run earlier use `XX:InitiatingHeapOccupancyPercent=N`. The default is 45 so when the heap is 45% full (across all generations) a GC will be triggered. 