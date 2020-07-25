from datetime import datetime
import jwt
from functools import wraps
from flask import request, jsonify, Blueprint, current_app
from projects import db, bcrypt
from projects.models import (
    PriceMenu, WeekMenus,
    # TypeMenu, DetailTypesMenu
)
from projects.schemas import (
    pricemenu_schema,
    weekmenus_schema,
    # typemenu_schema,
    # detailtypemenu_schema
)
import marshmallow


blueprint = Blueprint('users', __name__)


def check_token():
    authorization = request.headers.get('Authorization')

    if authorization is None:
        return False

    split_auth = authorization.split(' ')

    if len(split_auth) != 2:
        return False

    if split_auth[0] != 'Bearer':
        return False

    token = split_auth[1]

    try:
        jwt.decode(token, current_app.config['SECRET'])
        return True
    except:
        return False


def authentificater(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        check_response = check_token()
        if check_response is False:
            return 'Unauthorized', 401

        return f(check_response, *args, **kwargs)

    return wrapper


## ==============PRICE================

@blueprint.route('/add_price_menu_week', methods=['POST'])
@authentificater
def add_price_menu_week(payload):
    price_menu_week = pricemenu_schema.load(request.json)

    db.session.add(price_menu_week)
    db.session.commit()

    return pricemenu_schema.dump(price_menu_week), 201


@blueprint.route('/update_price_menu_week/<id>', methods=['PUT'])
@authentificater
def update_price_menu_week(payload, id):
    price_menu_week = PriceMenu.query.get_or_404(id)
    price_menu_week = pricemenu_schema.load(
        data=request.json,
        instance=price_menu_week,
        partial=False
    )

    db.session.add(price_menu_week)
    db.session.commit()

    return pricemenu_schema.dump(price_menu_week), 200


@blueprint.route('/get_price_menu_week/<id>', methods=['GET', 'POST'])
@authentificater
def get_price_menu_week(payload, id):
    price_menu_week = PriceMenu.query.get_or_404(id)

    return pricemenu_schema.dump(price_menu_week), 200


## ==============MENUS================

@blueprint.route('/add_week_menu', methods=['POST'])
@authentificater
def add_week_menus(payload):
    week_menus = weekmenus_schema.load(request.json)

    db.session.add(week_menus)
    db.session.commit()

    return weekmenus_schema.dump(week_menus), 201


@blueprint.route('/get_week_menu', methods=['GET', 'POST'])
@authentificater
def get_week_menus(payload):
    week_menus = WeekMenus.query.all()

    return jsonify(weekmenus_schema.dump(week_menus, many=True)), 200


@blueprint.route('/get_week_menu/<id>', methods=['GET', 'POST'])
@authentificater
def get_one_week_menu(payload, id):
    week_menu = WeekMenus.query.get_or_404(id)

    return weekmenus_schema.dump(week_menu), 200


@blueprint.route('/update_week_menu/<id>', methods=['PUT'])
@authentificater
def update_week_menu(payload, id):
    week_menu = WeekMenus.query.get_or_404(id)
    week_menu = weekmenus_schema.load(
        data=request.json,
        instance=week_menu,
        partial=False
    )

    db.session.add(week_menu)
    db.session.commit()

    return weekmenus_schema.dump(week_menu), 200


@blueprint.route('/delete_week_menu/<id>', methods=['DELETE'])
@authentificater
def delete_week_menu(payload, id):
    week_menu = WeekMenus.query.get_or_404(id)

    db.session.delete(week_menu)
    db.session.commit()

    return '', 204

