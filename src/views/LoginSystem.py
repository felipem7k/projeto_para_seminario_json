from controllers.UserController import UserController
from models.User import User

class LoginSystem:
    def __init__(self):
        self.user_controller = UserController()
    
    def display_login_options(self):
        print("\n=== Sistema de Login ===")
        options = [
            "1. Criar conta",
            "2. Fazer login",
            "3. Sair"
        ]
        for option in options:
            print(option)
        print("=" * 24)
    
    def create_account(self) -> User|None:
        print("\n--- Criação de Conta ---")
        try:
            account = self.user_controller.account_creation()
            if account is not None:
                print("✓ Conta criada com sucesso!")
                return account
            else:
                print("✗ Falha na criação da conta. Tente novamente.")
                return None
        except Exception as e:
            print(f"✗ Erro ao criar conta. {e}")
            return None
    
    def login_account(self) -> User|None:
        print("\n--- Login ---")
        try:
            account = self.user_controller.login()
            if account is not None:
                print("✓ Login realizado com sucesso!")
                return account
            else:
                print("✗ Usuário ou senha inválidos.")
                return None
        except Exception as e:
            print(f"✗ Erro ao fazer login: {e}")
            return None
    
    def get_user_choice(self) -> str|None:
        try:
            choice = input("\nEscolha uma opção (1-3): ").strip()
            return choice
        except KeyboardInterrupt:
            print("\n\nSaindo do sistema...")
            return "3"
        except Exception:
            return None
    
    def handle_user_choice(self, choice) -> str|None:
        if choice == '1':
            return self.create_account()
        elif choice == '2':
            return self.login_account()
        elif choice == '3':
            print("Saindo do sistema. Até logo!")
            return "EXIT"
        else:
            print("✗ Opção inválida. Escolha uma opção entre 1 e 3.")
            return None
    
    def run(self) -> User|None:
        account = None
        max_attempts = 5
        attempts = 0
        
        while account is None and attempts < max_attempts:
            self.display_login_options()
            choice = self.get_user_choice()
            
            if choice is None:
                attempts += 1
                print(f"Tentativa {attempts}/{max_attempts}")
                continue
            
            result = self.handle_user_choice(choice)
            
            if result == "EXIT":
                return None
            elif result is not None:
                account = result
                break
            
            attempts += 1
            if attempts < max_attempts:
                print(f"\nTentativa {attempts}/{max_attempts}")
                input("Pressione Enter para continuar...")
        
        if account is None:
            print(f"\n✗ Número máximo de tentativas ({max_attempts}) excedido.")
            return None
        
        return account