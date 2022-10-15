import re
from canvas import *
from helper import clean_screen
from json import loads, dump
from os.path import sep
from order_product import render_products

path = "." + sep + 'db' + sep


def get_users_info():
    users = []
    with open(path + "users.json", 'r') as users_file:
        for line in users_file:
            users.append(loads(line.strip()))
    return users


def render_entry():
    register_button = Button(root, text="Register", bg='blue', fg='black', width=20, height=4, command=register)
    login_button = Button(root, text="Login", bg='green', fg='black', width=20, height=4, command=login)
    frame.create_window(400, 320, window=register_button)
    frame.create_window(400, 400, window=login_button)


def register():
    clean_screen()
    frame.create_text(200, 100, text='e-mail:', font='bold')
    frame.create_text(200, 150, text='company_name:', font='bold')
    frame.create_text(200, 200, text='password:', font='bold')
    frame.create_text(200, 250, text='confirm password:', font='bold')
    frame.create_window(350, 100, window=email_line)
    frame.create_window(350, 150, window=company_name_line)
    frame.create_window(350, 200, window=password_line)
    frame.create_window(350, 250, window=confirm_pass_line)
    btn = Button(root, text='Submit', bg='grey', fg='black', width=8, height=1, command=registration_data)
    frame.create_window(280, 300, window=btn)


def registration_data():
    data_dict = {
        'e-mail': email_line.get(),
        "company_name": company_name_line.get(),
        'password': password_line.get(),
        'confirm password': confirm_pass_line.get(),
        'products': []
    }
    if registration_validation(data_dict):
        data_dict.pop("confirm password")
        with open(path + 'users.json', 'a') as users_file:
            dump(data_dict, users_file)
            users_file.write('\n')
            login()


def registration_validation(data):
    frame.delete('error')
    pattern = r'^[\w\-\.]+@([\w-]+\.)+[\w-]{2,4}$'
    if not re.match(pattern, data['e-mail']):
        frame.create_text(280, 330, text="Not valid e-mail", font='bold', fill='red', tag='error')
        return False
    for val in list(data.values())[1:-1]:
        if val.strip() == '':
            frame.create_text(280, 330, text="You have empty field", font='bold', fill='red', tag='error')
            return False
    if not data['password'] == data['confirm password']:
        frame.create_text(280, 330, text="Passwords are not matching", font='bold', fill='red', tag='error')
        return False
    users_info = get_users_info()
    for i in range(len(users_info)):
        if users_info[i]['e-mail'] == data['e-mail']:
            frame.create_text(280, 330, text="The e-mail is already exist!", font='bold', fill='red', tag='error')
            return False
    frame.delete('error')
    return True


def login():
    clean_screen()
    password_line.delete(0, "end")
    email_line.delete(0, "end")
    frame.create_text(200, 100, text='e-mail:', font='bold')
    frame.create_text(200, 150, text='password:', font='bold')
    frame.create_window(350, 100, window=email_line, )
    frame.create_window(350, 150, window=password_line)
    btn_login = Button(root, text='Login', bg='grey', fg='black', width=8, height=1, command=login_correct)
    frame.create_window(280, 200, window=btn_login)


def login_correct():
    if login_validation():
        render_products()
    else:
        frame.create_text(280, 250, text="Invalid e-mail or password", font='bold', fill='red', tag='error')


def login_validation():
    password, mail = password_line.get(), email_line.get()
    users_info = get_users_info()
    for i in range(len(users_info)):
        if users_info[i]['e-mail'] == mail and users_info[i]['password'] == password:
            return True
    return False


email_line = Entry(root)
company_name_line = Entry(root)
password_line = Entry(root, show="*")
confirm_pass_line = Entry(root, show='*')
