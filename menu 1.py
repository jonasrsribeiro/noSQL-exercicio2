from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://jonas:zlVsnz3v8A59vGwo@nosql.ocxhdgk.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"

client = MongoClient(uri, server_api=ServerApi('1'))
global db
db = client.biblioteca

""" GET_ALL """

def get_all(collection_name):
    global db
    mycol = db[collection_name]
    results = mycol.find({})
    for doc in results:
        print(f"{collection_name}s disponíveis: ")
        print("ID:", doc['_id'])
        print("Nome:", doc['nome'])

""" USUARIO """

def create_usuario():
    global db
    mycol = db.usuario
    print("\nInserindo um novo usuário")
    nome = input("Nome: ")
    senha = input("Senha: ")
    email = input("Email: ")
    sobrenome = input("Sobrenome: ")
    cpf = input("CPF: ")
    key = 1
    end = []
    while (key != 'N'):
        rua = input("Rua: ")
        num = input("Num: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        cep = input("CEP: ")
        endereco = {
            "rua":rua,
            "num": num,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "cep": cep
        }
        end.append(endereco)
        key = input("Deseja cadastrar um novo endereço (S/N)? ")
    mydoc = { "nome": nome, "sobrenome": sobrenome, "cpf": cpf, "senha": senha, "email": email, "end": end }
    x = mycol.insert_one(mydoc)
    print("Documento inserido com ID ", x.inserted_id)

def read_usuario(nome):
    global db
    mycol = db.usuario
    print("Usuários existentes: ")
    if not len(nome):
        mydoc = mycol.find().sort("nome")
        for x in mydoc:
            print(x["nome"], x["cpf"])
    else:
        myquery = {"nome": nome}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)

def update_usuario(nome):
    global db
    mycol = db.usuario
    myquery = {"nome": nome}
    mydoc = mycol.find_one(myquery)
    print("Dados do usuário: ", mydoc)

    nome = input("Mudar Nome:")
    if len(nome):
        mydoc["nome"] = nome

    sobrenome = input("Mudar Sobrenome:")
    if len(sobrenome):
        mydoc["sobrenome"] = sobrenome

    email = input("Mudar Email:")
    if len(sobrenome):
        mydoc["email"] = email

    cpf = input("Mudar CPF:")
    if len(cpf):
        mydoc["cpf"] = cpf

    newvalues = { "$set": mydoc }
    mycol.update_one(myquery, newvalues)

def delete_usuario(nome, sobrenome):
    global db
    mycol = db.usuario
    myquery = {"nome": nome, "sobrenome":sobrenome}
    mydoc = mycol.delete_one(myquery)
    print("Deletado o usuário ", mydoc)

""" VENDEDOR """

def create_vendedor():
    global db
    mycol = db.vendedor
    print("\nInserindo um novo vendedor")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    cpf = input("CPF: ")
    email = input("E-mail: ")
    cnpj = input("CNPJ: ")
    key = 1
    end = []
    while (key != 'N'):
        rua = input("Rua: ")
        num = input("Num: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        cep = input("CEP: ")
        endereco = {
            "rua":rua,
            "num": num,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "cep": cep
        }
        end.append(endereco) #estou inserindo na lista
        key = input("Deseja cadastrar um novo endereço (S/N)? ")
    mydoc = { "nome": nome, "sobrenome": sobrenome, "cpf": cpf, "email": email, "cnpj": cnpj, "end": end }
    x = mycol.insert_one(mydoc)
    print("Documento inserido com ID ", x.inserted_id)

def read_vendendor(nome):
    global db
    mycol = db.vendedor
    print("Vendedores existentes: ")
    if not len(nome):
        mydoc = mycol.find().sort("nome")
        for x in mydoc:
            print(x["nome"], x["cpf"])
    else:
        myquery = {"nome": nome}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)

def update_vendedor(nome):
    global db
    mycol = db.vendedor
    myquery = {"nome": nome}
    mydoc = mycol.find_one(myquery)
    print("Dados do vendedor: ", mydoc)

    nome = input("Mudar Nome:")
    if len(nome):
        mydoc["nome"] = nome

    sobrenome = input("Mudar Sobrenome:")
    if len(sobrenome):
        mydoc["sobrenome"] = sobrenome

    email = input("Mudar Email:")
    if len(sobrenome):
        mydoc["email"] = email

    cpf = input("Mudar CPF:")
    if len(cpf):
        mydoc["cpf"] = cpf

    cnpj = input("Mudar CNPJ:")
    if len(cnpj):
        mydoc["cnpj"] = cnpj

    newvalues = { "$set": mydoc }
    mycol.update_one(myquery, newvalues)

