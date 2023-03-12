from abc import ABC, abstractmethod
from sys import exit	

class Associa(ABC):
    @abstractmethod
    def relacionar(self, nome):
        pass
# class associa serve de base para as associacoes

class Aluno(Associa):
    def relacionar(self, nome):
        return f"{nome} é um aluno da Fatec."
        
class Aluna(Associa):
    def relacionar(self, nome):
        return f"{nome} é um aluna da Fatec."        

class Professor(Associa):
    def relacionar(self, nome):
        return f"{nome} é um professor na Fatec."
        
class Professora(Associa):
    def relacionar(self, nome):
        return f"{nome} é um professora na Fatec."        

class Coordenador(Associa):
    def relacionar(self, nome):
        return f"{nome} é um coordenador na Fatec."

class Coordenadora(Associa):
    def relacionar(self, nome):
        return f"{nome} é um coordenadora na Fatec."
        
class Diretor(Associa):
    def relacionar(self, nome):
        return f"{nome} é um diretor na Fatec."
        
class Diretora(Associa):
    def relacionar(self, nome):
        return f"{nome} é um diretora na Fatec."        

class Administrador(Associa):
    def relacionar(self, nome):
        return f"{nome} é um administrador na Fatec."
        
class Administradora(Associa):
    def relacionar(self, nome):
        return f"{nome} é um administradora na Fatec."        

class Vestibulando(Associa):
    def relacionar(self, nome):
        return f"{nome} é um vestibulando na Fatec."

class FabricaAssociacao:
    def criar_assos(self, tipo_assos):
        if tipo_assos == "Aluno":
            return Aluno()
        elif tipo_assos == "Aluna":
            return Aluna()    
        elif tipo_assos == "Professor":
            return Professor()
        elif tipo_assos == "Professora":
            return Professora()    
        elif tipo_assos == "Coordenador":
            return Coordenador()
        elif tipo_assos == "Coordenadora":
            return Coordenadora()    
        elif tipo_assos == "Diretor":
            return Diretor()
        elif tipo_assos == "Diretora":
            return Diretora()    
        elif tipo_assos == "Administrador":
            return Administrador()
        elif tipo_assos == "Administradora":
            return Administradora()    
        elif tipo_assos == "Vestibulando":
            return Vestibulando()

repeat = True
while repeat == True:
    print("\n==MENU== \nDigite 'q' para sair")
    nome = input("Entre com o seu nome: ")
    if nome.lower() == "q":
        exit()
    relac = input("Qual a sua relação com a FATEC? ")

    fabrica_associacao = FabricaAssociacao()
    if relac.lower() == "aluno":
        alun = fabrica_associacao.criar_assos("Aluno")
        print(alun.relacionar(nome))
        #caso do aluno
    elif relac.lower() == "aluna":
        alun = fabrica_associacao.criar_assos("Aluna")
        print(alun.relacionar(nome))
        #caso do aluna    
    elif relac.lower() == "professor":
        prof = fabrica_associacao.criar_assos("Professor")
        print(prof.relacionar(nome))
        #caso do professor
    elif relac.lower() == "professora":
        prof = fabrica_associacao.criar_assos("Professora")
        print(prof.relacionar(nome))
        #caso do professora    
    elif relac.lower() == "coordenador":
        coord = fabrica_associacao.criar_assos("Coordenador")
        print(coord.relacionar(nome))
        #caso do coordenador
    elif relac.lower() == "coordenadora":
        coord = fabrica_associacao.criar_assos("Coordenadora")
        print(coord.relacionar(nome))
        #caso do coordenadora   
    elif relac.lower() == "diretor":
        diret = fabrica_associacao.criar_assos("Diretor")
        print(diret.relacionar(nome))
        #caso do diretor
    elif relac.lower() == "diretora":
        diret = fabrica_associacao.criar_assos("Diretora")
        print(diret.relacionar(nome))
        #caso do diretora    
    elif relac.lower() == "administrador":
        adm = fabrica_associacao.criar_assos("Administrador")
        print(adm.relacionar(nome))
        #caso do administrador
    elif relac.lower() == "administradora":
        adm = fabrica_associacao.criar_assos("Administradora")
        print(adm.relacionar(nome))
        #caso do administradora    
    elif relac.lower() == "vestibulando":
        vestb = fabrica_associacao.criar_assos("Vestibulando")
        print(vestb.relacionar(nome))
        #caso do vestibulando
    else:
        print(f"{nome}, você não tem relação com a Fatec, por gentileza se dirija à secretaria.")
        #caso nao tenha uma das relacoes acima
