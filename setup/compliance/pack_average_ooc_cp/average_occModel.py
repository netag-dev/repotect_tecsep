import psycopg2
import conection.connect as connecao

def cadastrar(model_average, depth_location, sample_number, date_of_test, 
time_of_test, number_of_shakers, number_of_cutting_driver, sample_location, 
average_dry_cuttings, average_wet_cuttings, mass_of_wet_cuttings, 
mass_balance_requirement, mass_of_naf_base_fluids, mass_of_dry_cuttings,
report_information):
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO average_ooc_cpp (model_average, depth_location, sample_number, date_of_test, 
time_of_test, number_of_shakers, number_of_cutting_driver, sample_location, 
average_dry_cuttings, average_wet_cuttings, mass_of_wet_cuttings, 
mass_balance_requirement, mass_of_naf_base_fluids, mass_of_dry_cuttings,
report_information) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """, 
(model_average, depth_location, sample_number, date_of_test, 
time_of_test, number_of_shakers, number_of_cutting_driver, sample_location, 
average_dry_cuttings, average_wet_cuttings, mass_of_wet_cuttings, 
mass_balance_requirement, mass_of_naf_base_fluids, mass_of_dry_cuttings,
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