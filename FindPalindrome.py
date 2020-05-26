
# Given a number, write a function that reverses a number and adds the reverse to the original
# Return a count for how many times the function was ran before the number becomes a palindrome
import sys


def find_palindrome(num, count):
    if num >= sys.maxsize:
        return 'Palindrome not found'

    num_string = str(num)
    reverse_num_string = num_string[::-1]
    reverse_num = int(reverse_num_string)

    if reverse_num != num:
        count += 1
        num += reverse_num
        return find_palindrome(num, count)
    else:
        return count


if __name__ == '__main__':
    print(find_palindrome(187, 0))
