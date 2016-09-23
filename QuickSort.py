#Test command commit
import random
import time

start = time.time()

def partition(array, left, right):
    i = left-1
    for j in range(left, right):
        if array[j] <= array[right]:
            i += 1
            array[j], array[i] = array[i], array[j]
    array[i+1], array[right] = array[right], array[i+1]
    return i+1

def quicksort(array, left, right):
    if left < right:
        pivot = partition(array, left, right)
        quicksort(array, left, pivot-1)
        quicksort(array, pivot+1, right)

#create random array        
array = []
max = 10000 

for x in range(max+1):
    array.append(random.randint(0,max)) 

#quick sort    
quicksort(array, 0, max)


end = time.time()
elapsed = end - start

print array
print "Time taken: ", elapsed, "seconds."
print "-END-"




