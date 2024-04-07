import psycopg2
import conection.connect as connecao

def cadastrar(pm_work_order, pm_description, pm_original_hours, pm_hours_brocked_td, pm_qt_hours_brocked_td, pm_hours_brocked_date, pm_hours_remaining_td, pm_visual_perc_complete, id_report_tc):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO tb_produtive_man_tc
                       (pm_work_order, pm_description, pm_original_hours, pm_hours_brocked_td, 
                       pm_qt_hours_brocked_td, pm_hours_brocked_date, pm_hours_remaining_td, pm_visual_perc_complete, id_report_tc) 
                       values (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(pm_work_order, pm_description, pm_original_hours, pm_hours_brocked_td, 
                       pm_qt_hours_brocked_td, pm_hours_brocked_date, pm_hours_remaining_td, pm_visual_perc_complete, id_report_tc))    
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def editar(param1, param2, param3, param4, param5, param6, param7, param8, param9, param10):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_produtive_man_tc set pm_work_order = '"+param2+"', pm_description = '"+param3+"', pm_original_hours = '"+param4+"', pm_hours_brocked_td = '"+param5+"', pm_qt_hours_brocked_td = '"+param6+"', pm_hours_brocked_date = '"+param7+"', pm_hours_remaining_td = '"+param8+"', pm_visual_perc_complete = '"+param9+"', id_physical_person = '"+param10+"' where id = '"+param1+"' ")                
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
        cursor.execute("DELETE FROM tb_produtive_man_tc WHERE id = '"+param+"' ")
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
        cursor.execute("SELECT *FROM tb_produtive_man_tc")
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

def verificar_registo_existente_com_report(id_report):    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tb_produtive_man_tc WHERE id_report_tc = %s ORDER BY id DESC LIMIT 1",(id_report,))
        dados = cursor.fetchone()
        
        #print(dados)
        
        
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            if dados is None:
                return -1
            return dados[6]


    



