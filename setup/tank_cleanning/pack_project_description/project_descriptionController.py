import tank_cleanning.pack_project_description.project_descriptionModel

def carregar_cadastro(data1, data2, data3):
    tank_cleanning.pack_project_description.project_descriptionModel.cadastrar(data1, data2, data3) 

def carregar_edicao(data1, data2, data3):
    tank_cleanning.pack_project_description.project_descriptionModel.editar(data1, data2, data3)

def carregar_eliminar(data):
    tank_cleanning.pack_project_description.project_descriptionModel.eliminar(data)

def carregar_listagem():
    tank_cleanning.pack_project_description.project_descriptionModel.listar()

