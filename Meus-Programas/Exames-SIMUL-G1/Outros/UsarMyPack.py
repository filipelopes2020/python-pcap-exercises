import sys

# caminho onde está o package
sys.path.append(r"D:\OneDrive\Documentos\REPOS\PYTHON\Curso_Python-5H\Meus-Programas\packages")

#from PackT import funcX, constY     # expor a função e o modulo
from PackP.ModuleZ import funcX, constY	


print(funcX())
print(constY)

print(__name__)


