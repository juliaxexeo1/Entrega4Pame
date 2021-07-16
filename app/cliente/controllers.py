#controlers

from flask.wrappers import Request
from app.cliente.model import Cliente
from flask import request,jsonify,render_template
from flask.views import MethodView
from app.extensions import db, mail
from flask_mail import Message
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.cliente.utils import testa_email, testa_cpf


import bcrypt

class ClienteCreate(MethodView):#'/cliente/create'
    

    def get(self):
        cliente = Cliente.query.all()
        return jsonify ([cliente.json()for cliente in cliente]),200

    def post(self):

        dados = request.json

        nome = dados.get('nome')
        cpf = dados.get('cpf')
        endereco = dados.get('endereco')
        email = dados.get('email')
        senha = dados.get('senha')

        #validação de dados
        if not isinstance(nome,str): 
            return{'error':'nome invalido'},400
        elif not testa_cpf(cpf):
            return{'error':'cpf invalido'},400
        elif not isinstance(endereco,str):
            return{'error':'endereco invalido'},400
        elif not testa_email (email):
            return{'error':'email invalido'},400
        
        cliente = Cliente.query.filter_by(email = email).first()

        if cliente:
            return {'error':'Email já cadastrado'},400

        cliente = Cliente.query.filter_by(cpf = cpf).first()

        if cliente:
            return {'error':'CPF já cadastrado'},400






        senha_hash = bcrypt.hashpw(senha.encode(),bcrypt.gensalt())

        cliente = Cliente(nome=nome,cpf=cpf,endereco=endereco,email=email,senha_hash=senha_hash)
        db.session.add(cliente)
        db.session.commit()

        msg = Message(
            sender= 'julia.xexeo@poli.ufrj.br',
            recipients=[email],
            subject= "Cadastro feito com sucesso",
            html=render_template('email.html',nome=nome)

        )
        mail.send(msg)

        return cliente.json(),200

class ClientesDetails(MethodView):#'/cliente/details/<int:id>'

    decorators = [jwt_required()]
   
    def get (self,id):

        if (get_jwt_identity() != id):
            return{'error':'Usuário não permitido '},400
        
        cliente = Cliente.query.get_or_404(id)
        return cliente.json(),200
    
 
    def put (self,id):
        if (get_jwt_identity() != id):
            return{'error':'Usuário não permitido '},400

        cliente = Cliente.query.get_or_404(id)
        dados = request.json

        nome = dados.get('nome')
        cpf = dados.get('cpf')
        endereco = dados.get('endereco')
        email = dados.get('email')
        senha = dados.get('senha')

       



         #validação de dados
        if not isinstance(nome,str): 
            return{'error':'nome invalido'},400
        elif not  testa_cpf(cpf):
            return{'error':'cpf invalido'},400
        elif not isinstance(endereco,str):
            return{'error':'endereco invalido'},400
        elif not testa_email (email):
            return{'error':'email invalido'},400


        senha_hash = bcrypt.hashpw(senha.encode(),bcrypt.gensalt())
        

        cliente.nome = nome
        cliente.cpf = cpf
        cliente.endereco = endereco
        cliente.email = email
        cliente.senha_hash = senha_hash

        db.session.commit()

        return cliente.json(),200
    

    def patch(self,id):

        if (get_jwt_identity() != id):
            return{'error':'Usuário não permitido '},400

        cliente = Cliente.query.get_or_404(id)
        dados = request.json

        nome = dados.get('nome',cliente.nome)
        cpf = dados.get('cpf',cliente.cpf)
        endereco = dados.get('endereco',cliente.endereco)
        email = dados.get('email',cliente.email)
        senha = dados.get('senha',cliente.senha_hash)
        


      

        if not isinstance(nome,str): 
            return{'error':'nome invalido'},400
        elif not testa_cpf(cpf):
            return{'error':'cpf invalido'},400
        elif not isinstance(endereco,str):
            return{'error':'endereco invalido'},400
        elif not testa_email (email):
            return{'error':'email invalido'},400
        
        if  isinstance(senha,str):
            senha_hash = bcrypt.hashpw(senha.encode(),bcrypt.gensalt())
        else:
            senha_hash = senha


     
       

        cliente.nome = nome
        cliente.cpf = cpf
        cliente.endereco = endereco
        cliente.email = email
        cliente.senha_hash = senha_hash
       

        db.session.commit()

        return cliente.json(),200



    def delete(self,id):
        if (get_jwt_identity() != id):
            return{'error':'Usuário não permitido '},400
        cliente = Cliente.query.get_or_404(id)
        db.session.delete(cliente)
        db.session.commit()
        return cliente.json(),200


class ClienteLogin(MethodView):
    def post(self):
        dados = request.json

           
        email = dados.get('email')
        senha = dados.get('senha')

        cliente=Cliente.query.filter_by(email = email).first()
        if (not cliente) or (not bcrypt.checkpw (senha.encode(), cliente.senha_hash)): 
            return{'error':'email ou senha invalidos'},400
        
        token = create_access_token(identity = cliente.id)
        return {"token":token},200



