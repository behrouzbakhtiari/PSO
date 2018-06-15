import random
import Problem
import numpy as np
 
# This class contains the code of the Particles in the swarm
class Particle:
    def __init__(self,problem,c1,c2,w):
        self.problem = problem
        self.c1 = c1
        self.c2 = c2
        self.w = w
        self.position = problem.generate_random_ponit()
        self.velocity = np.random.uniform(0,1,problem.n)
        self.personal_best = self.position.copy()
        self.personal_best_value = 0

    def update_positions(self):
        #Update the position:
        #position = position + velocity 
        self.position = self.position + self.velocity   
        return
 
    def update_velocities(self, golbal_best):
        #Update the velocity:
        #velocity = w * velocity + c1 * r1 * (golbal_best - position) 
        #           + c2 * r2 * (personal_best - position).
        for i in range(self.problem.n):
            r1 = np.random.rand()
            r2 = np.random.rand()
            
            #social part
            social = self.c1 * r1 * (golbal_best[i] - self.position[i])
            
            #recognition part
            cognitive = self.c2 * r2 * (self.personal_best[i] - self.position[i])
            
            self.velocity[i] = (self.w * self.velocity[i]) + social + cognitive
        return
 

# This class contains the particle swarm optimization algorithm
class ParticleSwarmOptimizer:
    def __init__(self,problem,swarmSize,iterations,c1,c2,w):
        self.problem = problem
        self.swarmSize = swarmSize
        self.iterations = iterations
        self.swarm = []
        self.generate_init_swarms(c1,c2,w)

    def generate_init_swarms(self,c1,c2,w):
        for i in range(self.swarmSize):
            #Initialize particle
            particle = Particle(self.problem,c1,c2,w)
            particle.personal_best_value = self.fitness_function(particle.personal_best)
            self.swarm.append(particle)
        self.update_global_best()        
        
 
    #update the global best particle
    def update_global_best(self):
        self.global_best = self.swarm[0].position
        self.global_best_value = self.swarm[0].personal_best_value
        for j in range(self.swarmSize):
        
            #If the personal best value value is better than the global best 
            # value Set current personal best value as the new global best
            personal_best_value = self.swarm[j].personal_best_value
            if personal_best_value < self.global_best_value:
                self.global_best = self.swarm[j].personal_best
                self.global_best_value = personal_best_value
    
    #Update the personal best positions
    def update_personal_best(self):
        for l in range(self.swarmSize):
            
            #If the fitness value is better than the personal best fitness
            # value Set current value as the personal best
            personal_best_value = self.swarm[l].personal_best_value
            current_value = self.fitness_function(self.swarm[l].position)
            if current_value < personal_best_value:
                self.swarm[l].personal_best = self.swarm[l].position  
                self.swarm[l].personal_best_value = current_value

    def fitness_function(self,position):
        return self.problem.get_value(position)

    def optimize(self):
        for i in range(self.iterations ):
            for k in range(self.swarmSize):
                #Update velocitie of each paricle
                self.swarm[k].update_velocities(self.global_best)
                #Update position of each paricle
                self.swarm[k].update_positions()
            self.update_personal_best()
            self.update_global_best()
        return self.global_best