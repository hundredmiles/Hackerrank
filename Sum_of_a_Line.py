line = input("Enter the line of numbers: ")
arr = list(map(int, line.split()))
print('No. of elements: ', len(arr))
print('Sum of numbers: ', sum(arr))