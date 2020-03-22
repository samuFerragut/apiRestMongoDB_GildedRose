
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
    def Inventario():
            db = get_db()

            items = []
            for item in g.Item.objects():
                items.append(item)
            return items
