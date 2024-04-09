import compliance.pack_sample_cp.sample_cpModel as model

def cadastrar(synthetic_sg,rop_at_time,
             weight_empty,weight_filled_body_sample,weight_filled_body_sample_water,
             weight_graduated_cyinder,weight_graduated_cyinder_condensate,
             volume_of_water,weight_retort_cell,weight_of_sample,weight_of_water,volume_of_sample,
             weight_oil,weight_condensate_gms,density_sample_sg,vol_oil,weight_water,
             weight_dry_solids_calculated,perc_water_by_volume,perc_oil_by_volume,weight_dry_solids_actual,
             perc_solids_by_volume,perc_oil_by_weight,perc_water_by_weight,perc_solids_by_weight,ooc,soc,mud_weight,acuracy_check):
    
    return model.cadastrar(synthetic_sg,rop_at_time,
             weight_empty,weight_filled_body_sample,weight_filled_body_sample_water,
             weight_graduated_cyinder,weight_graduated_cyinder_condensate,
             volume_of_water,weight_retort_cell,weight_of_sample,weight_of_water,volume_of_sample,
             weight_oil,weight_condensate_gms,density_sample_sg,vol_oil,weight_water,
             weight_dry_solids_calculated,perc_water_by_volume,perc_oil_by_volume,weight_dry_solids_actual,
             perc_solids_by_volume,perc_oil_by_weight,perc_water_by_weight,perc_solids_by_weight,ooc,soc,mud_weight,acuracy_check)


def buscar_solids_by_job_ref(job_ref):
    return model.buscar_solids_by_job_ref(job_ref)