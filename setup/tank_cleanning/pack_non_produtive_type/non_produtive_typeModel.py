import psycopg2
import conection.connect as connecao


def editar(param1, param2, param3, param4, param5, param6, param7, param8, param9, param10):
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_non_produtive_type_tc set npt_breaks = '"+param2+"', npt_weather = '"+param3+"', npt_safety_meetings = '"+param4+"', npt_indutions = '"+param5+"', npt_travel_to = '"+param6+"', npt_toolbox = '"+param7+"', npt_guaranteed = '"+param8+"', npt_permit = '"+param9+"', npt_ops_delays = '"+param10+"' where id = '"+param1+"' ")                
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
        cursor.execute("DELETE FROM tb_non_produtive_type_tc WHERE id = '"+param+"' ")
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
        cursor.execute("SELECT npt_description FROM tb_non_produtive_type_tc")
        lista_non_produtive_type = cursor.fetchall()

        new_lista_non_produtive_type = [item[0] for item in lista_non_produtive_type]

        
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
            return new_lista_non_produtive_type
        
def buscar_id_non_produtive_por_tipo(tipo):
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT id FROM tb_non_produtive_type_tc WHERE npt_description = %s """,(tipo,))
        id_turno = cursor.fetchone()
        cursor.close()
    except Exception as e:
        print(f"Erro ao retornar id do turno : {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

            return id_turno
        



    



