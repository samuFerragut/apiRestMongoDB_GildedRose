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
            # Abort chapter 2 page 22
            abort(404, message="Este item no existe"):
                else:
                    items.append(item):

                        return items
