import modulo_wbco.enginierwbcoModel

def listar():
    return modulo_wbco.enginierwbcoModel.listar()

def buscar_id_by_shift(wb_eng_shift):
    modulo_wbco.enginierwbcoModel.buscar_id_by_shift(wb_eng_shift)

def editar(name, email, id_personnel_position,id):
    return modulo_wbco.enginierwbcoModel.editar(name, email, id_personnel_position,id)

def delete_data(name,email):
    return  modulo_wbco.enginierwbcoModel.delete_data(name,email)

def save_data(name, email, id_personnel_position):
    return modulo_wbco.enginierwbcoModel.save_data(name, email, id_personnel_position)

def buscar_id_by_name_email(name,email):
    return modulo_wbco.enginierwbcoModel.buscar_id_by_name_email(name,email)
    
    