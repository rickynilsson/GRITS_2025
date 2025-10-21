some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Write a function that calculates the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Write a function that reverses a string
def reverse_string(s):
    return s[::-1]


# Write a function that takes two strings and checks if they are anagrams.
# The function should ignore spaces and case.
def are_anagrams(str1, str2):
    '''Check if two strings are anagrams.'''
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Sort the characters of both strings and compare
    return sorted(str1) == sorted(str2)


# def find_first_non_repeating_char(text):
#     for i in range(len(text)):
#         is_repeated = False
#         for j in range(len(text)):
#             if i != j and text[i] == text[j]:
#                 is_repeated = True
#                 break
#         if not is_repeated:
#             return text[i]
#     return None


def find_first_non_repeating_char(text):
    # Create a dictionary to count occurrences of each character
    char_count = {}
    
    # Count each character in the text
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the first character with a count of 1
    for char in text:
        if char_count[char] == 1:
            return char
    
    return None


# def find_median(data):
#     n = len(data)
#     if n % 2 == 1:
#         return data[n // 2]
#     else:
#         mid = n // 2
#         return data[mid]


def find_median(data):
    # Sort the data to ensure correct median calculation
    data = sorted(data)
    n = len(data)
    if n % 2 == 1:
        return data[n // 2]
    else:
        mid = n // 2
        return (data[mid - 1] + data[mid]) / 2
    