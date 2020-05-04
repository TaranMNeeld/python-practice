# Reverse and return an array without using any built in array functionality


def reverse_array(arr):

    newArr = []

    solution = 2

    if solution == 1:
        for i in range(1, len(arr) + 1):
            newArr += arr[-i]

        return newArr

    if solution == 2:
        # Reverse an return the same array without creating a new array or using any built-in array functionality
        return arr


if __name__ == '__main__':
    array = ['d', 'l', 'e', 'e', 'n', 'n', 'a', 'r', 'a', 't']
    r = reverse_array(array)
    print(r)
