


abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar_encrypt(text:str,steps:int)->str:
    text=text.lower()
    encrypt=''
    for letter in text:
        if letter in abc:
            encrypt+=abc[(abc.index(letter)+steps) % 26]
    return encrypt

def caesar_decrypt(text:str,steps:int)->str:
    text=text.lower()
    decrypt=''
    for letter in text:
        if letter in abc:
            decrypt+=abc[(abc.index(letter)-steps) % 26]
    return decrypt


def fence_encrypt(text:str)->str:
    text=text.replace(" ",'')
    encrypt=''
    for letter in text[::2]:
        if letter in abc:
            encrypt+=letter
    for letter in text[1::2]:
        if letter in abc:
            encrypt += letter
    return encrypt

def fence_decrypt(text:str)->str:
    decrypt = ''
    for i ,l in enumerate(text[(len(text)/2).__ceil__():]):
        decrypt+=text[i]
        decrypt+=l
    if len(decrypt)<len(text):
        decrypt+=text[len(text)//2]
    return decrypt



