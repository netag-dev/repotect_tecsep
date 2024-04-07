import filtration.pack_enginer_day.enginer_dayModel


def cadastrar(eng_shift, eng_total_dayst, id_employee, id_report_ft):
    filtration.pack_enginer_day.enginer_dayModel.cadastrar(eng_shift, eng_total_dayst, id_employee, id_report_ft)


def listar(job_ref):
    return filtration.pack_enginer_day.enginer_dayModel.listar(job_ref)