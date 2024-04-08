import psycopg2
import conection.connect as connecao

def cadastrar(cp_name, cp_unit_completed, cp_element_completed, cp_perc_completed_date, cp_comment, id_physical_person, id_report_tc):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO tb_competency_profiles_tc(cp_name, cp_unit_completed, cp_element_completed, cp_perc_completed_date, cp_comment, id_physical_person, id_report_tc) 
                       values(%s,%s,%s,%s,%s,%s,%s)""",(cp_name, cp_unit_completed, cp_element_completed, cp_perc_completed_date, cp_comment, id_physical_person, id_report_tc))    
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def editar(param1, param2, param3, param4, param5, param6, param7):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_competency_profiles_tc set cp_name = '"+param2+"', cp_unit_completed = '"+param3+"', cp_element_completed = '"+param4+"', cp_perc_completed_date = '"+param5+"', cp_comment = '"+param6+"', id_physical_person = '"+param7+"' where id = '"+param1+"' ")                
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
        cursor.execute("DELETE FROM tb_competency_profiles_tc WHERE id = '"+param+"' ")
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
        cursor.execute("SELECT *FROM tb_competency_profiles_tc")
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


def buscar_competence_profile(ref_report):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT cp_name,cp_unit_completed,cp_element_completed,cp_perc_completed_date,cp_comment FROM tb_report_tc,tb_competency_profiles_tc 
                            WHERE tb_report_tc.id = tb_competency_profiles_tc.id_report_tc AND tb_report_tc.id = %s """,(ref_report,))
            
            lista_prfile_competence = cursor.fetchall()
            #print(lista_cabecalho_information[0])


            return lista_prfile_competence
    finally:
        connection.close()


def get_id_consumibele(nome_consumivel):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT id FROM tb_consumables_tc WHERE cs_name = %s """,(nome_consumivel,))
            
            id_consumivel = cursor.fetchone()

            return id_consumivel
    finally:
        connection.close()


def get_stoq_consumivel(id):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT cs_daily_used FROM tb_consumables_tc WHERE id = %s """,(id,))
            
            quantity = cursor.fetchone()

            return quantity[0]
    finally:
        connection.close()


def get_id_ppe(nome_ppe):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT id FROM tb_pipe_tc WHERE pi_name = %s """,(nome_ppe,))
            
            id_ppe = cursor.fetchone()

            return id_ppe
    finally:
        connection.close()


def get_stoq_ppe(id):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT pi_daily_used FROM tb_pipe_tc WHERE id = %s """,(id,))
            
            quantity = cursor.fetchone()

            return quantity[0]
    finally:
        connection.close()


def get_id_asset(nome_asset):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT id FROM tb_assets_tc WHERE as_name = %s """,(nome_asset,))
            
            id_asset = cursor.fetchone()

            return id_asset
    finally:
        connection.close()


def get_stoq_asset(id):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT as_quantity FROM tb_assets_tc WHERE id = %s """,(id,))
            
            quantity = cursor.fetchone()

            return quantity[0]
    finally:
        connection.close()

        ################################### Cadastros ####################################################
    
def cadastrar_consumivel(id_consumivel,id_report,quantidade):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" INSERT INTO tb_consumiveis_tc_report(id_consumiveis,id_report_tc,quantidade_add) values (%s,%s,%s) """,(id_consumivel,id_report,quantidade))
            
            connection.commit()
    
    except Exception as e:
        print(f"Erro ao Salvar Consumivel {e}")
        return -1

    finally:
        return 0
    

def cadastrar_ppe(id,id_report,quantidade):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" INSERT INTO tb_ppe_tc_report(id_ppe,id_report_tc,quantidade_add) values (%s,%s,%s) """,(id,id_report,quantidade))
            
            connection.commit()
    
    except Exception as e:
        print(f"Erro ao Salvar Consumivel")
        return -1

    finally:
        return 0
    

def cadastrar_asset(id,id_report,quantidade):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" INSERT INTO tb_asset_tc_report(id_asset,id_report_tc,quantidade_add) values (%s,%s,%s) """,(id,id_report,quantidade))
            
            connection.commit()
    
    except Exception as e:
        print(f"Erro ao Salvar Consumivel")
        return -1

    finally:
        return 0
    

    ############################################ Actualizar O Stoque ##############################################
def update_stoque_consumiveis(id_consumivel,quantidade):
    connection = connecao.cria_connecao()

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" UPDATE tb_consumables_tc SET cs_daily_used = %s WHERE id = %s """,(quantidade,id_consumivel))
            
            connection.commit()

    except Exception as e:
        print(f"Erro ao Actualizar Quantidade de Consumivel {e}")
        return -1

    finally:
        return 0
    

def update_stoque_ppe(id,quantidade):
    connection = connecao.cria_connecao()

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" UPDATE tb_pipe_tc SET pi_daily_used = %s WHERE id = %s """,(quantidade,id))
            
            connection.commit()

    except Exception as e:
        print(f"Erro ao Actualizar Quantidade de PPE {e}")
        return -1

    finally:
        return 0
    

def update_stoque_asset(id,quantidade):
    connection = connecao.cria_connecao()

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" UPDATE tb_assets_tc SET as_quantity = %s WHERE id = %s """,(quantidade,id))
            
            connection.commit()

    except Exception as e:
        print(f"Erro ao Actualizar Quantidade de PPE {e}")
        return -1

    finally:
        return 0


