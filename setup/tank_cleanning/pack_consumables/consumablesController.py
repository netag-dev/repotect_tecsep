import tank_cleanning.pack_consumables.consumablesModel

def cadastrar(cs_name, cs_quantity):
    return tank_cleanning.pack_consumables.consumablesModel.cadastrar(cs_name, cs_quantity)

def editar(param1, param2, param3):
    return tank_cleanning.pack_consumables.consumablesModel.editar(param1, param2, param3)

def eliminar(param,param2):
    return tank_cleanning.pack_consumables.consumablesModel.eliminar(param,param2)

def listar():
    return tank_cleanning.pack_consumables.consumablesModel.listar()

def listar_table():
    return tank_cleanning.pack_consumables.consumablesModel.listar_table()

def buscar_id_nome_stoq(nome,stoq):
    return tank_cleanning.pack_consumables.consumablesModel.buscar_id_nome_stoq(nome,stoq)

def buscar_consumiveis(report):
    return tank_cleanning.pack_consumables.consumablesModel.buscar_consumiveis(report)

def buscar_quantidade_stoke(nome):
    return tank_cleanning.pack_consumables.consumablesModel.buscar_quantidade_stoke(nome)



