'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    print("before", arr)
    
    zerocount = 0
    for num in range(len(arr)):
        if arr[num] == 0:
            arr.append(arr[num])
            zerocount += 1

    for i in range(zerocount):
        arr.remove(0)

            
            
    print(arr)
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 2, 1] 

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")