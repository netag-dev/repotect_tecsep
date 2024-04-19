import psycopg2
import conection.connect as connecao

def cadastrar(cs_name, cs_quantity):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO tb_consumables_tc (cs_name, cs_quantity) 
                       values(%s,%s)""",(cs_name, cs_quantity))    
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

def editar(param1, param2, param3):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_consumables_tc set cs_name = %s, cs_daily_used = %s where id = %s ",(param1,param2,param3))                
        connection.commit()
        cursor.close()
        return 0
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
        return -1
    finally:
        if connection:
            cursor.close()

def eliminar(nome,quantidade):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tb_consumables_tc WHERE cs_name = %s AND cs_daily_used = %s ",(nome,quantidade))
        connection.commit()
        cursor.close()
        return 0
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
        return -1
    finally:
        if connection:
            cursor.close()
                
def listar():    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tb_consumables_tc")
        dados = cursor.fetchall()
        
        dados_novo = [item[1] for item in dados]

        connection.commit()
        cursor.close()
        return dados
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
        return -1
    finally:
        if connection:
            cursor.close()
            return dados_novo
        

def listar_table():    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tb_consumables_tc")
        dados = cursor.fetchall()
        

        connection.commit()
        cursor.close()
        return dados
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
        return -1
    finally:
        if connection:
            cursor.close()
            return dados
        

def buscar_id_nome_stoq(nome,stoq):    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM tb_consumables_tc WHERE cs_name = %s AND cs_daily_used = %s",(nome,stoq))
        dados = cursor.fetchone()
       
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            return dados[0]
        

def buscar_consumiveis(ref_report):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT cs_name,open_stock,aditional_stock,total_stock,cs_daily_used,closing_bal ,'Consumable' as consumivel_type FROM tb_consumables_tc,tb_consumiveis_tc_report, tb_report_tc
                            WHERE tb_consumiveis_tc_report.id_consumiveis = tb_consumables_tc.id
                            AND tb_consumiveis_tc_report.id_report_tc = tb_report_tc.id
                            AND tb_report_tc.id = %s """,(ref_report,))
            
            lista_hse = cursor.fetchall()


            return lista_hse
    finally:
        connection.close()


def buscar_quantidade_stoke(nome_equipamento):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(" SELECT cs_daily_used FROM tb_consumables_tc  WHERE cs_name = %s",(nome_equipamento,))    
        quantidade_stoke = cursor.fetchone()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
        return -1
    finally:
         return quantidade_stoke



            

