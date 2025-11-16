import string
import secrets
import random

MIN_LENGTH = 8

def generate(length, lc_enabled, uc_enabled,digits_enabled,symbols_enabled):
    character_classes = ""
    generated = []
       
    if length < MIN_LENGTH:
        return None

    if lc_enabled:
        character_classes += string.ascii_lowercase
        generated.append(str(secrets.choice(string.ascii_lowercase)))
    if uc_enabled:
        character_classes += string.ascii_uppercase
        generated.append(str(secrets.choice(string.ascii_uppercase)))
    if digits_enabled:
        character_classes += string.digits
        generated.append(str(secrets.choice(string.digits)))
    if symbols_enabled:
        character_classes += "!@$%^&*#_-"
        generated.append(str(secrets.choice("!@$%^&*#_-")))
    
    if character_classes == "":
        return None
    
    lengthgen = length - len(generated)
    generated.extend(secrets.choice(character_classes) for i in range(lengthgen))

    random.shuffle(generated)
    
    return "".join(generated) 