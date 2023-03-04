import streamlit as st
import sqlite3

conn = sqlite3.connect('TaxiDriver.db')
cursor = conn.cursor()

# create the CARS table
cursor.execute('''CREATE TABLE IF NOT EXISTS CARS (
    MODEL VARCHAR(255),
    YEARS VARCHAR(255),
    REGISTER VARCHAR(255)
)''')

# create the DRIVERS table
cursor.execute('''CREATE TABLE IF NOT EXISTS DRIVERS (
    NAME_OF_DRIVERS VARCHAR(255),
    SURNAME_OF_DRIVERS VARCHAR(255),
    PHONE_NUMBER VARCHAR(255),
    ADDRESS VARCHAR(255)
)''')

def search_cars(value, cars='BMW'):
    cursor.execute(f"SELECT * FROM {cars} WHERE MODEL=?", (value.strip(),))

def update_table(YEARS, MODEL, REGISTER, CARS):
    search_cars(MODEL, REGISTER, CARS)
    prod_name = cursor.fetchall()
    if prod_name:
        var_list = list(prod_name[0])
        var_list[1] = int(var_list[1]) + int(YEARS)
        cursor.execute(f"UPDATE {REGISTER} SET YEARS={str(var_list[1])}")
    else:
        cursor.execute(f"INSERT INTO {REGISTER} VALUES (?, ?, ?)", (MODEL, YEARS, REGISTER))

col1, col2, col3, col4 = st.columns(4)

with col1:
    input_NAME_OF_DRIVERS = st.text_input('Name of Drivers')

with col2:
    input_SURNAME_OF_DRIVERS = st.text_input('Surname')

with col3:
    input_PHONE_NUMBER = st.text_input('Phone Number')

with col4:
    input_ADDRESS = st.text_input('Address')

if st.button("Upload Driver's Data"):
    cursor.execute("INSERT INTO DRIVERS (NAME_OF_DRIVERS, SURNAME_OF_DRIVERS, PHONE_NUMBER, ADDRESS) VALUES (?, ?, ?, ?)", (input_NAME_OF_DRIVERS.strip(), input_SURNAME_OF_DRIVERS.strip(), input_PHONE_NUMBER.strip(), input_ADDRESS.strip()))
    conn.commit()

input_model = st.selectbox('Select MODEL', ('BMW', 'FORD', 'VOLVO'))
col1, col2 = st.columns(2)

with col1:
    search_value = st.text_input('Register:')

with col2:
    search_cars = st.selectbox('Select from years', ('2004', '2015', '2000'))

if st.button("Upload Car's Data"):
    
    conn.commit()

conn.close()
