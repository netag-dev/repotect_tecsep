import modulo_wbco.threadModel

def listar_thread_con():
    return modulo_wbco.threadModel.listar_thread_con()

def buscar_id_by_description(description,thread):
    return modulo_wbco.threadModel.buscar_id_by_description(description,thread)

def editar_thread(thread,description,id):
    return modulo_wbco.threadModel.editar_thread(thread,description,id)

def delete_data(thread,description):
    return modulo_wbco.threadModel.delete_data(thread,description)

def save_data(thread,description):
    return modulo_wbco.threadModel.save_data(thread,description)

def listar_thread_para_combo():
    return modulo_wbco.threadModel.listar_thread_para_combo()


def buscar_id_by_tch(tch):
    return modulo_wbco.threadModel.buscar_id_by_tch(tch)
    
    