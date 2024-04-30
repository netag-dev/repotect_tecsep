import psycopg2
import conection.connect as connecao
import config_email.config_email as email

def cadastrar(findings, yes_no, time, contractor, report_information_cp):
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO audit_questionnaire_cp (findings, yes_no, time, contractor, report_information_cp) VALUES (%s, %s, %s, %s, %s) """,
(findings, yes_no, time, contractor, report_information_cp))
        connection.commit()
        cursor.close()
        return 0
    except Exception as e:
        print(f"Erro na Base de dados: {e}")
        body = f"Erro na Base de dados: {e}"
        email.save_error(body)
        return -1
        
def buscar_avarage_information_by_job_ref(job_ref):
    connection = connecao.cria_connecao()
    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT audit_questionnaire_cp.findings,audit_questionnaire_cp.yes_no,audit_questionnaire_cp.time,audit_questionnaire_cp.contractor
            FROM audit_questionnaire_cp,report_information_cp WHERE  
            report_information_cp.id = audit_questionnaire_cp.report_information_cp
            AND report_information_cp.job_ref_number = %s """,(job_ref,))
            dados = cursor.fetchall()
            return dados
    except Exception as e:
        return e
    finally:
        return dados  
