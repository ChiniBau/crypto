def encrypt(text,key):
    rail=['' for _ in range(key)]
    r,d=0,1
    for c in text:
        rail[r]+=c
        r+=d
        if r==0 or r==key-1: d*=-1
    return ''.join(rail)

def decrypt(cipher,key):
    n=len(cipher)
    rail=[['\n']*n for _ in range(key)]
    r,d=0,1
    for i in range(n):
        rail[r][i]='*'
        r+=d
        if r==0 or r==key-1: d*=-1
    idx=0
    for i in range(key):
        for j in range(n):
            if rail[i][j]=='*':
                rail[i][j]=cipher[idx]; idx+=1
    res=""
    r,d=0,1
    for i in range(n):
        res+=rail[r][i]
        r+=d
        if r==0 or r==key-1: d*=-1
    return res

while True:
    print("\n1.Encrypt 2.Decrypt 3.Exit")
    ch=int(input())
    if ch==3: break
    t=input("Text: ")
    k=int(input("Key: "))
    print(encrypt(t,k) if ch==1 else decrypt(t,k))
