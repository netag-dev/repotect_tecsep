import psycopg2
import conection.connect as connecao

def cadastrar(param1, param2, param3, param4, param5, param6): 
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()

        with open(param5, 'rb') as file:
            data = file.read()
            cursor.execute(""" INSERT INTO tb_legal_person(lp_nif,lp_name,lp_email,lp_phone,lp_logo,lp_address) values(%s,%s,%s,%s,%s,%s) """,(param1,param2,param3,param4,data,param6,))
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
        return -1
    finally:
        return 0

def listar_poco(): 
    try: 
        connection = connecao.cria_connecao()
        print("Conexão Aberta.")
        cursor = connection.cursor()
        cursor.execute("SELECT tb_well.id,wl_number,wl_name,lp_name FROM tb_legal_person,tb_well WHERE tb_legal_person.id = tb_well.id_legal_person")
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
        cursor.execute("DELETE FROM tb_well WHERE id = %s ",(param,))
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

def editar_poco(param1, param2, param3,param4): 
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_well set  wl_name= %s, wl_number = %s, id_legal_person = %s where id = %s ",(param1, param2, param3, param4))
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
        
def buscar_poco_por_id(id_poco): 
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT wl_number,wl_name,tb_legal_person.lp_name FROM tb_legal_person,tb_well  
        WHERE tb_legal_person.id = tb_well.id_legal_person
        AND tb_well.id = %s """,(id_poco))
        dados = cursor.fetchone()
        cursor.close()
    except Exception as e:
        print(f"Erro ao actualizar dados no tb_well: {e}")
        return -1
    finally:
        return dados
    
def buscar_customer_by_name(nome): 
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT id FROM tb_legal_person WHERE  lp_name= %s """,(nome,))
        dados = cursor.fetchone()
        cursor.close()
    except Exception as e:
        print(f"Erro ao actualizar dados no tb_well: {e}")
        return -1
    finally:
        return dados
