import psycopg2
import conection.connect as connecao

def cadastrar(ft_wellbone_displacement, ft_time, ft_pumping_time, ft_volume_pumped,ft_volume_pumped_type, ft_ntu, ft_tss_perc_solids, id_report_ft):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()

        # Retornar O Valor Do Sample

        cursor.execute(""" SELECT COUNT(ft_sample) FROM tb_fluid_analisys_ft WHERE id_report_ft = %s """,(id_report_ft))
        total_sample = cursor.fetchone()
        total_sample = total_sample[0]
        print(total_sample)
        if total_sample is None :
            total_sample = 0
        total_sample += 1
        var_sample = "Sample "+str(total_sample)

        cursor.execute(""" INSERT INTO tb_fluid_analisys_ft(ft_wellbone_displacement, ft_time, ft_pumping_time, ft_volume_pumped,ft_volume_pumped_type, ft_ntu, ft_tss_perc_solids, ft_sample, id_report_ft)
                       values(%s,%s,%s,%s,%s,%s,%s,%s,%s) """,(ft_wellbone_displacement, ft_time, ft_pumping_time, ft_volume_pumped,ft_volume_pumped_type, ft_ntu, ft_tss_perc_solids, var_sample, id_report_ft))    
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
        connection = psycopg2.connect( database = "repotec", host = "localhost", user = "postgres", password = "0000", port = "5432" )
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_fluid_analisys_ft set ft_wellbone_displacement = '"+param2+"', ft_time= '"+param3+"', ft_pumping_time= '"+param4+"', ft_volume_pumped= '"+param5+"', ft_ntu= '"+param6+"', ft_tss_perc_solids= '"+param7+"', id_physical_person = '"+param8+"' where id = '"+param1+"' ")                
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
        cursor.execute("DELETE FROM tb_fluid_analisys_ft WHERE id = '"+param+"' ")
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
                
def listar():    
    try: 
        connection = psycopg2.connect( database = "repotec", host = "localhost", user = "postgres", password = "0000", port = "5432" )
        cursor = connection.cursor()
        cursor.execute("SELECT *FROM tb_fluid_analisys_ft")
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


def listar_por_job_ref(job_ref):    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("""SELECT ft_wellbone_displacement,ft_sample,ft_time,ft_pumping_time,ft_volume_pumped || '(' || ft_volume_pumped_type || ')' as ft_volume_pumped ,ft_ntu,ft_tss_perc_solids FROM tb_fluid_analisys_ft,tb_report_ft,tb_report_header 
                    WHERE tb_fluid_analisys_ft.id_report_ft =  tb_report_ft.id 
                    AND tb_report_header.id = tb_report_ft.id_report_header
                    AND tb_report_header.rpt_job_ref_number = %s ORDER BY tb_fluid_analisys_ft.id DESC""",(job_ref,))
        dados = cursor.fetchall()
        
        print(dados)

        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados




    



