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


def salvar_info_report(id_physical_person,id_legal_person,id_shit_activity_tc,id_employee,id_report_header):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO 
                           tb_report_tc
                           (id_physical_person,id_legal_person,id_shit_activity_tc,id_employee,id_report_header) 
                           values
                           (%s,%s,%s,%s,%s) """,(id_physical_person,id_legal_person,id_shit_activity_tc,id_employee,id_report_header))
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
        cursor.execute("SELECT *FROM tb_report_tc")
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

def buscar_ultimo_registo_dayshift_activity():
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT id FROM public.tb_shift_activity_tc ORDER BY id DESC LIMIT 1 """) 
        
        id_dayshidt_activity = cursor.fetchone()

        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            return id_dayshidt_activity
        

def buscar_ultimo_registo_report():
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT id FROM public.tb_report_tc ORDER BY id DESC LIMIT 1 """) 
        
        id_report = cursor.fetchone()

        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            return id_report
        


def lista_report_tank_cleaning():
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT  tb_legal_person.lp_name,tb_report_header.rpt_job_ref_number,tb_report_header.rpt_rig_name,
                        tb_physical_person.pp_name,tb_report_header.rpt_report_date FROM tb_report_tc,tb_legal_person,tb_physical_person,tb_report_header 
                        WHERE tb_legal_person.id = tb_report_tc.id_legal_person
                        AND tb_report_tc.id_physical_person = tb_physical_person.id
						AND tb_report_header.id = tb_report_tc.id_report_header
                        ORDER BY tb_report_tc.id  """)
            
            lista_report_tank_cleaning = cursor.fetchall()

            return lista_report_tank_cleaning
    finally:
        connection.close()
        

def buscar_cabecalho_report_information_with_report(ref_report):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT tb_report_tc.id,rpt_job_ref_number,rpt_rig_name,rpt_field_locations,rpt_job_type,rpt_shift,
                            rpt_report_date,lp_name,pp_name,emp_name,lp_logo 
							FROM public.tb_report_tc,tb_legal_person,tb_report_header,
                            tb_physical_person,tb_employee_tc WHERE tb_report_tc.id_legal_person = tb_legal_person.id
                            AND tb_report_tc.id_physical_person = tb_physical_person.id 
							AND tb_report_tc.id_employee = tb_employee_tc.id
							AND tb_report_tc.id_report_header = tb_report_header.id
                            AND tb_report_header.rpt_job_ref_number = %s
                           ORDER BY tb_report_tc.id DESC LIMIT 1  """,(ref_report,))
            
            lista_cabecalho_information = cursor.fetchone()
            #print(lista_cabecalho_information[0])


            return lista_cabecalho_information
    finally:
        connection.close()
        




    



