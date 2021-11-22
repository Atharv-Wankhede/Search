def creatingarray(n):
    array = []
    for i in range(n):
        employeeid = int(input("Enter Employee id ---"))
        array.append(employeeid)
    return array



def linearSearch(key, array):
    for i in range(len(array)):
        if key == array[i]:
            print("Employee attended program--linear search")
        else:
        	pass


def sentinalSearch(array, key):
        array.append(key)
        i=0
        while True:
        	if(array[i]==key):
        		i=i+1
        		print("Employee attended program ---sentinal search")
        		break
        	else:
        		print("Employee didnt attended program---sentinal search")
        		break


def binarySearch(key, array, low, high):     
    if high>= low:
        mid = (low + high)//2 
        if key == array[mid]:
            print("Employee attended program ---binary search")
        elif key< array[mid]:
            return binarySearch(key, array, low, mid-1)
        else:
        	print("Employee didnt attended program--binary search")

def FibonacciGenerator(n):    
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return FibonacciGenerator(n - 1) + FibonacciGenerator(n - 2)

def FibonacciSearch(arr, key):
	while FibonacciGenerator(m) < len(arr): 
        m = m + 1 
        offset = -1
        while (FibonacciGenerator(m) > 1):
         i = min( offset + FibonacciGenerator(m - 2) , len(arr) - 1)
        if (key > arr[i]):
            m = m - 1
            offset = i
        elif (key < arr[i]):
            m = m - 2
        else:
            return i
    if(FibonacciGenerator(m - 1) and arr[offset + 1] == key):
        return offset + 1
    return -1       	

n = int(input("Enter number of employee ---: "))
array = creatingarray(n)
key = int(input("Enter employee id you want to search---: "))
low = 0
high = len(array)-1
e= binarySearch(key, array, low, high)
f= linearSearch(key, array)
g= sentinalSearch(array, key)




