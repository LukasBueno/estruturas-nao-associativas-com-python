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
    verificador_id = VerificadorIdentidades(quaternios)
    
    print("------ASSOCIATIVIDADE------")
    verificador.associatividade()

    print("------COMUTATIVIDADE------")
    verificador.comutatividade()

    print("------ALTERNATIVIDADE------")
    verificador_id.alternatividade()

    print("------FLEXIBILIDADE------")
    verificador_id.flexibilidade()   
    
if __name__ == "__main__":
    main()