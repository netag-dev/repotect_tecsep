import psycopg2
import conection.connect as connecao
import config_email.config_email

def cadastrar(synthetic_sg,rop_at_time,
             weight_empty,weight_filled_body_sample,weight_filled_body_sample_water,
             weight_graduated_cyinder,weight_graduated_cyinder_condensate,
             volume_of_water,weight_retort_cell,weight_of_sample,weight_of_water,volume_of_sample,
             weight_oil,weight_condensate_gms,density_sample_sg,vol_oil,weigth_water,
             weight_dry_solids_calculated,perc_water_by_volume,perc_oil_by_volume,weight_dry_solids_actual,
             perc_solids_by_volume,perc_oil_by_weight,perc_water_by_weight,perc_solids_by_weight,ooc,soc,mud_weight,acuracy_check):
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO samples_cp(synthetic_sg,rop_at_time,
             weight_empty,weight_filled_body_sample,weight_filled_body_sample_water,
             weight_graduated_cyinder,weight_graduated_cyinder_condensate,
             volume_of_water,weight_retort_cell,weight_of_sample,weight_of_water,volume_of_sample,
             weight_oil,weight_condensate_gms,density_sample_sg,vol_oil,weigth_water,
             weight_dry_solids_calculated,perc_water_by_volume,perc_oil_by_volume,weight_dry_solids_actual,
             perc_solids_by_volume,perc_oil_by_weight,perc_water_by_weight,perc_solids_by_weight,ooc,soc,mud_weight,acuracy_check) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """, 
            (synthetic_sg,rop_at_time,
             weight_empty,weight_filled_body_sample,weight_filled_body_sample_water,
             weight_graduated_cyinder,weight_graduated_cyinder_condensate,
             volume_of_water,weight_retort_cell,weight_of_sample,weight_of_water,volume_of_sample,
             weight_oil,weight_condensate_gms,density_sample_sg,vol_oil,weigth_water,
             weight_dry_solids_calculated,perc_water_by_volume,perc_oil_by_volume,weight_dry_solids_actual,
             perc_solids_by_volume,perc_oil_by_weight,perc_water_by_weight,perc_solids_by_weight,ooc,soc,mud_weight,acuracy_check))
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
            cursor.execute(""" SELECT * FROM solids_control_cp,sample_location_cp,report_information_cp
            WHERE solids_control_cp.location_of_sample = sample_location_cp.id
            AND report_information_cp.id = solids_control_cp.report_information
            AND report_information_cp.job_ref_number =  %s """,(job_ref,))
            dados = cursor.fetchone()
            return dados
    except Exception as e:
        return e
    finally:
        return dados  

