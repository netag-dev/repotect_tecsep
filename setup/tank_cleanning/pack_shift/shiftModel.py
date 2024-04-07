import psycopg2
import conection.connect as connecao

def cadastrar_dayshift_personeel(sh_trade,sh_planed_demmed,sh_crew_change,id_period,id_employee,id_report_tc):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO tb_shift_tc(sh_trade,sh_planed_demmed,sh_crew_change,id_period,id_employee,id_report_tc) 
                       values(%s,%s,%s,%s,%s,%s)""",(sh_trade,sh_planed_demmed,sh_crew_change,id_period,id_employee,id_report_tc,))    
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def listar_tipo_shift():
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT pr_type FROM tb_period_tc """)
        lista_tipo_shift = cursor.fetchall()
        lista_tipo_shift_convertida = [item[0] for item in lista_tipo_shift]
        cursor.close()
    except Exception as e:
        print(f"Erro ao listar :{e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            
            return lista_tipo_shift_convertida
        

def buscar_id_shift_por_tipo(tipo):
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT id FROM tb_period_tc WHERE pr_type = %s """,(tipo,))
        id_turno = cursor.fetchone()
        cursor.close()
    except Exception as e:
        print(f"Erro ao retornar id do turno : {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

            return id_turno

def editar(param1, param2, param3, param4, param5, param6, param7):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_shift_tc set sh_name = '"+param2+"', sh_trade = '"+param3+"', sh_planed_demmed = '"+param4+"', sh_crew_change = '"+param5+"', id_period = '"+param6+"', id_physical_person = '"+param7+"' where id = '"+param1+"' ")                
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
        cursor.execute("DELETE FROM tb_shift_tc WHERE id = '"+param+"' ")
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
        cursor.execute("SELECT *FROM tb_shift_tc")
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


def buscar_shift_person_day(id_report):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT  tb_employee_tc.emp_name, sh_trade, sh_planed_demmed, sh_crew_change FROM tb_shift_tc,tb_employee_tc 
                        WHERE tb_employee_tc.id = tb_shift_tc.id_employee AND id_report_tc = %s AND id_period = 1 """,(id_report,))
            
            lista_perssoa_turno_diurno = cursor.fetchall()
            #print(lista_cabecalho_information[0])


            return lista_perssoa_turno_diurno
    finally:
        connection.close()


def buscar_shift_person_nigth(id_report):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT  tb_employee_tc.emp_name, sh_trade, sh_planed_demmed, sh_crew_change FROM tb_shift_tc,tb_employee_tc 
                        WHERE tb_employee_tc.id = tb_shift_tc.id_employee AND id_report_tc = %s AND id_period = 2  """,(id_report,))
            
            lista_perssoa_turno_noturno = cursor.fetchall()
            #print(lista_cabecalho_information[0])


            return lista_perssoa_turno_noturno
    finally:
        connection.close()

    



