import psycopg2
import conection.connect as connecao

def cadastrar(emp_name, emp_email, personel_position):
    try:  
        connection = connecao.cria_connecao()
        cursor = connection.cursor()

        cursor.execute(""" INSERT INTO tb_employee_ft(emp_name, emp_email, emp_personel_position)
                       values(%s,%s,%s) """,(emp_name, emp_email, personel_position))    
        connection.commit()
        cursor.close()
        return 0 
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
        return -1
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
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tb_employee_ft")
        dados = cursor.fetchall()
        
        novos_dados = [item[1] for item in dados]

        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return novos_dados
        

def listar_table():    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("""SELECT emp_name,emp_email,pp_description FROM tb_employee_ft,tb_personal_position
WHERE tb_employee_ft.emp_personel_position = tb_personal_position.id""")
        dados = cursor.fetchall()
        
        

        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados

def buscar_id_by_name_email(name, email):
    connection = connecao.cria_connecao()
    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT id FROM tb_employee_ft WHERE name = %s AND email = %s """,(name, email))
            id_size = cursor.fetchone()
    finally:
        connection.close()
        return id_size
    
def apagar(nome,email):
    connection = connecao.cria_connecao()
    try:
        cursor = connection.cursor()
        cursor.execute(""" DELETE FROM tb_employee_ft WHERE emp_name = %s AND emp_email = %s """,(nome, email))
        connection.commit()
        return 0
    except Exception as e:
        print(f"Erro: {e}")
        return -1
    finally:
        connection.close()
        


