import bcrypt
   
senha = "123456"

hash = bcrypt.hashpw(senha.encode(),bcrypt.gensalt())

print("\n\n senha: "+ senha +"hash: "+ str(hash) +"\n\n")

x = "1234f56"

if bcrypt.checkpw (x.encode(), hash):
    print("deu match")
else:
    print("senha errada...")