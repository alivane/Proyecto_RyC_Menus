from projects import db, bcrypt


class WeekMenus(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    salad = db.Column(db.String, nullable=True)
    dessert = db.Column(db.String, nullable=True)
    drink = db.Column(db.String, nullable=True)
    image_url = db.Column(db.String, nullable=True)

    def __init__(self, **kwargs):
        super(WeekMenus, self).__init__(**kwargs)


class PriceMenu(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.String, nullable=False)

    def __init__(self, **kwargs):
        super(PriceMenu, self).__init__(**kwargs)


class TypeMenu(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    details_type_menus = db.relationship('DetailTypesMenu', backref='type_menu')
    
    def __init__(self, **kwargs):
        super(TypeMenu, self).__init__(**kwargs)


class DetailTypesMenu(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=True)
    id_type_menu = db.Column(db.Integer, db.ForeignKey(TypeMenu.id), nullable=False)
    
    def __init__(self, **kwargs):
        super(DetailTypesMenu, self).__init__(**kwargs)

