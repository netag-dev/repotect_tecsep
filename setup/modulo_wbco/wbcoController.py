import modulo_wbco.wbcoModel

def carregar_supervisor():
    if(modulo_wbco.wbcoModel.buscar_supervisor() is None):
        return -1
    else:
        return modulo_wbco.wbcoModel.buscar_supervisor()
    

def salvar_report_cabecalho(rpt_job_ref_number,rpt_field_locations,rpt_job_type,rpt_shift,rpt_report_date,id_physical_person,rpt_rig_name):
    modulo_wbco.wbcoModel.salvar_report_cabecalho(rpt_job_ref_number,rpt_field_locations,rpt_job_type,rpt_shift,rpt_report_date,id_physical_person,rpt_rig_name)


def buscar_id_report_header_ultimo():
    return modulo_wbco.wbcoModel.buscar_id_report_header_ultimo()
    

def carregar_tecnico():
    if(modulo_wbco.wbcoModel.buscar_tecnico() is None):
        return -1
    else:
        return modulo_wbco.wbcoModel.buscar_tecnico()
    
def carregar_id_supervisor(nome_supervisor):
    if(modulo_wbco.wbcoModel.buscar_id_supervisor_by_name(nome_supervisor) is None):
        return -1
    else:
        return modulo_wbco.wbcoModel.buscar_id_supervisor_by_name(nome_supervisor)
    

def carregar_id_supervisor_by_email(email_supervisor):
    return modulo_wbco.wbcoModel.buscar_id_supervisor_by_email(email_supervisor)
    

def carregar_cliente():
    if(modulo_wbco.wbcoModel.buscar_cliente() is None):
        return -1
    else:
        return modulo_wbco.wbcoModel.buscar_cliente()
    

def carregar_poco(nome_poco):
    if(modulo_wbco.wbcoModel.buscar_poco(nome_poco) is None):
        return -1
    else:
        return modulo_wbco.wbcoModel.buscar_poco(nome_poco)
    
def carregar_buscar_id_poco(nome_poco):
    if(modulo_wbco.wbcoModel.buscar_id_poco(nome_poco) is None):
        return -1
    else:
        return modulo_wbco.wbcoModel.buscar_id_poco(nome_poco)
    
def carregar_buscar_id_cliente(nome_cliente):
    if(modulo_wbco.wbcoModel.buscar_id_cliente(nome_cliente) is None):
        return -1
    else:
        return modulo_wbco.wbcoModel.buscar_id_cliente(nome_cliente)
    
def carregar_buscar_id_empregador_por_nome(nome):
    return modulo_wbco.wbcoModel.carregar_buscar_id_empregador_por_nome(nome) 
         
    
    
def salvar_report_information(rpt_ongoing_rig,rpt_casing_size,rpt_length,rpt_od,rpt_id,rpt_size,rpt_weight_rangeng,
                              rpt_volume_capacity,rpt_hole_volume,rpt_wbco_tools_activity,rpt_shift_supervisor,rpt_total_day_supervisor,id_well,id_physical_person,id_legal_person,id_employee,id_report_header):
    
    modulo_wbco.wbcoModel.salvar_report_information(rpt_ongoing_rig,rpt_casing_size,rpt_length,rpt_od,rpt_id,rpt_size,rpt_weight_rangeng,
                              rpt_volume_capacity,rpt_hole_volume,rpt_wbco_tools_activity,rpt_shift_supervisor,rpt_total_day_supervisor,id_well,id_physical_person,id_legal_person,id_employee,id_report_header) 
      
    
def salvar_tecnico_em_servico(id_employee,wb_eng_shift,wb_eng_total_dayst,id_report_wbco):
    if(modulo_wbco.wbcoModel.salvar_wbco_tools_enginer(id_employee,wb_eng_shift,wb_eng_total_dayst,id_report_wbco) == 0):
        return 0
    else:
        return -1


def carregar_buscar_id_report():
    if(modulo_wbco.wbcoModel.buscar_id_ultimo_report() is None):
        return -1
    else:
        return modulo_wbco.wbcoModel.buscar_id_ultimo_report()
    
