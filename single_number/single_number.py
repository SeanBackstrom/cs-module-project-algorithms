'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

#its basically a different version of the fibonnaci sequence

def single_number(arr):
    """
    for i in arr:
        count = 0

        for j in arr:

            if i == j:
                count +=1

            if count == 2:
                break

        if count != 2:
            return i"""
    s = set()

    for num in arr: # O(n)
        if num in s: # O(1)
            s.remove(num) # O(1)
        else:
            s.add(num) # O(1)
    return s.pop()
    # at this point, the only element in the set 
    # is our odd-element-out
#    return list(s)[0] # O(1)

                



            
                

        

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")