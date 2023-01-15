def is_palindrome(number):
    """Returns true if the number is a palindrome"""
    number = str(number)
    for i in range(len(number) // 2):
        if number[i] != number[-(i + 1)]:
            return False
    return True

def largest_palindrome_product():
    largest = ""
    for i in range(1000):
        for j in range(1000):
            if is_palindrome(i * j):
                if len(str(i * j)) >= len(largest):
                    if largest == "":
                        largest = str(i * j)
                    elif (i*j) > int(largest):
                        largest = str(i * j)
    return largest
    
print(largest_palindrome_product())

