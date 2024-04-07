import compliance.pack_sample_location.sample_locationModel as model

def cadastrar(description):
    return model.cadastrar(description)

def editar(description, id):
    return model.editar(description, id)

def delete_data(id):
    return model.delete_data(id)

def listar():
    return model.listar()

def listar_table():
    return model.listar_table()



