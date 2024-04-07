import filtration.pack_fluid_consumables.fluid_consumablesModel


def carregar_cadastro(id_consumivel, id_type, ft_openning_stock, ft_additional_stock, ft_total_stock, ft_daily_used, ft_total_used, ft_closing_bal, id_report_ft):
    filtration.pack_fluid_consumables.fluid_consumablesModel.cadastrar(id_consumivel, id_type, ft_openning_stock, ft_additional_stock, ft_total_stock, ft_daily_used, ft_total_used, ft_closing_bal, id_report_ft) 

def carregar_edicao(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10):
    filtration.pack_fluid_consumables.fluid_consumablesModel.editar(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10)

def carregar_eliminar(data):
    filtration.pack_fluid_consumables.fluid_consumablesModel.eliminar(data)

def carregar_listagem(job_ref):
    return filtration.pack_fluid_consumables.fluid_consumablesModel.listar(job_ref)

def listar_type():
    return filtration.pack_fluid_consumables.fluid_consumablesModel.listar_type()

def listar_consumiveis():
    return filtration.pack_fluid_consumables.fluid_consumablesModel.listar_consumiveis()


def buscar_quantidade_stoke(nome):
    return filtration.pack_fluid_consumables.fluid_consumablesModel.buscar_quantidade_stoke(nome)

def buscar_id(nome):
    return filtration.pack_fluid_consumables.fluid_consumablesModel.buscar_id(nome)

def buscar_id_tipo(nome):
    return filtration.pack_fluid_consumables.fluid_consumablesModel.buscar_id_tipo(nome)

