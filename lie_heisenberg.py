import sympy as sp
from algebra import *

def main():
    x, y, z = sp.symbols('x y z', commutative = False)
    base_heisenberg = [x, y, z]

    tabela_heisenberg = {
        x*x: 0, y*y: 0, z*z: 0,
        x*y: z, y*x: -z,        
        x*z: 0, z*x: 0,
        y*z: 0, z*y: 0
    }

    algebra_heisenberg = AlgebraPorTabela(base_heisenberg, tabela_heisenberg)
    verificador_id = VerificadorIdentidades(algebra_heisenberg)
    verificador_ax = VerificadorAxiomas(algebra_heisenberg)

    print("-------- COMUTATIVIDADE ---------")
    verificador_ax.comutatividade()
    
    print("-------- ASSOCIATIVIDADE ---------")
    verificador_ax.associatividade()

    print("-------- ALTERNATIVIDADE ---------")
    verificador_id.alternatividade()

    print("-------- FLEXIBILIDADE ---------")
    verificador_id.flexibilidade()
if __name__ == "__main__":
    main()