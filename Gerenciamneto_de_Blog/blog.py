from conexao_orm import Base, engine, session
from user import User
from post import Post

# cria as tabelas
Base.metadata.create_all(engine)

# função para exibir o menu de opções
def show_menu():
    print('Menu de opções:\n')
    print('1. Adcionar Usuário\n')
    print('2. Adcionar Post\n')
    print('3. Consultar Usuário e posts\n')
    print('4. Sair\n')
#Função para adcionar Usuário
def add_user():
    print('Adcionar novo Usuário:')
    name = input('Nome: ')
    email = input('e-mail: ')
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    print('Usuário criado com sucesso!')
    
#Funcção para adcionar um novo post
def add_post():
    print('Adcionar post:')
    title = input('Titulo:')
    content = input('Conteudo:')
    author_id = input('ID do Autor')
    user = session.query(User).filter_by(id=author_id).first()
    if user:
        post = Post(title=title,content=content,author=user)
        session.add(post)
        session.commit()
    else:
        print('Usuario não encontrado!')
#função para consulktar usuários e seus posts
def query_user_post():
    users = session.query(User).join(User.posts).order_by(User.name).all()
    for user in users:
        print(f'User:{user.name},e-mail:{user.email}')
        for post in user.posts:
            print(f'- Post:{Post.title},content: {Post.content}')