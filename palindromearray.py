def PalinArray(arr, n):
    for i in range(n):
        if str(arr[i]) != str(arr[i])[::-1]:
            return 0  # If any element is not a palindrome, return 0
    return 1  # If all elements are palindromes, return 1
