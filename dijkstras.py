import heapq
import cv2
import numpy as np
import random


class MinHeap:
	def __init__(self):
		self.heap = []
		self.entries = {}
		
	def add(self,location,cost):
		if location in self.entries:
			self.remove(location)
		entry = [cost, location, True]
		self.entries[location]=entry
		heapq.heappush(self.heap, entry)

	def remove(self,location):
		entry = self.entries.pop(location)
		entry[-1] = False

	def pop(self):
		while self.heap:
			cost,location,isActive = heapq.heappop(self.heap)
			if isActive:
				del self.entries[location]
				return location,cost
		raise KeyError('pop from an empty priority queue')
   
	

datax=[224,2352,2112,1760,878,610,2816,1488]
datay=[320,1824,2864,3328,3902,760,2784,3504]
h=MinHeap()
visited=set()
img=cv2.imread("map.png",0)
print(img)
height,width=img.shape
cost=img*0.0+9999999
start=(610,760)
cost[start[::-1]]=0
h.add(start,0)
end=(width,height)
i=0
d = 1
currelev = 0
prevelev = 0
while True:
	(x,y),c=h.pop()
	if (x,y)==end:
		break
	visited.add((x,y))
	prevelev=img[y,x]
	for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
		x2=x+dx
		y2=y+dy
		currelev = img[y2,x2]
		for j in range(len(datax)):
			if x2<0 or y2<0 or x2>=width or y2>=height or ((x2 > datax[j] and x2 < datax[j] + 100) and (y2 > datay[j] and y2 < datay[j] + 100)):
				continue
		if (x2,y2) not in visited:
			if prevelev != currelev:
				d = 1
			else:
				d+=1
			cost2=c
			cost2+=1+100.0/(d * d)
			if cost2<cost[y2,x2]:
				h.add((x2,y2),cost2)
				cost[y2,x2]=cost2
	
	i+=1
	if i%100==0:
		print(y,x,cost2,d)
		#cv2.imshow("image",out)
		#cv2.waitKey(1)
out=cost*1
out[out>=1000]=0
out/=np.max(out)
out*=255
cv2.imshow("image",out)
cv2.waitKey(0)
cv2.destroyAllWindows()
	