def salvar_wbco_primary(tl_description,tl_size,tl_thead_connetions,tl_od,tl_id,tl_drift_size,id_physical_person,id_report_tools):
    if(modulo_wbco.wbcoModel.salvar_wbco_primary(tl_description,tl_size,tl_thead_connetions,tl_od,tl_id,tl_drift_size,id_physical_person,id_report_tools) == 0):
        return 0
    else:
        return -1
    
def salvar_wbco_backup(tl_description,tl_size,tl_thead_connetions,tl_od,tl_id,tl_drift_size,id_physical_person,id_report_tools):
    if(modulo_wbco.wbcoModel.salvar_wbco_backup(tl_description,tl_size,tl_thead_connetions,tl_od,tl_id,tl_drift_size,id_physical_person,id_report_tools) == 0):
        return 0
    else:
        return -1
    

def carregar_info_report_cabecalho():
    if(modulo_wbco.wbcoModel.buscar_cabecalho_report_information() is None):
        return -1
    else:
        return modulo_wbco.wbcoModel.buscar_cabecalho_report_information()
    

def carregar_info_report_cabecalho_por_job_ref(job_ref):
    if(modulo_wbco.wbcoModel.buscar_cabecalho_report_information_with_report(job_ref) is None):
        return -1
    else:
        return modulo_wbco.wbcoModel.buscar_cabecalho_report_information_with_report(job_ref)
     

def carregar_well_information():
    if(modulo_wbco.wbcoModel.buscar_well_information() is None):
        return -1
    else:
        return modulo_wbco.wbcoModel.buscar_well_information()
    

def carregar_well_information_por_job_ref(job_ref):
    if(modulo_wbco.wbcoModel.buscar_well_information_with_report(job_ref) is None):
        return -1
    else:
        return modulo_wbco.wbcoModel.buscar_well_information_with_report(job_ref)
    

def carregar_wbco_primary(id_report):
    if(modulo_wbco.wbcoModel.buscar_wbco_primary_informatio(id_report) is None):
        return -1
    else:
        return modulo_wbco.wbcoModel.buscar_wbco_primary_informatio(id_report)
    
def carregar_wbco_primary_by_job_ref(job_ref):
    if(modulo_wbco.wbcoModel.buscar_wbco_primary_informatio_by_job_ref(job_ref) is None):
        return -1
    else:
        return modulo_wbco.wbcoModel.buscar_wbco_primary_informatio_by_job_ref(job_ref)
    
def carregar_wbco_back_up(id_report):
    if(modulo_wbco.wbcoModel.buscar_wbco_back_up_informatio(id_report) is None):
        return -1
    else:
        return modulo_wbco.wbcoModel.buscar_wbco_back_up_informatio(id_report)
    
def carregar_wbco_back_up_by_job_ref(job_ref):
    if(modulo_wbco.wbcoModel.buscar_wbco_back_up_informatio_by_job_ref(job_ref) is None):
        return -1
    else:
        return modulo_wbco.wbcoModel.buscar_wbco_back_up_informatio_by_job_ref(job_ref)
    

def carregar_empregado(id_report):
    if(modulo_wbco.wbcoModel.buscar_empregado(id_report) is None):
        return -1
    else:
        return modulo_wbco.wbcoModel.buscar_empregado(id_report)
    

def carregar_empregado_by_job_ref(job_ref):
    if(modulo_wbco.wbcoModel.buscar_empregado_by_job_ref(job_ref) is None):
        return -1
    else:
        return modulo_wbco.wbcoModel.buscar_empregado_by_job_ref(job_ref)
    

def listar_report():
    return modulo_wbco.wbcoModel.lista_report_wbco()

def lista_personel_position():
    return modulo_wbco.wbcoModel.lista_personel_position()

def buscar_id_personeel_postion(pp_description):
    return modulo_wbco.wbcoModel.buscar_id_personeel_postion(pp_description)


def buscar_total_days_supervisor(job_ref,id_supervisor):
    return modulo_wbco.wbcoModel.buscar_total_days_supervisor(job_ref,id_supervisor)

def verificar_job_ref(job_ref,id_supervisor):
    return modulo_wbco.wbcoModel.verificar_job_ref(job_ref,id_supervisor)