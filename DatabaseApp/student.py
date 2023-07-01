from tkinter import *
import tkinter as tk
import psycopg2
root = Tk()


def store_data(name, age):

    conn = psycopg2.connect(dbname="postgres", user="postgres",
                            host="localhost", port="5432", password="gulla99")
    cur = conn.cursor()
    query = '''INSERT INTO student(NAME,age) VALUES (%s,%s);'''
    cur.execute(query, (name, age))
    print('Data inserted')
    conn.commit()
    conn.close()
    display_all()


def search_data(name):
    conn = psycopg2.connect(dbname="postgres", user="postgres",
                            host="localhost", port="5432", password="gulla99")
    cur = conn.cursor()
    query = f'''SELECT * FROM student where name='{name}';'''
    print(query)
    cur.execute(query)
    data = cur.fetchone()
    display_search_result(data)
    conn.commit()
    conn.close()


def display_search_result(row):
    listbox = Listbox(frame, width=20, height=1)
    listbox.grid(row=9, column=1)
    listbox.insert(END, row)


def display_all():
    conn = psycopg2.connect(dbname="postgres", user="postgres",
                            host="localhost", port="5432", password="gulla99")

    print('Connection Success')
    cur = conn.cursor()
    query = f'''SELECT * FROM student;'''
    cur.execute(query)
    data = cur.fetchall()
    listbox = Listbox(frame, width=20, height=5)
    listbox.grid(row=10, column=1)
    for d in data:
        listbox.insert(END, d)
    conn.commit()
    conn.close()


# Create Canvas
canvas = Canvas(root, height=480, width=700)

# Add canvas to root window
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

root.title("Student Database")

label = Label(frame, text="Add Data")
label.grid(row=0, column=1)

label = Label(frame, text="Name")
label.grid(row=1, column=0)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1)


label = Label(frame, text="Age")
label.grid(row=2, column=0)

entry_age = Entry(frame)
entry_age.grid(row=2, column=1)


button = Button(frame, text="Add Entery into Database",
                command=lambda: store_data(entry_name.get(), entry_age.get()))


button.grid(row=3, column=1)

label = Label(frame, text="Search Data")
label.grid(row=5, column=0)

label = Label(frame, text="Search by student name")
label.grid(row=6, column=0)

search_name = Entry(frame)
search_name.grid(row=6, column=1)

button = Button(frame, text="Search",
                command=lambda: search_data(search_name.get()))
button.grid(row=6, column=2)

display_all()
root.mainloop()
