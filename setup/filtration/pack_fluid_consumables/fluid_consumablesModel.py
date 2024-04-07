import psycopg2
import conection.connect as connecao




def listar_type():
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(" SELECT description FROM tb_fluid_consumables_type_ft ")    
        lista_type = cursor.fetchall()

        nova_lista_tipo = [item[0] for item in lista_type]
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            return nova_lista_tipo
        
def listar_consumiveis():
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(" SELECT nome_consumivel FROM tb_consumiveis ")    
        lista_equipamento = cursor.fetchall()

        nova_lista_tipo = [item[0] for item in lista_equipamento]
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            return nova_lista_tipo
        

def buscar_quantidade_stoke( nome_equipamento):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(" SELECT initial_stock FROM tb_consumiveis  WHERE nome_consumivel = %s",(nome_equipamento,))    
        quantidade_stoke = cursor.fetchone()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            return quantidade_stoke


def cadastrar(id_consumivel, id_type, ft_openning_stock, ft_additional_stock, ft_total_stock, ft_daily_used, ft_total_used, ft_closing_bal, id_report_ft):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO tb_filtration_consumables_ft(id_consumivel, id_type, ft_openning_stock, ft_additional_stock, ft_total_stock, ft_daily_used, ft_total_used, ft_closing_bal, id_report_ft)
                       values(%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(id_consumivel, id_type, ft_openning_stock, ft_additional_stock, ft_total_stock, ft_daily_used, ft_total_used, ft_closing_bal, id_report_ft))    
        connection.commit()
        cursor.close()

        cursor = connection.cursor()
        cursor.execute(""" UPDATE tb_consumiveis SET initial_stock = %s WHERE id = %s""",(ft_closing_bal,id_consumivel))
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
                
def listar():    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT *FROM tb_fluid_consumables_ft")
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


def buscar_id( nome_equipamento):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(" SELECT id FROM tb_consumiveis  WHERE nome_consumivel = %s",(nome_equipamento,))    
        id = cursor.fetchone()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            return id
        
def buscar_id_tipo( nome_equipamento):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(" SELECT id FROM tb_fluid_consumables_type_ft  WHERE description = %s",(nome_equipamento,))    
        id = cursor.fetchone()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            return id
        


def listar(job_ref):    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT nome_consumivel,description,ft_openning_stock,ft_additional_stock,ft_total_stock,ft_daily_used,ft_total_used,ft_closing_bal FROM tb_filtration_consumables_ft,tb_fluid_consumables_type_ft,tb_consumiveis,tb_report_header,tb_report_ft
                        WHERE tb_report_header.id = tb_report_ft.id_report_header
                        AND tb_report_ft.id =  tb_filtration_consumables_ft.id_report_ft
                        AND tb_fluid_consumables_type_ft.id = tb_filtration_consumables_ft.id_type
                        AND tb_consumiveis.id = tb_filtration_consumables_ft.id_consumivel
                        AND tb_report_header.rpt_job_ref_number = %s """,(job_ref,))
        dados = cursor.fetchall()
        
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados

    



