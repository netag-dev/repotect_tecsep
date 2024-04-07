import psycopg2
import conection.connect as connecao

def cadastrar(param2, param3, param4, param5, param6, param7): 
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO tb_physical_person (pp_name,bi,pp_email,pp_senha,pp_phone,pp_type) values('"+param2+"','"+param3+"','"+param4+"','"+param5+"','"+param6+"','"+param7+"') ")
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao inserir dados no tb_physical_person: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexão fechada.")

def editar(param1, param2, param3, param4, param5, param6, param7): 
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("UPDATE tb_physical_person set bi = %s, pp_name = %s, pp_email = %s, pp_senha = %s, pp_phone = %s, pp_type = %s where id = %s ",(param2,param3,param4,param5,param6,param7,param1))
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao actualizar dados no tb_physical_person: {e}")
        return -1
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexão fechada.")
            return 0

def eliminar(param): 
    try: 
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tb_physical_person WHERE bi = %s ",(param,))
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao inserir dados no tb_physical_person: {e}")
        return -1
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexão fechada.")
            return 0
    
def listar(): 
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tb_physical_person")
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
            print("Conexão fechada.")

def buscar_pessoa_por_bi(id_card): 
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tb_physical_person WHERE bi = %s",(id_card,))
        dados = cursor.fetchone()
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao Listar dados no tb_physical_person: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            return dados
            print("Conexão fechada.")

