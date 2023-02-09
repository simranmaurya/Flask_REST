from flask_jwt import jwt_required
from flask_restful import Resource
from models.product import ProductModel


class ProductList(Resource):

    @jwt_required()

    def get(self):
        prod1 = ProductModel(101, 'Notebook')
        prod1.save_to_db()
        prod2 = ProductModel(102, 'Textbook')
        prod2.save_to_db()
        prod3 = ProductModel(103, 'Pen')
        prod3.save_to_db()
        prod4 = ProductModel(104, 'Pencil')
        prod4.save_to_db()
        prod5 = ProductModel(105, 'Geometry set')
        prod5.save_to_db()
        prod6 = ProductModel(106, 'Charts')
        prod6.save_to_db()
        prod7 = ProductModel(107, 'Bottle')
        prod7.save_to_db()
        prod8 = ProductModel(108, 'Color')
        prod8.save_to_db()
        prod9 = ProductModel(109, 'Sketch Pen')
        prod9.save_to_db()
        prod10 = ProductModel(110, 'Drawing book')
        prod10.save_to_db()

        return {"product_items": [x.json() for x in ProductModel.query.all()]}

