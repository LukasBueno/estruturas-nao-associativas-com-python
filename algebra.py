from abc import ABC, abstractmethod
import sympy as sp
import itertools

class Algebra(ABC):
    def __init__(self, base):
        self._base = base

    @property
    def base(self):
        return self._base

    @abstractmethod
    def multiplicar_elementos(self, a, b):
        pass 


class AlgebraPorTabela(Algebra):
    def __init__(self, base, tabela_multiplicacao):
        super().__init__(base)

        self._regras = {a * b : 0 for a, b in itertools.product(base, repeat=2)}
        self._regras.update(tabela_multiplicacao)

    @property
    def regras(self):
        return self._regras

    def multiplicar_elementos(self, a, b):
        produto = a * b

        return self._regras.get(produto, 0)


class VerificadorAxiomas:
    def __init__(self, algebra: Algebra):
        self.algebra = algebra

    def calcular_associador_base(self, x, y, z):
        """
        Método destinado ao cálculo do Associador individualmente (x, y, z) = (xy)z - x(yz)
        """
        
        regras = getattr(self.algebra, 'regras', {})
        xy = self.algebra.multiplicar_elementos(x, y)
        yz = self.algebra.multiplicar_elementos(y, z)

        esquerda = sp.expand(xy * z).subs(regras)
        direita = sp.expand(x * yz).subs(regras)

        return sp.simplify(esquerda - direita)

    def calcular_comutador_base(self, x, y):
        """
        Método destinado ao cálculo do Comutador individualmente (x, y) = xy - yx
        """
        xy = self.algebra.multiplicar_elementos(x, y)
        yx = self.algebra.multiplicar_elementos(y, x)

        return sp.simplify(xy - yx)

    def associatividade(self):
        """
        Método destinado à verificação da associatividade
        """

        trincas = itertools.product(self.algebra.base, repeat=3)
        associativa = True

        for x, y, z in trincas:
            associador = self.calcular_associador_base(x, y, z)

            if associador != 0:
                print(f"[Falha na associatividade] Associador({x}, {y}, {z}) = {associador}")
                associativa = False

        if associativa:
             print(f"A álgebra é ASSOCIATIVA!")

        return associativa

    def comutatividade(self):
        """
        Método destinado à verificação da comutatividade
        """

        pares = itertools.product(self.algebra.base, repeat=2)
        comutativa = True

        for x, y in pares:
            comutador = self.calcular_comutador_base(x, y)

            if comutador != 0:
                print(f"[Falha na comutatividade] Comutador({x}, {y}) = {comutador}")
                comutativa = False

        if comutativa:
            print(f"A álgebra é COMUTATIVA!")

        return comutativa    
