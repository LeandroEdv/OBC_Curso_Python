import psycopg2

conn = psycopg2.connect(
    database = "fliperama",
    user = "postgres",
    password = "alcest20",
    host = "localhost",
    port = "5432"      
)
