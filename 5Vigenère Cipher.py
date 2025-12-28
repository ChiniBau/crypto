def encrypt(text,key):
    res=""
    for i in range(len(text)):
        res+=chr((ord(text[i])+ord(key[i%len(key)])-130)%26+65)
    return res

def decrypt(text,key):
    res=""
    for i in range(len(text)):
        res+=chr((ord(text[i])-ord(key[i%len(key)])+26)%26+65)
    return res

while True:
    print("\n1.Encrypt 2.Decrypt 3.Exit")
    ch=int(input())
    if ch==3: break
    t=input("Text: ").upper()
    k=input("Key: ").upper()
    print(encrypt(t,k) if ch==1 else decrypt(t,k))
