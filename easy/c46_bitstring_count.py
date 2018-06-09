def count_bits(num):
    count = 0
    bitstring = bin(num)
    print("Bitstring: " + bitstring)
    for place in bitstring[2:]:
        if place == '1':
            count += 1
            
    print("Num bits on: ", count)
        
if __name__ == '__main__':
    count_bits(2)
    count_bits(4)
    count_bits(6)
