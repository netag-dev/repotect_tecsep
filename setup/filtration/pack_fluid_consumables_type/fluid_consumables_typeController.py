import filtration.pack_fluid_consumables_type.fluid_consumables_typeModel


def cadastrar(description):
    return filtration.pack_fluid_consumables_type.fluid_consumables_typeModel.cadastrar(description)

def editar(param1, param2):
    return filtration.pack_fluid_consumables_type.fluid_consumables_typeModel.editar(param1, param2)

def eliminar(param):
    return filtration.pack_fluid_consumables_type.fluid_consumables_typeModel.eliminar(param)

def listar():  
    return filtration.pack_fluid_consumables_type.fluid_consumables_typeModel.listar()

def buscar_id_by_name_email(description):
    return filtration.pack_fluid_consumables_type.fluid_consumables_typeModel.buscar_id_by_name_email(description)

def buscar_by_id(id):
    return filtration.pack_fluid_consumables_type.fluid_consumables_typeModel.buscar_by_id(id)
