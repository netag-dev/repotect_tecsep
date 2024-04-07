import tank_cleanning.pack_inventory_imob.inventory_imobModel

def carregar_cadastro(cp_name, cp_unit_completed, cp_element_completed, cp_perc_completed_date, cp_comment, id_physical_person, id_report_tc):
    tank_cleanning.pack_competency_profies.competency_profiesModel.cadastrar(cp_name, cp_unit_completed, cp_element_completed, cp_perc_completed_date, cp_comment, id_physical_person, id_report_tc) 

def carregar_edicao(data1, data2, data3, data4, data5, data6, data7):
    tank_cleanning.pack_competency_profies.competency_profiesModel.editar(data1, data2, data3, data4, data5, data6, data7)

def carregar_eliminar(data):
    tank_cleanning.pack_competency_profies.competency_profiesModel.eliminar(data)

def carregar_listagem():
    tank_cleanning.pack_competency_profies.competency_profiesModel.listar()


def listar_competence_profile(id_report):
    return tank_cleanning.pack_inventory_imob.inventory_imobModel.buscar_competence_profile(id_report)


def get_id_consumibele(nome_consumable):
    return tank_cleanning.pack_inventory_imob.inventory_imobModel.get_id_consumibele(nome_consumable)

def get_id_ppe(nome_ppe):
    return tank_cleanning.pack_inventory_imob.inventory_imobModel.get_id_ppe(nome_ppe)


def get_id_asset(nome_asset):
    return tank_cleanning.pack_inventory_imob.inventory_imobModel.get_id_asset(nome_asset)


def get_stoq_consumivel(id):
    return tank_cleanning.pack_inventory_imob.inventory_imobModel.get_stoq_consumivel(id)

def get_stoq_ppe(id):
    return tank_cleanning.pack_inventory_imob.inventory_imobModel.get_stoq_ppe(id)

def get_stoq_asset(id):
    return tank_cleanning.pack_inventory_imob.inventory_imobModel.get_stoq_asset(id)

######################## Cadastro ###################################################

def cadastrar_consumivel(id_consumivel,id_report,quantidade):
    return tank_cleanning.pack_inventory_imob.inventory_imobModel.cadastrar_consumivel(id_consumivel,id_report,quantidade)

def cadastrar_ppe(id,id_report,quantidade):
    return tank_cleanning.pack_inventory_imob.inventory_imobModel.cadastrar_ppe(id,id_report,quantidade) 

def cadastrar_asset(id,id_report,quantidade):
    return tank_cleanning.pack_inventory_imob.inventory_imobModel.cadastrar_asset(id,id_report,quantidade)

####################################### Actualizar ########################################################################


def update_stoque_consumiveis(id_consumivel,quantidade):
    return tank_cleanning.pack_inventory_imob.inventory_imobModel.update_stoque_consumiveis(id_consumivel,quantidade)


def update_stoque_ppe(id,quantidade):
    return tank_cleanning.pack_inventory_imob.inventory_imobModel.update_stoque_ppe(id,quantidade)


def update_stoque_asset(id,quantidade):
    return tank_cleanning.pack_inventory_imob.inventory_imobModel.update_stoque_asset(id,quantidade)

