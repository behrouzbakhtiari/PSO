import PSO
import Problem
import numpy as np

 
problem = Problem.ProblemFactory.generateProblem(
                Problem.ProblemType.Ackley, 5, -32, 32)
                
iterations = 100
swarmSize = 50
c1 = 2 #social constant
c2 = 2 #cognative constant
w =  0.2 #constant inertia weight
pso = PSO.ParticleSwarmOptimizer(problem, swarmSize, iterations, c1, c2, w)
solution = pso.optimize()
print('global best position : {0} - global best value : {1}'.format(solution,problem.get_value(solution)))
            