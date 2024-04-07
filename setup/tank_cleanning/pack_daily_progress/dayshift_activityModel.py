import psycopg2
import conection.connect as connecao

def salvar_dayshift_activity(pd_description,id_physical_person,daily_progress,planned_activity,norm_reading,equipament_material):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO tb_shift_activity_tc(pd_description,id_physical_person,daily_progress,planned_activity,norm_reading,equipament_material) values(%s,%s,%s,%s,%s,%s) """,(pd_description,id_physical_person,daily_progress,planned_activity,norm_reading,equipament_material,))
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def editar_dayshift_activity(pd_description, id_physical_person, daily_progress,planned_activity,norm_reading,equipament_material,id_dayshift):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" UPDATE tb_shift_activity_tc set 
                       pd_description = %s, id_physical_person = %s, daily_progress = %s, planned_activity = %s, norm_reading = %s, equipament_material = %s Where id = %s """,(pd_description,id_physical_person,daily_progress,planned_activity,planned_activity,norm_reading,equipament_material,id_dayshift,) )                
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()

def eliminar_dayshift_activity(param):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tb_shift_activity_tc WHERE id = %s",(param))
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
                
def listar_dayshift_activity():    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT *FROM tb_daily_progress_tc")
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


def buscar_shift_activity(id_report):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT pd_description,daily_progress,planned_activity,norm_reading,equipament_material FROM public.tb_shift_activity_tc,tb_report_tc 
                        WHERE tb_report_tc.id_shit_activity_tc = tb_shift_activity_tc.id AND tb_report_tc.id = %s  """,(id_report,))
            
            lista_actividade = cursor.fetchone()
            #print(lista_cabecalho_information[0])


            return lista_actividade
    finally:
        connection.close()





    



