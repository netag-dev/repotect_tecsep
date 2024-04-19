import filtration.pack_fluid_consumables_type.fluid_consumables_typeModel


def cadastrar(type,description):
    return filtration.pack_fluid_consumables_type.fluid_consumables_typeModel.cadastrar(type,description)

def editar(type,desc,id):
    return filtration.pack_fluid_consumables_type.fluid_consumables_typeModel.editar(type,desc,id)

def eliminar(param):
    return filtration.pack_fluid_consumables_type.fluid_consumables_typeModel.eliminar(param)

def listar():  
    return filtration.pack_fluid_consumables_type.fluid_consumables_typeModel.listar()

def buscar_id_by_name_email(description):
    return filtration.pack_fluid_consumables_type.fluid_consumables_typeModel.buscar_id_by_name_email(description)

def buscar_by_id(id):
    return filtration.pack_fluid_consumables_type.fluid_consumables_typeModel.buscar_by_id(id)
