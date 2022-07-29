from turtle import clear


cadastro = {
    'id':1,
    'nome':'joão carlos silva',
    'filhos':["joana", "sarah"],
    'compras':[
        {
            'id': 4732,
            'produtos': 'Notebook Gamer',
            'preço': 2647.99
        }
   ]
}

print(f"O usuario {cadastro['nome']} realizou a seguinte compra : {cadastro.get(['compras','produtos'])}")
