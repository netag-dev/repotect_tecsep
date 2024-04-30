import psycopg2
from config_email.config_email import save_error

def fazer_login(email, senha):
    connection = psycopg2.connect( database = "repotec", host = "102.219.126.14", user = "postgres", password = "Angola2023#", port = "5432" )  
    try:
        with connection.cursor() as cursor:
            cursor.execute(" SELECT * FROM tb_physical_person WHERE pp_email=%s AND pp_senha=%s", (email, senha))
            usrm = cursor.fetchone()
            if(usrm):
                return 0
            else:
                return -1
    except Exception as e:
        error = "Erro ao efectuar o Login:"+str(e)
        save_error(str(error))
        return -1
    finally:
        connection.close()       
    