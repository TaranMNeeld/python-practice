
# At a given index 'idx', rotate all of the values after the index, so those values are shifted to the front of the
# given array 'arr' Example arr = [0, 1, 2, 3, 4], idx = 2 output = [2, 3, 4, 0, 1]


def rotate_array_at_index(arr, idx):

    newArr = []

    for i in range(len(arr)):
        if i >= idx:
            newArr.append(arr[i])

    for i in range(len(arr)):
        if i < idx:
            newArr.append(arr[i])

    return newArr


if __name__ == '__main__':
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    r = rotate_array_at_index(array, 5)
    print(r)
