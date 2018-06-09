def caeser_cipher(shamt, plain):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "!@#$%^&*()_+=,.;-'\"[]`~<>/?:{}\| "
    plain = plain.upper()
    encrypted = ""
    
    for ch in plain:
        if ch not in symbols:
            index = alphabet.index(ch) + shamt
            if index > 25:                      # roll over; 26th index = A
                index %= 26                     # get remaining roll over
                encrypted += alphabet[index]
            else:
                encrypted += alphabet[index]
        else:
            encrypted += ch 
    return encrypted
    

if __name__ == '__main__':
    print(caeser_cipher(3, "Hello"))
    print(caeser_cipher(6, "Daily programmer"))
    
    dp = caeser_cipher(6, "Daily Programmer")
    dp2 = caeser_cipher(20, dp)
    print(dp2)
