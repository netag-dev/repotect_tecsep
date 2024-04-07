import filtration.pack_fluid_information.fluid_informationModel

def carregar_cadastro(ft_fluid_type_filtered, ft_daily_total, ft_density_sg,ft_density_type, ft_viscosity, ft_hole_volume,ft_hole_volume_type, ft_vol_filtered_date, id_report_ft):
    filtration.pack_fluid_information.fluid_informationModel.cadastrar(ft_fluid_type_filtered, ft_daily_total, ft_density_sg,ft_density_type, ft_viscosity, ft_hole_volume,ft_hole_volume_type, ft_vol_filtered_date, id_report_ft) 

def carregar_edicao(data1, data2, data3, data4, data5, data6, data7, data8):
    filtration.pack_fluid_information.fluid_informationModel.editar(data1, data2, data3, data4, data5, data6, data7, data8)

def carregar_eliminar(data):
    filtration.pack_fluid_information.fluid_informationModel.eliminar(data)

def carregar_listagem():
    filtration.pack_fluid_information.fluid_informationModel.listar()

def listar_fluid_por_job_ref(job_ref):
    return filtration.pack_fluid_information.fluid_informationModel.listar_fluid_por_job_ref(job_ref)

