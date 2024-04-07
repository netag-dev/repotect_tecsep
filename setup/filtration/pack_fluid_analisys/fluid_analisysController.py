import filtration.pack_fluid_analisys.fluid_analisysModel


def carregar_cadastro(ft_wellbone_displacement, ft_time, ft_pumping_time, ft_volume_pumped,ft_volume_pumped_type, ft_ntu, ft_tss_perc_solids, id_report_ft):
    filtration.pack_fluid_analisys.fluid_analisysModel.cadastrar(ft_wellbone_displacement, ft_time, ft_pumping_time, ft_volume_pumped,ft_volume_pumped_type, ft_ntu, ft_tss_perc_solids, id_report_ft) 

def carregar_edicao(data1, data2, data3, data4, data5, data6, data7, data8):
    filtration.pack_fluid_analisys.fluid_analisysModel.editar(data1, data2, data3, data4, data5, data6, data7, data8)

def carregar_eliminar(data):
    filtration.pack_fluid_analisys.fluid_analisysModel.eliminar(data)

def carregar_listagem():
    filtration.pack_fluid_analisys.fluid_analisysModel.listar()


def listar_por_job_ref(job_ref):
    return filtration.pack_fluid_analisys.fluid_analisysModel.listar_por_job_ref(job_ref)

