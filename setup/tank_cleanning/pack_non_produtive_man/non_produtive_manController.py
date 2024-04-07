import tank_cleanning.pack_non_produtive_man.non_produtive_manModel

def carregar_cadastro(id_non_produtive_type, npm_hours, npm_comments, id_report_tc):
    tank_cleanning.pack_non_produtive_man.non_produtive_manModel.cadastrar(id_non_produtive_type, npm_hours, npm_comments, id_report_tc) 

def carregar_edicao(data1, data2, data3, data4, data5):
    tank_cleanning.pack_non_produtive_man.non_produtive_manModel.editar(data1, data2, data3, data4, data5)

def carregar_eliminar(data):
    tank_cleanning.pack_non_produtive_man.non_produtive_manModel.eliminar(data)

def carregar_listagem():
    tank_cleanning.pack_non_produtive_man.non_produtive_manModel.listar()


def listar_produtive_man_hour(id_report):
    return tank_cleanning.pack_non_produtive_man.non_produtive_manModel.buscar_produtive_man_hour(id_report)


def listar_non_produtive_man(id_report):
    return tank_cleanning.pack_non_produtive_man.non_produtive_manModel.buscar_non_produtive_man(id_report)

