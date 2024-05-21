# AUTENTICAÇÃO

usuario_salvo = "admin"
senha_salva = "123123"

def autenticar_usuario(nome_usuario, senha):
    if nome_usuario == usuario_salvo:
        if senha == senha_salva:
            return "Login bem-sucedido"
        else:
            return "Senha Incorreta"
    else:
        return "usuario não existe"
    
def main():
    nome_usuario = input("Digite seu nome de usuario: ")
    senha = input("Digite sua senha: ")

    resultado_autenticacao = autenticar_usuario(nome_usuario, senha)
    print(resultado_autenticacao)

if __name__ == "__main__":
    main()

