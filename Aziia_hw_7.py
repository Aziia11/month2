# array_list = [76, 79, 64, 31, 57, 71, 23, 18, 34, 78]
def bubble_sort(array_list):
    length = len(array_list)
    for i in range(0, length):
        for b in range(0, length - i - 1):
            if array_list[b] > array_list[b + 1]:
                num = array_list[b]
                array_list[b] = array_list[b + 1]
                array_list[b + 1] = num


array_list = [76, 79, 64, 31, 57, 71, 23, 18, 34, 78]
bubble_sort(array_list)
print(array_list)


def binary_search(list, item):
    First = 0
    Last = len(list) - 1
    # ResultOk = False
    while First <= Last:
        middle = (First + Last) // 2
        if list[middle] == item:
            return f'Element found: {middle}'
        else:
            if list[middle] > item:
                Last = middle - 1
            if list[middle] < item:
                First = middle + 1



N = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450]
print(N)
print(binary_search(N, 300))
