import psycopg2
import conection.connect as connecao

def cadastrar(description):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO sample_location_cp(cutting_dier1) VALUES (%s)", (description,))
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

def editar(description,id):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" UPDATE sample_location_cp SET cutting_dier1 = %s where id = %s """,(description,id))    
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
        cursor.execute(""" DELETE FROM sample_location_cp WHERE id = %s""",(id))
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
    

