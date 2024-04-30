import psycopg2
import conection.connect as connecao
import config_email.config_email

def cadastrar(description):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO sample_location_cp(cutting_dier1) VALUES (%s)", (description,))
        connection.commit()
        cursor.close()
        return 0
    except Exception as e:
        print(f"Erro: {e}")
        body = f"Erro: {e}"
        config_email.config_email.save_error(body)
        return -1

def editar(description,id):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" UPDATE sample_location_cp SET cutting_dier1 = %s where id = %s """,(description,id))    
        connection.commit()
        cursor.close()
        return 0
    except Exception as e:
        print(f"Erro: {e}")
        body = f"Erro: {e}"
        config_email.config_email.save_error(body)
        return -1

def delete_data(id):
    connection = connecao.cria_connecao()
    try:
        cursor = connection.cursor()
        cursor.execute(""" DELETE FROM sample_location_cp WHERE id = %s""",(id))
        connection.commit()
        return 0
    except Exception as e:
        print(f"Erro: {e}")
        body = f"Erro: {e}"
        config_email.config_email.save_error(body)
        return -1   
                
def listar():    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM sample_location_cp ORDER BY id ASC")
        dados = cursor.fetchall()
        dados_novo = [(item[0],item[1]) for item in dados]
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
        cursor.execute("SELECT * FROM sample_location_cp  ORDER BY id ASC")
        dados = cursor.fetchall()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados
    

