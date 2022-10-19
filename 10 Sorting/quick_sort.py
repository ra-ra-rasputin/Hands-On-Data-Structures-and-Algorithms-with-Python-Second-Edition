
def partition(unsorted, first_index, last_index):
    pivot = unsorted[first_index]
    pivot_index = first_index
    index_of_last_element = last_index
    right_pointer = index_of_last_element
    left_pointer = first_index + 1
    while True:
        while unsorted[left_pointer] < pivot and left_pointer < last_index:
            left_pointer += 1
        while unsorted[right_pointer] > pivot and right_pointer >= first_index:
            right_pointer -= 1
        if left_pointer < right_pointer:
            temp = unsorted[left_pointer]
            unsorted[left_pointer] = unsorted[right_pointer]
            unsorted[right_pointer] = temp
        else:
            break
    unsorted[pivot_index] = unsorted[right_pointer]
    unsorted[right_pointer] = pivot
    return right_pointer


def quick_sort(unsorted, first, last):
    if last - first <= 0:
        return
    else:
        partition_point = partition(unsorted, first, last)
        quick_sort(unsorted, first, partition_point-1)
        quick_sort(unsorted, partition_point+1, last)


my_array = [13, 95, 10, 43, 3, 64, 48, 52, 75, 12, 51]
print(my_array)
quick_sort(my_array, 0, len(my_array)-1)
print(my_array)

