import psycopg2
import conection.connect as connecao

def cadastrar(model,serial_number):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO model_average_cp(model,serial_number) values(%s,%s) """,(model,serial_number))    
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
        return e
    finally:
        if connection:
            cursor.close()
            connection.close()
            return 0

def editar(model,serial_number,id):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" UPDATE model_average_cp SET model = %s, serial_number = %s where id = %s """,(model,serial_number,id))    
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

def delete_data(id):
    connection = connecao.cria_connecao()
    try:
        cursor = connection.cursor()
        cursor.execute(""" DELETE FROM model_average_cp WHERE id = %s""",(id))
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
        cursor.execute("SELECT * FROM model_average_cp")
        dados = cursor.fetchall()
        dados_novo = [(item[0], item[1], item[2]) for item in dados]
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
        cursor.execute("SELECT * FROM model_average_cp")
        dados = cursor.fetchall()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados
    

