"""
author: Konrad Dagiel 120329501
"""

class Page:
    """
    Pages have an id and an accessed bit
    """
    def __init__(self, id, accessed=1):
        self._id=id
        self._accessed=accessed
    def __str__(self):
        return "id: "+str(self._id)+" A= "+str(self._accessed)

#initialize variables
numberOfFrames=3 #size of working set
pagehits=0 #total page hits
pagefaults=0 #total page faults
pointer=0 #points to which of the frames is being targeted

p0=Page(0)
p1=Page(1)
p2=Page(2)
p3=Page(3)
p4=Page(4)
p5=Page(5)
p6=Page(6)
p7=Page(7)

requestList=[p7,p0,p1,p2,p0,p3,p0,p4,p2,p4,p0,p3,p2] #order in which requests come through

frameList=[] #the working set of pages

"""
Second chance is an extension of FIFO: when a page is pulled off the head of the queue, 
the accessed (A) bit is examined. If it's 0, the page is swapped out, else the bit is cleared 
and the page is reinserted at the tail of the queue. A second examination of the queue 
will produce available pages. 

Total page hits and page faults are given at the end of the run.
"""

for _ in range(numberOfFrames):
    #populate frame list with dummy processes
    frameList.append(Page(-1, 0))


for i in requestList:
    #page hit! make accessed bit 1, to give it a "second chance"
    if i in frameList:
        if i._accessed==0:
            i._accessed=1
        print("page hit")
        pagehits+=1
    #page fault!
    else:
        print("page fault")
        pagefaults+=1
        added=False
        while added==False:
            #make accessed bit 0 if its 1, move pointer
            if frameList[pointer]._accessed==1:
                frameList[pointer]._accessed=0
                pointer+=1
                #pointer loops around if it goes off the list
                if pointer>numberOfFrames-1:
                    pointer=0

            if frameList[pointer]._accessed==0:
                #replace page if accessed bit is 0, eixit loop
                frameList[pointer]=i
                i._accessed=1
                added=True
                
                pointer+=1
                if pointer>numberOfFrames-1:
                    pointer=0
    for j in frameList:
        print(j)
    print("pointer: ",pointer)
    print("-------------------------")

print("Total page hits:",pagehits)
print("Total page faults:",pagefaults)
