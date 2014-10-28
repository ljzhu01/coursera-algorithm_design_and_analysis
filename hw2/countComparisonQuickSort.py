import sys

def swap(A, i, j):
    if i == j:
        return 
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def pivotMedian(A, l, r):
    tempArr = sorted([A[l], A[r], A[(l+r)/2]])
    median = tempArr[1]
    if median == A[l]:
        return l
    elif median == A[r]:
        return r
    else:
        return (l+r)/2
        
def quickSortPartition(A, l, r, method):
    if l == r:
        return l
    if not (method == "first" or method == "last" \
        or method == "median"):
        print "Wrong pivot method!"
        exit()
    # choose pivot    
    pivot = l 
    if method == "last":
        pivot = r
    elif method == "median": 
        pivot = pivotMedian(A, l, r)
    pivotValue = A[pivot]
    # swap the pivot with the first element
    swap(A, l, pivot)
    # now do the partition 
    i = l + 1
    for j in xrange(l+1, r+1):
        if A[j] < pivotValue:
            swap(A, i, j)
            i += 1
    swap(A, i-1, l)
    return i-1 

def mQuickSort(A, l, r, method):
    numSwap = 0
    p = quickSortPartition(A, l, r, method)
    numSwap += (r-l)
    if p > l + 1:
        numSwap += mQuickSort(A, l, p-1, method)
    if p < r-1:
        numSwap += mQuickSort(A, p+1, r, method)
    return numSwap
    
def readArray(filename):
    result = []
    with open(filename, 'r') as f:
        for line in f:
            result.append(int(line.strip()))
    return result
    
def main():
    filename = sys.argv[1]
    dataArr = readArray(filename)
    methods = ["first", "last", "median"]
    for method in methods:
        copyArr = dataArr[:]
        print mQuickSort(copyArr, 0, len(copyArr)-1, method)
        sortArr = ''
        for i in range(10):
            sortArr += str(copyArr[i]) + ","
        print sortArr 
        
if __name__ == "__main__":
    main()
    
    
    