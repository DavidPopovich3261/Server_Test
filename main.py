from fastapi import FastAPI
import uvicorn
import Ciphers
from pydantic import BaseModel
import json
app=FastAPI()


class Caesar(BaseModel):
    text:str
    offset:int
    mode:str

class Fence(BaseModel):
    text:str

@app.get("/test")
def test():
    return json.dumps({"msg":"hi from test"})

@app.get("/test/{name}")
def name(name):
    with open("names.txt","a") as f:
        f.write(f"{name}\n")
    return json.dumps({"msg":"saved user"})



@app.post("/caesar")
def caesar(item:Caesar):
    if item.mode=="encrypt":
        encrypt=Ciphers.caesar_encrypt(item.text,item.offset)
        return json.dumps({"encrypted_text":encrypt})
    elif item.mode=="decrypt":
        decrypt=Ciphers.caesar_decrypt(item.text,item.offset)
        return json.dumps({"decrypted_text":decrypt})



@app.get("/fence/encrypt")
def fence_encrypt(text):
    encrypt=Ciphers.fence_encrypt(text)
    return json.dumps({"encrypted_text":encrypt})



@app.post("/fence/decrypt")
def fence_decrypt(item:Fence):
    decrypt=Ciphers.fence_decrypt(item.text)
    return json.dumps({"decrypted":decrypt})

