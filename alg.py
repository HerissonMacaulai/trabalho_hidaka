import hashlib
import secrets
import pandas as pd
import string
import os



users_file = "users.csv"


def user_register(username, password):    
    #criar arquivo se ele não existir
    if not os.path.exists(users_file):    
     with open(users_file, mode="w", encoding="utf-8") as users:
        users.writelines("username,password\n")
        
    file = pd.read_csv(users_file)
        
    #verifica se o usuario ja existe
    users = file["username"].tolist()
    if username in users:
       print("deu ruim")
       return False
    else:
        with open(users_file, mode="a", encoding="utf-8") as users:
            users.writelines(f"{username},{password}\n")
            
        #ao adicionar no df, cria um arquivo csv exclusivo pra cada usuario
        with open(f"{username}_data.csv", mode="w", encoding="utf-8") as user_data:
            user_data.writelines("system,user,password\n")
        
        print("bom deu")
        return True

def user_delete(username, password):
    file = pd.read_csv(users_file)
    
    users = file["username"].tolist()
    passwords =file["password"].tolist()
    
    if str(passwords[users.index(username)]) != password:
        return False
    else:
    
        file = file[file["username"] != username]
        file.to_csv(users_file, index=False)
        
        os. remove(f"{username}_data.csv") 
        
        return True    
    
def psswd_delete(user, index):
    file = pd.read_csv(f"{user}_data.csv")
    file = file.drop(index)
    file.to_csv(f"{user}_data.csv", index=False)    
    file = pd.read_csv(f"{user}_data.csv")
    return file
    
    
def new_psswd(user, system, username, password):
     with open(f"{user}_data.csv", mode="a", encoding="utf-8") as users:
            users.writelines(f"{system},{username},{password}\n")

        
def login(username, password):
    #criar arquivo se ele não existir
    if not os.path.exists(users_file):    
     with open(users_file, mode="w", encoding="utf-8") as users:
        users.writelines("username,password\n")
        
    file = pd.read_csv(users_file)
    
    users = file["username"].tolist()
    passwords =file["password"].tolist()
    
    if username not in users:
        return 2
    
    if str(passwords[users.index(username)]) != password:
        return 1
    else:
        return 0
    

def list_psswd(user):
    df = pd.read_csv(f"{user}_data.csv")
    return df.values.tolist()

def edit_line(user, new_system, new_user, new_senha, index):
    file = pd.read_csv(f"{user}_data.csv")
    
    file.at[index, "user"] = new_user
    file.at[index, "system"] = new_system
    file.at[index, "password"] = new_senha
    
    
    
    file.to_csv(f"{user}_data.csv", index = False)
    


def gerar_senha():
   
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation


    upper_char = secrets.choice(uppercase_letters)
    lower_char = secrets.choice(lowercase_letters)
    digit_char = secrets.choice(digits)
    special_char = secrets.choice(special_characters)

    all_chars = upper_char + lower_char + digit_char + special_char

    
    random_bytes = secrets.token_bytes(32)  
    hash_object = hashlib.sha3_256(random_bytes)
    hashed_bytes = hash_object.digest()
    senha_hex = hashed_bytes[:4].hex()

    senha_gerada = all_chars + senha_hex

    return senha_gerada


