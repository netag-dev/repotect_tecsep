import tank_cleanning.pack_assets.assetsModel

def cadastrar(as_name, as_quantity):
    return tank_cleanning.pack_assets.assetsModel.cadastrar(as_name, as_quantity)

def editar(param1, param2, param4):
    return tank_cleanning.pack_assets.assetsModel.editar(param1, param2, param4)

def eliminar(param1, param2):
    return tank_cleanning.pack_assets.assetsModel.eliminar(param1, param2)

def listar():
    return tank_cleanning.pack_assets.assetsModel.listar()

def listar_table():
    return tank_cleanning.pack_assets.assetsModel.listar_table()


def buscar_id_nome_stoq(nome,stoq):
    return tank_cleanning.pack_assets.assetsModel.buscar_id_nome_stoq(nome,stoq)


def buscar_asset(report):
    return tank_cleanning.pack_assets.assetsModel.buscar_asset(report)



