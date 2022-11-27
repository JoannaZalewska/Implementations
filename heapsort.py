class priority_queue():
    '''
    This class is made to create a priority queue.
    Our priority queue is a list in with items are ordered as a heap, with minimal element at the top.
    Class contains methods to:
    - move the item up the heap if it is in the wrong place,
    - move the item down the heap if it is in the wrong place,
    - add the item to the list,
    - get the smallest value from the list.
    '''

    def __init__(self, your_list: int = None):
        if your_list is None:
            self.items = []
        else:
            self.items = your_list.copy()
            for item_index in range(len(self.items))[::-1]:
                self.siftdown(item_index)

    def __str__(self):
        return ' '.join(map(str, self.items))

    def __len__(self):
        return len(self.items)

    def siftup(self, item_index: int):
        '''
        Move the item up the heap if it is smaller than its parent.
        :param item_index: Index of the item to move up.
        '''

        parent_index = (item_index - 1)//2
        while (parent_index >= 0) and (self.items[item_index] < self.items[parent_index]):
            self.items[item_index], self.items[parent_index] = self.items[parent_index], self.items[item_index]
            item_index = parent_index
            parent_index = (item_index - 1) // 2

    def siftdown(self, item_index: int):
        '''
        Moves the item down the heap if it is larger than its children.
        :param item_index: Index of the item to move down.
        '''

        leftchild_index = 2 * item_index + 1
        rightchild_index = 2 * item_index + 2
        while (leftchild_index < len(self.items) and self.items[item_index] > self.items[leftchild_index]) or (rightchild_index < len(self.items) and self.items[item_index] > self.items[rightchild_index]):
            if rightchild_index >= len(self.items) or self.items[leftchild_index] < self.items[rightchild_index]:
                smallest_child_index = leftchild_index
            else:
                smallest_child_index = rightchild_index
            self.items[item_index], self.items[smallest_child_index] = self.items[smallest_child_index], self.items[item_index]
            item_index = smallest_child_index
            leftchild_index = 2 * item_index + 1
            rightchild_index = 2 * item_index + 2

    def add_item(self, item: int):
        '''
        Adds the item at the end of the heap and move it up to preserve the structure of the heap.
        :param item: Number to add to the heap.
        '''

        self.items.append(item)
        if len(self.items) == 1:
            return
        item_index = len(self.items) - 1
        self.siftup(item_index)

    def get_min(self) -> int:
        '''
        Removes the first (minimal) element from the heap and restores the structure of the heap.
        :return: Minimal element of the list.
        '''

        if self.items == []:
            return ValueError("This list is empty. Nothing to get.")
        min_value = self.items[0]
        if len(self.items) == 1:
            self.items.pop(-1)
            return min_value
        self.items[0] = self.items[-1]
        self.items.pop(-1)
        self.siftdown(0)
        return min_value


def heapsort(list_to_sort: list[int]) -> list[int]:
    '''
    Sorts the list by making a heap of it and then removing the first item from it one by one.
    :param list_to_sort: The list of numbers you want to sort.
    :return: The list of numbers in increasing order.
    '''

    if list_to_sort is None:
        raise ValueError("Wrong value. You must provide a list of integers.")
    if len(list_to_sort) == 1 or len(list_to_sort) == 0:
        return list_to_sort
    auxiliary_p_queue = priority_queue()
    sorted_list = []
    for item in list_to_sort:
        auxiliary_p_queue.add_item(item)
    for _ in range(len(list_to_sort)):
        min_value = auxiliary_p_queue.get_min()
        sorted_list.append(min_value)
    return sorted_list


def heapsort2(list_to_sort: list[int]) -> list[int]:
    '''
    Another way to do heapsort. This time we're making a heap at once instead of adding elements to it one by one.
    :param list_to_sort: The list of numbers you want to sort.
    :return: The list of numbers in increasing order.
    '''

    if list_to_sort is None:
        raise ValueError("Wrong value. You must provide a list of integers.")
    if len(list_to_sort) == 1 or len(list_to_sort) == 0:
        return list_to_sort
    our_heap = priority_queue(list_to_sort)
    sorted_list = []
    for _ in range(len(our_heap)):
        min_value = our_heap.get_min()
        sorted_list.append(min_value)
    return sorted_list


if __name__ == '__main__':
    print(heapsort([8, 3, 5, 7, 1, 10, 4, 2]))
    print(heapsort2([8, 3, 5, 7, 1, 10, 4, 2]))

