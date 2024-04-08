import psycopg2
import conection.connect as connecao


def listar():
    connection = connecao.cria_connecao()
    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT emp_name,emp_email,pp_description FROM tb_employee_wbco,tb_personal_position
                           WHERE tb_employee_wbco.emp_personal_position = tb_personal_position.id ORDER BY tb_employee_wbco.id ASC""")
            lista_empregado = cursor.fetchall()
    finally:
        connection.close()
        return lista_empregado


def buscar_id_by_shift(wb_eng_shift):
    connection = connecao.cria_connecao()
    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT id FROM tb_engineer_wbco WHERE wb_eng_shift = %s """,(wb_eng_shift))
            id_shift = cursor.fetchone()
    finally:
        connection.close()
        return id_shift   

def editar(name, email, id_personnel_position,id):
    connection = connecao.cria_connecao()
    try:
         with connection.cursor() as cursor:
            cursor.execute(""" UPDATE tb_employee_wbco SET emp_name = %s, emp_email = %s, emp_personal_position = %s  WHERE id = %s  """,(name, email, id_personnel_position,id))
            connection.commit()
    except Exception as e:
        print(f"Erro {e}")
        return -1
    finally:  
        connection.close()
        return 0 


def delete_data(nome,email):
    connection = connecao.cria_connecao()
    try:
        cursor = connection.cursor()
        cursor.execute(""" DELETE FROM tb_employee_wbco WHERE emp_name = %s AND emp_email = %s """,(nome, email))
        connection.commit()
    except Exception as e:
        print(f"Erro: {e}")
        return -1
    finally:
        connection.close()
        return 0   

def save_data(name, email, id_personnel_position):
    connection = connecao.cria_connecao()
    try:
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO tb_employee_wbco(emp_name,emp_email,emp_personal_position) VALUES (%s,%s,%s)  """,(name, email, id_personnel_position))
        connection.commit()
    except Exception as e:
        print(f"Erro: {e}")
        return -1
    finally:
        connection.close()
        return 0
    

def buscar_id_by_name_email(name, email):
    connection = connecao.cria_connecao()
    try:
        cursor = connection.cursor()
        cursor.execute(""" SELECT id FROM tb_employee_wbco WHERE emp_name = %s AND emp_email = %s """,(name,email))
        id_empregado = cursor.fetchone()
    except Exception as e:
        print(f"Erro: {e}")
        return -1
    finally:
        connection.close()
        return id_empregado
    

def verificar_job_ref(job_ref,id_supervisor):
    connection = connecao.cria_connecao()
    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT COUNT(*) FROM tb_engineer_wbco,tb_report_header WHERE tb_report_header.id = tb_report_wbco.id_report_header
            AND tb_report_header.rpt_job_ref_number = %s AND tb_report_header.id_physical_person = %s """,(job_ref,id_supervisor))
            job_ref = cursor.fetchone()
    except Exception as e:
        print(f"Erro: {e}")
        return e
    finally:
        return job_ref[0]
