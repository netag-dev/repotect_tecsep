import tank_cleanning.pack_period.periodModel

def carregar_cadastro(data1, data2):
    tank_cleanning.pack_period.periodModel.cadastrar(data1, data2)

def carregar_edicao(data1, data2):
    tank_cleanning.pack_period.periodModel.editar(data1, data2)

def carregar_eliminar(data):
    tank_cleanning.pack_period.periodModel.eliminar(data)

def carregar_listagem():
    tank_cleanning.pack_period.periodModel.listar() 
    
