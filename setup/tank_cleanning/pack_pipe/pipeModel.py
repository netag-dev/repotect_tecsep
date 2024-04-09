import psycopg2
import conection.connect as connecao

def cadastrar(pi_name, pi_quantity):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO tb_pipe_tc (pi_name, pi_quantity) 
                       values(%s,%s)""",(pi_name, pi_quantity))    
        connection.commit()
        cursor.close()
        return 0
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
        return -1
    finally:
        if connection:
            cursor.close()
            connection.close()

def editar(nome, stoq, id):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_pipe_tc set pi_name = %s, pi_quantity = %s  where id = %s ",(nome,stoq,id))                
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
        return -1
    finally:
        if connection:
            cursor.close()
            return 0

def eliminar(param1, param2):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" DELETE FROM tb_pipe_tc WHERE pi_name = %s AND pi_quantity = %s """,(param1, param2))
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
        cursor.execute("SELECT * FROM tb_pipe_tc")
        dados = cursor.fetchall()
       
        dados_novo = [item[1] for item in dados]
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            return dados_novo


def listar_table(): 
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tb_pipe_tc")
        dados = cursor.fetchall()
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao Listar dados no tb_pipe_tc: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            return dados
            print("Conexão fechada.")



def buscar_id_nome_stoq(nome,stoq):    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM tb_pipe_tc WHERE pi_name = %s AND pi_daily_used = %s",(nome,stoq))
        dados = cursor.fetchone()
        print(dados)
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            return dados[0]
        

def buscar_ppe(ref_report):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT pi_name,pi_daily_used ,'PPE' as ppe_type FROM tb_pipe_tc,tb_ppe_tc_report, tb_report_tc
                            WHERE tb_ppe_tc_report.id_ppe = tb_pipe_tc.id
                            AND tb_ppe_tc_report.id_report_tc = tb_report_tc.id
                            AND tb_report_tc.id = %s """,(ref_report,))
            
            lista_hse = cursor.fetchall()


            return lista_hse
    finally:
        connection.close()

