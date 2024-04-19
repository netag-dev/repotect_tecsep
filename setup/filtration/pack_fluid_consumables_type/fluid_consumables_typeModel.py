import psycopg2
import conection.connect as connecao

def cadastrar(type,description):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()

        cursor.execute(""" INSERT INTO tb_fluid_consumables_type_ft(type,description)
                       values(%s,%s) """,(type,description,))    
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
        return -1
    finally:
       return 0

def editar(type,desc,id):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_fluid_consumables_type_ft set type = %s, description = %s where id = %s ",(type,desc,id))                
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
        return -1
    finally:
       return 0

def eliminar(param):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tb_fluid_consumables_type_ft WHERE id = '"+param+"' ")
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
        return -1
    finally:
       return 0
                
def listar():    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT  *FROM tb_fluid_consumables_type_ft")
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
    

def buscar_by_id(id):
    connection = connecao.cria_connecao()
    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT description FROM tb_fluid_consumables_type_ft WHERE id = %s """,(id))
            dados = cursor.fetchone()
    except Exception as e:
        print(f"{e}")
        return -1
    finally:
        connection.close()
        return dados[0]
    



