# Given a string 'str' count and return the number of times the target appears in the string


def count_occurrences_in_string(str, target):

    count = 0

    def reduce_str(str):
        nonlocal count
        if target in str:
            count += 1
            new_str = str.replace(target, '', 1)
            print(new_str)
            reduce_str(new_str)
        else:
            return

    if target in str:
        reduce_str(str)

    return count


if __name__ == '__main__':
    provided_str = 'abcdefgabcabcxyzabc'
    targ = 'abc'
    c = count_occurrences_in_string(provided_str, targ)
    print(c)
