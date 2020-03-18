#!/bin/python3

import os
import sys
import math

#
# Complete the bonetrousle function below.
#

"""
solved till now: 0, 1, 2, 3, 4, 5, 6, 14
"""


def bonetrousle(n, k, b):
    #
    # Write your code here.
    #
    #

    val_box = []
    for i in range(1, k+1):
        val_box.append(i)
    print(max(val_box))
    # val_box = [val for val in range(1, k+1)]
    # print(max(val_box))
    outcome = []
    temp = 0
    temp_one = 0
    temp_two = 0
    flag = False
    flag_one = True

    if (n == b == 1) and (k >= n):
        outcome.append(1)
        return outcome

    elif (b == 1) and (n > b) and (n <= k):
        outcome = []
        outcome.append(n)
        return outcome

    elif (n == b == k) \
    or ((k * (k + 1))/2 < n) \
    or ((b * (b + 1))/2 > n) \
    or ((b * (b - 1))/2 == n) \
    or (n < b) \
    or (n/b >= k):
        outcome.append(-1)
        return outcome

    else:
        for j in range(b):
            if (j == 0):
                temp = math.ceil(n/b)
                print('temp: ', temp)
                outcome.append(temp)

            elif (j == (b - 1)):
                # print('j: ', j)
                s = sum(outcome)
                diff = n - s
                print('line 51')
                print(outcome)
                print('diff: ', diff)

                if (diff > 0) and (diff in val_box) :
                    if (diff not in outcome):
                        print('line 58')
                        outcome.append(diff)
                        outcome.sort()
                        print(outcome)
                        return outcome

                    elif (diff in outcome):
                        if max(outcome) == k:
                            outcome = []
                            outcome.append(-1)
                            return outcome
                        else:
                            print('line 65')
                            if (len(outcome) == 1) and diff == min(outcome):
                                print('line 66')
                                t = min(outcome)
                                outcome.append(t + 1)
                                outcome.remove(t)
                                outcome.append(t-1)
                            else:
                                temp_min = min(outcome)
                                outcome.append(max(outcome) + 1)
                                diff = n - sum(outcome)
                                if (temp_min - abs(diff) > 0):
                                    outcome.remove(temp_min)
                                    outcome.append(temp_min - abs(diff))
                                    return outcome
                                else:
                                    outcome.append(1)
                                    s = sum(outcome)
                                    rem = abs(n - s)
                                    if rem in outcome:
                                        outcome.remove(rem)
                                    elif len(outcome) == 3:
                                        outcome.remove(1)
                                        rem = abs(n - s)
                                        m = min(outcome)
                                        outcome.remove(m)
                                        outcome.append(m - rem)

                        if max(outcome) <= max(val_box):
                            outcome.sort()
                            return outcome
                        else:
                            outcome = []
                            outcome.append(-1)
                            return outcome

                elif (diff < 0):
                    temp_min = min(outcome)
                    if diff == -1:
                        # temp_min = min(outcome)
                        outcome.append(1)
                        outcome.remove(temp_min)
                        outcome.append(temp_min - 2)
                        return outcome

                    else:
                        # temp_min = min(outcome)
                        outcome.append(1)
                        diff = n - sum(outcome)

                        if sum(outcome) == n:
                            print(sum(outcome))
                            outcome.sort()
                            return outcome

                        elif abs(diff) in outcome:
                            outcome.append(2)
                            diff = n - sum(outcome)
                            if abs(diff) in outcome:
                                outcome.remove(abs(diff))
                                outcome.sort()
                                return outcome
                            else:
                                outcome = []
                                outcome.append(-1)
                                return outcome

                        elif abs(diff) not in outcome:
                            print('line 138')
                            print("diff: ", diff)
                            print('temp_min: ', temp_min)
                            if (temp_min - abs(diff) > 0):
                                print('line 141')
                                if temp_min - abs(diff) == 1:
                                    print('line 143')
                                    outcome.remove(temp_min + 1)
                                    outcome.append(temp_min - abs(diff) + 1)

                                else:
                                    print('line 147')
                                    outcome.remove(temp_min)
                                    outcome.append(temp_min - abs(diff))

                                return outcome
                            else:
                                outcome = []
                                outcome.append(-1)
                                return outcome

                elif (diff == 0):
                    s_n = min(outcome)
                    outcome.remove(s_n)
                    outcome.append(s_n - 1)
                    outcome.append(1)
                    outcome.sort()
                    print(outcome)
                    return outcome

                else:
                    outcome = []
                    outcome.append(-1)
                    return outcome

            else:
                if (j % 2 != 0) and (not flag):
                    if (j < 2):
                        temp_one = temp + 1
                        outcome.append(temp_one)
                    else:
                        temp_one += 1
                        outcome.append(temp_one)

                elif (j % 2 == 0) and (not flag):
                    if (j == 2):
                        temp_two = temp - 1
                        if temp_two == 1:
                            flag = True
                        outcome.append(temp_two)

                    else:
                        temp_two -= 1
                        if temp_two == 1:
                            flag = True
                        outcome.append(temp_two)

                elif flag:
                    if flag_one:
                        flag_one = False
                        avg_new = math.ceil((n - sum(outcome))/(b - j - 1))
                        if math.floor(avg_new) in outcome:
                            outcome = []
                            outcome.append(-1)
                            return outcome
                        else:
                            outcome.append(avg_new)
                            temp_one = avg_new
                            temp_two = avg_new

                    elif not flag_one:
                        if (j % 2 != 0):
                            temp_one += temp_one
                            outcome.append(temp_one)
                        elif (j % 2 != 0):
                            temp_two += temp_two
                            outcome.append(temp_two)

    outcome.sort()
    print(outcome)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

t = int(input())

for t_itr in range(t):
    nkb = input().split()

    n = int(nkb[0])

    k = int(nkb[1])

    b = int(nkb[2])

    result = bonetrousle(n, k, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

fptr.close()
