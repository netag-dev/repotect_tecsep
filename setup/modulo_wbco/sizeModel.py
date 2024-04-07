import psycopg2
import conection.connect as connecao

#Função para listar todos os Sizes 
def listar_size():
    connection = connecao.cria_connecao()

    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT size,description FROM tb_wbco_size ORDER BY id ASC""")
            
            lista_size = cursor.fetchall()

            #nova_lista_size = [item[1] for item in lista_size]
            print(lista_size)

            return 0
    finally:
        connection.close()
        return lista_size


def buscar_id_by_size_description(size,description):
    connection = connecao.cria_connecao()

    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT id FROM tb_wbco_size WHERE size = %s AND description = %s """,(size,description))
            id_size = cursor.fetchone()
    finally:
        connection.close()
        return id_size
    
def save_editad_data(size,description,id):
    connection = connecao.cria_connecao()
    try:
         with connection.cursor() as cursor:
             cursor.execute(""" UPDATE tb_wbco_size SET size = %s, description = %s WHERE id = %s  """,(size,description,id))
             connection.commit()
    except Exception as e:
        print(f"Erro {e}")
        return -1
    finally:
        connection.close()
        return 0   


def delete_data(size,description):
    connection = connecao.cria_connecao()
    try:
        cursor = connection.cursor()
        cursor.execute(""" DELETE FROM tb_wbco_size WHERE size = %s AND description = %s """,(size,description))
        connection.commit()
    except Exception as e:
        print(f"Erro: {e}")
        return -1
    finally:
        connection.close()
        return 0
    
def save_data(size,description):
    connection = connecao.cria_connecao()
    try:
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO tb_wbco_size(size,description) values(%s,%s) """,(size,description))
        connection.commit()
    except Exception as e:
        print(f"Erro: {e}")
        return -1
    finally:
        connection.close()
        return 0
    

def listar_size_para_combo():
    connection = connecao.cria_connecao()

    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT size FROM tb_wbco_size ORDER BY id ASC""")
            
            lista_size = cursor.fetchall()
            nova_lista_size = [item[0] for item in lista_size]
    except Exception as e:
        print(f"erro {e}")
    finally:
        connection.close()
        return nova_lista_size
    

def buscar_id_by_size(size):
    connection = connecao.cria_connecao()

    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT id FROM tb_wbco_size WHERE size = %s """,(size,))
            id_size = cursor.fetchone()
    finally:
        connection.close()
        return id_size
