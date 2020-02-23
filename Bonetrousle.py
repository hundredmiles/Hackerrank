#!/bin/python3

import os
import sys
import math

#
# Complete the bonetrousle function below.
#
def bonetrousle(n, k, b):
    #
    # Write your code here.
    #
    #
    val_box = [val for val in range(1, k+1)]
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
                        print('line 57')
                        outcome.append(diff)
                        outcome.sort()
                        print(outcome)
                        return outcome

                    elif (diff in outcome):
                        print('line 64')
                        if (len(outcome) == 1) and diff == min(outcome):
                            print('line 66')
                            t = min(outcome)
                            outcome.append(t + 1)
                            outcome.remove(t)
                            outcome.append(t-1)
                        else:
                            print('line 72')
                            outcome.append(max(outcome) + 1)
                            outcome.append(1)
                            # outcome.append(max(outcome) + 1)
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
                        if (temp_min - abs(diff) > 0):
                            outcome.remove(temp_min)
                            outcome.append(temp_min - abs(diff))
                            return outcome
                        else:
                            outcome = []
                            outcome.append(-1)
                            return outcome

                    
                    # print(diff)
                    # print('line 95')
                    # print(outcome)
                    # outcome.append(1)
                    # print(sum(outcome))

                    # if sum(outcome) == n:
                    #     print(sum(outcome))
                    #     outcome.sort()
                    #     return outcome
                    
                    # else:
                    #     outcome.append(2)
                    #     if sum(outcome) == n:
                    #         print(sum(outcome))
                    #         outcome.sort()
                    #         return outcome
                    #     else:
                    #         s = sum(outcome)
                    #         rem = abs(n - s)
                    #         if rem in outcome:
                    #             outcome.remove(rem)
                    #             return outcome

                    #         elif (min(outcome) - rem) < 1:
                    #             outcome = []
                    #             outcome.append(-1)
                    #             return outcome

                    #         elif (min(outcome) - rem) > 1:
                    #             min_val = min(outcome)
                    #             outcome.remove(min_val)
                    #             outcome.append(min_val - 4)
                    #             outcome.sort()
                    #             print(outcome)
                    #             return outcome

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
	

"""

***********Sample Input - 4***********
20
4 7 1
78 34 9
79 30 12
34 82 5
185 231 16
48 84 2
232 9 3
9 5 4
234 40 16
255 39 10
60 55 4
286 164 3
90 14 10
280 300 2
2 27 1
223 21 19
77 47 6
280 300 1
173 45 10
61 15 5
***********Expected Output***********
4
16 1 2 3 4 5 6 7 34
13 1 2 3 4 5 6 7 8 9 10 11
24 1 2 3 4
65 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
47 1
-1
-1
14 1 2 3 4 5 6 7 8 9 10 11 37 38 39 40
30 1 2 3 34 35 36 37 38 39
54 1 2 3
121 1 164
5 1 7 8 9 10 11 12 13 14
279 1
2
4 1 2 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
20 1 2 3 4 47
280
20 1 2 3 4 5 6 43 44 45
7 12 13 14 15
----------------My Output----------------------
4
2 6 7 8 9 10 11 12 13
1 2 3 4 5 6 7 8 9 10 11 13
4 6 7 8 9
1 5 6 7 8 9 10 11 12 13 14 15 17 18 19 20
23 25
-1
-1
1 8 9 10 11 12 13 14 16 17 18 19 20 21 22 23
21 22 23 24 25 26 27 28 29 30
1 14 15 16 17 - wrong
93 96 97
1 5 7 8 9 10 11 12 13 14
139 141
2
12 13 11 14 10 15 9 16 8 17 7 18 6 19 5 20 21 1 1 - wrong
1 11 12 13 14 15 16 - wrong
280
11 14 15 16 17 18 19 20 21 22
7 12 13 14 15

***********Sample Input***********
20
300 299 1
300 299 2
300 100 3
300 101 3
7 300 3
5 300 3
3 300 1
3 300 2
298 150 2
299 150 2
300 150 2
300 300 300
300 300 3
300 300 2
300 300 1
1 1 1
299 300 24
300 300 23
300 300 25
300 300 24
***********Expected Output***********
-1
299 1
-1
99 100 101
4 1 2
-1
3
2 1
148 150
149 150
-1
-1
297 1 2
299 1
300
1
-1
47 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
-1
24 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23

---------------My output---------------
300
149 151
-1
99 100 101
1 2 4
-1
3
1 2
148 150
149 150
-1
-1
99 100 101
149 151
300
1
-1
1 2 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 23 24 25
-1
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24

***********Sample Input***********
20
38 10 7
2 3 1
125 16 14
77 18 7
3 3 1
172 17 9
124 19 11
3 2 2
173 19 18
3 2 2
50 16 7
122 16 13
73 19 6
7 14 1
6 3 3
13 17 4
59 13 7
31 8 7
11 13 3
3 6 2
***********Expected Output***********
5 1 2 3 8 9 10
2
7 1 2 3 4 8 9 10 11 12 13 14 15 16
8 1 2 15 16 17 18
3
-1
6 1 2 3 13 14 15 16 17 18 19
2 1
18 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 19
2 1
9 1 2 3 4 15 16
4 1 2 7 8 9 10 11 12 13 14 15 16
16 1 2 17 18 19
7
3 1 2
7 1 2 3
3 1 9 10 11 12 13
6 1 2 3 4 7 8
8 1 2
2 1
---------------My output---------------
1 2 5 6 7 8 9
2
1 3 4 5 6 7 8 10 11 12 13 14 15 16
8 9 10 11 12 13 14
3
-1


"""
	