import timeit
import numpy as np
import matplotlib.pyplot as plt

n = 50


def merge_sort(lst):

    def merge(left, right):
        merged = []
        left_index = 0
        right_index = 0

        # Merge smaller elements first
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        while left_index < len(left):
            merged.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            merged.append(right[right_index])
            right_index += 1

        return merged

    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j]:
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key
    return lst


results = np.zeros((4, n))

for i in range (1, n+1):
    current_list = np.random.randint(0, 10**9, size=i)


    # Calculating execution times
    results[0, i-1] = 10**i
    results[1, i-1] = timeit.timeit("merge_sort(current_list)",
                                    setup="from __main__ import merge_sort, current_list", number=10000)
    results[2, i-1] = timeit.timeit("insertion_sort(current_list)",
                                    setup="from __main__ import insertion_sort, current_list", number=10000)
    results[3, i-1] = timeit.timeit("sorted(current_list)",
                                    setup="from __main__ import insertion_sort, current_list", number=10000)

# Plotting results
fig, ax = plt.subplots()
ax.plot(results[0, :], results[1, :], label="merge sort")
ax.plot(results[0, :], results[2, :], label="insertion sort")
ax.plot(results[0, :], results[3, :], label="sorted")

# Setting logarithmic scale
ax.set_xscale('log')

# Adding legend and labels
ax.legend()
ax.set_title("Sort results")
ax.set_xlabel("List length: 10^n")
ax.set_ylabel("Time (s)")

plt.show()
