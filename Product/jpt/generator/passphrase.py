import secrets


def generate(length,uc_enabled, digits_enabled, delimiter):
    final = ""
    words = open("words_alpha.txt","r").read()
    wordlist = words.splitlines()

    if delimiter:
        final = "-".join(secrets.choice(wordlist).title() if uc_enabled else secrets.choice(wordlist) for i in range(length))
    else:
        final = "".join(secrets.choice(wordlist).title() if uc_enabled else secrets.choice(wordlist) for i in range(length))
    
    if digits_enabled:
        return final+(str(secrets.choice(list(range(0,100)))))
    
    return final
 

