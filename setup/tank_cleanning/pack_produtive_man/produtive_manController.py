import tank_cleanning.pack_produtive_man.produtive_manModel

def carregar_cadastro(pm_work_order, pm_description, pm_original_hours, pm_hours_brocked_td, 
                       pm_qt_hours_brocked_td, pm_hours_brocked_date, pm_hours_remaining_td, pm_visual_perc_complete, id_report_tc):
    
    tank_cleanning.pack_produtive_man.produtive_manModel.cadastrar(pm_work_order, pm_description, pm_original_hours, pm_hours_brocked_td, 
                       pm_qt_hours_brocked_td, pm_hours_brocked_date, pm_hours_remaining_td, pm_visual_perc_complete, id_report_tc) 

def carregar_edicao(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10):
    tank_cleanning.pack_produtive_man.produtive_manModel.editar(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10)

def carregar_eliminar(data):
    tank_cleanning.pack_produtive_man.produtive_manModel.eliminar(data)

def carregar_listagem():
    tank_cleanning.pack_produtive_man.produtive_manModel.listar()

def verificar_registo_existente_com_report(id_report):
    return tank_cleanning.pack_produtive_man.produtive_manModel.verificar_registo_existente_com_report(id_report)

