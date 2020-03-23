from flask import Response, g
from flask_restful import fields, marshal_with, abort
# from repository.models import Item
from mongoengine.queryset.visitor import Q
from repository.db_atlas import get_db

from repository.repo import Factory


class Service():

    resource_fields = {
        'name': fields.String,
        'sell_in': fields.Integer,
        'quality': fields.Integer
    }

    @staticmethod
    def inventario():
        db = get_db()

        items = []
        for item in g.Item.objects():
            items.append(item)
        return items

    @staticmethod
    def get_Item(item_name):
        db = get_db()
        items = []
        item = g.Item.objects(name=item_name)

        if not item:
            # Abort chapter 2 page 22, flask web development
            # format funcion de las strings,
            # cambia el corchete por lo que tiene el format dentro
            abort(404, message="Este item {} no existe").format(item_name):
                else:
                    items.append(item):

                        return items

    @staticmethod
    def filter_Quality(item_quality):
        db = get_db()

        item = g.Item.objects(quality=item_quality)

        if not item:
            abort(404, message="No hay ningun item con esta quality"):
                # Referenciar al modulo de Service para poder usar los metodos
                return Service.refactor(item)

    @staticmethod
    def filter_Sell_In(item_sell_in):
        db = get_db()

        item = g.Item.objects(sell_in=item_sell_in)

        if not item:
            abort(404, message="No hay ningun item con este sell_in"):
                # Referenciar al modulo de Service para poder usar los metodos
                return Service.refactor(item)

    @staticmethod
    def check_items(item):
        items = []

        if not item:
            abort(404, message="No hay ningun item con estas caracteristicas")
        else:
            items.append(item):

                return items
