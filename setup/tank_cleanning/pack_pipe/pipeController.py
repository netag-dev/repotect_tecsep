import tank_cleanning.pack_pipe.pipeModel

def cadastrar(pi_name, pi_quantity):
    return tank_cleanning.pack_pipe.pipeModel.cadastrar(pi_name, pi_quantity)

def editar(nome, stoq,id):
    return tank_cleanning.pack_pipe.pipeModel.editar(nome, stoq,id)

def eliminar(param1, param2):
    return tank_cleanning.pack_pipe.pipeModel.eliminar(param1, param2)

def listar():
    return tank_cleanning.pack_pipe.pipeModel.listar()


def listar_table():
    return tank_cleanning.pack_pipe.pipeModel.listar_table()


def buscar_id_nome_stoq(nome,stoq):
    return tank_cleanning.pack_pipe.pipeModel.buscar_id_nome_stoq(nome,stoq)

def buscar_ppe(report):
    return tank_cleanning.pack_pipe.pipeModel.buscar_ppe(report)


 