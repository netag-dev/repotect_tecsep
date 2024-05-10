import modulo_personnel.personnelModel

def carregar_cadastro(data2, data3, data4, data5, data6, data7):
    return modulo_personnel.personnelModel.cadastrar( data2, data3, data4, data5, data6, data7) 

def carregar_listagem():
    return modulo_personnel.personnelModel.listar()


def carregar_pessoa_por_bi(numero_bi):
    return modulo_personnel.personnelModel.buscar_pessoa_por_bi(numero_bi)


def carregar_pessoa_editar(param1, param2, param3, param4, param5, param6, param7):
    return modulo_personnel.personnelModel.editar(param1, param2, param3, param4, param5, param6, param7)


def eleminar_pessoa(param):
    return modulo_personnel.personnelModel.eliminar(param)

def buscar_tipo_usuario(email):
    return modulo_personnel.personnelModel.buscar_tipo_usuario(email)

def buscar_card_id(email):
    return modulo_personnel.personnelModel.buscar_card_id(email)



