import conection.connect as connecao

############ Listando Physical_person ###############
def listar_physical(pp_email):
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT pp_name, pp_email, pp_type, pp_senha FROM tb_physical_person WHERE pp_email = %s """, (pp_email))
        dados = cursor.fetchall()
        dados_novo = [item[1] for item in dados]
        cursor.close()
    except Exception as e:
        print(f"Erro na Base de dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados_novo
        
        