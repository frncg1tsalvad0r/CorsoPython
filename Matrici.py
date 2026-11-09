import sympy as sy  # type: ignore[import-untyped]

sy.init_printing()

M = sy.Matrix([[1,2], [3,4]])

b = sy.Matrix([3,2])
P = M*M

x = M.LUsolve(b)
print(M.inv())
print(x)