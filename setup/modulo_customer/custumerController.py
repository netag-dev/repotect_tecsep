import modulo_customer.custumerModel

def cadastrar(param1, param2, param3, param4, param5, param6):
    return modulo_customer.custumerModel.cadastrar(param1, param2, param3, param4, param5, param6)

def listar():
    return modulo_customer.custumerModel.listar()

def eliminar(param):
    return modulo_customer.custumerModel.eliminar(param)

#def carregar_listagem():
#    return modulo_customer.custumerModel.listar()

#def carregar_eliminar(param):
#    return modulo_customer.custumerModel.eliminar(param)

def carregar_listagem_poco():
    return modulo_customer.custumerModel.listar_poco()

def carregar_cadastro_de_poco(data1, data2, data3,data4):
    modulo_customer.custumerModel.cadastrar_poco(data1, data2, data3,data4)
    
def carregar_eliminar_poco(param):
    return modulo_customer.custumerModel.eliminar_poco(param)

def carregar_editar_poco(data1, data2):
    return modulo_customer.custumerModel.editar_poco(data1, data2)