import sympy as sp
from algebra import *

def main():
    e1, e2, e3 = sp.symbols('e1 e2 e3', commutative=False)
    base = [e1, e2, e3]

    tabela_de_multiplicacao = {
       e1 * e1: e1,  e1 * e2: e2,  e1 * e3: e3,
       e2 * e1: e2,  e2 * e2: e1,  e2 * e3: e3,
       e3 * e1: e3,  e3 * e2: e3,  e3 * e3: 0
    }

    exemplo_livro = AlgebraPorTabela(base, tabela_de_multiplicacao)
    verificador = VerificadorAxiomas(exemplo_livro)
    verificador_id = VerificadorIdentidades(exemplo_livro)

    print("------[ASSOCIATIVIDADE]------")
    verificador.associatividade()

    print("------[COMUTATIVIDADE]------")
    verificador.comutatividade()

    print("------[ALTERNATIVIDADE]------")
    verificador_id.alternatividade()
       
if __name__ == "__main__":
    main()