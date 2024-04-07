import tank_cleanning.pack_tank_information.tank_informationModel

def cadastrar(ti_number_tank, ti_volume_waste, ti_type_waste, ti_tank_type, id_report_tc):
    tank_cleanning.pack_tank_information.tank_informationModel.cadastrar(ti_number_tank, ti_volume_waste, ti_type_waste, ti_tank_type, id_report_tc)

def editar(param1, param2, param3, param4, param5, param6):
    tank_cleanning.pack_tank_information.tank_informationModel.editar(param1, param2, param3, param4, param5, param6)

def eliminar(param):
    tank_cleanning.pack_tank_information.tank_informationModel.eliminar(param)

def listar():
    tank_cleanning.pack_tank_information.tank_informationModel.listar()

def buscar_tank_information(id_report):
    return tank_cleanning.pack_tank_information.tank_informationModel.buscar_tank_information(id_report)



