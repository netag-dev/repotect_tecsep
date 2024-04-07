import psycopg2
import conection.connect as connecao

def cadastrar(ft_fluid_type_filtered, ft_daily_total, ft_density_sg,ft_density_type, ft_viscosity, ft_hole_volume,ft_hole_volume_type, ft_vol_filtered_date, id_report_ft):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO tb_fluid_information_ft(ft_fluid_type_filtered, ft_daily_total, ft_density_sg,ft_density_type, ft_viscosity, ft_hole_volume,ft_hole_volume_type, ft_vol_filtered_date, id_report_ft) 
                       values(%s,%s,%s,%s,%s,%s,%s,%s,%s) """,(ft_fluid_type_filtered, ft_daily_total, ft_density_sg,ft_density_type, ft_viscosity, ft_hole_volume,ft_hole_volume_type, ft_vol_filtered_date, id_report_ft))    
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def editar(param1, param2, param3, param4, param5, param6, param7, param8):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_fluid_information_ft set ft_fluid_type_filtered = '"+param2+"', ft_daily_total = '"+param3+"', ft_density_sg = '"+param4+"', ft_viscosity = '"+param5+"', ft_hole_volume = '"+param6+"', ft_vol_filtered_date = '"+param7+"',  id_physical_person = '"+param8+"' where id = '"+param1+"' ")                
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()

def eliminar(param):
    try: 
        connection = psycopg2.connect( database = "repotec", host = "localhost", user = "postgres", password = "0000", port = "5432" )
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tb_fluid_information_ft WHERE id = '"+param+"' ")
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
                
def listar():    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT *FROM tb_fluid_information_ft")
        dados = cursor.fetchall()
        for linha in dados:
            print(linha)
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()


def listar_fluid_por_job_ref(job_ref):    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT ft_fluid_type_filtered,ft_daily_total,ft_density_sg || '(' || ft_density_type || ')' as ft_density_sg ,ft_viscosity,ft_hole_volume || '(' || ft_hole_volume_type || ')' as ft_hole_volume,ft_vol_filtered_date FROM tb_fluid_information_ft,tb_report_ft,tb_report_header WHERE
                        tb_fluid_information_ft.id_report_ft = tb_report_ft.id AND
                        tb_report_ft.id_report_header = tb_report_header.id AND
                        tb_report_header.rpt_job_ref_number = %s""",(job_ref,))
        dados = cursor.fetchall()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados

    



