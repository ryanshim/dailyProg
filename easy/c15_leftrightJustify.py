'''r/dailyprogrammer [Easy] Challenge 15: left right justify'''
'''currently performs right justification with "0" to show justification'''

f = open('c15_sample.txt', 'r')
temp_line = []
for line in f.readlines():
    temp_line.append(line)
f.close()

f = open('c15_sample.txt', 'w')
for x in range(len(temp_line)):
    temp_line[x] = temp_line[x].rjust(50, '0')
    f.write(temp_line[x])
f.close()
