def water_sum(arr):
    size=len(arr)
    water = 0
    left_msf=size*[0]
    right_msf=size*[0]
    
    left=[]
    
    for i in range(size):
        left_msf=arr[0]
        if left_msf<arr[i]:
            left_msf=arr[i]
        left.append(left_msf)
        
    right=[]
    
    for i in range(size-1,-1,-1):
        right_msf=arr[-1]
        if left_msf<arr[i]:
            left_msf=arr[i]
        right.append(right_msf)
    
    for i in range(size):
        water= water+min(left[i],right[i])-arr[i]
    
    return water

print(water_sum([2,0,1,1,0,4]))