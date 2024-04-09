import compliance.pack_audit.auditModel as model

def cadastrar(findings, yes_no, time, contractor, report_information):
    return model.cadastrar(findings, yes_no, time, contractor, report_information)


def buscar_avarage_information_by_job_ref(job_ref):
    return model.buscar_avarage_information_by_job_ref(job_ref)