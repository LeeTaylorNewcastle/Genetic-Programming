from Classes import NodeStructure, GeneticProgram, List
from GlobalVariables import func_set, measure_fitness, xt

# Testing NodeStructure.__copy__()
# nsObj = NodeStructure()
# nsObjC = nsObj.__copy__()

# Testing generation depth 3
""" 
Naming: nsd31 -> NodeStructureDepth3[Instance]1
Results: 
 Depth 3 - Good! 
"""
# nsd31 = NodeStructure(depth_lim_lower=3, depth_lim_upper=3)
# strucs = [nsObj, nsObjC, nsd31]

''' TEST: Change from Python27 to Python37 '''
# AttributeError: 'int' object has no attribute '__div__'
# x, y = 4, 4
# # print(x.__truediv__(y))
# # print(4 / 4)

''' TESTING: class.List output string of values as opposed to just 'X' '''
# abc = [1, 2, 3, 4, 5, 6]
# efg = List(abc)
# print(efg)

''' TEST: Activating List for Node '''
something = xt
if something == xt:
    something = xt()
print(something, type(something))

''' Testing Genetic Program 'runs' # of times '''
runs = 12_400
for _ in range(runs):
    # print(f'RUN_i: >>> {_} <<<')
    gp   = GeneticProgram()
    sarr = gp.selection()
    gp._crossover(sarr)
    # print('PASSED: S1-S2-S3\n')
print (str(runs) + " runs complete!")

''' TEST: Unknown '''
# random_node = nsObj.rand_node()
# truth_value = nsObj.isleft(random_node)
# def test_isleft():
#     rn = nsObj.rand_node()
#     tv = nsObj.isleft(rn)
#     print(rn, tv)

''' TEST: None - is a function '''
def outf(arr=None, out=False):
    """ Print fitness for each population member
    of passed list 'arr'. """
    if arr is None:
        pass
        # arr = strucs
    rv = "|"
    for struc in arr: rv = rv + str(round(measure_fitness(struc), 3)) + "|"
    if out: print(rv)
    return rv

