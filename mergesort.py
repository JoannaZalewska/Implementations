def merge(left, right):
    sorted_list = []
    left_index = 0
    right_index = 0

    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    while len(sorted_list) < (len(left) + len(right)):
        if left[left_index] <= right[right_index]:
            sorted_list.append(left[left_index])
            if left_index == (len(left) - 1):
                sorted_list.extend(right[right_index:])
                return sorted_list
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            if right_index == (len(right) - 1):
                sorted_list.extend(left[left_index:])
                return sorted_list
            right_index += 1

def mergesort(list_to_sort):
    list_length = len(list_to_sort)
    if list_length == 1:
        return list_to_sort
    mid_index = list_length//2
    left = list_to_sort[0:mid_index]
    right = list_to_sort[mid_index:]

    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)


if __name__ == '__main__':

    list_to_sort = [1, 4, 2, 6, 3, 12, 9, 4]
    print(mergesort(list_to_sort))