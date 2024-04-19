import psycopg2
import conection.connect as connecao

def cadastrar(pi_name, pi_quantity):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO tb_pipe_tc (pi_name, pi_daily_used) 
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
        cursor.execute("UPDATE tb_pipe_tc set pi_name = %s, pi_daily_used = %s  where id = %s ",(nome,stoq,id))                
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
        return -1
    finally:
        if connection:
            cursor.close()
            return 0

def eliminar(param1):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" DELETE FROM tb_pipe_tc WHERE id = %s """,(param1,))
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

        

def buscar_ppe(ref_report):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT pi_name,open_stock,aditional_stock,total_stock,quantidade_add,closing_bal ,'PPE' as ppe_type FROM tb_pipe_tc,tb_ppe_tc_report, tb_report_tc
                            WHERE tb_ppe_tc_report.id_ppe = tb_pipe_tc.id
                            AND tb_ppe_tc_report.id_report_tc = tb_report_tc.id
                            AND tb_report_tc.id = %s ORDER BY tb_ppe_tc_report.id DESC""",(ref_report,))
            
            lista_hse = cursor.fetchall()


            return lista_hse
    finally:
        connection.close()

def buscar_quantidade_stoke(nome_equipamento):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(" SELECT pi_daily_used FROM tb_pipe_tc  WHERE pi_name = %s",(nome_equipamento,))    
        quantidade_stoke = cursor.fetchone()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
        return -1
    finally:
         return quantidade_stoke

