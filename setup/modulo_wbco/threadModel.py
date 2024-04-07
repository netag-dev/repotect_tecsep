import psycopg2
import conection.connect as connecao


def listar_thread_con():
    connection = connecao.cria_connecao()
    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT thc,thc_description FROM tb_thread_con ORDER BY id ASC""")
            lista_thread = cursor.fetchall()
    finally:
        connection.close()
        return lista_thread


def buscar_id_by_description(description,thread):
    connection = connecao.cria_connecao()
    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT id FROM tb_thread_con WHERE thc_description = %s AND thc = %s """,(description,thread))
            id_thred = cursor.fetchone()
            print(id_thred)
    finally:
        connection.close()
        return id_thred   

def editar_thread(thread,description,id):
    connection = connecao.cria_connecao()
    try:
         with connection.cursor() as cursor:
             cursor.execute(""" UPDATE tb_thread_con SET thc_description = %s, thc = %s WHERE id = %s  """,(description,thread,id))
             connection.commit()
    except Exception as e:
        print(f"Erro {e}")
        return -1
    finally:  
        connection.close()
        return 0 


def delete_data(description,thread):
    connection = connecao.cria_connecao()
    try:
        cursor = connection.cursor()
        cursor.execute(""" DELETE FROM tb_thread_con WHERE thc_description = %s AND thc = %s """,(description,thread))
        connection.commit()
    except Exception as e:
        print(f"Erro: {e}")
        return -1
    finally:
        connection.close()
        return 0   

def save_data(thread,description):
    connection = connecao.cria_connecao()
    try:
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO tb_thread_con(thc,thc_description) values(%s,%s) """,(thread,description))
        connection.commit()
    except Exception as e:
        print(f"Erro: {e}")
        return -1
    finally:
        connection.close()
        return 0
    

def listar_thread_para_combo():
    connection = connecao.cria_connecao()

    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT thc FROM tb_thread_con ORDER BY id ASC""")
            
            lista_thread = cursor.fetchall()
            nova_lista_thread = [item[0] for item in lista_thread]
    except Exception as e:
        print(f"erro {e}")
    finally:
        connection.close()
        return nova_lista_thread
    

def buscar_id_by_tch(tch):
    connection = connecao.cria_connecao()

    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT id FROM tb_thread_con WHERE thc = %s """,(tch,))
            id_thread = cursor.fetchone()
    except Exception as e:
        print(f"erro {e}")
    finally:
        connection.close()
        return id_thread
