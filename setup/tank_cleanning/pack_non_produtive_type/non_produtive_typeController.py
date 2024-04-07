import tank_cleanning.pack_non_produtive_type.non_produtive_typeModel

def carregar_cadastro(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10):
    tank_cleanning.pack_non_produtive_type.non_produtive_typeModel.cadastrar(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10) 

def carregar_edicao(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10):
    tank_cleanning.pack_non_produtive_type.non_produtive_typeModel.editar(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10)

def carregar_eliminar(data):
    tank_cleanning.pack_non_produtive_type.non_produtive_typeModel.eliminar(data)

def carregar_listagem():
    return tank_cleanning.pack_non_produtive_type.non_produtive_typeModel.listar()


def carregar_id_por_tipo_non_produtive(tipo):
    return tank_cleanning.pack_non_produtive_type.non_produtive_typeModel.buscar_id_non_produtive_por_tipo(tipo)

