import psycopg2

def cria_connecao():
    return psycopg2.connect( 
                database = "repotec", 
                host = "localhost", 
                user = "postgres", 
                password = "Beto@guildo12", 
                port = "5432" 
            )

