class priority_queue():
    def __init__(self, p_queue=[]):
        self.p_queue = p_queue

    def __str__(self):
        p_queue_string = ''
        for item in self.p_queue:
            p_queue_string = p_queue_string + f' {item}'
        return p_queue_string

    def add_item(self, item):
        self.p_queue.append(item)
        if len(self.p_queue) == 1:
            return
        item_index = len(self.p_queue) - 1
        parent_index = (item_index - 1)//2
        parent = self.p_queue[parent_index]
        while item < parent:
            self.p_queue[item_index], self.p_queue[parent_index] = self.p_queue[parent_index], self.p_queue[item_index]
            item_index = parent_index
            if item_index == 0:
                return
            parent_index = (item_index - 1)//2
            parent = self.p_queue[parent_index]

    def get_min(self):
        if self.p_queue == []:
            return "Nothing to get. Priority queue is empty"
        min_value = self.p_queue[0]
        if len(self.p_queue) == 1:
            self.p_queue.pop(-1)
            return min_value
        self.p_queue[0] = self.p_queue[-1]
        self.p_queue.pop(-1)
        new_first_element_index = 0
        new_first_element = self.p_queue[new_first_element_index]
        leftchild_index = 2*new_first_element_index + 1
        rightchild_index = 2*new_first_element_index + 2
        if leftchild_index >= len(self.p_queue):
            return min_value
        if rightchild_index >= len(self.p_queue):
            left_child = self.p_queue[leftchild_index]
            if new_first_element > left_child:
                self.p_queue[new_first_element_index], self.p_queue[leftchild_index] = self.p_queue[leftchild_index], self.p_queue[new_first_element_index]
            return min_value
        left_child = self.p_queue[leftchild_index]
        right_child = self.p_queue[rightchild_index]
        while (new_first_element > left_child) or (new_first_element > right_child):
            if left_child < right_child:
                self.p_queue[new_first_element_index], self.p_queue[leftchild_index] = self.p_queue[leftchild_index], self.p_queue[new_first_element_index]
                new_first_element_index = leftchild_index
                leftchild_index = 2 * new_first_element_index + 1
                rightchild_index = 2 * new_first_element_index + 2
                if leftchild_index >= len(self.p_queue):
                    return min_value
                if rightchild_index >= len(self.p_queue):
                    left_child = self.p_queue[leftchild_index]
                    if new_first_element > left_child:
                        self.p_queue[new_first_element_index], self.p_queue[leftchild_index] = self.p_queue[leftchild_index], self.p_queue[new_first_element_index]
                    return min_value
                left_child = self.p_queue[leftchild_index]
                right_child = self.p_queue[rightchild_index]
            else:
                self.p_queue[new_first_element_index], self.p_queue[rightchild_index] = self.p_queue[rightchild_index], self.p_queue[new_first_element_index]
                new_first_element_index = rightchild_index
                leftchild_index = 2 * new_first_element_index + 1
                rightchild_index = 2 * new_first_element_index + 2
                if leftchild_index >= len(self.p_queue):
                    return min_value
                if rightchild_index >= len(self.p_queue):
                    left_child = self.p_queue[leftchild_index]
                    if new_first_element > left_child:
                        self.p_queue[new_first_element_index], self.p_queue[leftchild_index] = self.p_queue[leftchild_index], self.p_queue[new_first_element_index]
                    return min_value
                left_child = self.p_queue[leftchild_index]
                right_child = self.p_queue[rightchild_index]
        return min_value

def heapsort(list_to_sort):
    if list_to_sort is None:
        return "Nothing to sort"
    if len(list_to_sort) == 0:
        return "Nothing to sort"
    if len(list_to_sort) == 1:
        return list_to_sort
    auxiliary_p_queue = priority_queue()
    sorted_list = []
    for item in list_to_sort:
        auxiliary_p_queue.add_item(item)
    for _ in range(len(list_to_sort)):
        min_value = auxiliary_p_queue.get_min()
        sorted_list.append(min_value)
    return sorted_list

if __name__ == '__main__':
    print(heapsort([8, 3, 5, 7, 1, 10, 4, 2]))

