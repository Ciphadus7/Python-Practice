# Use whatever name for the functions's parameter
def reverse(x, func):
    """
    This function returns a new string with all characters reversed.
    """
    ## YOUR CODE STARTS HERE
    return func(x)
    
reversedWord = reverse('Python', lambda x: x[::-1])
print(reversedWord)


