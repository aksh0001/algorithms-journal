""" You are given an array with n positive integers where all values in the array are repeated except for one.
 Return the one that is not repeated.
 Eg. [1,2,5,4,2,5,1,3*,4] return 3
 Solution:
    Track frequencies of elements using a dict. If elem has been seen already, delete from dict.
    According to the problem, there will be only one element left over; this is the answer
 Solution improvements: Use bit-shifting, specifically XOR.
 """


def solution(a):
    seen = {}
    freq = {}
    for val in a:
        if seen.get(val) is None:
            freq[val] = 1
            seen[val] = 1
        else:
            freq.pop(val)  # We pop from the freq

    # Only element left will be the unique one
    return freq.popitem()[0]


if __name__ == "__main__":
    print(solution([1, 2, 5, 4, 2, 5, 1, 3, 4, 2, 1, 5, 1]))
