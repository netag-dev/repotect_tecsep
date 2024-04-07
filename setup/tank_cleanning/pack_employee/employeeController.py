import tank_cleanning.pack_employee.employeeModel


def cadastrar(emp_name, emp_email):
    return tank_cleanning.pack_employee.employeeModel.cadastrar(emp_name, emp_email)

def editar(nome, email, id):
    return tank_cleanning.pack_employee.employeeModel.editar(nome, email, id)

def delete_data(name,email):
    return  tank_cleanning.pack_employee.employeeModel.delete_data(name,email)

def listar():  
    return tank_cleanning.pack_employee.employeeModel.listar()


def listar_table():
    return tank_cleanning.pack_employee.employeeModel.listar_table()

def buscar_id_by_name_email(name, email):
    return tank_cleanning.pack_employee.employeeModel.buscar_id_by_name_email(name, email)

def carregar_buscar_id_empregador_por_nome(nome):
    return tank_cleanning.pack_employee.employeeModel.carregar_buscar_id_empregador_por_nome(nome)

