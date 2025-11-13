arr=[1,2,6,3,8,2,1]
''' Bubble Sort
temp=0
for i in range(0,len(arr)-1):
    sapped=False
    for j in range(0,len(arr)-1-i):
        if(arr[j]>arr[j+1]):
            sapped=True
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
    print(arr)
    if(not sapped):
        break
print(arr)'''

''' Selection Sort
for i in range(0,len(arr)-1):
    min=i
    for j in range(i+1,len(arr)):
        if(arr[j]<arr[min]):
            min=j
    arr[i],arr[min]=arr[min],arr[i]
    print(arr)
'''
"INSERTION SORT"
'''for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while( j>=0 and arr[j]>key):
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
    print(arr)'''

gap=len(arr)//2
while(gap>=1):
    for i in range(0,len(arr)):
        key=arr[i]
        j=i-1
        while( j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    gap=gap//2
    print(arr)
