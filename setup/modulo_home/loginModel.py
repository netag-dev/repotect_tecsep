import psycopg2

def fazer_login(email, senha):
    connection = psycopg2.connect( database = "repotec", host = "localhost", user = "postgres", password = "postgres", port = "5433" )  
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM tb_physical_person WHERE pp_email=%s AND pp_senha=%s", (email, senha))
            usrm = cursor.fetchone()
            print(usrm)
            if(usrm):
                return 0
            else:
                return -1

    finally:
        connection.close()       
    