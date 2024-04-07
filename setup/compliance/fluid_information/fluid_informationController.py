import compliance.pack_fluid_information.fluid_informationModel as model

def cadastrar(mud_type, rig_type, density_type, hole_type, rig_total_volume, density, viscosity_vp, viscosity_yp, hole_volume):
    return model.cadastrar(mud_type, rig_type, density_type, hole_type, rig_total_volume, density, viscosity_vp, viscosity_yp, hole_volume)

def editar(mud_type, rig_type, density_type, hole_type, rig_total_volume, density, viscosity_vp, viscosity_yp, hole_volume, id):
    return model.editar(mud_type, rig_type, density_type, hole_type, rig_total_volume, density, viscosity_vp, viscosity_yp, hole_volume, id)

def delete_data(density, viscosity_vp, viscosity_yp, hole_volume):
    return model.delete_data(density, viscosity_vp, viscosity_yp, hole_volume)

def listar():
    return model.listar()

def listar_table():
    return model.listar_table()

def buscar_id_by_hole_volume(hole_volume):
    return model.buscar_id_by_hole_volume(hole_volume)

