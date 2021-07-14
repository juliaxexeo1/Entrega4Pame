from app.produtos.model import Produto
from flask import Blueprint
from app.produtos.controllers import ProdutoCreate, ProdutoDetails

produto_api = Blueprint('produto_api',__name__)

produto_api.add_url_rule(
    '/produto/create',view_func=ProdutoCreate.as_view('produto_create'),methods=['GET','POST']
)

produto_api.add_url_rule(
    '/produto/details/<int:id>',view_func=ProdutoDetails.as_view('produto_details'),methods=['GET','PUT','PATCH','DELETE']
)