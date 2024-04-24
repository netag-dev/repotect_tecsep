import psycopg2
import conection.connect as connecao

def cadastrar(id_non_produtive_type, npm_hours, npm_comments, id_report_tc):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO tb_non_produtive_man_tc(id_non_produtive_type, npm_hours, npm_comments, id_report_tc)
                       values (%s,%s,%s,%s)""",(id_non_produtive_type, npm_hours, npm_comments, id_report_tc))    
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def editar(param1, param2, param3, param4, param5):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_non_produtive_man_tc set npm_hours = '"+param2+"', npm_comments = '"+param3+"', id_non_produtive_type = '"+param4+"', id_physical_person = '"+param5+"' where id = '"+param1+"' ")                
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
        cursor.execute("DELETE FROM tb_non_produtive_man_tc WHERE id = '"+param+"' ")
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
        cursor.execute("SELECT *FROM tb_non_produtive_man_tc")
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


def buscar_produtive_man_hour(ref_report):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT pm_work_order,
                        pm_description,pm_original_hours,pm_hours_brocked_td,pm_qt_hours_brocked_td,pm_hours_brocked_date,pm_hours_remaining_td,
                        pm_visual_perc_complete FROM tb_produtive_man_tc,tb_physical_person,tb_report_tc 
                        WHERE tb_produtive_man_tc.id_report_tc = tb_report_tc.id 
                         AND tb_report_tc.id = %s  """,(ref_report,))
            
            lista_cprodutive_man_hour = cursor.fetchall()
            #print(lista_cabecalho_information[0])


            return lista_cprodutive_man_hour
    finally:
        connection.close()


def buscar_non_produtive_man(ref_report):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT tb_non_produtive_type_tc.npt_description,npm_hours,npm_comments FROM tb_non_produtive_type_tc,tb_non_produtive_man_tc,tb_report_tc
                            WHERE tb_non_produtive_man_tc.id_non_produtive_type = tb_non_produtive_type_tc.id AND
                            tb_non_produtive_man_tc.id_report_tc = tb_report_tc.id AND tb_report_tc.id = %s
                            ORDER BY tb_non_produtive_type_tc.id ASC  """,(ref_report,))
            
            lista_hse = cursor.fetchall()


            return lista_hse
    finally:
        connection.close()

    



