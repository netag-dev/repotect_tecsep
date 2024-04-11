import psycopg2
import conection.connect as connecao

def cadastrar(param1, param2, param3, param4, param5, param6): 
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO tb_legal_person(lp_nif,lp_name,lp_email,lp_phone,lp_logo,lp_address) values('"+param1+"','"+param2+"','"+param3+"','"+param4+"','"+param5+"','"+param6+"') ")
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao na Base de Dados: {e}")
        return -1
    finally: 
        if connection:
            cursor.close()
            connection.close()
        return 0
    
def editar(nif, name, email, phone, adress): 
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_legal_person SET lp_name = %s, lp_email = %s, lp_phone = %s, lp_address = %s WHERE lp_nif = %s ",(name,email,phone,adress,nif,))
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao actualizar dados no tb_legal_person: {e}")
        return -1
    finally:
        return 0

def listar(): 
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tb_legal_person")
        dados = cursor.fetchall()
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao Listar dados no tb_physical_person: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
        return dados

def eliminar(param): 
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tb_legal_person WHERE lp_nif = %s ",(param,))
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao eliminar dados no tb_legal_person: {e}")
        return -1
    finally:
        if connection:
            cursor.close()
            connection.close() 
        return 0
    

##########################################################################################################################################
#                                                           WELL
##########################################################################################################################################

def cadastrar_poco(nome,numero,cliente,pessoa_criar):
    try: 
        connection = connecao.cria_connecao()
        print("Conexão Aberta.")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO tb_well(wl_name,wl_number,id_legal_person,id_physical_person) values(%s,%s,%s,%s) ",(nome,numero,cliente,pessoa_criar))
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao inserir dados no tb_well: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexão fechada.")

def listar_poco(): 
    try: 
        connection = connecao.cria_connecao()
        print("Conexão Aberta.")
        cursor = connection.cursor()
        cursor.execute("SELECT wl_number,wl_name,lp_name FROM tb_legal_person,tb_well WHERE tb_legal_person.id = tb_well.id_legal_person")
        dados = cursor.fetchall()
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao Listar dados na Tabela Well: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
        return dados

def eliminar_poco(param): 
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tb_well WHERE wl_number = %s ",(param,))
        connection.commit()
        cursor.close()
    except Exception as e: 
        print(f"Erro ao eliminar dados no tb_well: {e}")
        return -1
    finally:
        if connection:
            cursor.close()
            connection.close() 
            return 0

def editar_poco(param1, param2): 
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_well set wl_number = %s, wl_name = %s where wl_number = %s ",(param1, param2, param1))
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao actualizar dados no tb_well: {e}")
        return -1
    finally:
        if connection:
            cursor.close()
            connection.close()
            return 0
