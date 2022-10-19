
def selection_sort(unsorted_list):
    size_of_list = len(unsorted_list)
    for i in range(size_of_list):
        for j in range(i+1, size_of_list):
            if unsorted_list[j] < unsorted_list[i]:
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[j]
                unsorted_list[j] = temp
                
list_d = [95, 13, 10, 43, 3, 64, 48, 52, 75, 12, 51, 46, 66, 86, 1, 70, 30, 45, 8, 96]
selection_sort(list_d)
print(list_d)