"""import modules
print(__name__)""" #to check module

"""x=int(input("Enter a number: "))
modules.checkfun(x)"""

"""check=modules.checkfun
check(9)"""

#to import only the function not the full module
"""from modules import checkfun  

checkfun(9)"""

#to change module name
"""import modules as mod

mod.checkfun(1)"""

#to change function name
"""from modules import checkfun as check
check(0)"""

#default modules in python
import platform

print(platform.processor())
print(platform.python_compiler())
print(platform.system())

