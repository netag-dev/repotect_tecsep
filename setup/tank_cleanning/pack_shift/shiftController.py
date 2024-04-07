import tank_cleanning.pack_shift.shiftModel

def carregar_cadastro(sh_trade,sh_planed_demmed,sh_crew_change,id_period,id_employee,id_report_tc):
    tank_cleanning.pack_shift.shiftModel.cadastrar_dayshift_personeel(sh_trade,sh_planed_demmed,sh_crew_change,id_period,id_employee,id_report_tc) 

def carregar_edicao(data1, data2, data3, data4, data5, data6, data7):
    tank_cleanning.pack_shift.shiftModel.editar(data1, data2, data3, data4, data5, data6, data7)

def carregar_eliminar(data):
    tank_cleanning.pack_shift.shiftModel.eliminar(data)

def carregar_listagem():
    tank_cleanning.pack_shift.shiftModel.listar()

def carregar_listagem_tipo_shift():
    return tank_cleanning.pack_shift.shiftModel.listar_tipo_shift()


def carregar_id_por_tipo_shift(tipo):
    return tank_cleanning.pack_shift.shiftModel.buscar_id_shift_por_tipo(tipo)


def listar_pessoa_turno_diurno(id):
    return tank_cleanning.pack_shift.shiftModel.buscar_shift_person_day(id)


def listar_pessoa_turno_noturno(id_report):
    return tank_cleanning.pack_shift.shiftModel.buscar_shift_person_nigth(id_report) 



