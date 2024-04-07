import filtration.pack_filtration_sumary.fluid_sumaryModel

def carregar_cadastro(ft_start_time,ft_stop_time, ft_total_minutes_per_cicles, ft_volume_per_cicles,ft_volume_per_cicles_type, ft_d_e_per_cicle_20kg, ft_cartridge_filtrers, id_report_ft, id_num_cicle):
    filtration.pack_filtration_sumary.fluid_sumaryModel.cadastrar(ft_start_time,ft_stop_time, ft_total_minutes_per_cicles, ft_volume_per_cicles,ft_volume_per_cicles_type, ft_d_e_per_cicle_20kg, ft_cartridge_filtrers, id_report_ft, id_num_cicle) 

def carregar_edicao(data1, data2, data3, data4, data5, data6, data7, data8, data9):
    filtration.pack_filtration_sumary.fluid_sumaryModel.editar(data1, data2, data3, data4, data5, data6, data7, data8, data9)

def carregar_eliminar(data):
    filtration.pack_filtration_sumary.fluid_sumaryModel.eliminar(data)

def carregar_listagem():
    filtration.pack_filtration_sumary.fluid_sumaryModel.listar()


def listar_ciclos():
    return filtration.pack_filtration_sumary.fluid_sumaryModel.listar_ciclos()


def buscar_report_primeiro_ciclo(job_ref):
    return filtration.pack_filtration_sumary.fluid_sumaryModel.buscar_report_primeiro_ciclo(job_ref)

def buscar_report_segundo_ciclo(job_ref):
    return filtration.pack_filtration_sumary.fluid_sumaryModel.buscar_report_segundo_ciclo(job_ref)

def buscar_report_terceiro_ciclo(job_ref):
    return filtration.pack_filtration_sumary.fluid_sumaryModel.buscar_report_terceiro_ciclo(job_ref)

def buscar_report_quarto_ciclo(job_ref):
    return filtration.pack_filtration_sumary.fluid_sumaryModel.buscar_report_quarto_ciclo(job_ref)

def buscar_report_quinto_ciclo(job_ref):
    return filtration.pack_filtration_sumary.fluid_sumaryModel.buscar_report_quinto_ciclo(job_ref)

def buscar_report_sexto_ciclo(job_ref):
    return filtration.pack_filtration_sumary.fluid_sumaryModel.buscar_report_sexto_ciclo(job_ref)

def buscar_report_setimo_ciclo(job_ref):
    return filtration.pack_filtration_sumary.fluid_sumaryModel.buscar_report_setimo_ciclo(job_ref)

def buscar_report_oitavo_ciclo(job_ref):
    return filtration.pack_filtration_sumary.fluid_sumaryModel.buscar_report_oitavo_ciclo(job_ref)

