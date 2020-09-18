'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    
    #make final empty array
    final = []
    s = 0
    if k == 0:
        return

    for i in range(k, len(nums) + 1):

    #make sub array nums of size k
        subarr = nums[s:k]
    #loop inside subarray, append highest number to final
        maxi = subarr[0]
        for num in subarr:
            if num > maxi:
                maxi = num
        final.append(maxi)
        s += 1
        k += 1

    return final

    


    


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
