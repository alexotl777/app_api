'''
It's flask server
'''
from flask import Flask
import flask
import vk
import miem
import json

PORT = 3333

app = Flask(__name__, 
            static_url_path='',
            static_folder='./')

memes_img = {
    "mem1": "https://userpic.fishki.net/2021/02/12/1779359/34e66ded0ec312d472a4070c5640c28d.jpg",
    "mem2": "https://bipbap.ru/wp-content/uploads/2017/01/developer11.jpeg",
    "mem3": "https://otkritkis.com/wp-content/uploads/2022/02/1464729791156456568.jpg"
}

cities = {
    "city1": "New York",
    "city2": "Berlin",
    "city3": "Moscow",
}

data_vk = []

@app.before_first_request
def load_info():
    global data_vk
    vk.get_info_vk()
    with open('vk.json') as f:
        data_vk = json.load(f)

@app.route("/mem/<mem_title>")
def get_mem(mem_title):
    if mem_title in memes_img:
        return memes_img[mem_title]
    return f"Mem {mem_title} not found!"

@app.route("/city/<city_name>")
def get_city(city_name):
    if city_name in cities:
        return cities[city_name]
    return f"City {city_name} not found!"

@app.route("/")
def open_main_html():
    return flask.render_template("index.html", 
                                name = data_vk['response'][0]['first_name'],
                                surname = data_vk['response'][0]['last_name'],
                                id = data_vk['response'][0]['id'])

if __name__ == '__main__':
    app.run(port = PORT)