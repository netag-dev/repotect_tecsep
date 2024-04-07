import psycopg2
import conection.connect as connecao

def add_preapred_to_report(id_physical_peraon, id_report_filtration):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO tb_prepared(id_physical_person,id_report_filtration) values (%s,%s) ",(id_physical_peraon,id_report_filtration))    
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def add_approved_to_report(id_physical_peraon, id_report_filtration):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO tb_aproved(id_employee,id_report_filtration) values (%s,%s) ",(id_physical_peraon,id_report_filtration))    
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()


def buscar_id_supersover_nome_por(nome ):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT id From tb_physical_person WHERE pp_name = %s""",(nome,))    
        id_supervisor = cursor.fetchone()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            return id_supervisor
        
def buscar_id_empregado_nome_por(nome ):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT id From tb_employee_ft WHERE emp_name = %s""",(nome,))    
        id_supervisor = cursor.fetchone()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            return id_supervisor
        

def buscar_nome_prepared(job_ref ):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT pp_name FROM tb_physical_person, tb_prepared, tb_report_ft,tb_report_header WHERE
                    tb_prepared.id_physical_person = tb_physical_person.id AND
                    tb_prepared.id_report_filtration = tb_report_ft.id AND
                    tb_report_ft.id_report_header = tb_report_header.id AND
                    tb_report_header.rpt_job_ref_number =  %s """,(job_ref,))    
        lista_prepared = cursor.fetchall()

        nova_lista_prepared = [item[0] for item in lista_prepared]

        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            return nova_lista_prepared
        

def buscar_nome_aproved(job_ref ):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT emp_name FROM tb_employee_ft, tb_aproved, tb_report_ft,tb_report_header WHERE
                    tb_aproved.id_employee = tb_employee_ft.id AND
                    tb_aproved.id_report_filtration = tb_report_ft.id AND
                    tb_report_ft.id_report_header = tb_report_header.id AND
                    tb_report_header.rpt_job_ref_number =  %s """,(job_ref,))    
        lista_prepared = cursor.fetchall()

        nova_lista_prepared = [item[0] for item in lista_prepared]

        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            return nova_lista_prepared