import json
import os
import hashlib
from getpass import getpass
from cryptography.fernet import Fernet

password_file = "passwords.enc"
encryption_key = "encrypt.key"
system_pswd = "system.hash"

def encrypt_setup():
    if not os.path.exists(encryption_key):
        key = Fernet.generate_key()
        with open(encryption_key,"wb") as f:
            f.write(key)
    return open(encryption_key,"rb").read()

def create_system_pswd(x,y):
    if not os.path.exists(system_pswd):
        system_password = x
        confirm = y
        if system_password == confirm:
            with open(system_pswd,"wb") as f:
                f.write(hashlib.sha256(system_password.encode()).digest())
            return True
        else:
            return False
    else:
        return

def load(cipher):
    if os.path.exists(password_file):
        with open(password_file,"rb") as f:
            return json.loads(cipher.decrypt(f.read()).decode())
    return {}

def pswd_verification(password):
    with open(system_pswd,"rb") as f:
        return f.read() == hashlib.sha256(password.encode()).digest()
    

def save(passwords, cipher):
    with open(password_file, "wb") as f:
        f.write(cipher.encrypt(json.dumps(passwords).encode()))

def add(passwords,s,u,p):
    service = s
    if service in passwords:
        return
    username = u
    password = p
    passwords[service] = {"username": username, "password": password}

def delete(passwords,del_service):
    service = del_service
    del passwords[service]


def update(passwords, s, u, p):
    service = s
    if service in passwords:
        new_user = u
        new_pswd = p
        if new_user:
            passwords[service]["username"] = new_user
        if new_pswd:
            passwords[service]["password"] = new_pswd
            return True
    else:
        return False


    

