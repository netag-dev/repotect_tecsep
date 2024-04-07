import tank_cleanning.pack_type_hse.type_hseModel

def carregar_cadastro(data1, data2):
    tank_cleanning.pack_type_hse.type_hseModel.cadastrar(data1, data2)

def carregar_edicao(data1, data2):
    tank_cleanning.pack_type_hse.type_hseModel.editar(data1, data2)

def carregar_eliminar(data):
    tank_cleanning.pack_type_hse.type_hseModel.eliminar(data)

def carregar_listagem():
    tank_cleanning.pack_type_hse.type_hseModel.listar() 
    
