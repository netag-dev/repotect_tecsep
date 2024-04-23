import psycopg2

def cria_connecao():
    return psycopg2.connect( 
                database = "repotec", 
                host = "102.219.126.14", 
                user = "postgres", 
                password = "Angola2023#", 
                port = "5432" 
            )

