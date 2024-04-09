import psycopg2
import conection.connect as connecao

def cadastrar(mud_type, rig_type, density_type, hole_type, rig_total_volume, density, viscosity_vp, viscosity_yp, hole_volume,id_report):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO fluid_information_cp(mud_type, rig_type, density_type, hole_type, rig_total_volume, density, viscosity_vp, viscosity_yp, hole_volume,id_report) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """,(mud_type, rig_type, density_type, hole_type, rig_total_volume, density, viscosity_vp, viscosity_yp, hole_volume,id_report,))    
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
        return e
    return 0

def editar(mud_type, rig_type, density_type, hole_type, rig_total_volume, density, viscosity_vp, viscosity_yp, hole_volume, id):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE fluid_information_cp set mud_type = %s, rig_type = %s, hole_type = %s, rig_total_volume = %s, density = %s, viscosity_vp = %s, viscosity_yp = %s, hole_volume = %s, where id = %s ",(mud_type, rig_type, density_type, hole_type, rig_total_volume, density, viscosity_vp, viscosity_yp, hole_volume,id))                
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
        return -1
    return 0

def delete_data(density, viscosity_vp, viscosity_yp, hole_volume):
    connection = connecao.cria_connecao()
    try:
        cursor = connection.cursor()
        cursor.execute(""" DELETE FROM fluid_information_cp WHERE density = %s AND viscosity_vp = %s AND viscosity_yp = %s AND hole_volume = %s """,(density, viscosity_vp, viscosity_yp, hole_volume))
        connection.commit()
    except Exception as e:
        print(f"Erro: {e}")
        return -1
    return 0   
                
def listar():    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM fluid_information_cp")
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
        cursor.execute("SELECT * FROM fluid_information_cp")
        dados = cursor.fetchall()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados
    
def buscar_id_by_hole_volume(hole_volume):
    connection = connecao.cria_connecao()
    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT id FROM fluid_information_cp WHERE hole_volume = %s""",(hole_volume,))
            id_fluid = cursor.fetchone()
            return id_fluid
    finally:
        connection.close()


def buscar_fluid_information_by_job_ref(job_ref):
    connection = connecao.cria_connecao()
    try:
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT * FROM fluid_information_cp, report_information_cp,mud_type_cp WHERE fluid_information_cp.id_report = report_information_cp.id 
            AND mud_type_cp.id = fluid_information_cp.mud_type
            AND report_information_cp.job_ref_number = %s""",(job_ref,))
            dados = cursor.fetchone()
            return dados
    except Exception as e:
        return e
    finally:
        return dados
