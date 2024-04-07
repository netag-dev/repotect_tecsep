import compliance.pack_report_information.report_informationModel as model

def cadastrar(custumer, well, report_date, aproved_by, job_ref_number, rig_name, field_location, job_type, project_description, hole_size, total_depth, feets_drilled, average_rop, time_at_depth, prepared_by, shift, ongoing_rig_activity, monitoring_comments):
    return model.cadastrar(custumer, well, report_date, aproved_by, job_ref_number, rig_name, field_location, job_type, project_description, hole_size, total_depth, feets_drilled, average_rop, time_at_depth, prepared_by, shift, ongoing_rig_activity, monitoring_comments)

def editar(custumer, well, report_date, aproved_by, job_ref_number, rig_name, field_location, job_type, project_description, hole_size, total_depth, feets_drilled, average_rop, time_at_depth, prepared_by, shift, ongoing_rig_activity, monitoring_comments, id):
    return model.editar(custumer, well, report_date, aproved_by, job_ref_number, rig_name, field_location, job_type, project_description, hole_size, total_depth, feets_drilled, average_rop, time_at_depth, prepared_by, shift, ongoing_rig_activity, monitoring_comments, id)

def delete_data(job_ref_number, rig_name, field_location, job_type):
    return model.delete_data(job_ref_number, rig_name, field_location, job_type)

def listar():
    return model.listar()

def listar_table():
    return model.listar_table()

def buscar_id_by_report_date(report_date):
    return model.buscar_id_by_report_date(report_date)

