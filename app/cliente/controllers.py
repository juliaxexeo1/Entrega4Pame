#controlers

from flask.wrappers import Request
from app.cliente.model import Cliente
from flask import request,jsonify,render_template
from flask.views import MethodView
from app.extensions import db, mail
from flask_mail import Message
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
        elif not isinstance (cpf,int):
            return{'error':'cpf invalido'},400
        elif not isinstance(endereco,str):
            return{'error':'endereco invalido'},400
        elif not isinstance (email,str):
            return{'error':'email invalido'},400
        
        cliente = Cliente.query.filter_by(email = email).first()

        if cliente:
            return {'error':'Email já cadastrado'},400

#cliente = Cliente.query.filter_by(cpf = cpf).first()

        #if cliente:
            #return {'error':'CPF já cadastrado'},400






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
   
    def get (self,id):
        cliente = Cliente.query.get_or_404(id)
        return cliente.json(),200
    
#fazer validação de dados
    def put (self,id):
        cliente = Cliente.query.get_or_404(id)
        dados = request.json

        nome = dados.get('nome')
        cpf = dados.get('cpf')
        endereco = dados.get('endereco')
        email = dados.get('email')


         #validação de dados
        if not isinstance(nome,str): 
            return{'error':'nome invalido'},400
        elif not isinstance (cpf,int):
            return{'error':'cpf invalido'},400
        elif not isinstance(endereco,str):
            return{'error':'endereco invalido'},400
        elif not isinstance (email,str):
            return{'error':'email invalido'},400

        cliente.nome = nome
        cliente.cpf = cpf
        cliente.endereco = endereco
        cliente.email = email
       

        db.session.commit()

        return cliente.json(),200
    
#fazer validação de dados
    def patch(self,id):
        cliente = Cliente.query.get_or_404(id)
        dados = request.json

        nome = dados.get('nome',cliente.nome)
        cpf = dados.get('cpf',cliente.cpf)
        endereco = dados.get('endereco',cliente.endereco)
        email = dados.get('email',cliente.email)

         #validação de dados
        if not isinstance(nome,str): 
            return{'error':'nome invalido'},400
        elif not isinstance (cpf,int):
            return{'error':'cpf invalido'},400
        elif not isinstance(endereco,str):
            return{'error':'endereco invalido'},400
        elif not isinstance (email,str):
            return{'error':'email invalido'},400

        cliente.nome = nome
        cliente.cpf = cpf
        cliente.endereco = endereco
        cliente.email = email
       

        db.session.commit()

        return cliente.json(),200

    def delete(self,id):
        cliente = Cliente.query.get_or_404(id)
        db.session.delete(cliente)
        db.session.commit()
        return cliente.json(),200


'''class ClienteLogin(MethodView):'''