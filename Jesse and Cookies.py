n,k=map(int, input().split())
a=list(map(int, input().split()))
import heapq
i=0
heapq.heapify(a)
try:
	while(a[0]<k):
		print(a)
		x=a[0]
		heapq.heappop(a)
		y=a[0]
		heapq.heappop(a)
		heapq.heappush(a,x+2*y)
		i+=1
	print(i)
except IndexError:
	print(-1)