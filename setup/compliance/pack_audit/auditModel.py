import psycopg2
import conection.connect as connecao

def cadastrar(findings, yes_no, time, contractor, report_information_cp):
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO audit_questionnaire_cp (findings, yes_no, time, contractor, report_information_cp) VALUES (%s, %s, %s, %s, %s) """,
(findings, yes_no, time, contractor, report_information_cp))
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