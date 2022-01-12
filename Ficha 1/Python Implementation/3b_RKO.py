# RKO Problem - Reaction Knockout Optimization Problem.
PRODUCT_ID = 'EX_succ_e'
BIOMASS_ID = 'BIOMASS_Ec_iML1515_core_75p37M'

from mewpy.optimization.evaluation import BPCY, WYIELD
# Biomass-Product Coupled Yield usado para maximizar biomassa-produto
# WYIELD
evaluator_1 = BPCY(BIOMASS_ID, PRODUCT_ID, method='pFBA')
evaluator_2 = WYIELD(BIOMASS_ID, PRODUCT_ID)

from mewpy.problems import RKOProblem
problem = RKOProblem(model, fevaluation = [evaluator_1, evaluator_2], envcond=environ_conditions, candidate_max_size=5)

from mewpy.optimization import EA #Evolutionary Algorithm
mutante = EA(problem, max_generations=25, visualizer=True)
mutante_run= mutante.run()
print(mutante_run)
lista_genes = open('3b_RKO_list_WYIELD.txt', 'w')
for i in mutante_run:
    lista_genes.write(str(i) + '\n')

lista_genes.close()

from mewpy.util.constants import ModelConstants
ModelConstants.RESET_SOLVER = True 