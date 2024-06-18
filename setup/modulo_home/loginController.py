from . import loginModel

def carregar_login(email, senha):

    try:

        response = loginModel.fazer_login(email, senha) 
        return response
    
    except Exception as e:
        print(f"Erro ao Fazer Login {e}")
        return -1
     
    