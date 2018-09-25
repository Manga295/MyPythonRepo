import heapq

num =[1,2,5,7,-9,31,54,43,98]
print(heapq.nlargest(3,num))
print(heapq.nsmallest(3,num))


portfolio = [ {'name': 'IBM', 'shares': 100, 'price': 91.1}, {'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75}, {'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'ACME', 'shares': 75, 'price': 115.65} ]
#portfolio is a list of key -value pairs or dictionaries
cheap=heapq.nsmallest(3,portfolio ,key=lambda s: s['price'])
expensive =heapq.nlargest(3,portfolio,key=lambda s: s['price'])
print(cheap)
print(expensive)

nums =[1,2,3,4,-9,32,42,54,98]
import heapq
heap =list(nums) #that heap has been created with a list of numbers
heapq.heapify(heap) #using the heapify function we can heapify the list of numbers
print(heap)

print(heapq.heappop(heap)) #heappop will pop out the smallest number and replace it with the next smallest number
print(heapq.heappop(heap))
print(heapq.heappop(heap))