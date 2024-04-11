import psycopg2
import conection.connect as connecao

def cadastrar(nome_consumivel,initial_stock):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO tb_consumiveis(nome_consumivel, initial_stock) values(%s, %s) """,(nome_consumivel, initial_stock))    
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

def editar(param1, param2,param3):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_consumiveis set nome_consumivel = %s, initial_stock = %s WHERE  id = %s",(param1,param2,param3))                
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
        return 0

def eliminar(param):
    try:  
        connection = connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tb_consumiveis WHERE id = %s ",(param))
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
                
def listar():    
    try: 
        connection = connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tb_consumiveis")
        dados = cursor.fetchall()
       
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        return dados

def buscar_id(nome_consumivel, initial_stock):
    connection = psycopg2.connect( database = "repotec", host = "localhost", user = "postgres", password = "postgres", port = "5432" )
    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT id FROM tb_consumiveis WHERE nome_consumivel = %s AND initial_stock = %s """,(nome_consumivel, initial_stock))
            id_size = cursor.fetchone()
    finally:
        connection.close()
        return id_size
    


