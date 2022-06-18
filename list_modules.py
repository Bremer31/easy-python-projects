import pymem

pm = pymem.Pymem('python version of your system')
modules = list(pm.list_modules())
for module in modules:
    print(module.name)
