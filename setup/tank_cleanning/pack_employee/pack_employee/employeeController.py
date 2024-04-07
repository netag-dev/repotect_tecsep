import filtration.pack_employee.employeeModel


def cadastrar(emp_name, emp_email):
    filtration.pack_employee.employeeModel.cadastrar(emp_name, emp_email)

def editar(param1, param2, param3):
    filtration.pack_employee.employeeModel.editar(param1, param2, param3)

def eliminar(param):
    filtration.pack_employee.employeeModel.eliminar(param)

def listar():  
    return filtration.pack_employee.employeeModel.listar()

def buscar_id_by_name_email(name, email):
    return filtration.pack_employee.employeeModel.buscar_id_by_name_email(name, email)