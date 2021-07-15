from app.extensions import db

class Produto(db.Model):
    __tablename__='produto'
    id=db.Column(db.Integer, primary_key=True)
    tipo_de_produto=db.Column(db.String(100),nullable=False)
    marca=db.Column(db.String(100),nullable=False)
    quantidade=db.Column(db.Integer,nullable=False)
    preco=db.Column(db.Integer,nullable=False)

    cliente_id = db.Column(db.Integer,db.ForeignKey('cliente.id'))
    
    def json(self):
        return{'tipo_de_produto':self.tipo_de_produto,
        'marca':self.marca,
        'quantidade':self.quantidade,
        'preco':self.preco}
  