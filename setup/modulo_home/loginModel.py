import psycopg2

def fazer_login(email, senha):
    connection = psycopg2.connect( database = "repotec", host = "localhost", user = "postgres", password = "postgres", port = "5432" )  
    try:
        with connection.cursor() as cursor:
            cursor.execute(" SELECT * FROM tb_physical_person WHERE pp_email=%s AND pp_senha=%s", (email, senha))
            usrm = cursor.fetchone()
            if(usrm):
                tipo_usuario = usrm[6]
                return [tipo_usuario,0]
            else:
                return -1
    except Exception as e:
        error = "Erro ao efectuar o Login:"+str(e)
        print(str(error))
        return -1
    finally:
        connection.close()       
    