import filtration.pack_consumiveis.consumiveisModel


def cadastrar(nome_consumivel,initial_stock):
    return filtration.pack_consumiveis.consumiveisModel.cadastrar(nome_consumivel,initial_stock)

def editar(param1, param2,param3):
    return filtration.pack_consumiveis.consumiveisModel.editar(param1, param2,param3)

def eliminar(param):
    filtration.pack_consumiveis.consumiveisModel.eliminar(param)

def listar():     
    return filtration.pack_consumiveis.consumiveisModel.listar()

def buscar_id(nome_consumivel, initial_stock):
    return filtration.pack_consumiveis.consumiveisModel.buscar_id(nome_consumivel, initial_stock)
