import psycopg2
import conection.connect as connecao

def cadastrar(type_fluid_proprieties, value, report_information_cp):
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO drilling_fluid_proprieties_cp(type_fluid_proprieties, value, report_information_cp) VALUES (%s, %s, %s)""", (type_fluid_proprieties, value, report_information_cp))
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao inserir novo registo: {e}")
        return -1
    finally:
        if connection:
            cursor.close()
            connection.close()
            return 0
def editar(type_fluid_proprieties, value, report_information_cp):
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE drilling_fluid_proprieties_cp SET type_fluid_proprieties = %s, value = %s, report_information_cp = %s, WHERE id = %s", (type_fluid_proprieties, value, report_information_cp))
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao atualizar dados")
        return -1
    finally:
        if connection:
            cursor.close()
            return 0
        
def eliminar(type_fluid_proprieties, value, report_information_cp):
    connection = connecao.cria_connecao()
    try:
        cursor = connection.cursor()
        cursor.execute(""" DELETE FROM drilling_fluid_proprieties_cp WHERE type_fluid_proprieties = %s AND value = %s""", (type_fluid_proprieties, value))
        connection.commit()
    except Exception as e:
        print(f"Erro: {e}")
        return -1
    finally:
        connection.close()
        return 0
    
################## Listagens #####################

def listar_drilling_fluid():
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM drilling_fluid_proprieties_cp")
        dados = cursor.fetchall()
        dados_novo = [item[1] for item in dados]
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados_novo                        
        