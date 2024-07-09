def sort_numbers(nums):
    return sorted(nums)

# Example usage
numbers = [5, 2, 9, 1, 5, 6]
print(sort_numbers(numbers))  # Output: [1, 2, 5, 5, 6, 9]
def filter_even_numbers(nums):
    return [num for num in nums if num % 2 == 0]

# Example usage
numbers = [1, 2, 3, 4, 5, 6]
print(filter_even_numbers(numbers))  # Output: [2, 4, 6]

def find_max_number(nums):
    return max(nums)

# Example usage
numbers = [1, 2, 3, 4, 5, 6]
print(find_max_number(numbers))  # Output: 6


def reverse_list(lst):
    return lst[::-1]

# Example usage
numbers = [1, 2, 3, 4, 5]
print(reverse_list(numbers))  # Output: [5, 4, 3, 2, 1]

def remove_duplicates(lst):
    return list(set(lst))

# Example usage
numbers = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4, 5]

def square_numbers(nums):
    return [num ** 2 for num in nums]

# Example usage
numbers = [1, 2, 3, 4]
print(square_numbers(numbers))  # Output: [1, 4, 9, 16]


def find_longest_string(strings):
    return max(strings, key=len)

# Example usage
words = ["apple", "banana", "cherry", "date"]
print(find_longest_string(words))  # Output: "banana"


def concatenate_strings(strings):
    return ''.join(strings)

# Example usage
words = ["hello", " ", "world"]
print(concatenate_strings(words))  # Output: "hello world"

