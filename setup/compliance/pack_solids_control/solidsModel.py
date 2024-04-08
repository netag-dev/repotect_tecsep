import psycopg2
import conection.connect as connecao

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
    except Exception as e:
        print(f"Erro na Base de dados: {e}")
        return -1
    finally:
        if connection:
            cursor.close()
            connection.close()
            return 0