# The Second Chance algorithm

The algorithm works as follows:

Second chance is an extension of FIFO: when a page is pulled off the head of the queue, 
the accessed (A) bit is examined. If it's 0, the page is swapped out, else the bit is cleared 
and the page is reinserted at the tail of the queue. A second examination of the queue 
will produce available pages. 

Total page hits and page faults are given at the end of the run.

We assume a "working set" of 3 pages in this demonstration.
