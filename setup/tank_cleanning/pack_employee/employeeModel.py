import psycopg2
import conection.connect as connecao

def cadastrar(emp_name, emp_email):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()

        cursor.execute(""" INSERT INTO tb_employee_tc(emp_name, emp_email) values(%s,%s) """,(emp_name, emp_email))    
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
        return -1
    finally:
        if connection:
            cursor.close()
            connection.close()
            return 0


def editar(nome, email, id):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_employee_tc set emp_name = %s, emp_email= %s where id = %s ",(nome,email,id))                
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
        return -1
    finally:
        if connection:
            cursor.close()
            return 0

def delete_data(nome,email):
    connection = connecao.cria_connecao()
    try:
        cursor = connection.cursor()
        cursor.execute(""" DELETE FROM tb_employee_tc WHERE emp_name = %s AND emp_email = %s """,(nome, email))
        connection.commit()
    except Exception as e:
        print(f"Erro: {e}")
        return -1
    finally:
        connection.close()
        return 0   
                
def listar():    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tb_employee_tc")
        dados = cursor.fetchall()
        
        dados_novo = [item[1] for item in dados]

        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados_novo
        

def listar_table():    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tb_employee_tc")
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
            cursor.execute(""" SELECT id FROM tb_employee_tc WHERE emp_name = %s AND emp_email = %s """,(name, email))
            id_empregador = cursor.fetchone()
    finally:
        connection.close()
        return id_empregador
    

def carregar_buscar_id_empregador_por_nome(nome):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT id FROM public.tb_employee_tc WHERE emp_name = %s""",(nome,))
            buscar_id_empregador = cursor.fetchone()


            return buscar_id_empregador
    finally:
        connection.close()
    



