import psycopg2
import conection.connect as connecao

def cadastrar(synthetic_sg, rop_at_time, weight_empty,weight_filled_body_sample, weight_filled_body_sample_water, 
weight_graduated_cyinder, weight_graduated_cyinder_condensate, volume_of_water, 
weight_retort_cell, weight_of_sample, weight_of_water, volume_of_sample, 
density_sample_sg, weight_condensate_gms, weight_oil, vol_oil, weight_water, 
weight_dry_solids_actual, perc_oil_by_volume, perc_water_by_volume, 
weight_dry_solids_calculated, perc_solids_by_volume, perc_oil_by_weight, perc_water_by_weight, perc_solids_by_weight,
soc, ooc, mud_weight, acuracy_check):
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO samples_cp (synthetic_sg, rop_at_time, weight_empty,weight_filled_body_sample, weight_filled_body_sample_water, 
        weight_graduated_cyinder, weight_graduated_cyinder_condensate, volume_of_water, 
        weight_retort_cell, weight_of_sample, weight_of_water, volume_of_sample, 
        density_sample_sg, weight_condensate_gms, weight_oil, vol_oil, weight_water, 
        weight_dry_solids_actual, perc_oil_by_volume, perc_water_by_volume, 
        weight_dry_solids_calculated, perc_solids_by_volume, perc_oil_by_weight, perc_water_by_weight, perc_solids_by_weight,
        soc, ooc, mud_weight, acuracy_check) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,) """, 
(synthetic_sg, rop_at_time, weight_empty,weight_filled_body_sample, weight_filled_body_sample_water, 
weight_graduated_cyinder, weight_graduated_cyinder_condensate, volume_of_water, 
weight_retort_cell, weight_of_sample, weight_of_water, volume_of_sample, 
density_sample_sg, weight_condensate_gms, weight_oil, vol_oil, weight_water, 
weight_dry_solids_actual, perc_oil_by_volume, perc_water_by_volume, 
weight_dry_solids_calculated, perc_solids_by_volume, perc_oil_by_weight, perc_water_by_weight, perc_solids_by_weight,
soc, ooc, mud_weight, acuracy_check))
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
