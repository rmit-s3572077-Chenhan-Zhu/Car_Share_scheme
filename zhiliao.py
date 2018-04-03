# encoding: utf-8
from flask import Flask, render_template, request, redirect, url_for, session, flash, Blueprint
import config
import requests
from modules import User, Car_rental, Cars, CarsDataset
from exits import db
import os
from decoratars import login_required
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from flask_admin import Admin, BaseView, expose
from flask_paginate import Pagination, get_page_parameter
from math import *


ip = '128.250.51.47'
url = 'http://freegeoip.net/json/' + ip
r = requests.get(url)
js = r.json()
#
# SAMPLE_RESPONSE = """{
#     "ip":"108.46.131.77",
#     "country_code":"US",
#     "country_name":"United States",
#     "region_code":"NY",
#     "region_name":"New York",
#     "city":"Brooklyn",
#     "zip_code":"11249",
#     "time_zone":"America/New_York",
#     "latitude":40.645,
#     "longitude":-73.945,
#     "metro_code":501
# }"""


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
app.secret_key = os.urandom(24)
GoogleMaps(app)

flask_admin = Admin()
flask_admin.init_app(app)
EARTH_REDIUS = 6378.137


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username == username, User.password == password).first()
        if user:
            session['user_id'] = user.id
            session['username'] = user.username
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return u'wrong username or password,please try again '


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if password1 != password2:
            return u'different passwords,please try again!'
        else:
            user = User(username=username, password=password1)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))


@app.route('/car_rental/', methods=['GET', 'POST'])
@login_required
def car_rental():
    if request.method == 'GET':
        return render_template('car_rental.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        car_rental = Car_rental(title=title, content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        car_rental.author = user
        db.session.add(car_rental)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/logout/')
@login_required
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.context_processor
def my_context_processor():
    user = session.get('username')
    if user:
        return {'user': user}
    return {}


def url_for_other_page(page):
    # args = request.view_args.copy()
    args = dict(request.view_args.items() + request.args.to_dict().items())  # 如果采用上面那句则换页时querystring会丢失
    args['page'] = page
    return url_for(request.endpoint, **args)


app.jinja_env.globals['url_for_other_page'] = url_for_other_page


@app.route('/users/', methods=['GET', 'POST'])
# @login_required
def users():
    return render_template('users.html')


@app.route('/ContactUs/', methods=['GET', 'POST'])
# @login_required
def ContactUs():
    return render_template('ContactUs.html')


@app.route('/tables/', methods=['GET', 'POST'])
# @login_required
def tables():
    context = {
        'Cars': Cars.query.all()
    }

    return render_template('tables.html', **context)


@app.route('/booking/', methods=['GET', 'POST'])
# @login_required
def booking():
    page_data = CarsDataset.query
    tid = request.args.get("tid", 0)
    if int(tid) != 0:
        if int(tid) == 1:
            page_data = page_data.filter_by(brand='audi')

        if int(tid) == 2:
            page_data = page_data.filter_by(brand='volkswagen')

        if int(tid) == 3:
            page_data = page_data.filter_by(brand='bmw')

        if int(tid) == 4:
            page_data = page_data.filter_by(brand='peugeot')

        if int(tid) == 5:
            page_data = page_data.filter_by(brand='mercedes benz')

        if int(tid) == 6:
            page_data = page_data.filter_by(brand='ford')

    time = request.args.get("time", 0)
    if int(time) == 1:
        page_data = page_data.filter_by(gearbox='manuell')
    if int(time) == 2:
        page_data = page_data.filter_by(gearbox='automatik')

    pm = request.args.get("pm", 0)
    p = dict(
        tid=tid,
        time=time,
        pm=pm
    )

    context = {
        'CarsDataset': CarsDataset.query.all()
    }

    sndmap = Map(
        identifier="sndmap",
        lat=-37.8253632,
        lng=144.9504107,
        style="height:500px;width:500px;margin:0;",

        markers=[
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': -37.8222763,
                'lng': 144.9556639,
                'infobox': "<b>Hello World</b>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': -37.8079088,
                'lng': 144.9654394,
                'infobox': "<b>Hello World from other place</b>"
            }
        ]
    )
    # Lat_A = -37.8253632
    # Lng_A = 144.9504107
    Lat_B = page_data.with_entities(CarsDataset.lat).all()
    Lng_B = page_data.with_entities(CarsDataset.lng).all()

    # sb = Distance1(Lat_A, Lng_A, Lat_B, Lng_B)

    if request.method == 'POST':
        location = request.form.get('location')
        Bdatetime = request.form.get('Bdatetime')
        Btime = request.form.get('Btime')
        Bday = request.form.get('Bday')

        Rdatetime = request.form.get('Rdatetime')
        Rtime = request.form.get('Rtime')
        Rday = request.form.get('Rday')

        cattype = request.form.get('type')
        gearbox = request.form.get('gear')

        car = Cars(location=location, Rdatetime=Rdatetime, Bdatetime=Bdatetime, cattype=cattype, gearbox=gearbox,
                   Rday=Rday, Rtime=Rtime, Btime=Btime, Bday=Bday)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        car.author = user
        db.session.add(car)
        db.session.commit()

    return render_template('booking.html', sndmap=sndmap, page_data=page_data,  Lng_B=Lng_B,Lat_B=Lat_B, p=p, **context)

def Distance1(Lat_A,Lng_A,Lat_B,Lng_B): #第一种计算方法
    ra=6378.140 #赤道半径
    rb=6356.755 #极半径 （km）
    flatten=(ra-rb)/ra  #地球偏率
    rad_lat_A=radians(Lat_A)
    rad_lng_A=radians(Lng_A)
    rad_lat_B=radians(Lat_B)
    rad_lng_B=radians(Lng_B)
    pA=atan(rb/ra*tan(rad_lat_A))
    pB=atan(rb/ra*tan(rad_lat_B))
    xx=acos(sin(pA)*sin(pB)+cos(pA)*cos(pB)*cos(rad_lng_A-rad_lng_B))
    c1=(sin(xx)-xx)*(sin(pA)+sin(pB))**2/cos(xx/2)**2
    c2=(sin(xx)+xx)*(sin(pA)-sin(pB))**2/sin(xx/2)**2
    dr=flatten/8*(c1-c2)
    distance=ra*(xx+dr)
    return distance

if __name__ == '__main__':
    app.run()
