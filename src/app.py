from views.LoginSystem import LoginSystem

def main():
    login_system = LoginSystem()
    account = login_system.run()

    if account is not None:
        try:
            print(f"\n🎉 Bem-vindo(a), {account.personal_data.name}!")
            print(f"Você tem {account.personal_data.birth.age()} anos.")
        except AttributeError:
            print("\n🎉 Login realizado com sucesso!")
            print("Sistema pronto para uso.")
    else:
        print("\nSistema encerrado.")

if __name__ == "__main__":
    main()