import modulo_wbco.sizeModel

def listar_size():
    return modulo_wbco.sizeModel.listar_size()

def buscar_id_by_size_description(size,description):
    return modulo_wbco.sizeModel.buscar_id_by_size_description(size,description)

def save_editad_data(size,description,id):
    return modulo_wbco.sizeModel.save_editad_data(size,description,id)

def delete_data(size,description):
    return modulo_wbco.sizeModel.delete_data(size,description)

def save_data(size,description):
    return modulo_wbco.sizeModel.save_data(size,description)

def listar_size_para_combo():
    return modulo_wbco.sizeModel.listar_size_para_combo()


def buscar_id_by_size(size):
    return modulo_wbco.sizeModel.buscar_id_by_size(size)