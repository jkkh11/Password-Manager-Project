
import hashlib
import requests

def breach_search(password):
    if password == "":
        return None
    hashvar = ((hashlib.sha1(password.encode("utf-8"))).hexdigest()).upper()
    hashprefix = hashvar[0:5]
    hashsuffix = hashvar[5:]
    response = requests.get(f"https://api.pwnedpasswords.com/range/{hashprefix}")

    hashlist = response.text.splitlines()
    

    for line in hashlist:
        if line.startswith(hashsuffix):
            count = line.split(":")[1]
            return count
        
    return "0"

   




