#model
#trasformei cpf em string

from app.extensions import db

class Cliente(db.Model):
    __tablename__='cliente'
    id=db.Column(db.Integer, primary_key=True)
    nome=db.Column(db.String(100),nullable=False)
    cpf=db.Column(db.String(11),nullable=False, unique=True)
    endereco=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),nullable=False, unique=True)
    senha_hash = db.Column(db.String(300),nullable=False)

    produto=db.relationship('Produto',backref='cliente')

    
    def json(self):
        return{
        'nome':self.nome,
        'cpf':self.cpf,
        'endereco':self.endereco,
        'email':self.email}


