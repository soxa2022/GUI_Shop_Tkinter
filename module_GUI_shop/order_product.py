from json import load, dump
import PIL
from PIL import Image, ImageTk
from helper import clean_screen
from canvas import *

path = "." + sep + 'db' + sep


def render_products():
    clean_screen()
    display_products()


def display_products():
    with open(path + 'products.json', 'r') as file:
        products_info = load(file)

    x = 150
    y = 50
    for name, data in products_info.items():
        product_img = ImageTk.PhotoImage(PIL.Image.open(data['image']))
        images.append(product_img)
        frame.create_text(x, y, text=f'{name} - {data["type"]}', font='bold', fill='black')
        frame.create_image(x, y + 135, image=product_img)

        if data['quantity'] > 0:
            text = f"Price: {data['price']}lv. - in stock {data['quantity']} pcs."
            color = 'green'
            btn = Button(root, text='Buy', bg='grey', fg='black',
                         width=6, command=lambda b=name: buy(products_info, b))
            frame.create_window(x, y + 300, window=btn)
        else:
            text = "Out of stock"
            color = 'red'

        frame.create_text(x, y + 270, text=text, font='bold', fill=color)

        x += 230
        if x > 700:
            x = 150
            y += 370


def buy(info, item):
    info[item]["quantity"] -= 1
    with open(path + 'products.json', 'w') as file:
        dump(info, file)
    render_products()


images = []