def delete_vendedor(nome, sobrenome):
    global db
    mycol = db.vendedor
    myquery = {"nome": nome, "sobrenome":sobrenome}
    mydoc = mycol.delete_one(myquery)
    print("Deletando o vendedor ", mydoc)

""" PRODUTO """

def create_produto():
    global db
    mycol = db.produto
    print("\nInserindo um novo produto")
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    descricao = input("Descrição do produto: ")
    categoria = input("Categoria do produto: ")
    mydoc = { "nome": nome, "preco": preco, "descricao": descricao, "categoria": categoria }
    x = mycol.insert_one(mydoc)
    print("Produto inserido com ID ", x.inserted_id)

def read_produto(nome):
    global db
    mycol = db.produto
    print("Produtos existentes: ")
    if not len(nome):
        mydoc = mycol.find().sort("nome")
        for x in mydoc:
            print(x["nome"], x["categoria"], x["preco"])
    else:
        myquery = {"nome": nome}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)

def update_produto(nome):
    global db
    mycol = db.produto
    myquery = {"nome": nome}
    mydoc = mycol.find_one(myquery)
    print("Dados do produto: ", mydoc)

    nome = input("Mudar Nome do produto:")
    if len(nome):
        mydoc["nome"] = nome

    preco = float(input("Mudar Preço do produto:"))
    if preco:
        mydoc["preco"] = preco

    descricao = input("Mudar Descrição do produto:")
    if len(descricao):
        mydoc["descricao"] = descricao

    categoria = input("Mudar Categoria do produto:")
    if len(categoria):
        mydoc["categoria"] = categoria

    newvalues = { "$set": mydoc }
    mycol.update_one(myquery, newvalues)

def delete_produto(nome):
    global db
    mycol = db.produto
    myquery = {"nome": nome}
    mydoc = mycol.delete_one(myquery)
    print("Produto deletado com ID ", mydoc.deleted_id)

""" COMPRA """

def create_compra():
    global db
    mycol = db.compra
    print("\nInserindo uma nova compra")
    data_compra = input("Data da compra (DD-MM-AAAA): ")
    data_entrega = input("Data de entrega (DD-MM-AAAA): ")
    status_compra = input("Status da compra: ")
    usuario_id = input("ID do usuário que realizou a compra: ")
    produto_id = input("ID do produto comprado: ")
    
    mydoc = {"data_compra": data_compra, "data_entrega": data_entrega, "status_compra": status_compra, "usuario_id": usuario_id, "produto_id": produto_id}
    
    x = mycol.insert_one(mydoc)
    print("Compra inserida com ID ", x.inserted_id)

def read_compra(compra_id):
    global db
    mycol = db.compra
    print("Compras existentes: ")
    if not len(compra_id):
        mydoc = mycol.find().sort("data_compra")
        for x in mydoc:
            print(x["compra_id"], x["data_compra"])
    else:
        myquery = {"compra_id": compra_id}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)

def update_compra(compra_id):
    global db
    mycol = db.compra
    myquery = {"compra_id": compra_id}
    mydoc = mycol.find_one(myquery)
    print("Dados da compra: ", mydoc)

    data_compra = input("Mudar Data da compra (DD-MM-AAAA):")
    if len(data_compra):
        mydoc["data_compra"] = data_compra

    data_entrega = input("Mudar Data de entrega (DD-MM-AAAA):")
    if len(data_entrega):
        mydoc["data_entrega"] = data_entrega

    status_compra = input("Mudar Status da compra:")
    if len(status_compra):
        mydoc["status_compra"] = status_compra

    newvalues = { "$set": mydoc }
    mycol.update_one(myquery, newvalues)

def delete_compra(compra_id):
    global db
    mycol = db.compra
    myquery = {"compra_id": compra_id}
    mydoc = mycol.delete_one(myquery)
    print("Compra deletada com ID ", mydoc.deleted_id)

""" FAVORITOS """

def create_favorito():
    global db
    mycol = db.favorito
    get_all("usuario")
    print("\nAdicionando um novo favorito")
    usuario_id = input("ID do usuário: ")
    get_all("produto")
    produto_id = input("ID do produto: ")
    mydoc = {"usuario_id": usuario_id, "produto_id": produto_id}
    x = mycol.insert_one(mydoc)
    print("Favorito inserido com ID ", x.inserted_id)


