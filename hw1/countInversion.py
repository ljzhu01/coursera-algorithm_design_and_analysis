import sys

def readFile(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(int(line.strip()))
    return data

def merge(arr1, s, m, e, arr2):
    invnum = 0
    # base case
    if m - s < 1 or e - m < 1:
        return invnum
        
    i = s 
    j = m 
    for k in range(s, e):
        if j < e and (i == m or arr1[i] >= arr1[j]):
            arr2[k] = arr1[j]
            j += 1
            invnum += (m-i) 
        else:
            arr2[k] = arr1[i]
            i += 1
    # copy the array back to arr1 
    for k in range(s, e):
        arr1[k] = arr2[k]
    return invnum 

def mergeInvCount(data, start, end, dataprime):
    mid = int(start + (end - start) /2 )
    invnum = 0
    if mid - start > 1:
        invnum += mergeInvCount(data, start, mid, dataprime)
    if end - mid > 1:
        invnum += mergeInvCount(data, mid, end, dataprime)
    invnum += merge(data, start, mid, end, dataprime)
    return invnum
    
#---------------------------------------------    
def main():
    filename = sys.argv[1]
    data = readFile(filename)
    dataprime = [None] * len(data)
    invCount = mergeInvCount(data, 0, len(data), dataprime)
    print(invCount)
        
if __name__ == '__main__':
    main()