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
        
def buscar_avarage_information_by_job_ref(job_ref):
    connection = connecao.cria_connecao()
    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT average_ooc_cpp.depth_location,sample_location_cp.cutting_dier1,average_ooc_cpp.sample_number,average_ooc_cpp.date_of_test,
            average_ooc_cpp.time_of_test,average_ooc_cpp.average_dry_cuttings,average_ooc_cpp.average_wet_cuttings,average_ooc_cpp.mass_of_wet_cuttings,
            average_ooc_cpp.mass_balance_requirement,average_ooc_cpp.mass_of_naf_base_fluids,average_ooc_cpp.mass_of_dry_cuttings,average_ooc_cpp.number_of_cutting_driver,
            average_ooc_cpp.number_of_shakers,model_average_cp.model,model_average_cp.serial_number
            FROM average_ooc_cpp, model_average_cp,sample_location_cp,report_information_cp 
            WHERE average_ooc_cpp.model_average = model_average_cp.id
            AND sample_location_cp.id = average_ooc_cpp.sample_location
            AND report_information_cp.id = average_ooc_cpp.report_information
            AND report_information_cp.job_ref_number =  %s """,(job_ref,))
            dados = cursor.fetchone()
            return dados
    except Exception as e:
        return e
    finally:
        return dados  

