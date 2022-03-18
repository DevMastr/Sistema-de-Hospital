from os import system
import platform

cadastros = []
options_sexo = {"Masculino": "M", "Feminino": "F"}
options_comorbidade = {"sim":"S", "nao": "N"}


def os_verifier():
    """Verificar o seu Sistema Operacional"""

    OS = platform.system()
    if OS == "Windows":
        return "cls"
    else:
        return "clear"


class Tratamento():
    """Classe dedicada ao tratamento do terminal / erros"""

    @staticmethod
    def clearMessage():
        clearTerminal = os_verifier()
        system(clearTerminal)

    @staticmethod
    def erro_Message():
        print("ERROR: Opção Inválida!")

class Options():
    """Classe dedicada a mostra das opções disponiveis"""

    @staticmethod
    def options_Sexo():
        global options_sexo
        Tratamento.clearMessage()
        print(f'SEXO:\n{"-"*10}\n[{options_sexo["Masculino"]}]asculino',
            f'\n[{options_sexo["Feminino"]}]eminino\n{"-"*10}')

        return options_sexo

    @staticmethod
    def options_Comorbidade():
        global options_comorbidade
        Tratamento.clearMessage() 
        print(f'COMORBIDADES:\n{"-"*10}\n[{options_comorbidade["sim"]}]im',
            f'\n[{options_comorbidade["nao"]}]ão\n{"-"*10}')

        return options_comorbidade

class Users():
    """Classe dedicada a configurações dos usuários no Banco de Dados

    Returns:
        _type_: None
    """

    @staticmethod
    def cadastro_Users(nome:str, idade:int) -> bool:
        """Essa função servirá para cadastrar os usuários
        Args:
            nome (str): Nome do usuário
            idade (int): Idade do usuário
        
        Returns:
            bool: True
        """

        Options.options_Sexo()
        sexo = input("Digite seu Sexo: ").upper()[0]

        while not sexo in options_sexo.values(): # Verificar se o valor da variavel está de acordo com as opções válidas 
            Tratamento.erro_Message()
            sexo = input(f"Digite seu Sexo: ").upper()[0]

        Options.options_Comorbidade()
        comorbidade = input("Você tem alguma comorbidade?: ").upper()[0]

        while not comorbidade in options_comorbidade.values(): # Verificar se o valor da variavel está de acordo com as opções válidas
            Tratamento.erro_Message()
            comorbidade = input("Você tem alguma comorbidade?: ").upper()[0]

        cadastros.append({"nome": nome, "idade": idade, "sexo": sexo, "comorbidade": comorbidade})
        print("\nConta Cadastrada!!")
        return True

    @staticmethod
    def ordenarUrgencia() -> dict: # Colocar cada fita em cada usuário correspondente
        urgencia = {
            'branca':
                [(x) for x in cadastros if x["comorbidade"] == "N" and x["idade"] <= 50],
            'verde':
                [(x) for x in cadastros if x["comorbidade"] == "S" and x["idade"] >= 12 and x["idade"] <= 29],
            'amarelo':
                [(x) for x in cadastros if x["comorbidade"] == "S" and x["idade"] >= 30 and x["idade"] <= 49],
            'vermelha': 
                [(x) for x in cadastros if x["comorbidade"] == "S" and x["idade"] >= 50 or x["comorbidade"] == "S" and x["idade"] <= 6]}
        
        return urgencia.items()

class Visualizer():
    """Classe dedicada a funções de visualização do Banco de Dados"""

    @staticmethod
    def visualizarDB(): # Visualizar os usuários cadastrados no Banco de Dados
        global cadastros
        for x in cadastros:
            print(f'{"-"*10}\n',
                  f'Nome: {x["nome"]}\n',
                  f'Idade: {x["idade"]}\n',
                  f'Sexo: {x["sexo"]}\n',
                  f'Comorbidade: {x["comorbidade"]}')

    @staticmethod
    def visualizarUgencias(): # Visualizar o nivel de urgência de todos os usuários
        for x in Users.ordenarUrgencia():
            print(x)


def main():
    nome = input("\nDigite seu nome: ").title()
    idade = int(input("Digite sua Idade: "))
    Users.cadastro_Users(nome, idade)
    Visualizer.visualizarUgencias()


if __name__=="__main__":
    while True:
        main()
