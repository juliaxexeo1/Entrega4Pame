#routes

from app.cliente.model import Cliente
from flask import Blueprint
from app.cliente.controllers import ClienteCreate, ClientesDetails, ClienteLogin

cliente_api = Blueprint('cliente_api',__name__)

cliente_api.add_url_rule(
    '/cliente/create',view_func=ClienteCreate.as_view('cliente_create'),methods=['GET','POST']
)

cliente_api.add_url_rule(
    '/cliente/details/<int:id>',view_func=ClientesDetails.as_view('clientes_details'),methods=['GET','PUT','PATCH','DELETE']
)
cliente_api.add_url_rule(
    '/cliente/login',view_func=ClienteLogin.as_view('cliente_login'),methods=['POST']
)