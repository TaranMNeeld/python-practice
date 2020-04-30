
# Given an array of numbers 'nums' , find every pair of numbers that adds up to the number 'n'


def sum_of_two_nums(nums, n):

    allSums = []
    pairs = {}

    for i in range(len(nums)):
        pairs[nums[i]] = None

    for i in range(len(nums)):
        keys = pairs.keys()
        if n - nums[i] in keys:
            pairs[n - nums[i]] = nums[i]
            allSums.append([n - nums[i], nums[i]])
    return allSums


if __name__ == '__main__':
    nums = [0, 1, 2, 4, 5, 6, 12, 23, -12, 3, 1, 20, 9, -10, 21]
    n = 11
    s = sum_of_two_nums(nums, n)
    print(s)
