import filtration.pack_fluid_consumables_type.fluid_consumables_typeModel


def cadastrar(description):
    filtration.pack_fluid_consumables_type.fluid_consumables_typeModel.cadastrar(description)

def editar(param1, param2):
    filtration.pack_fluid_consumables_type.fluid_consumables_typeModel.editar(param1, param2)

def eliminar(param):
    filtration.pack_fluid_consumables_type.fluid_consumables_typeModel.eliminar(param)

def listar():  
    return filtration.pack_fluid_consumables_type.fluid_consumables_typeModel.listar()

def buscar_id_by_name_email(description):
    return filtration.pack_fluid_consumables_type.fluid_consumables_typeModel.buscar_id_by_name_email(description)
