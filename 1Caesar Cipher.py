def encrypt(text, shift):
    res = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            res += chr((ord(c)-base+shift)%26+base)
        else:
            res += c
    return res

def decrypt(text, shift):
    return encrypt(text, -shift)

while True:
    print("\n1.Encrypt  2.Decrypt  3.Exit")
    ch = int(input("Choice: "))
    if ch == 3:
        break
    msg = input("Message: ")
    s = int(input("Shift: "))
    print(encrypt(msg,s) if ch==1 else decrypt(msg,s))
