import psycopg2
import conection.connect as connecao

# Função para carregar todos os supervisores
def buscar_supervisor():
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT pp_name FROM tb_physical_person ORDER BY pp_name")
            usrm = cursor.fetchall()

            usrm_list = [item[0] for item in usrm]
            return usrm_list

    finally:
        connection.close() 



def buscar_tecnico():
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(" SELECT emp_name FROM public.tb_employee_wbco ORDER BY emp_name ")
            usrm = cursor.fetchall()

            usrm_list = [item[0] for item in usrm]

            print(usrm_list)

            
            return usrm_list

    finally:
        connection.close() 


def salvar_report_cabecalho(rpt_job_ref_number,rpt_field_locations,rpt_job_type,rpt_shift,rpt_report_date,id_physical_person,rpt_rig_name):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(""" INSERT INTO tb_report_header(rpt_job_ref_number,rpt_field_locations,rpt_job_type,rpt_shift,rpt_report_date,id_physical_person,rpt_rig_name)
            VALUES (%s,%s,%s,%s,%s,%s,%s)""",(rpt_job_ref_number,rpt_field_locations,rpt_job_type,rpt_shift,rpt_report_date,id_physical_person,rpt_rig_name,))

            connection.commit()   

    finally:
        connection.close()   



def buscar_id_report_header_ultimo():
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM tb_report_header ORDER BY id DESC LIMIT 1")
            id_last_report = cursor.fetchone()



            
            return id_last_report

    finally:
        connection.close() 


# Função para carregar todos os supervisores
def buscar_id_supervisor_by_name(nome_supervisor):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM tb_physical_person WHERE pp_name = %s", (nome_supervisor, ))
            id_supervisor = cursor.fetchone()



            
            return id_supervisor

    finally:
        connection.close() 


# Função para carregar todos os supervisores
def buscar_id_supervisor_by_email(nome_email):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM tb_physical_person WHERE pp_email = %s", (nome_email, ))
            id_supervisor = cursor.fetchone()



            
            return id_supervisor

    finally:
        connection.close() 


# Funcão para carregar todos os clientes
def buscar_cliente():
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT lp_name FROM tb_legal_person ")
            lista_cliente = cursor.fetchall()

            lista_cliente_convertida = [item[0] for item in lista_cliente]


            
            return lista_cliente_convertida

    finally:
        connection.close()       


# Função para carregar Pocos
        
def buscar_poco(nome_pessoa_legal):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT id FROM tb_legal_person WHERE lp_name = %s""",(nome_pessoa_legal,))
            id_cliente = cursor.fetchone()

            cursor.execute(""" SELECT wl_number FROM tb_well,tb_legal_person 
                           WHERE tb_well.id_legal_person = tb_legal_person.id 
                           AND tb_well.id_legal_person = %s""",(id_cliente))
            
            lista_poco = cursor.fetchall()

            lista_poco_convertida = [item[0] for item in lista_poco]

            return lista_poco_convertida
    finally:
        connection.close()


# Função para carregar Pocos
        
def buscar_id_poco(nome_poco):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT id FROM tb_well WHERE wl_number  = %s""",(nome_poco,))
            id_poco = cursor.fetchone()


            return id_poco
    finally:
        connection.close()


def buscar_id_cliente(nome_cliente):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT id FROM tb_legal_person WHERE lp_name  = %s""",(nome_cliente,))
            id_cliente = cursor.fetchone()


            return id_cliente
    finally:
        connection.close()


def carregar_buscar_id_empregador_por_nome(nome):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT id FROM public.tb_employee_wbco WHERE emp_name = %s""",(nome,))
            buscar_id_empregador = cursor.fetchone()


            return buscar_id_empregador
    finally:
        connection.close()



#Funcçaõ para salvar engenheiros
def salvar_wbco_tools_enginer(id_employee,wb_eng_shift,wb_eng_total_dayst,id_report_wbco):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            cursor.execute(""" INSERT INTO tb_engineer_wbco(id_employee,wb_eng_shift,wb_eng_total_dayst,id_report_wbco) values(%s,%s,%s,%s) """,(id_employee,wb_eng_shift,wb_eng_total_dayst,id_report_wbco))
            connection.commit()
            return 0
    finally:
        connection.close()



