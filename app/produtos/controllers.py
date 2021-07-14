from flask.wrappers import Request
from app.produtos.model import Produto
from flask import request,jsonify
from flask.views import MethodView
from app.extensions import db

class ProdutoCreate(MethodView):#/produto/create
    def get(self):
        produto=Produto.query.all()
        return jsonify ([produto.json()for produto in produto]),200

    def post(self):
        dados=request.json

        tipo_de_produto=dados.get('tipo_de_produto')
        marca=dados.get('marca')
        quantidade=dados.get('quantidade')
        preco=dados.get('preco')

        #validação de dados:
        if not isinstance(tipo_de_produto,str):
            return{'error':'tipo invalido'} 
        elif not isinstance(marca,str):
            return{'error':'marca invalida'} 
        elif not isinstance (quantidade,int):
            return{'error':'quantidade invalida'}
        elif not isinstance (preco,int):
            return{'error':'preco invalida'}
       
        
        produto=Produto(tipo_de_produto=tipo_de_produto,marca=marca,quantidade=quantidade,preco=preco)#continuar
        db.session.add(produto)
        db.session.commit()

        return produto.json(),200

class ProdutoDetails(MethodView): #'/produto/details/<int:id>'
   
    def get (self,id):
        produto = Produto.query.get_or_404(id)
        return produto.json(),200
    

    def put (self,id):
        produto = Produto.query.get_or_404(id)
        dados = request.json

        tipo_de_produto = dados.get('tipo_de_produto')
        marca = dados.get('marca')
        quantidade = dados.get('quantidade')
        preco = dados.get('preco')
        
        #validação de dados:
        if not isinstance(tipo_de_produto,str):
            return{'error':'tipo invalido'}  
        elif not isinstance(marca,str):
            return{'error':'marca invalida'}
        elif not isinstance (quantidade,int):
            return{'error':'quantidade invalida'}
        elif not isinstance (preco,int):
            return{'error':'preco invalida'}
       

        produto.tipo_de_produto=tipo_de_produto
        produto.marca=marca
        produto.quantidade=quantidade
        produto.preco=preco

        
        db.session.commit()

        return produto.json(),200
    

    def patch(self,id):
        produto = Produto.query.get_or_404(id)
        dados = request.json

        
        tipo_de_produto=dados.get('tipo_de_produto',produto.tipo_de_produto)
        marca=dados.get('marca',produto.marca)
        quantidade=dados.get('quantidade',produto.quantidade)
        preco=dados.get('preco',produto.preco)
        
        
        #validação de dados:
        if not isinstance(tipo_de_produto,str):
            return{'error':'tipo invalido'}  
        elif not isinstance(marca,str):
            return{'error':'marca invalida'}
        elif not isinstance (quantidade,int):
            return{'error':'quantidade invalida'}
        elif not isinstance (preco,int):
            return{'error':'preco invalida'}
       

        produto.tipo_de_produto=tipo_de_produto
        produto.marca=marca
        produto.quantidade=quantidade
        produto.preco=preco

        db.session.commit()

        return produto.json(),200

    def delete(self,id):
        produto = Produto.query.get_or_404(id)
        db.session.delete(produto)
        db.session.commit()
        return produto.json(),200