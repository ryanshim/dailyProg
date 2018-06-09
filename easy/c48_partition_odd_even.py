def partition_even_odd(num_list):
    left = []
    right = []
    
    for num in num_list:
        if num % 2 == 0:
            right.append(num)
        else:
            left.append(num)
    
    return left + right
    
        
if __name__ == '__main__':
    l1 = [5, 2, 1, 13, 9]
    print(partition_even_odd(l1))