#Funcao para pegar o ultimo registo salvo na tabela report 
def buscar_id_ultimo_report():
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT id FROM public.tb_report_wbco ORDER BY tb_report_wbco.id DESC LIMIT 1""")
            buscar_id_report = cursor.fetchone()


            return buscar_id_report
    finally:
        connection.close()


# Salvar o WBCO_primary
def salvar_wbco_primary(tl_description,tl_thead_connetions_box,tl_thead_connetions,tl_od,tl_id,tl_drift_size,id_physical_person,id_report_tools):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            cursor.execute(""" INSERT INTO tb_tools_on_board_primary(tl_description,tl_thead_connetions_box,tl_thead_connetions,tl_od,tl_id,tl_drift_size,id_physical_person,id_report_tools) values(%s,%s,%s,%s,%s,%s,%s,%s) """,(tl_description,tl_thead_connetions_box,tl_thead_connetions,tl_od,tl_id,tl_drift_size,id_physical_person,id_report_tools))
            connection.commit()
    except Exception as e:
        print(f"{e}")
        return -1
    finally:
        return 0

# Salvar o WBCO_BackUp
def salvar_wbco_backup(tlb_description,tl_thead_connetions_box,tlb_thead_connetions,tlb_od,tlb_id,tlb_drift_size,id_physical_person,id_report_tools):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            cursor.execute(""" INSERT INTO tb_tools_on_board_backup (tlb_description,tlb_thead_connetions_box,tlb_thead_connetions,tlb_od,tlb_id,tlb_drift_size,id_physical_person,id_report_tools) values(%s,%s,%s,%s,%s,%s,%s,%s) """,(tlb_description,tl_thead_connetions_box,tlb_thead_connetions,tlb_od,tlb_id,tlb_drift_size,id_physical_person,id_report_tools))
            connection.commit()
    except Exception as e:
        print(f"{e}")
        return -1
    finally:
        return 0

#Funcçaõ para Report Information
def salvar_report_information(rpt_ongoing_rig,rpt_casing_size,rpt_length,rpt_od,rpt_id,rpt_weight_rangeng,
                              rpt_volume_capacity,rpt_hole_volume,rpt_wbco_tools_activity,rpt_shift_supervisor,rpt_total_day_supervisor,id_well,id_physical_person,id_legal_person,id_employee,id_report_header):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:

            cursor.execute(""" INSERT INTO 
                           tb_report_wbco
                           (rpt_ongoing_rig,rpt_casing_size,rpt_length,rpt_od,rpt_id,rpt_weight_rangeng,
                              rpt_volume_capacity,rpt_hole_volume,rpt_wbco_tools_activity,rpt_shift_supervisor,rpt_total_day_supervisor,id_well,id_physical_person,id_legal_person,id_employee,id_report_header) 
                           values
                           (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """,(rpt_ongoing_rig,rpt_casing_size,rpt_length,rpt_od,rpt_id,rpt_weight_rangeng,
                              rpt_volume_capacity,rpt_hole_volume,rpt_wbco_tools_activity,rpt_shift_supervisor,rpt_total_day_supervisor,id_well,id_physical_person,id_legal_person,id_employee,id_report_header,))
            connection.commit()
            return 0
    finally:
        connection.close()

#---------------------------------------- Query Para serem colocadas no Report ------------------------------------
def buscar_cabecalho_report_information():
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT rpt_job_ref_number,rpt_rig_name,rpt_field_locations,rpt_job_type,rpt_shift,
                            rpt_report_date,lp_name,wl_number,pp_name,rpt_ongoing_rig,rpt_wbco_tools_activity,rpt_shift_supervisor,rpt_total_day_supervisor,emp_name 
							FROM public.tb_report_wbco,tb_legal_person,tb_report_header,tb_employee_wbco,
                            tb_physical_person,tb_well WHERE tb_report_wbco.id_legal_person = tb_legal_person.id
                            AND tb_report_wbco.id_physical_person = tb_physical_person.id 
							AND tb_report_header.id = tb_report_wbco.id_report_header
							AND tb_employee_wbco.id = tb_report_wbco.id_employee
                            AND tb_report_wbco.id_well = tb_well.id ORDER BY tb_report_wbco.id DESC LIMIT 1""")
            
            lista_cabecalho_information = cursor.fetchone()
            #print(lista_cabecalho_information[0])


            return lista_cabecalho_information
    finally:
        connection.close()


# -------------------------------------------- Query --------------------------------------------------------------------------
        
