import psycopg2
import conection.connect as connecao
import config_email.config_email

def cadastrar(type_fluid_proprieties, value, report_information_cp):
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO drilling_fluid_proprieties_cp(type_fluid_proprieties, value, report_information_cp) VALUES (%s, %s, %s)""", (type_fluid_proprieties, value, report_information_cp))
        connection.commit()
        cursor.close()
        return 0
    except Exception as e:
        print(f"Erro: {e}")
        body = f"Erro: {e}"
        config_email.config_email.save_error(body)
        return -1

def editar(type_fluid_proprieties, value, report_information_cp):
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE drilling_fluid_proprieties_cp SET type_fluid_proprieties = %s, value = %s, report_information_cp = %s, WHERE id = %s", (type_fluid_proprieties, value, report_information_cp))
        connection.commit()
        cursor.close()
        return 0
    except Exception as e:
        print(f"Erro: {e}")
        body = f"Erro: {e}"
        config_email.config_email.save_error(body)
        return -1
        
def eliminar(type_fluid_proprieties, value, report_information_cp):
    connection = connecao.cria_connecao()
    try:
        cursor = connection.cursor()
        cursor.execute(""" DELETE FROM drilling_fluid_proprieties_cp WHERE type_fluid_proprieties = %s AND value = %s""", (type_fluid_proprieties, value))
        connection.commit()
        return 0
    except Exception as e:
        print(f"Erro: {e}")
        body = f"Erro: {e}"
        config_email.config_email.save_error(body)
        return -1
    
################## Listagens #####################

def listar_drilling_fluid():
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM drilling_fluid_proprieties_cp")
        dados = cursor.fetchall()
        dados_novo = [item[1] for item in dados]
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados_novo    


def buscar_drilling_information_by_job_ref(job_ref):
    connection = connecao.cria_connecao()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""SELECT type_fluid_proprieties.type,drilling_fluid_proprieties_cp.value FROM drilling_fluid_proprieties_cp,type_fluid_proprieties,
            report_information_cp WHERE drilling_fluid_proprieties_cp.report_information_cp = report_information_cp.id
            AND drilling_fluid_proprieties_cp.type_fluid_proprieties = type_fluid_proprieties.id
            AND report_information_cp.job_ref_number = %s""",(job_ref,))
            dados = cursor.fetchall()
            return dados
    except Exception as e:
        return e
    finally:
        return dados                    
        