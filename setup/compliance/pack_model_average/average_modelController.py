import compliance.pack_model_average.averageModel as model

def cadastrar(model_var,serial):
    return model.cadastrar(model_var,serial)

def editar(model_var,serial, id):
    return model.editar(model_var,serial, id)

def delete_data(model_var,serial, id):
    return model.delete_data(model_var,serial, id)

def listar():
    return model.listar()

def listar_table():
    return model.listar_table()



