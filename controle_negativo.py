import sympy as sp
from algebra import *

def main():
    a, b = sp.symbols('a b', commutative=False)
    base = [a, b]
    tabela = {a*a: b, b*a: a, a*b: 0, b*b: 0}

    controle_negativo = AlgebraPorTabela(base, tabela)
    verificador_id = VerificadorIdentidades(controle_negativo)
    verificador_ax = VerificadorAxiomas(controle_negativo)

    print("------COMUTATIVIDADE------")
    verificador_ax.comutatividade()

    print("------ASSOCIATIVIDADE------")
    verificador_ax.associatividade()

    print("------ALTERNATIVIDADE------")
    verificador_id.alternatividade()

    print("------FLEXIBILIDADE------")
    verificador_id.flexibilidade()   
    
if __name__ == "__main__":
    main()