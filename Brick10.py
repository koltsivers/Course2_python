"""S = "Строка параметров {0} другой параметр {1} парметр {0}"
print(S)
par1, par2 = 99, "Москва"
s = S.format(par1, par2)
print(s)"""
#-----------------------------------------------------
"""par1, par2 = 99, "Москва"
with open("Brick10", encoding="utf-8") as F:
    S=F.read()
#S = f"Строка параметров {par1} другой параметр {par2} парметр {par1}" Находится в файле Brick10
print(S)
s=S.format(par1=par1, par2=par2)
print(s)"""
#-----------------------------------------------------
from string import Template
with open("Brick10", encoding="utf-8") as F:
    S=F.read()
#print(S)
#S = f"Строка параметров $par1 другой параметр $par2 парметр $par1"
template1=Template(S)
s = template1.safe_substitute({'par1': 99})
print(s)