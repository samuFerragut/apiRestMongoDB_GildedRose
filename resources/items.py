from flask_restful import Resource, Api, reqparse
from repository.models import Item
from services.service import Service


class Items(Resource):

    def get(self, itemName):
        return Service.get_Item(item_name), 200

    def post(self):
        args = self.parseRequest()
        Service.postItem(args)
        # Estado de respuesta 201 created
        return '', 201

    def delete(self):
        args = self.parseRequest()
        Service.deleteItem(args)
        # Estado de respuesta 204 no content
        return '', 204
