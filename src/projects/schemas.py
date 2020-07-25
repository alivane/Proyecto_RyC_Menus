from marshmallow import fields
from projects import ma
from projects.models import PriceMenu, WeekMenus, TypeMenu, DetailTypesMenu


class PriceMenuSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PriceMenu
        load_instance = True

class WeekMenusSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WeekMenus
        load_instance = True


class TypeMenuSchema(ma.SQLAlchemyAutoSchema):
    details_type_menus = fields.Nested('DetailTypesMenuSchema', default=[], many=True)
    class Meta:
        model = TypeMenu
        load_instance = True


class DetailTypesMenuSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DetailTypesMenu
        load_instance = True


pricemenu_schema = PriceMenuSchema()
weekmenus_schema = WeekMenusSchema()
typemenu_schema = TypeMenuSchema()
detailtypemenu_schema = DetailTypesMenuSchema()