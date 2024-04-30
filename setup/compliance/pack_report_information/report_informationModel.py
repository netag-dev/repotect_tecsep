import psycopg2
import conection.connect as connecao
import config_email.config_email

def cadastrar(custumer, well, report_date, aproved_by, job_ref_number, rig_name, field_location, job_type, project_description, hole_size, total_depth, feets_drilled, average_rop, time_at_depth, prepared_by, shift, ongoing_rig_activity, monitoring_comments):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO report_information_cp(custumer, well, report_date, aproved_by, job_ref_number, rig_name, field_location, job_type, project_description, hole_size, total_depth, feets_drilled, average_rop, time_at_depth, prepared_by, shift, ongoing_rig_activity, monitoring_comments) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """,(custumer, well, report_date, aproved_by, job_ref_number, rig_name, field_location, job_type, project_description, hole_size, total_depth, feets_drilled, average_rop, time_at_depth, prepared_by, shift, ongoing_rig_activity, monitoring_comments))    
        connection.commit()
        cursor.close()
        return 0
    except Exception as e:
        print(f"Erro: {e}")
        body = f"Erro: {e}"
        config_email.config_email.save_error(body)
        return -1

def editar(custumer, well, report_date, aproved_by, job_ref_number, rig_name, field_location, job_type, project_description, hole_size, total_depth, feets_drilled, average_rop, time_at_depth, prepared_by, shift, ongoing_rig_activity, monitoring_comments, id):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE report_information_cp set custumer = %s, well = %s, report_date = %s, aproved_by = %s, job_ref_number = %s, rig_name = %s, field_location = %s, job_type = %s, project_description = %s, hole_size = %s, total_depth = %s, feets_drilled = %s, average_rop = %s, time_at_depth = %s, prepared_by = %s, shift = %s, ongoing_rig_activity = %s, monitoring_comments = %s, where id = %s ",(custumer, well, report_date, aproved_by, job_ref_number, rig_name, field_location, job_type, project_description, hole_size, total_depth, feets_drilled, average_rop, time_at_depth, prepared_by, shift, ongoing_rig_activity, monitoring_comments,id))                
        connection.commit()
        cursor.close()
        return 0
    except Exception as e:
        print(f"Erro: {e}")
        body = f"Erro: {e}"
        config_email.config_email.save_error(body)
        return -1

def delete_data(job_ref_number, rig_name, field_location, job_type):
    connection = connecao.cria_connecao()
    try:
        cursor = connection.cursor()
        cursor.execute(""" DELETE FROM report_information_cp WHERE job_ref_number = %s AND rig_name = %s AND field_location = %s AND job_type = %s """,(job_ref_number, rig_name, field_location, job_type))
        connection.commit()
        return 0
    except Exception as e:
        print(f"Erro: {e}")
        body = f"Erro: {e}"
        config_email.config_email.save_error(body)
        return -1   
                
def listar():    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM report_information_cp")
        dados = cursor.fetchall()
        dados_novo = [item[1] for item in dados]
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados_novo
        
def listar_table():    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM report_information_cp")
        dados = cursor.fetchall()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados
    
def buscar_id_by_report_date(report_date):
    connection = connecao.cria_connecao()
    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT id FROM report_information_cp WHERE report_date = %s""",(report_date,))
            id_fluid = cursor.fetchone()
            return id_fluid
    finally:
        connection.close()


