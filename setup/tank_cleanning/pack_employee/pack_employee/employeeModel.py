import psycopg2





def cadastrar(emp_name, emp_email):
    try: 
        connection = psycopg2.connect( database = "repotec", host = "localhost", user = "postgres", password = "postgres", port = "5432" )
        cursor = connection.cursor()

        cursor.execute(""" INSERT INTO tb_employee_ft(emp_name, emp_email)
                       values(%s,%s) """,(emp_name, emp_email))    
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()


def editar(param1, param2, param3):
    try: 
        connection = psycopg2.connect( database = "repotec", host = "localhost", user = "postgres", password = "0000", port = "5432" )
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_employee_ft set emp_name = '"+param2+"', emp_email= '"+param3+"' where id = '"+param1+"' ")                
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()

def eliminar(param):
    try: 
        connection = psycopg2.connect( database = "repotec", host = "localhost", user = "postgres", password = "0000", port = "5432" )
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tb_employee_ft WHERE id = '"+param+"' ")
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
                
def listar():    
    try: 
        connection = psycopg2.connect( database = "repotec", host = "localhost", user = "postgres", password = "postgres", port = "5432" )
        cursor = connection.cursor()
        cursor.execute("SELECT *FROM tb_employee_ft")
        dados = cursor.fetchall()
        
        novos_dados = [item[1] for item in dados]

        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return novos_dados

def buscar_id_by_name_email(name, email):
    connection = psycopg2.connect( database = "repotec", host = "localhost", user = "postgres", password = "postgres", port = "5432" )
    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT id FROM tb_employee_ft WHERE name = %s AND email = %s """,(name, email))
            id_size = cursor.fetchone()
    finally:
        connection.close()
        return id_size
    



