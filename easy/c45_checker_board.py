def make_board(grid):
    print("*" * (grid * 4 + 1))
    alt = False
    
    block = "###"
    blank = "*   *"
    
    if grid % 2 == 0:
        for i in range(grid):
            if alt:
                for j in range(3):
                    print('*' + (block + blank) * (grid // 2))
                    alt = False
            else:
                for j in range(3):
                    print((blank + block) * (grid // 2) + '*')
                    alt = True
            print("*" * (grid * 4 + 1))
    else:
        for i in range(grid):
            if alt:
                for j in range(3):
                    print('*' + (block + blank) * (grid // 2) + block + '*')
                    alt = False
            else:
                for j in range(3):
                    print((blank + block) * (grid // 2) + blank)
                    alt = True
            print("*" * (grid * 4 + 1))       

if __name__ == '__main__':
    make_board(2)
    print('\n\n')
    make_board(3)
    print('\n\n')
    make_board(4)
    print('\n\n')
    make_board(5)
