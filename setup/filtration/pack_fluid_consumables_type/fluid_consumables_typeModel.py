import psycopg2
import conection.connect as connecao

def cadastrar(description):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()

        cursor.execute(""" INSERT INTO tb_fluid_consumables_type_ft(description)
                       values(%s) """,(description))    
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()


def editar(param1, param2):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_fluid_consumables_type_ft set description = '"+param2+"' where id = '"+param1+"' ")                
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
        cursor.execute("DELETE FROM tb_fluid_consumables_type_ft WHERE id = '"+param+"' ")
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
        cursor.execute("SELECT *FROM tb_fluid_consumables_type_ft")
        dados = cursor.fetchall()
        
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        return dados

def buscar_id_by_name_email(description):
    connection = connecao.cria_connecao()
    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT id FROM tb_fluid_consumables_type_ft WHERE description = %s """,(description))
            id_size = cursor.fetchone()
    finally:
        connection.close()
        return id_size
    



