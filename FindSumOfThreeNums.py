
# Given an array of numbers 'nums' , find and return every three numbers that add up to the number 'n'


def sum_of_three_nums(nums, n):

    allSums = []
    triplets = {}

    for i in range(len(nums)):
        triplets[nums[i]] = None

    for i in range(len(nums)):
        for j in range(len(nums)):
            num1 = nums[i]
            num2 = nums[j]
            keys = triplets.keys()
            if n - (num1 + num2) in keys:
                tripletArr = [n - (num1 + num2), num1, num2]
                tripletArr.sort()
                if tripletArr not in allSums:
                    allSums.append(tripletArr)

    allSums.sort()
    return allSums


if __name__ == '__main__':
    nums = [0, 1, 2, 4, 5, 6, 12, 23, -12, 3, 1, 20, 9, -10, 21, 6, 13, 10]
    n = 24
    s = sum_of_three_nums(nums, n)
    print(s)
