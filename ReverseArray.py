

def reverse_array(arr):
    # Reverse and return an array without using any built in array functionality

    newArr = []

    solution = 2

    if solution == 1:
        for i in range(1, len(arr) + 1):
            newArr += arr[-i]

        return newArr

    if solution == 2:
        # Reverse an return the same array without creating a new array or using any built-in array functionality

        for i in range(int(len(arr)/2)):
            start_element = arr[i]
            end_element = arr[-(i + 1)]
            arr[i] = end_element
            arr[-(i + 1)] = start_element

        return arr


if __name__ == '__main__':
    array = ['!', 'd', 'l', 'e', 'e', 'n', 'n', 'a', 'r', 'a', 't']
    r = reverse_array(array)
    print(r)
