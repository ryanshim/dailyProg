'''r/dailyprogrammer [Easy] Challenge 9: sorting algo'''

# Can use python's digit's library sort() function
# following shows merge sort implemented by default
# copy of: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
# need to review

def merge_sort(numbers):
    if len(numbers) > 1:
        mid = len(numbers)//2
        left = numbers[:mid]
        right = numbers[mid:]

    # recursively sort both sublists
        merge_sort(left)
        merge_sort(right)

        x = 0
        y = 0
        z = 0
        while x < len(left) and y < len(right):
            if left[x] < right[y]:
                numbers[z] = left[x]
                x += 1
            else:
                numbers[z] = right[y]
                y += 1
            z += 1

        while x < len(left):
            numbers[z] = left[x]
            x += 1
            z += 1

        while y < len(right):
            numbers[z] = right[y]
            y += 1
            z += 1

    print numbers

string_list = raw_input('Enter digits to sort: ')
numbers = []
for num in string_list:
    numbers.append(int(num))
merge_sort(numbers)
