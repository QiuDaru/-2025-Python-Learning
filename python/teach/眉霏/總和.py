def two_sum(arr, target):
    num_dict = {}  
    
    for i, num in enumerate(arr):
        complement = target - num  
        if complement in num_dict:
            return [num_dict[complement], i]  
        num_dict[num] = i  
    
    return None  


arr = [1,1,1,1,1]
target = 5
result = two_sum(arr, target)
print("結果:", result) 