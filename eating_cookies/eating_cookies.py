'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    cap = 3
    o = n - 2
    p = 1
    if n == 0:
        return 1
    if n < 3:
        return n
    if n >= 3:
        return n * o + p
    
    
    

    return 

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 6

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

