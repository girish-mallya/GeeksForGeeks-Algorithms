import time
def threecolorsort(arr):
	lo=0
	hi=len(arr)-1
	mid=0


	while(mid<=hi):
		if arr[mid]==0:
			arr[lo],arr[mid] = arr[mid],arr[lo]
			mid=mid+1
			lo=lo+1

		elif arr[mid]==1:
			mid=mid+1
		else:
			arr[mid],arr[hi]=arr[hi],arr[mid]
			mid=mid-1
			hi=hi-1


def printarr(arr):
	for i in arr:
		print(i)



def main():
	arr= [0,0,1,2,1,2,0,2,1,0,2,0,1,0]
	print("this is arr before sorting")
	printarr(arr)
	print("*************************")


	start = time.time()
	arr.sort()
	end = time.time()
	print("Time to sort using python function: " ,(end - start))
	arr= [0,0,1,2,1,2,0,2,1,0,2,0,1,0]

	start=time.time()

	threecolorsort(arr)
	end =time.time()
	print("Time using 3cs algorithm: ",  (end-start))
	print("This is arr after sorting")
	printarr(arr)



main()
