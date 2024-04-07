import tank_cleanning.pack_daily_progress.dayshift_activityModel

def carregar_cadastro(data1, data2, data3):
    tank_cleanning.pack_daily_progress.daily_progressModel.cadastrar(data1, data2, data3) 

def carregar_edicao_dayshift(pd_description, id_physical_person, daily_progress,planned_activity,norm_reading,equipament_material,id_dayshift):
   tank_cleanning.pack_daily_progress.dayshift_activityModel.editar_dayshift_activity(pd_description, id_physical_person, daily_progress,planned_activity,norm_reading,equipament_material,id_dayshift)

def carregar_eliminar(data):
    tank_cleanning.pack_daily_progress.dayshift_activityModel.eliminar_dayshift_activity(data)

def carregar_listagem():
    tank_cleanning.pack_daily_progress.dayshift_activityModel.listar_dayshift_activity()


def carregar_cadastro_dayshift_activity(pd_description,id_physical_person,daily_progress,planned_activity,norm_reading,equipament_material):
    tank_cleanning.pack_daily_progress.dayshift_activityModel.salvar_dayshift_activity(pd_description,id_physical_person,daily_progress,planned_activity,norm_reading,equipament_material)


def listar_actividade(id_report):
    return tank_cleanning.pack_daily_progress.dayshift_activityModel.buscar_shift_activity(id_report)
      
