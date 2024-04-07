from . import loginModel

def carregar_login(email, senha):
    if(loginModel.fazer_login(email, senha) == 0):
        return 0
    elif (loginModel.fazer_login(email, senha) == -1):
        return -1
     
    