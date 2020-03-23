from flask_restful import Resource, Api, reqparse
from repository.models import Item
from services.service import Service


class Items(Resource):

    def get(self, itemName):
        return Service.get_Item(item_name), 200

    def post(self):
        args = self.parseRequest()
        Service.postItem(args)
        return '', 201
