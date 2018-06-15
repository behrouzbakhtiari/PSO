from abc import ABC,abstractmethod
from enum import Enum
import numpy as np
import math
#Problem interface for all test functions
class IProblem(ABC):
    n = 0
    lbound = 0
    ubound  = 0

    def generate_random_ponit(self):
        return np.random.uniform(self.lbound,self.ubound,size=(self.n))    

    def generate_random_ponits(self,count):
        return np.random.uniform(self.lbound,self.ubound,size=(count,self.n))
   
    @abstractmethod
    def get_value(self, swarm):
        pass

#an enum for test functions
class ProblemType(Enum):
    Ackley = 1,
    PowellSum = 2,
    Booth = 3,
    DropWave = 4,
    SumSquares = 5,
    Griewank  = 6

#a factory class for generate test function class
class ProblemFactory:
    @staticmethod
    def generateProblem(type: ProblemType,n,lbound,ubound):
        if  type == ProblemType.Ackley:
            return Ackley(n,lbound,ubound)
        elif type == ProblemType.Booth:
            return  Booth(n,lbound,ubound)
        elif type == ProblemType.PowellSum:
            return PowellSum(n,lbound,ubound)
        elif type == ProblemType.DropWave:
            return DropWave(n,lbound,ubound)
        elif type == ProblemType.SumSquares:
            return SumSquares(n,lbound,ubound)
        elif type == ProblemType.Griewank:
            return Griewank(n,lbound,ubound)
class PowellSum(IProblem):

    def __init__(self,n,lbound,ubound):
        self.n = n
        self.lbound = lbound
        self.ubound = ubound
    
    #get value for custom state
    def get_value(self, swarm):
        value = 0
        for i in range(self.n):
            value = value + abs(swarm[i])**(i+2)
        return value

class Booth(IProblem):
    def __init__(self,n,lbound,ubound):
        self.n = n
        self.lbound = lbound
        self.ubound = ubound

    def get_value(self,swarm):
        value = (swarm[0] + (2 * swarm[1]) - 7)**2 + ( (2 * swarm[0]) + swarm[1] - 5)**2
        return value

class DropWave(IProblem):
    def __init__(self,n,lbound,ubound):
        self.n = n
        self.lbound = lbound
        self.ubound = ubound

    def get_value(self, swarm):
        part1 =  -1 * math.cos(12 * (math.sqrt((swarm[0]**2) + (swarm[1]**2))))
        part2 =  (0.5 * (swarm[0]**2) + (swarm[1]**2)) + 2
        value = part1 / part2
        return value        

class Ackley(IProblem):
    C1=20 
    C2=.2
    C3=2*np.pi
    def __init__(self,n,lbound,ubound):
        self.n = n
        self.lbound = lbound
        self.ubound = ubound    
    def get_value(self, swarm):
        part1 = -1. * self.C1 * np.exp(
            -1. * self.C2 * np.sqrt((1./self.n) * sum(map(lambda nb: nb**2, swarm)))
            )
        part2 = -1. * np.exp(
            (1./self.n) * \
            sum(map(lambda nb: np.cos(self.C3 * nb), swarm))
            )
        return part1 + part2 + self.C1 + np.exp(1)

class SumSquares(IProblem):
    def __init__(self,n,lbound,ubound):
        self.n = n
        self.lbound = lbound
        self.ubound = ubound
    def get_value(self, swarm):
        return np.sum(np.arange(1,self.n+1) * (swarm**2))

class Griewank(IProblem):
    def __init__(self,n,lbound,ubound):
        self.n = n
        self.lbound = lbound
        self.ubound = ubound    
    def get_value(self, swarm):
        part1 = 0
        for i in range(len(swarm)):
            part1 += swarm[i]**2
        part2 = 1
        for i in range(len(swarm)):
            part2 *= math.cos(float(swarm[i]) / math.sqrt(i+1))
        return 1 + (float(part1)/4000.0) - float(part2)   


