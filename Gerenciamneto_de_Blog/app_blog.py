from blog import show_menu, add_post, add_user, query_user_post

while True:
    
    show_menu()
    option = input('Digite uma Opção')
    
    if option == "1":
        add_user()
    elif option == '2':
        add_post()
    elif option == '3':
        query_user_post()
    else:
        break