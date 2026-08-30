import sympy as sp
from algebra import *

def main():
    one, i, j, k = sp.symbols('1 i j k', commutative=False)
    base = [one, i, j, k]
    tabela_de_multiplicacao = {
        one * one:  one,  one * i:  i,  one * j:  j,  one * k:  k,
        i * one:  i,  i * i: -one,  i * j:  k,  i * k: -j,
        j * one:  j,  j * i: -k,  j * j: -one,  j * k:  i,
        k * one:  k,  k * i:  j,  k * j: -i,  k * k: -one
    }

    quaternios = AlgebraPorTabela(base, tabela_de_multiplicacao)
    verificador = VerificadorAxiomas(quaternios)
    
    print("------[ASSOCIATIVIDADE]------")
    verificador.associatividade()

    print("------[COMUTATIVIDADE]------")
    verificador.comutatividade()

    # e1, e2, e3 = sp.symbols('e1 e2 e3', commutative=False)
    # base = [e1, e2, e3]

    # tabela_de_multiplicacao = {
    #     e1 * e1: e1,  e1 * e2: e2,  e1 * e3: e3,
    #     e2 * e1: e2,  e2 * e2: e1,  e2 * e3: e3,
    #     e3 * e1: e3,  e3 * e2: e3,  e3 * e3: 0
    # }

    # exemplo_livro = AlgebraPorTabela(base, tabela_de_multiplicacao)
    # verificador = VerificadorAxiomas(exemplo_livro)

    # print("------[ASSOCIATIVIDADE]------")
    # verificador.associatividade()

    # print("------[COMUTATIVIDADE]------")
    # verificador.comutatividade()

if __name__ == "__main__":
    main()