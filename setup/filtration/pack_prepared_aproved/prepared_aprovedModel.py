import filtration.pack_prepared_aproved.prepared_aprovedModel

def add_preapred_to_report(id_physical_peraon,id_report_filtration):
    filtration.pack_prepared_aproved.prepared_aprovedModel.add_preapred_to_report(id_physical_peraon,id_report_filtration)


def add_approved_to_report(id_physical_peraon,id_report_filtration):
    filtration.pack_prepared_aproved.prepared_aprovedModel.add_approved_to_report(id_physical_peraon,id_report_filtration)


def buscar_id_supersover_nome_por(nome):
    return filtration.pack_prepared_aproved.prepared_aprovedModel.buscar_id_supersover_nome_por(nome) 


def buscar_id_empregado_nome_por(nome):
    return filtration.pack_prepared_aproved.prepared_aprovedModel.buscar_id_empregado_nome_por(nome) 

def buscar_nome_prepared(job_ref):
    return filtration.pack_prepared_aproved.prepared_aprovedModel.buscar_nome_prepared(job_ref)


def buscar_nome_aproved(job_ref):
    return filtration.pack_prepared_aproved.prepared_aprovedModel.buscar_nome_aproved(job_ref)