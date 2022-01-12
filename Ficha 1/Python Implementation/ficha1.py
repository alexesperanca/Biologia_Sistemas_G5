from cobra.io import read_sbml_model
from mewpy.simulation import get_simulator

model = read_sbml_model ('iML1515.xml') #abrir o modelo com o cobrapy
model.solver = 'gurobi'
environ_conditions = {'EX_o2_e': (-20.0, 100000.0), 'EX_glc__D_e': (-15.0,100000.0)} #definir as variáveis ambiente
# print(model.summary()) ----- BIOMASS_Ec_iML1515_core_75p37M

simul = get_simulator(model, envcond = environ_conditions) #inicializar o simulador
result = simul.simulate (method = 'FBA') #simular com o metodo Flux Balance Analysis
#simul.reactions
#succinato - EX_succ_e

# Exercicio 1) What is the wild-type production of your group’s compound?
print('Qual é a produção wild-type do succinato?')
print(result.fluxes['EX_succ_e'])
# wild-type não produz succinato

# Exercicio 2) What are the maximum compund production capabilities?
print(simul.FVA(reactions = ['EX_succ_e'], format = 'df')) #realiza um Flux Variability Analysis e retorna o resultado em formato dataframe
# Minimum = 0.0, Maximum = 6.26