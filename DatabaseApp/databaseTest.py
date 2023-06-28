import psycopg2

# Connect to DB


def create_database():
    conn = psycopg2.connect(dbname="postgres", user="postgres",
                            host="localhost", port="5432", password="gulla99")
    print('Connection Success')
    cur = conn.cursor()
    cur.execute('''
            CREATE TABLE student(ID SERIAL, NAME text, age int);
            ''')
    print('Table Created')
    conn.commit()
    conn.close()


def insert_data(name, age):
    conn = psycopg2.connect(dbname="postgres", user="postgres",
                            host="localhost", port="5432", password="gulla99")

    print('Connection Success')
    cur = conn.cursor()
    cur.execute(f'''
            INSERT INTO student(NAME,age) VALUES ('{name}',{age});
            ''')
    print('Data inserted')
    conn.commit()
    conn.close()


insert_data('Asfak', 23)
