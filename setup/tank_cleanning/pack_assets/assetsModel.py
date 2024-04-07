import psycopg2
import conection.connect as connecao


def cadastrar(as_name, as_quantity):
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO tb_assets_tc (as_name, as_quantity) 
                       values(%s,%s)""",(as_name, as_quantity))    
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

def editar(param1, param2, param4):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_assets_tc set as_name = %s, as_quantity = %s where id = %s ",(param1,param2,param4))                
        connection.commit()
        cursor.close()
        return 0
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
        return -1
    finally:
        if connection:
            cursor.close()

def eliminar(param1, param2):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tb_assets_tc as_name = '"+param1+"' AND as_quantity = '"+param2+"' ")
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
        cursor.execute("SELECT *FROM tb_assets_tc")
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
        cursor.execute("SELECT *FROM tb_assets_tc")
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
        cursor.execute("SELECT id FROM tb_assets_tc WHERE as_name = %s AND as_quantity = %s",(nome,stoq))
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
        


def buscar_asset(ref_report):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT as_name, as_quantity, 'Asset' as asset_type
                        FROM tb_assets_tc, tb_asset_tc_report, tb_report_tc
                        WHERE tb_asset_tc_report.id_asset = tb_assets_tc.id
                        AND tb_asset_tc_report.id_report_tc = tb_report_tc.id
                        AND tb_report_tc.id = %s""",(ref_report,))
            
            lista_hse = cursor.fetchall()


            return lista_hse
    finally:
        connection.close()


