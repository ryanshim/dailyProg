'''r/dailyprogrammer [Easy] Challenge 14: block reversal'''

def reverse(aList, block):
    new_list = []
    for i in range(0,len(aList),block):
        new_list.append(aList[i+1])
        new_list.append(aList[i])
    print new_list

aList = [12, 24, 32, 44, 55, 66]
block = 2
reverse(aList, block)
