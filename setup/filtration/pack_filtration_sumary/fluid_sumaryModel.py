import psycopg2
import conection.connect as connecao

def cadastrar(ft_start_time,ft_stop_time, ft_total_minutes_per_cicles, ft_volume_per_cicles,ft_volume_per_cicles_type, ft_d_e_per_cicle_20kg, ft_cartridge_filtrers, id_report_ft, id_num_cicle):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO tb_fluid_sumary_ft(ft_start_time,ft_stop_time, ft_total_minutes_per_cicles, ft_volume_per_cicles,ft_volume_per_cicles_type, ft_d_e_per_cicle_20kg, ft_cartridge_filtrers, id_report_ft, id_num_cicle) 
                       values(%s,%s,%s,%s,%s,%s,%s,%s,%s) """,(ft_start_time,ft_stop_time, ft_total_minutes_per_cicles, ft_volume_per_cicles,ft_volume_per_cicles_type, ft_d_e_per_cicle_20kg, ft_cartridge_filtrers, id_report_ft, id_num_cicle,))    
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()




def editar(param1, param2, param3, param4, param5, param6, param7, param8, param9):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_fluid_sumary_ft set ft_cicles = '"+param2+"', ft_start_time = '"+param3+"', ft_stop_time = '"+param4+"', ft_total_minutes_per_cicles = '"+param5+"', ft_volume_per_cicles = '"+param6+"', ft_d_e_per_cicle_20kg = '"+param7+"', ft_cartridge_filtrers = '"+param8+"',  id_physical_person = '"+param9+"' where id = '"+param1+"' ")                
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()

def eliminar(param):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tb_fluid_sumary_ft WHERE id = '"+param+"' ")
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
        cursor.execute("SELECT *FROM tb_fluid_sumary_ft")
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


def listar_ciclos():    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT ft_num_cicles FROM tb_cicles_ft")
        dados = cursor.fetchall()
        
        dados_convertido = [item[0] for item in dados]
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados_convertido
        


def buscar_report_primeiro_ciclo(job_ref):    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT ft_start_time,ft_stop_time,ft_total_minutes_per_cicles,ft_volume_per_cicles,ft_volume_per_cicles_type,ft_d_e_per_cicle_20kg,ft_cartridge_filtrers
                        FROM tb_fluid_sumary_ft, tb_cicles_ft, tb_report_ft, tb_report_header 
                        WHERE tb_fluid_sumary_ft.id_report_ft = tb_report_ft.id
                        AND tb_cicles_ft.id = tb_fluid_sumary_ft.id_num_cicle
                        AND tb_report_header.id = tb_report_ft.id_report_header
                        AND tb_report_header.rpt_job_ref_number = %s
                        AND tb_cicles_ft.ft_num_cicles = '1' """,(job_ref,))
        dados = cursor.fetchone()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados
        

def buscar_report_segundo_ciclo(job_ref):    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT ft_start_time,ft_stop_time,ft_total_minutes_per_cicles,ft_volume_per_cicles,ft_volume_per_cicles_type,ft_d_e_per_cicle_20kg,ft_cartridge_filtrers
                        FROM tb_fluid_sumary_ft, tb_cicles_ft, tb_report_ft, tb_report_header 
                        WHERE tb_fluid_sumary_ft.id_report_ft = tb_report_ft.id
                        AND tb_cicles_ft.id = tb_fluid_sumary_ft.id_num_cicle
                        AND tb_report_header.id = tb_report_ft.id_report_header
                        AND tb_report_header.rpt_job_ref_number = %s
                        AND tb_cicles_ft.ft_num_cicles = '2' """,(job_ref,))
        dados = cursor.fetchone()

        if dados is None:
            lista_vazia = ["","","","","","","",""]
            dados = lista_vazia
                
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados
        

def buscar_report_terceiro_ciclo(job_ref):    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT ft_start_time,ft_stop_time,ft_total_minutes_per_cicles,ft_volume_per_cicles,ft_volume_per_cicles_type,ft_d_e_per_cicle_20kg,ft_cartridge_filtrers
                        FROM tb_fluid_sumary_ft, tb_cicles_ft, tb_report_ft, tb_report_header 
                        WHERE tb_fluid_sumary_ft.id_report_ft = tb_report_ft.id
                        AND tb_cicles_ft.id = tb_fluid_sumary_ft.id_num_cicle
                        AND tb_report_header.id = tb_report_ft.id_report_header
                        AND tb_report_header.rpt_job_ref_number = %s
                        AND tb_cicles_ft.ft_num_cicles = '3' """,(job_ref,))
        dados = cursor.fetchone()
        if dados is None:
            lista_vazia = ["","","","","","","",""]
            dados = lista_vazia
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados
        

