import psycopg2
import conection.connect as connecao

def cadastrar(custumer, well, report_date, aproved_by, job_ref_number, rig_name, field_location, job_type, project_description, hole_size, total_depth, feets_drilled, average_rop, time_at_depth, prepared_by, shift, ongoing_rig_activity, monitoring_comments):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO report_information_cp(custumer, well, report_date, aproved_by, job_ref_number, rig_name, field_location, job_type, project_description, hole_size, total_depth, feets_drilled, average_rop, time_at_depth, prepared_by, shift, ongoing_rig_activity, monitoring_comments) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """,(custumer, well, report_date, aproved_by, job_ref_number, rig_name, field_location, job_type, project_description, hole_size, total_depth, feets_drilled, average_rop, time_at_depth, prepared_by, shift, ongoing_rig_activity, monitoring_comments))    
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
        return -1
    finally:
        if connection:
            cursor.close()
            connection.close()
            return 0

def editar(custumer, well, report_date, aproved_by, job_ref_number, rig_name, field_location, job_type, project_description, hole_size, total_depth, feets_drilled, average_rop, time_at_depth, prepared_by, shift, ongoing_rig_activity, monitoring_comments, id):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE report_information_cp set custumer = %s, well = %s, report_date = %s, aproved_by = %s, job_ref_number = %s, rig_name = %s, field_location = %s, job_type = %s, project_description = %s, hole_size = %s, total_depth = %s, feets_drilled = %s, average_rop = %s, time_at_depth = %s, prepared_by = %s, shift = %s, ongoing_rig_activity = %s, monitoring_comments = %s, where id = %s ",(custumer, well, report_date, aproved_by, job_ref_number, rig_name, field_location, job_type, project_description, hole_size, total_depth, feets_drilled, average_rop, time_at_depth, prepared_by, shift, ongoing_rig_activity, monitoring_comments,id))                
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
        return -1
    finally:
        if connection:
            cursor.close()
            return 0

def delete_data(job_ref_number, rig_name, field_location, job_type):
    connection = connecao.cria_connecao()
    try:
        cursor = connection.cursor()
        cursor.execute(""" DELETE FROM report_information_cp WHERE job_ref_number = %s AND rig_name = %s AND field_location = %s AND job_type = %s """,(job_ref_number, rig_name, field_location, job_type))
        connection.commit()
    except Exception as e:
        print(f"Erro: {e}")
        return -1
    finally:
        connection.close()
        return 0   
    

############# Listagens ########################################
    
def listar_employe():
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employee_cp")
        lista_empregado = cursor.fetchall()
        nova_lista = [(item[0],item[1]) for item in lista_empregado]
        print(nova_lista)
    except Exception as e:
        return e
    finally:
        return nova_lista
    
def buscar_cliente():
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM tb_legal_person")
            lista_cliente = cursor.fetchall()
            lista_cliente_convertida = [(item[0],item[2]) for item in lista_cliente]
            return lista_cliente_convertida
    except Exception as e:
        print(f"{e}")
    finally:
        connection.close() 
        return lista_cliente_convertida

def buscar_id_user_logado(email):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM tb_physical_person WHERE pp_email = %s ",(email))
            id_user = cursor.fetchone()
    except Exception as e:
        print(f"{e}")
    finally:
        connection.close() 
        return id_user


def listar_well(cliente):
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        
        cursor.execute(""" SELECT id FROM tb_legal_person WHERE lp_name = %s""",(cliente,))
        id_cliente = cursor.fetchone()

        cursor.execute("SELECT * FROM tb_well WHERE id_legal_person = %s ",(id_cliente,))
        lista_poco = cursor.fetchall()
        nova_lista = [(item[0],item[1]) for item in lista_poco]
    except Exception as e:
        print(f"{e}") 
    finally:
        return nova_lista
                
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
        cursor.execute(""" SELECT lp_name,job_ref_number,pp_name,report_date FROM 
        report_information_cp,tb_legal_person,tb_physical_person
        WHERE report_information_cp.custumer = tb_legal_person.id 
        AND tb_physical_person.id = report_information_cp.prepared_by""")
        dados = cursor.fetchall()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados
        
def listar_report_information_by_job_ref(job_ref):    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT report_information_cp.id,job_ref_number,rig_name,field_location,job_type,shift,report_date,lp_name,wl_name,pp_name,
        emp_name,hole_size,total_depth,feets_drilled,average_rop,time_at_depth FROM 
        report_information_cp,tb_legal_person,tb_physical_person,tb_well,employee_cp
        WHERE report_information_cp.custumer = tb_legal_person.id 
        AND tb_physical_person.id = report_information_cp.prepared_by 
		AND tb_well.id = report_information_cp.well
		AND employee_cp.id = report_information_cp.aproved_by 
        AND report_information_cp.job_ref_number = %s""",(job_ref,))
        dados = cursor.fetchone()
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

