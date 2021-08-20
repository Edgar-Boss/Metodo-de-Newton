from sympy import Symbol
from sympy.parsing.sympy_parser import parse_expr
import math

x=Symbol('x')



expr = "230*x**4+18*x**3+9*x**2-221*x-9"#input("Ingrese la funcion: ")#guarda expresion
y =	parse_expr(expr)#convierte tipo de variable

der = y.diff(x)#deriva

x0 = -0.5#float(input("Ingrese el x0: "))

it=0
tol=1.e-4
it_max=100
x_v = 1
while abs(x_v-x0) > tol and it <= it_max:
	
	it += 1
	print("///////////////////////",it)
	libres=dict(x=x0)   #evalua funcion
	funcs = vars(math)	                                 #evalua en f(n)
	fn=eval(expr, funcs,libres)#guarda resultado

	libres=dict(x=x0)   #evalua funcion derivada
	funcs = vars(math)	                                 #evalua en f'(n)
	fn_der=eval(str(der), funcs,libres)#guarda resultado

	print(fn)
	print(fn_der)
	x_v=x0
	x0 = x0-(fn/fn_der)
	print("x0: ",x0)
	

