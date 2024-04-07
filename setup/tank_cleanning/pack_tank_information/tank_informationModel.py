import psycopg2
import conection.connect as connecao

def cadastrar(ti_number_tank, ti_volume_waste, ti_type_waste, ti_tank_type, id_report_tc):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO tb_tank_information_tc (ti_number_tank, ti_volume_waste, ti_type_waste, ti_tank_type, id_report_tc) 
                       values(%s,%s,%s,%s,%s)""",(ti_number_tank, ti_volume_waste, ti_type_waste, ti_tank_type, id_report_tc))    
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def editar(param1, param2, param3, param4, param5, param6):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_tank_information_tc set ti_number_tank = '"+param2+"', ti_volume_waste = '"+param3+"', ti_type_waste = '"+param4+"', ti_tank_type = '"+param5+"', id_report_tc = '"+param6+"' where id = '"+param1+"' ")                
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
        cursor.execute("DELETE FROM tb_tank_information_tc WHERE id = '"+param+"' ")
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
        cursor.execute("SELECT *FROM tb_tank_information_tc")
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


def buscar_tank_information(id_report):
    connection = connecao.cria_connecao()
    print("Conexão Aberta.")

    try:
        with connection.cursor() as cursor:
            
            cursor.execute(""" SELECT ti_number_tank,ti_volume_waste,ti_type_waste,ti_tank_type FROM tb_tank_information_tc,
                    tb_report_tc,tb_report_header WHERE

                    tb_tank_information_tc.id_report_tc = tb_report_tc.id
                    AND tb_report_tc.id_report_header = tb_report_header.id
                    AND tb_report_tc.id = %s""",(id_report,))
            
            lista_prfile_competence = cursor.fetchall()


            return lista_prfile_competence
    finally:
        connection.close()
   



