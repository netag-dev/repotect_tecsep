import conection.connect as connecao

############ Listando Physical_person ###############
def listar_physical():
    try:
        connection = connecao.cria_connecao()
        cursor = connection.cursor()
        cursor.execute(""" SELECT * FROM tb_physical_person WHERE pp_name = %s AND pp_email = %s AND pp_type = %s AND pp_senha = %s """)
        dados = cursor.fetchall()
        dados_novo = [item[1] for item in dados]
        cursor.close()
    except Exception as e:
        print(f"Erro na Base de dados: {e}")
    finally:
        if connection:
            cursor.close()
            return dados_novo
        
        