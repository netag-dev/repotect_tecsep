import psycopg2
import compliance.pack_physical_person.physicalModel as model

def listar_physical(pp_email):
    return model.listar_physical(pp_email)