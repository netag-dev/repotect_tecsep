import filtration.pack_report.reportModel


def buscar_ultimo_registo_report():
    return filtration.pack_report.reportModel.buscar_ultimo_registo_report()

def carregar_cadastro(txt_job_ref,txt_field_location,txt_job_type,rpt_shift,dateEdit,id_supervisor,
                           txt_rig_name):
    
    filtration.pack_report.reportModel.cadastrar_report_information(txt_job_ref,txt_field_location,txt_job_type,rpt_shift,dateEdit,id_supervisor,
                           txt_rig_name)
    

def carregar_info_report_cabecalho_por_job_ref(job_ref):
    if(filtration.pack_report.reportModel.buscar_cabecalho_report_information_with_report(job_ref) is None):
        return -1
    else:
        return filtration.pack_report.reportModel.buscar_cabecalho_report_information_with_report(job_ref)
    


def listar_report():
    return filtration.pack_report.reportModel.lista_report_filtration()


def salvar_info_report(ft_ongoing_rig_activity,ft_filtration_activity,id_legal_person,id_report_header):
    filtration.pack_report.reportModel.salvar_info_report(ft_ongoing_rig_activity,ft_filtration_activity,id_legal_person,id_report_header)



def carregar_edicao(data1, data2, data3, data4, data5, data6, data7, data8, data9):
    filtration.pack_report.reportModel.editar(data1, data2, data3, data4, data5, data6, data7, data8, data9)

def carregar_eliminar(data):
    filtration.pack_report.reportModel.eliminar(data)

def carregar_listagem():
    filtration.pack_report.reportModel.listar()


def buscar_ongoing_activity(job_ref):
    return filtration.pack_report.reportModel.buscar_ongoing_activity(job_ref)

