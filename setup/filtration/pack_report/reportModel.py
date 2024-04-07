import psycopg2
import conection.connect as connecao

def cadastrar_report_information(rpt_job_ref_number,rpt_field_locations,rpt_job_type,rpt_shift,rpt_report,id_physical_person,rpt_rig_name):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO 
                           tb_report_header
                           (rpt_job_ref_number,rpt_field_locations,rpt_job_type,rpt_shift,rpt_report_date,id_physical_person,rpt_rig_name) 
                           values
                           (%s,%s,%s,%s,%s,%s,%s) """,(rpt_job_ref_number,rpt_field_locations,rpt_job_type,rpt_shift,rpt_report,id_physical_person,rpt_rig_name))
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()


def salvar_info_report(ft_ongoing_rig_activity,ft_filtration_activity,id_legal_person,id_report_header):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO 
                           tb_report_ft
                           (ft_ongoing_rig_activity,ft_filtration_activity,id_legal_person,id_report_header) 
                           values
                           (%s,%s,%s,%s) """,(ft_ongoing_rig_activity,ft_filtration_activity,id_legal_person,id_report_header))
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def editar_report_information(rpt_job_ref_number,rpt_rig_size,rpt_field_locations,rpt_job_type,
                           rpt_report,rpt_number_tank,rpt_volume_waste,rpt_type_waste,id_physical_person,id_report):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" UPDATE tb_report_tc SET rpt_job_ref_number = %s,rpt_rig_size = %s, rpt_field_locations = %s, rpt_job_type = %s, rpt_report = %s, rpt_number_tank = %s,
                       rpt_volume_waste = %s, rpt_type_waste = %s, id_physical_person = %s WHERE id = %s""",(rpt_job_ref_number,rpt_rig_size,rpt_field_locations,rpt_job_type,rpt_report,rpt_number_tank,rpt_volume_waste,rpt_type_waste,id_physical_person,id_report,))                
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()

def eliminar_report_information(param):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tb_report_tc WHERE id = '"+param+"' ")
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
                
def listar_report_information():    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tb_report_ft")
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

def buscar_ultimo_registo_report():
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT id FROM public.tb_report_ft ORDER BY id DESC LIMIT 1 """) 
        
        id_report = cursor.fetchone()

        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            return id_report
        


def lista_report_filtration():
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT  tb_legal_person.lp_name,tb_report_header.rpt_job_ref_number,tb_report_header.rpt_rig_name,
                        tb_report_header.rpt_report_date 
						FROM tb_report_ft,tb_legal_person,tb_report_header 
                        WHERE tb_legal_person.id = tb_report_ft.id_legal_person
						AND tb_report_header.id = tb_report_ft.id_report_header
                        ORDER BY tb_report_ft.id  """)
            
            lista_report_filtration = cursor.fetchall()

            return lista_report_filtration
    finally:
        connection.close()
        

def buscar_cabecalho_report_information_with_report(ref_report):
    connection = connecao.cria_connecao()

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT tb_report_ft.id,rpt_job_ref_number,rpt_rig_name,rpt_field_locations,rpt_job_type,rpt_shift,
                            rpt_report_date,lp_name,wl_number 
							FROM public.tb_report_ft,tb_legal_person,tb_report_header,tb_well
							WHERE tb_report_ft.id_legal_person = tb_legal_person.id
							AND tb_report_ft.id_report_header = tb_report_header.id
							AND tb_well.id_legal_person = tb_legal_person.id
                            AND tb_report_header.rpt_job_ref_number = %s
                           ORDER BY tb_report_ft.id DESC LIMIT 1  """,(ref_report,))
            
            lista_cabecalho_information = cursor.fetchone()


            return lista_cabecalho_information
    finally:
        connection.close()


def buscar_ongoing_activity(ref_report):
    connection = connecao.cria_connecao()

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT ft_ongoing_rig_activity,ft_filtration_activity FROM tb_report_ft,tb_report_header
                WHERE tb_report_header.id = tb_report_ft.id_report_header
                AND tb_report_header.rpt_job_ref_number = %s  """,(ref_report,))
            
            ongoing = cursor.fetchone()


            return ongoing
    finally:
        connection.close()
        




    



