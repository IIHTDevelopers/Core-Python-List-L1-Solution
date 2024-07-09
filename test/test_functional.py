import unittest

# Assuming yakshaAssert is a method provided in TestUtils class for assertion
class TestUtils:
    def yakshaAssert(self, test_name, condition, test_type):
        # This is a placeholder for the actual implementation of yakshaAssert
        assert condition, f"Test {test_name} failed for {test_type} test."

# Functions to be tested
def sort_numbers(nums):
    return sorted(nums)

def filter_even_numbers(nums):
    return [num for num in nums if num % 2 == 0]

def find_max_number(nums):
    return max(nums)

def reverse_list(lst):
    return lst[::-1]

def remove_duplicates(lst):
    return list(set(lst))

def square_numbers(nums):
    return [num ** 2 for num in nums]

def find_longest_string(strings):
    return max(strings, key=len)

def concatenate_strings(strings):
    return ''.join(strings)

class TestListManipulation(unittest.TestCase):
    def test_sort_numbers(self):
        test_utils_instance = TestUtils()
        numbers = [5, 2, 9, 1, 5, 6]
        expected = [1, 2, 5, 5, 6, 9]
        actual = sort_numbers(numbers)
        test_utils_instance.yakshaAssert("TestSortNumbers", expected == actual, "functional")
        if expected == actual:
            print("TestSortNumbers = Passed")
        else:
            print("TestSortNumbers = Failed")

    def test_filter_even_numbers(self):
        test_utils_instance = TestUtils()
        numbers = [1, 2, 3, 4, 5, 6]
        expected = [2, 4, 6]
        actual = filter_even_numbers(numbers)
        test_utils_instance.yakshaAssert("TestFilterEvenNumbers", expected == actual, "functional")
        if expected == actual:
            print("TestFilterEvenNumbers = Passed")
        else:
            print("TestFilterEvenNumbers = Failed")

    def test_find_max_number(self):
        test_utils_instance = TestUtils()
        numbers = [1, 2, 3, 4, 5, 6]
        expected = 6
        actual = find_max_number(numbers)
        test_utils_instance.yakshaAssert("TestFindMaxNumber", expected == actual, "functional")
        if expected == actual:
            print("TestFindMaxNumber = Passed")
        else:
            print("TestFindMaxNumber = Failed")

    def test_reverse_list(self):
        test_utils_instance = TestUtils()
        numbers = [1, 2, 3, 4, 5]
        expected = [5, 4, 3, 2, 1]
        actual = reverse_list(numbers)
        test_utils_instance.yakshaAssert("TestReverseList", expected == actual, "functional")
        if expected == actual:
            print("TestReverseList = Passed")
        else:
            print("TestReverseList = Failed")

    def test_remove_duplicates(self):
        test_utils_instance = TestUtils()
        numbers = [1, 2, 2, 3, 4, 4, 5]
        expected = sorted([1, 2, 3, 4, 5])  # Order doesn't matter in sets
        actual = sorted(remove_duplicates(numbers))
        test_utils_instance.yakshaAssert("TestRemoveDuplicates", expected == actual, "functional")
        if expected == actual:
            print("TestRemoveDuplicates = Passed")
        else:
            print("TestRemoveDuplicates = Failed")

    def test_square_numbers(self):
        test_utils_instance = TestUtils()
        numbers = [1, 2, 3, 4]
        expected = [1, 4, 9, 16]
        actual = square_numbers(numbers)
        test_utils_instance.yakshaAssert("TestSquareNumbers", expected == actual, "functional")
        if expected == actual:
            print("TestSquareNumbers = Passed")
        else:
            print("TestSquareNumbers = Failed")

    def test_find_longest_string(self):
        test_utils_instance = TestUtils()
        words = ["apple", "banana", "cherry", "date"]
        expected = "banana"
        actual = find_longest_string(words)
        test_utils_instance.yakshaAssert("TestFindLongestString", expected == actual, "functional")
        if expected == actual:
            print("TestFindLongestString = Passed")
        else:
            print("TestFindLongestString = Failed")

    def test_concatenate_strings(self):
        test_utils_instance = TestUtils()
        words = ["hello", " ", "world"]
        expected = "hello world"
        actual = concatenate_strings(words)
        test_utils_instance.yakshaAssert("TestConcatenateStrings", expected == actual, "functional")
        if expected == actual:
            print("TestConcatenateStrings = Passed")
        else:
            print("TestConcatenateStrings = Failed")

if __name__ == '__main__':
    unittest.main()