def buscar_cabecalho_report_information_with_report(ref_report):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT rpt_job_ref_number,rpt_rig_name,rpt_field_locations,rpt_job_type,rpt_shift,
                            rpt_report_date,lp_name,wl_number,pp_name,rpt_ongoing_rig,rpt_wbco_tools_activity,rpt_shift_supervisor,rpt_total_day_supervisor,emp_name,lp_logo 
							FROM public.tb_report_wbco,tb_legal_person, tb_employee_wbco,
                            tb_physical_person,tb_well,tb_report_header WHERE 
							tb_report_wbco.id_legal_person = tb_legal_person.id
                            AND tb_report_wbco.id_physical_person = tb_physical_person.id 
                            AND tb_report_wbco.id_well = tb_well.id 
							AND tb_report_header.id = tb_report_wbco.id_report_header
							AND tb_employee_wbco.id = tb_report_wbco.id_employee
                            AND tb_report_header.rpt_job_ref_number = %s
                           ORDER BY tb_report_wbco.id DESC LIMIT 1  """,(ref_report,))
            lista_cabecalho_information = cursor.fetchone()
    except Exception as e:
            print(f"{e}")
            return -1
    finally:
        return lista_cabecalho_information
    



def buscar_well_information_with_report(ref_report):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT rpt_casing_size,rpt_length,rpt_od,rpt_id,
                rpt_weight_rangeng,rpt_volume_capacity,rpt_hole_volume,tb_report_wbco.id FROM 
				public.tb_report_wbco,tb_report_header   WHERE tb_report_wbco.id_report_header =  tb_report_header.id 
				AND tb_report_header.rpt_job_ref_number = %s 
                ORDER BY tb_report_wbco.id DESC LIMIT 1  """,(ref_report,))
            
            lista_well_information = cursor.fetchone()


            return lista_well_information
    finally:
        connection.close()

#-------------------------------------------------------------------------------------------------------------------------------


def buscar_well_information():
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT rpt_casing_size,rpt_length,rpt_od,rpt_id,
                rpt_weight_rangeng,rpt_volume_capacity,rpt_hole_volume,tb_report_wbco.id FROM 
				public.tb_report_wbco,tb_report_header   WHERE tb_report_wbco.id_report_header =  tb_report_header.id 
                ORDER BY tb_report_wbco.id DESC LIMIT 1  """)
            
            lista_well_information = cursor.fetchone()


            return lista_well_information
    finally:
        connection.close()


def buscar_wbco_primary_informatio(id_report):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT tl_description,tb_thread_con.thc as pin ,thc_description,
                tl_od,tl_id,tl_drift_size FROM tb_tools_on_board_primary,tb_thread_con, tb_report_wbco WHERE 
                tb_report_wbco.id = tb_tools_on_board_primary.id_report_tools AND
				tb_thread_con.id = tb_tools_on_board_primary.tl_thead_connetions AND
                tb_report_wbco.id = %s  """,(id_report,))
            
            lista_wbco_primary = cursor.fetchall()

            return lista_wbco_primary
    finally:
        connection.close()


def buscar_wbco_primary_informatio_by_job_ref(job_ref):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" 
            SELECT 
            tl_description,
            thread_pin.thc || ' ' || thread_pin.thc_description || '' AS thc,
            thread_box.thc || ' ' || thread_box.thc_description || '' AS thc_box,
            tl_od,
            tl_id,
            tl_drift_size 
            FROM 
                tb_thread_con as thread_pin,tb_thread_con as thread_box, tb_tools_on_board_primary, tb_report_wbco, tb_report_header 
            WHERE 
            tb_report_wbco.id = tb_tools_on_board_primary.id_report_tools AND
            tb_report_header.id = tb_report_wbco.id_report_header AND
            thread_pin.id = tb_tools_on_board_primary.tl_thead_connetions AND
            thread_box.id = tb_tools_on_board_primary.tl_thead_connetions_box AND
            tb_report_header.rpt_job_ref_number = %s  """,(job_ref,))
            
            lista_wbco_primary = cursor.fetchall()
            print(lista_wbco_primary)

    except Exception as e:
            print(f"{e}")
            return -1
    finally:
        return lista_wbco_primary


def buscar_wbco_back_up_informatio(id_report):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT tlb_description,tlb_size,thc,thc_description,
                tlb_od,tlb_id,tlb_drift_size FROM tb_tools_on_board_backup,tb_thread_con, tb_report_wbco WHERE 
                tb_report_wbco.id = tb_tools_on_board_backup.id_report_tools AND
				tb_thread_con.id = tb_tools_on_board_backup.tlb_thead_connetions AND
                tb_report_wbco.id = %s  """,(id_report,))
            
            lista_wbco_back_up = cursor.fetchall()

            return lista_wbco_back_up
    finally:
        connection.close()


