import psycopg2
import conection.connect as connecao

def cadastrar(param1, param2, param3):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO tb_project_description_tc values('"+param1+"','"+param2+"','"+param3+"') ")    
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
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_project_description_tc set pd_description = '"+param2+"', id_physical_person = '"+param3+"' where id = '"+param1+"' ")                
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()

def eliminar(param):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tb_project_description_tc WHERE id = '"+param+"' ")
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
        cursor.execute("SELECT *FROM tb_project_description_tc")
        dados = cursor.fetchall()
        for linha in dados:
            print(linha)
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()

    



