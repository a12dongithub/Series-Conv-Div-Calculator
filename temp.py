from sympy import *
from sympy.parsing.sympy_parser import parse_expr
x = Symbol('x')
input("Welcome to Convergence and Divergence tester. Press Enter to continue.....")
task = input("Do you want to test for series or sequence :")
functionx = input('Please Enter the general term of your series or sequence where "x" is the parameter :')
functionx1 = functionx.replace('x', '(x+1)')
function = parse_expr(functionx)
function1 = parse_expr(functionx1)
def Test1(test1):
    t1 = limit(test1, x, oo)
    if t1 == 0:
        print('Basic Limit Test Valid(Could be Convergent)')
    else:
        print('Divergent')

def Test2(test2):
    t2 = integrate(test2, (x ,1 ,oo))
    if t2 == oo:
        print("Divergent Using Integration Test")
    elif t2 == -oo:
        print("Divergent Using Integration Test")
    else:
        print("Convergent Using Integration Test")

def Test3(test3,test33):
    t3 = limit(test33 / test3, x, oo)
    if t3 < 1:
        print("Convergent Using D'Alember's Test")
    elif t3 == 1:
        print("D'Alember's Test Fails")
    else:
        print("Divergent USing D'Alember's Test")
        
def Test4(test4, test44):
    t444 = 'x'
    t44 = parse_expr(t444)
    t4 = limit((t44*(test4-test44)/test44), x, oo)
    if t4 > 1:
        print("Convergent Using Raabe's Test")
    elif t4 == 1:
        print("Raabe's Test Fails")
    else:
        print("Divergent Using Raabe's Test")

def Test5(test5,test55): 
    t555 = 'x'
    t55 = parse_expr(t555)
    t5 = limit(t55*log(test5/test55), x, oo)
    if t5 > 1:
        print('Convergent Using Logarithmic Test')
    elif t5 == 1:
        print('Logarithmic Test Fails')
    else:
        print('Divergent Using Logarithmic Test')
        
def Test6(test6):
    t6 = limit((test6)**(1/x), x , oo)
    if t6 < 1:
        print("Convergent Using Cauchy's Root Test")
    elif t6 == 1:
        print("Cauchy's Root Test Fails")
    else:
        print("Divergent Using Cauchy's Root Test")

task = task.lower()
try:
    if task == "sequence":
        seq1 = limit(function, x , oo)
        if seq1 == oo:
            print("Divergent Sequence")
        elif seq1 == -oo:
            print("Divergent Sequence")
        else:
            print("Convergent Sequence")   
    elif task == "series":
        Test1(function)
        Test2(function)
        Test3(function,function1)
        Test4(function,function1)
        Test5(function,function1)
        Test6(function)
    else:    
        print("Invalid input")
except:
    print("oscillatory function")
             
input('press enter to exit........')
        










