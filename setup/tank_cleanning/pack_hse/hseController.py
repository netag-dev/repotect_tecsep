import tank_cleanning.pack_hse.hseModel

def carregar_cadastro(id_typehse, hse_quantity, hse_comments, id_report_tc):
    tank_cleanning.pack_hse.hseModel.cadastrar(id_typehse, hse_quantity, hse_comments, id_report_tc)

def carregar_edicao(data1, data2, data3, data4, data5):
    tank_cleanning.pack_hse.hseModel.editar(data1, data2, data3, data4, data5)

def carregar_eliminar(data):
    tank_cleanning.pack_hse.hseModel.eliminar(data)

def carregar_listagem():
    tank_cleanning.pack_hse.hseModel.listar()

def carregar_listagem_tipo_hse():
    return tank_cleanning.pack_hse.hseModel.listar_tipo_hse()

def carregar_id_por_tipo_hse(tipo):
    return tank_cleanning.pack_hse.hseModel.buscar_id_hse_por_tipo(tipo)


def listar_hse(id_report):
    return tank_cleanning.pack_hse.hseModel.buscar_chse(id_report)

