arr=[1,2,6,3,8,2,1]
'''temp=0
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


for i in range(0,len(arr)-1):
    min=i
    for j in range(i+1,len(arr)):
        if(arr[j]<arr[min]):
            min=j
    arr[i],arr[min]=arr[min],arr[i]
    print(arr)
    
