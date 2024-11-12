# Hussein's Github: https://github.com/husseinrit/activity3.git
# Joud's Github: 
# Yousuf's Github:
# Karam's Github: 


import random
import time

def create_sorted_data(size):
    # generating random digits and sorting them with insertion sort
    random_data = [random.randint(1, 100) for _ in range(size)]
    ordered_data = []
    unsorted_data = random_data

    while len(unsorted_data) > 0:
        current_element = unsorted_data[0]
        unsorted_data.remove(current_element)

        for index in range(len(ordered_data)):
            if current_element < ordered_data[index]:
                ordered_data.insert(index, current_element)
                break
        else:
            ordered_data.append(current_element)

    return ordered_data

def binary_search(sorted_array, target):
    low = 0
    high = len(sorted_array) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_array[mid] == target:
            return mid
        elif sorted_array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None

def linear_search(array, target):
    index = 0
    for element in array:
        if element == target:
            return index
        index += 1
    return None

# creating a large sorted array
sorted_array = create_sorted_data(1000)

#  target to search for
target = 72

# measuring time for linear search
start_time = time.perf_counter()
linear_search_result = linear_search(sorted_array, target)
linear_search_time = time.perf_counter() - start_time

# measueing time for binary search
start_time = time.perf_counter()
binary_search_result = binary_search(sorted_array, target)
binary_search_time = time.perf_counter() - start_time

# displaying the results
print("Linear Search Result:", linear_search_result)
print("Binary Search Result:", binary_search_result)
print("Linear Search Time:", linear_search_time)
print("Binary Search Time:", binary_search_time)

"""Reflection: Sorting helps searches by making binary search work faster. Binary search is quicker on large datasets because it cuts the data in half each time. Linear search checks every item so its slower. Good sorting speeds everything up
"""