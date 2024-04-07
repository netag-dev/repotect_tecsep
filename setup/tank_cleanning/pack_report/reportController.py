import tank_cleanning.pack_report.reportModel

def carregar_cadastro(txt_job_ref,txt_field_location,txt_job_type,rpt_shift,dateEdit,id_supervisor,
                           txt_rig_name):
    
    tank_cleanning.pack_report.reportModel.cadastrar_report_information(txt_job_ref,txt_field_location,txt_job_type,rpt_shift,dateEdit,id_supervisor,
                           txt_rig_name) 

def carregar_edicao(rpt_job_ref_number,rpt_rig_size,rpt_field_locations,rpt_job_type,
                           rpt_report,rpt_number_tank,rpt_volume_waste,rpt_type_waste,id_physical_person):
    
    tank_cleanning.pack_report.reportModel.editar_report_information(rpt_job_ref_number,rpt_rig_size,rpt_field_locations,rpt_job_type,
                           rpt_report,rpt_number_tank,rpt_volume_waste,rpt_type_waste,id_physical_person)

def carregar_eliminar(data):
    tank_cleanning.pack_report.reportModel.eliminar_report_information(data)

def carregar_listagem():
    tank_cleanning.pack_report.reportModel.listar_report_information()

def carregar_id_dayshift():
    return tank_cleanning.pack_report.reportModel.buscar_ultimo_registo_dayshift_activity()

def carregar_id_report():
    return tank_cleanning.pack_report.reportModel.buscar_ultimo_registo_report()



def carregar_info_report_cabecalho_por_job_ref(job_ref):
    if(tank_cleanning.pack_report.reportModel.buscar_cabecalho_report_information_with_report(job_ref) is None):
        return -1
    else:
        return tank_cleanning.pack_report.reportModel.buscar_cabecalho_report_information_with_report(job_ref)
    

def listar_report():
    return tank_cleanning.pack_report.reportModel.lista_report_tank_cleaning()


def salvar_info_report(id_physical_person,id_legal_person,id_shit_activity_tc,id_employee,id_report_header):
    tank_cleanning.pack_report.reportModel.salvar_info_report(id_physical_person,id_legal_person,id_shit_activity_tc,id_employee,id_report_header)

