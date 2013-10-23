#!/usr/bin/python

import math;
import sys;

# WARNING! There is no input validation!
n = int(sys.argv[1]) + 0.0;

solution = 2*math.pow(n,4)*math.factorial(n*(n-1))/math.pow(math.factorial(n), (n-1))

print("Hay " + str(int(solution)) + " recetas ricas en una torta de " + \
    str(n) + "x" + str(n) + " con " + str(n) + " ingredientes y un " + \
    "ingrediente magico.");