def buscar_wbco_back_up_informatio_by_job_ref(job_ref):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT 
            tlb_description,
            thread_pin.thc || ' ' || thread_pin.thc_description || '' AS thc,
            thread_box.thc || ' ' || thread_box.thc_description || '' AS thc_box,
            tlb_od,
            tlb_id,
            tlb_drift_size 
            FROM 
            tb_thread_con as thread_pin,tb_thread_con as thread_box, tb_tools_on_board_backup, tb_report_wbco, tb_report_header 
            WHERE 
            tb_report_wbco.id = tb_tools_on_board_backup.id_report_tools AND
            tb_report_header.id = tb_report_wbco.id_report_header AND
            thread_pin.id = tb_tools_on_board_backup.tlb_thead_connetions AND
            thread_box.id = tb_tools_on_board_backup.tlb_thead_connetions_box AND
            tb_report_header.rpt_job_ref_number =%s  """,(job_ref,))
            
            lista_wbco_back_up = cursor.fetchall()

    except Exception as e:
        print(f"{e}")
        return -1
    finally:
        connection.close()
        return lista_wbco_back_up


def buscar_empregado(id_report):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT emp_name,wb_eng_shift,wb_eng_total_dayst FROM tb_employee_wbco,tb_report_wbco, tb_engineer_wbco 
                            WHERE tb_employee_wbco.id = tb_engineer_wbco.id_employee
							AND tb_engineer_wbco.id_report_wbco = tb_report_wbco.id
                            AND tb_report_wbco.id = %s
                            ORDER BY tb_employee_wbco.id DESC LIMIT 1  """,(id_report,))
            
            lista_empregado = cursor.fetchone()

            return lista_empregado
    finally:
        connection.close()


def buscar_empregado_by_job_ref(job_ref):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT emp_name,wb_eng_shift,wb_eng_total_dayst FROM tb_engineer_wbco,tb_report_wbco,tb_report_header,tb_employee_wbco
                            WHERE tb_report_wbco.id = tb_engineer_wbco.id_report_wbco
							AND tb_employee_wbco.id = tb_engineer_wbco.id_employee
							AND tb_report_header.id = tb_report_wbco.id_report_header
						    AND tb_report_header.rpt_job_ref_number = %s
                            ORDER BY tb_employee_wbco.id DESC LIMIT 1  """,(job_ref,))
            
            lista_empregado = cursor.fetchone()

            return lista_empregado
    finally:
        connection.close()


def lista_report_wbco():
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT  tb_legal_person.lp_name,tb_report_header.rpt_job_ref_number,tb_well.wl_number,
                        tb_physical_person.pp_name,tb_report_header.rpt_report_date FROM tb_report_wbco,tb_legal_person,tb_well,tb_physical_person,tb_report_header 
                        WHERE tb_legal_person.id = tb_report_wbco.id_legal_person
                        AND tb_report_wbco.id_physical_person = tb_physical_person.id
						AND tb_report_header.id = tb_report_wbco.id_report_header
                        AND tb_report_wbco.id_well = tb_well.id  """)
            
            lista_report_wbco = cursor.fetchall()

            return lista_report_wbco
    finally:
        connection.close()

def lista_personel_position():
    connection = connecao.cria_connecao()

    try:
        with connection.cursor() as cursor:

            cursor.execute(""" SELECT pp_description FROM tb_personal_position """)

            lista_personal = cursor.fetchall()

            nova_lista = [item[0] for item in lista_personal]
    except Exception as e:
        print(f"Erro {e}")
    finally:
        connection.close()
        return nova_lista
    
def buscar_id_personeel_postion(pp_description):
    connection = connecao.cria_connecao()

    try:
        with connection.cursor() as cursor:

            cursor.execute(""" SELECT id FROM tb_personal_position WHERE pp_description = %s """,(pp_description,))

            id = cursor.fetchone()

    except Exception as e:
        print(f"Erro {e}")
    finally:
        connection.close()
        return id[0]
    

def buscar_total_days_supervisor(job_ref,id_supervisor):
    connection = connecao.cria_connecao()

    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT COUNT(*) FROM tb_report_wbco, tb_report_header  WHERE tb_report_wbco.id_report_header = tb_report_header.id AND 
            tb_report_header.rpt_job_ref_number = %s AND  tb_report_wbco.id_physical_person = %s """,(job_ref,id_supervisor))

            total_days = cursor.fetchone()

            print(total_days)

    except Exception as e:
        print(f"Erro {e}")
    finally:
        connection.close()
        return total_days[0]
    

def verificar_job_ref(job_ref,id_supervisor):
    connection = connecao.cria_connecao()
    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT COUNT(*) FROM tb_report_wbco,tb_report_header WHERE tb_report_header.id = tb_report_wbco.id_report_header
            AND tb_report_header.rpt_job_ref_number = %s AND tb_report_header.id_physical_person = %s """,(job_ref,id_supervisor))
            job_ref = cursor.fetchone()
    except Exception as e:
        print(f"Erro: {e}")
        return e
    finally:
        return job_ref[0]
            




