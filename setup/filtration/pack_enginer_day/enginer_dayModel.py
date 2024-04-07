import psycopg2
import conection.connect as connecao

def cadastrar(eng_shift, eng_total_dayst, id_employee, id_report_ft):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()

        # Retornar O Valor Do Sample

        cursor.execute(""" INSERT INTO tb_engineer_ft(eng_shift, eng_total_dayst, id_employee, id_report_ft)
                       values(%s,%s,%s,%s) """,(eng_shift, eng_total_dayst, id_employee, id_report_ft))
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()



def listar(job_ref):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()

        # Retornar O Valor Do Sample

        cursor.execute(""" SELECT emp_name,eng_shift,eng_total_dayst FROM tb_engineer_ft,tb_employee_ft,tb_report_header,tb_report_ft
                        WHERE tb_report_header.id = tb_report_ft.id_report_header
                        AND tb_report_ft.id =  tb_engineer_ft.id_report_ft
                        AND tb_employee_ft.id = tb_engineer_ft.id_employee
                        AND tb_report_header.rpt_job_ref_number = %s""",(job_ref,))
        
        dados = cursor.fetchall()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            return dados