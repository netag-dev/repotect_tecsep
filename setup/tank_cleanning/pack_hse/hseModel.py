import psycopg2
import conection.connect as connecao

def cadastrar(id_typehse, hse_quantity, hse_comments, id_report_tc):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO tb_hse_tc(id_typehse, hse_quantity, hse_comments, id_report_tc) values(%s,%s,%s,%s)",(id_typehse, hse_quantity, hse_comments, id_report_tc))    
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def editar(param1, param2, param3, param4, param5, param6, param7):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_hse_tc set hse_quantity = '"+param2+"', hse_comments = '"+param3+"', id_typeHse = '"+param4+"', id_physical_person = '"+param5+"' where id = '"+param1+"' ")                
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
        cursor.execute("DELETE FROM tb_hse_tc WHERE id = '"+param+"' ")
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
        cursor.execute("SELECT  *FROM tb_hse_tc")
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


def listar_tipo_hse():    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT thse_description FROM tb_typehse_tc")
        lista_tipo_hse = cursor.fetchall()

        lista_convertida_tipo = [item[0] for item in lista_tipo_hse]
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()

            return lista_convertida_tipo
        
def buscar_id_hse_por_tipo(tipo):
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT id FROM public.tb_typehse_tc WHERE tb_typehse_tc.thse_description = %s """,(tipo,))
        id_turno = cursor.fetchone()
        cursor.close()
    except Exception as e:
        print(f"Erro ao retornar id do turno : {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

            return id_turno
        

def buscar_chse(ref_report):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT thse_description,hse_quantity,hse_comments FROM tb_typehse_tc,tb_hse_tc,tb_report_tc
                    WHERE tb_hse_tc.id_typehse = tb_typehse_tc.id AND
                    tb_hse_tc.id_report_tc = tb_report_tc.id AND tb_report_tc.id = %s
                    ORDER BY tb_typehse_tc.id ASC  """,(ref_report,))
            
            lista_hse = cursor.fetchall()


            return lista_hse
    finally:
        connection.close()

    



