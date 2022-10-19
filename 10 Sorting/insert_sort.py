

def insertion_sort(unsorted_list):
    for index in range(1, len(unsorted_list)):
        search_index = index
        insert_value = unsorted_list[index]
        while search_index > 0 and unsorted_list[search_index-1] > insert_value :
            unsorted_list[search_index] = unsorted_list[search_index-1]
            search_index -= 1
        unsorted_list[search_index] = insert_value





my_list = [13, 95, 10, 43, 3, 64, 48, 52, 75, 12, 51]
print(my_list)
insertion_sort(my_list)
print(my_list)


