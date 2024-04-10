import psycopg2
import conection.connect as connecao


def listar():
    connection = connecao.cria_connecao()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""  SELECT * FROM employee_cp order BY id ASC""")
            lista_empregado = cursor.fetchall()
    finally:
        connection.close()
        return lista_empregado


def buscar_id_by_shift(wb_eng_shift):
    connection = connecao.cria_connecao()
    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT id FROM employee_cp WHERE wb_eng_shift = %s """,(wb_eng_shift))
            id_shift = cursor.fetchone()
    finally:
        connection.close()
        return id_shift   

def editar(name, email,id):
    connection = connecao.cria_connecao()
    try:
         with connection.cursor() as cursor:
            cursor.execute(""" UPDATE employee_cp SET emp_name = %s, emp_email = %s  WHERE id = %s  """,(name, email,id))
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
        cursor.execute(""" DELETE FROM employee_cp WHERE emp_name = %s AND emp_email = %s """,(nome, email))
        connection.commit()
    except Exception as e:
        print(f"Erro: {e}")
        return -1
    finally:
        connection.close()
        return 0   

def cadastrar(name, email):
    connection = connecao.cria_connecao()
    try:
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO employee_cp(emp_name,emp_email) VALUES (%s,%s)  """,(name, email))
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
        cursor.execute(""" SELECT id FROM employee_cp WHERE emp_name = %s AND emp_email = %s """,(name,email))
        id_empregado = cursor.fetchone()
    except Exception as e:
        print(f"Erro: {e}")
        return -1
    finally:
        connection.close()
        return id_empregado


def cadastrar_enginer(eng_shift,id_employe,id_report):
    connection = connecao.cria_connecao()
    try:
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO engineer_cp(eng_shift,id_employee,id_report) VALUES (%s,%s,%s)""",(eng_shift,id_employe,id_report))
        connection.commit()
    except Exception as e:
        print(f"Erro: {e}")
        return -1
    finally:
        connection.close()
        return 0
    

def buscar_enginer_by_job_ref(job_ref):
    connection = connecao.cria_connecao()
    try:
        cursor = connection.cursor()
        cursor.execute(""" SELECT employee_cp.emp_name,engineer_cp.eng_shift FROM report_information_cp,engineer_cp,employee_cp
        WHERE engineer_cp.id_employee = employee_cp.id
        AND report_information_cp.id = engineer_cp.id_report
        AND report_information_cp.job_ref_number = %s""",(job_ref,))
        dados = cursor.fetchall()
    except Exception as e:
        print(f"Erro: {e}")
        return -1
    finally:
        connection.close()
        return dados