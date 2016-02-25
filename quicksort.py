def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    left = [item for item in arr if item<pivot]
    right =[item for item in arr if item>pivot]
    middle =[item for item in arr if item==pivot]
    
    return quicksort(left)+middle+quicksort(right)

if __name__=="__main__":
    print(quicksort([10,23,44,2,44,232,123]))