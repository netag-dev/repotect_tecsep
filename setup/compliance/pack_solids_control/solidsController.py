import compliance.pack_solids_control.solidsModel as model

def cadastrar(shaker, scalper, back, middle, front, hours_run, location_of_sample,
dryer_screen_size , bowl_speed, flow, weight_in_ppg, daily_perc_ooc, 
report_information): 
    
    return model.cadastrar(shaker, scalper, back, middle, front, hours_run, location_of_sample,
dryer_screen_size , bowl_speed, flow, weight_in_ppg, daily_perc_ooc, 
report_information)


def buscar_solids_by_job_ref(job_ref):
    return model.buscar_solids_by_job_ref(job_ref)

def buscar_num_registo_solid_by_job_ref(job_ref):
    return model.buscar_num_registo_solid_by_job_ref(job_ref)