def list_favoritos(usuario_id):
    global db
    mycol = db.favorito
    print("Favoritos do usuário: ")
    myquery = {"usuario_id": usuario_id}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print("Produto ID:", x["produto_id"])


def delete_favorito(usuario_id, produto_id):
    global db
    mycol = db.favorito
    myquery = {"usuario_id": usuario_id, "produto_id": produto_id}
    mydoc = mycol.delete_one(myquery)
    print("Favorito deletado com ID ", mydoc.deleted_id)

""" CLI """

key = 0
sub = 0
while (key != 'S'):
    print("1-CRUD Usuário")
    print("2-CRUD Vendedor")
    print("3-CRUD Produto")
    print("4-CRUD Comprar")
    print("5- CRUD Favoritos")
    key = input("Digite a opção desejada? (S para sair) ")

    if (key == '1'):
        print("Menu do Usuário")
        print("1-Create Usuário")
        print("2-Read Usuário")
        print("3-Update Usuário")
        print("4-Delete Usuário")
        sub = input("Digite a opção desejada? (V para voltar) ")
        if (sub == '1'):
            print("Create usuario")
            create_usuario()
            
        elif (sub == '2'):
            nome = input("Read usuário, deseja algum nome especifico? ")
            read_usuario(nome)
        
        elif (sub == '3'):
            nome = input("Update usuário, deseja algum nome especifico? ")
            update_usuario(nome)

        elif (sub == '4'):
            print("delete usuario")
            nome = input("Nome a ser deletado: ")
            sobrenome = input("Sobrenome a ser deletado: ")
            delete_usuario(nome, sobrenome)
            
    elif (key == '2'):
        print("Menu do Vendedor")
        print("1-Create Vendedor")
        print("2-Read Vendedor")
        print("3-Update Vendedor")
        print("4-Delete Vendedor")
        sub = input("Digite a opção desejada? (V para voltar) ")
        if (sub == '1'):
            print("Create Vendedor")
            create_vendedor()

        elif (sub == '2'):
            nome = input("Read usuário, deseja algum nome especifico? ")
            read_vendendor(nome)
        
        elif (sub == '3'):
            nome = input("Update usuário, deseja algum nome especifico? ")
            update_vendedor(nome)

        elif (sub == '4'):
            print("Delete Vendedor")
            nome = input("Nome a ser deletado: ")
            sobrenome = input("Sobrenome a ser deletado: ")
            delete_vendedor(nome, sobrenome)

    elif key == '3':
        print("Menu do Produto")
        print("1. Create Produto")
        print("2. Read Produto")
        print("3. Update Produto")
        print("4. Delete Produto")
        sub = input("Digite a opção desejada? (V para voltar) ")
        if sub == '1':
            print("Create Produto")
            create_produto()
        elif sub == '2':
            nome = input("Read Produto, deseja algum nome específico? ")
            read_produto(nome)
        elif sub == '3':
            nome = input("Update Produto, deseja algum nome específico? ")
            update_produto(nome)
        elif sub == '4':
            print("Delete Produto")
            nome = input("Nome a ser deletado: ")
            delete_produto(nome)

    elif key == '4':
        print("Menu da Compra")
        print("1. Create Compra")
        print("2. Read Compra")
        print("3. Update Compra")
        print("4. Delete Compra")
        sub = input("Digite a opção desejada? (V para voltar) ")
        if sub == '1':
            print("Create Compra")
            create_compra()
        elif sub == '2':
            compra_id = input("Read Compra, deseja algum ID específico? ")
            read_compra(compra_id)
        elif sub == '3':
            compra_id = input("Update Compra, deseja algum ID específico? ")
            update_compra(compra_id)
        elif sub == '4':
            print("Delete Compra")
            compra_id = input("ID a ser deletado: ")
            delete_compra(compra_id)
    if key == '5':
        print("Menu de Favoritos")
        print("1. Adicionar Favorito")
        print("2. Listar Favoritos")
        print("3. Remover Favorito")
        sub = input("Digite a opção desejada? (V para voltar) ")
        if sub == '1':
            print("Adicionar Favorito")
            create_favorito()
        elif sub == '2':
            usuario_id = input("Digite o ID do usuário para listar seus favoritos: ")
            list_favoritos(usuario_id)
        elif sub == '3':
            usuario_id = input("ID do usuário: ")
            produto_id = input("ID do produto: ")
            delete_favorito(usuario_id, produto_id)
    else:
        print("Tchau Prof...")
