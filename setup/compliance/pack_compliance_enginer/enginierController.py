import compliance.pack_compliance_enginer.enginierModel

def listar():
    return compliance.pack_compliance_enginer.enginierModel.listar()

def buscar_id_by_shift(wb_eng_shift):
    compliance.pack_compliance_enginer.buscar_id_by_shift(wb_eng_shift)

def editar(name, email,id):
    return compliance.pack_compliance_enginer.enginierModel.editar(name, email,id)

def delete_data(name,email):
    return  compliance.pack_compliance_enginer.enginierModel.delete_data(name,email)

def cadastrar(name,email):
    return compliance.pack_compliance_enginer.enginierModel.cadastrar(name, email)

def buscar_id_by_name_email(name,email):
    return compliance.pack_compliance_enginer.enginierModel.buscar_id_by_name_email(name,email)

def cadastrar_enginer(eng_shift,id_employe,id_report):
    return compliance.pack_compliance_enginer.enginierModel.cadastrar_enginer(eng_shift,id_employe,id_report)
    
    