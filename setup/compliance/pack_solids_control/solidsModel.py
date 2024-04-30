import psycopg2
import conection.connect as connecao
import config_email.config_email

def cadastrar(shaker, scalper, back, middle, front, hours_run, location_of_sample,
dryer_screen_size , bowl_speed, flow, weight_in_ppg, daily_perc_ooc, 
report_information):
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO solids_control_cp (shaker, scalper, back, middle, front, hours_run, location_of_sample,
dryer_screen_size , bowl_speed, flow, weight_in_ppg, daily_perc_ooc, 
report_information) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """,
(shaker, scalper, back, middle, front, hours_run, location_of_sample,
dryer_screen_size , bowl_speed, flow, weight_in_ppg, daily_perc_ooc, 
report_information))
        connection.commit()
        cursor.close()
        return 0
    except Exception as e:
        print(f"Erro: {e}")
        body = f"Erro: {e}"
        config_email.config_email.save_error(body)
        return -1
        

def buscar_solids_by_job_ref(job_ref):
    connection = connecao.cria_connecao()
    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT solids_control_cp.scalper,solids_control_cp.back,solids_control_cp.middle,solids_control_cp.front,solids_control_cp.hours_run,
            sample_location_cp.cutting_dier1,solids_control_cp.dryer_screen_size,
            solids_control_cp.bowl_speed,solids_control_cp.hours_run,solids_control_cp.flow,solids_control_cp.weight_in_ppg,solids_control_cp.daily_perc_ooc
            FROM solids_control_cp,sample_location_cp,report_information_cp
            WHERE solids_control_cp.location_of_sample = sample_location_cp.id
            AND report_information_cp.id = solids_control_cp.report_information
            AND report_information_cp.job_ref_number = %s""",(job_ref,))
            dados = cursor.fetchall()
            return dados
    except Exception as e:
        return e
    finally:
        return dados
    

def buscar_num_registo_solid_by_job_ref(job_ref):
    connection = connecao.cria_connecao()
    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT COUNT(solids_control_cp.id) FROM solids_control_cp,report_information_cp
            WHERE solids_control_cp.report_information = report_information_cp.id
            AND report_information_cp.job_ref_number =   %s """,(job_ref,))
            dados = cursor.fetchone()
            return dados
    except Exception as e:
        return e
    finally:
        return dados 