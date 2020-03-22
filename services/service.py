
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
    @marshal_with(resource_fields)
    def inventario():
        db = get_db()
        items = []

        for i in g.Item.objects():
            items.append(i)
            return items

    @staticmethod
    def postItem(args):
        db = get_db()

        item = g.Item(name=args['name']
                      & sell_in=args['sell_in']
                      & quality=args['quality'])
        item.save()

    @staticmethod
    def deleteItem(args):
        db = get_db()

        item = g.Item(Q(name=args['name'])
                      & Q(sell_in=args['sell_in'])
                      & Q(quality=args['quality']))
        if item:
            item.delete()
            else:
                abort(404, message="Este item no existe")
