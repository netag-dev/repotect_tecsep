import compliance.pack_drilling_fluid_property.drilling_fluid_propertyModel as model

def cadastrar(type_fluid_proprieties, value , report_information_cp):
    return model.cadastrar(type_fluid_proprieties, value , report_information_cp)

def editar(type_fluid_proprieties, value, report_information_cp):
    return model.editar(type_fluid_proprieties, value, report_information_cp)

def eliminar(type_fluid_proprieties, value, report_information_cp):
    return model.eliminar(type_fluid_proprieties, value, report_information_cp)

def listar_drilling_fluid(): 
    return model.listar_drilling_fluid()
 