def buscar_report_quarto_ciclo(job_ref):    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT ft_start_time,ft_stop_time,ft_total_minutes_per_cicles,ft_volume_per_cicles,ft_volume_per_cicles_type,ft_d_e_per_cicle_20kg,ft_cartridge_filtrers
                        FROM tb_fluid_sumary_ft, tb_cicles_ft, tb_report_ft, tb_report_header 
                        WHERE tb_fluid_sumary_ft.id_report_ft = tb_report_ft.id
                        AND tb_cicles_ft.id = tb_fluid_sumary_ft.id_num_cicle
                        AND tb_report_header.id = tb_report_ft.id_report_header
                        AND tb_report_header.rpt_job_ref_number = %s
                        AND tb_cicles_ft.ft_num_cicles = '4' """,(job_ref,))
        dados = cursor.fetchone()
        if dados is None:
            lista_vazia = ["","","","","","","",""]
            dados = lista_vazia
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados
        

def buscar_report_quinto_ciclo(job_ref):    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT ft_start_time,ft_stop_time,ft_total_minutes_per_cicles,ft_volume_per_cicles,ft_volume_per_cicles_type,ft_d_e_per_cicle_20kg,ft_cartridge_filtrers
                        FROM tb_fluid_sumary_ft, tb_cicles_ft, tb_report_ft, tb_report_header 
                        WHERE tb_fluid_sumary_ft.id_report_ft = tb_report_ft.id
                        AND tb_cicles_ft.id = tb_fluid_sumary_ft.id_num_cicle
                        AND tb_report_header.id = tb_report_ft.id_report_header
                        AND tb_report_header.rpt_job_ref_number = %s
                        AND tb_cicles_ft.ft_num_cicles = '5' """,(job_ref,))
        dados = cursor.fetchone()
        if dados is None:
            lista_vazia = ["","","","","","","",""]
            dados = lista_vazia
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados
        


def buscar_report_sexto_ciclo(job_ref):    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT ft_start_time,ft_stop_time,ft_total_minutes_per_cicles,ft_volume_per_cicles,ft_volume_per_cicles_type,ft_d_e_per_cicle_20kg,ft_cartridge_filtrers
                        FROM tb_fluid_sumary_ft, tb_cicles_ft, tb_report_ft, tb_report_header 
                        WHERE tb_fluid_sumary_ft.id_report_ft = tb_report_ft.id
                        AND tb_cicles_ft.id = tb_fluid_sumary_ft.id_num_cicle
                        AND tb_report_header.id = tb_report_ft.id_report_header
                        AND tb_report_header.rpt_job_ref_number = %s
                        AND tb_cicles_ft.ft_num_cicles = '6' """,(job_ref,))
        dados = cursor.fetchone()
        if dados is None:
            lista_vazia = ["","","","","","","",""]
            dados = lista_vazia
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados
        

def buscar_report_setimo_ciclo(job_ref):    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT ft_start_time,ft_stop_time,ft_total_minutes_per_cicles,ft_volume_per_cicles,ft_volume_per_cicles_type,ft_d_e_per_cicle_20kg,ft_cartridge_filtrers
                        FROM tb_fluid_sumary_ft, tb_cicles_ft, tb_report_ft, tb_report_header 
                        WHERE tb_fluid_sumary_ft.id_report_ft = tb_report_ft.id
                        AND tb_cicles_ft.id = tb_fluid_sumary_ft.id_num_cicle
                        AND tb_report_header.id = tb_report_ft.id_report_header
                        AND tb_report_header.rpt_job_ref_number = %s
                        AND tb_cicles_ft.ft_num_cicles = '7' """,(job_ref,))
        dados = cursor.fetchone()
        if dados is None:
            lista_vazia = ["","","","","","","",""]
            dados = lista_vazia
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados
        


def buscar_report_oitavo_ciclo(job_ref):    
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT ft_start_time,ft_stop_time,ft_total_minutes_per_cicles,ft_volume_per_cicles,ft_volume_per_cicles_type,ft_d_e_per_cicle_20kg,ft_cartridge_filtrers
                        FROM tb_fluid_sumary_ft, tb_cicles_ft, tb_report_ft, tb_report_header 
                        WHERE tb_fluid_sumary_ft.id_report_ft = tb_report_ft.id
                        AND tb_cicles_ft.id = tb_fluid_sumary_ft.id_num_cicle
                        AND tb_report_header.id = tb_report_ft.id_report_header
                        AND tb_report_header.rpt_job_ref_number = %s
                        AND tb_cicles_ft.ft_num_cicles = '8' """,(job_ref,))
        dados = cursor.fetchone()
        if dados is None:
            lista_vazia = ["","","","","","","",""]
            dados = lista_vazia
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados
        



    



