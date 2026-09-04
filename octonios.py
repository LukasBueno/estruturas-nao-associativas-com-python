import sympy as sp
from algebra import *

def main():
    e0, e1, e2, e3, e4, e5, e6, e7 = sp.symbols('e0 e1 e2 e3 e4 e5 e6 e7', commutative=False)
    base_octonios = [e0, e1, e2, e3, e4, e5, e6, e7]
    tabela_octonios = {}

    # Elemento neutro e0 == 1
    for e in base_octonios:
        tabela_octonios[e0 * e] = e
        tabela_octonios[e * e0] = e
    tabela_octonios[e0 * e0] = e0

    # Quadrado dos imaginários (-e0) == -1
    for i in range(1, 8):
        tabela_octonios[base_octonios[i] * base_octonios[i]] = -e0

    # Produtos cruzados (Plano de Fano)
    fano_triplas = [
        (3, 2, 1), (5, 4, 1), (5, 6, 3),
        (6, 7, 1), (2, 7, 5), (3, 7, 4), (2, 6, 4)
    ] 

    for i, j, k in fano_triplas:
        ei, ej, ek = base_octonios[i], base_octonios[j], base_octonios[k]
        
        # Ordem direta
        tabela_octonios[ei * ej] = ek
        tabela_octonios[ej * ek] = ei
        tabela_octonios[ek * ei] = ej
        
        # Ordem inversa (anticomutativa)
        tabela_octonios[ej * ei] = -ek
        tabela_octonios[ek * ej] = -ei
        tabela_octonios[ei * ek] = -ej

    octonios = AlgebraPorTabela(base_octonios, tabela_octonios)
    verificador_ax = VerificadorAxiomas(octonios)
    verificador_id = VerificadorIdentidades(octonios)

    print("-------- ASSOCIATIVIDADE ---------")
    verificador_ax.associatividade()

    print("-------- COMUTATIVIDADE ---------")
    verificador_ax.comutatividade()

    print("-------- ALTERNATIVIDADE ---------")
    verificador_id.alternatividade()

    print("-------- FLEXIBILIDADE ---------")
    verificador_id.flexibilidade()

if __name__ == "__main__":
    main()