import psycopg2

def cria_connecao():
    return psycopg2.connect( 
                database = "repotec", 
                host = "localhost", 
                user = "postgres", 
                password = "postgres", 
                port = "5433" 
            )

