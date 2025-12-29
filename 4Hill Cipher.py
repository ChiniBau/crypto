import numpy as np

def modinv(a):
    for i in range(26):
        if (a*i)%26==1:
            return i

def encrypt(text,key):
    if len(text)%2: text+='X'
    res=""
    for i in range(0,len(text),2):
        v=np.array([[ord(text[i])-65],[ord(text[i+1])-65]])
        r=np.dot(key,v)%26
        res+=chr(r[0][0]+65)+chr(r[1][0]+65)
    return res

def decrypt(cipher,key):
    det=int(np.linalg.det(key))%26
    inv=modinv(det)
    adj=np.array([[key[1][1],-key[0][1]],[-key[1][0],key[0][0]]])
    invkey=(inv*adj)%26
    return encrypt(cipher,invkey)

key=np.array([[3,3],[2,5]])

while True:
    print("\n1.Encrypt 2.Decrypt 3.Exit")
    ch=int(input())
    if ch==3: break
    t=input("Text: ").upper()
    print(encrypt(t,key) if ch==1 else decrypt(t,key))
