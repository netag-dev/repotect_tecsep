import psycopg2

def cadastrar(param1, param2, param3, param4, param5, param6):
    try: 
        connection = psycopg2.connect( database = "repotec", host = "102.219.126.14", user = "postgres", password = "postgres", port = "5432" )
        cursor = connection.cursor()
        cursor.execute("INSERT INTO tb_typeHse_tc values('"+param1+"','"+param2+"','"+param3+"','"+param4+"','"+param5+"','"+param6+"') ")    
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
        connection = psycopg2.connect( database = "repotec", host = "102.219.126.14", user = "postgres", password = "postgres", port = "5432" )
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_typeHse_tc set thse_safety_obs = '"+param2+"', thse_near_miss = '"+param3+"', thse_permit_audits = '"+param4+"', thse_site_audits = '"+param5+"', thse_safety_meetings = '"+param6+"' where id = '"+param1+"' ")                
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()

def eliminar(param):
    try: 
        connection = psycopg2.connect( database = "repotec", host = "102.219.126.14", user = "postgres", password = "postgres", port = "5432" )
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tb_typeHse_tc WHERE id = '"+param+"' ")
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
    finally:
        if connection:
            cursor.close()
                
def listar():    
    try: 
        connection = psycopg2.connect( database = "repotec", host = "102.219.126.14", user = "postgres", password = "postgres", port = "5432" )
        cursor = connection.cursor()
        cursor.execute("SELECT *FROM tb_typeHse_tc")
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






