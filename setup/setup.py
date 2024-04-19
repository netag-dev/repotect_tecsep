import sys
import os
from cx_Freeze import setup , Executable

#ADD FILES
files = ['icon.ico']
path = os.path.abspath('img')
#Target
target = Executable(
    script="Run.py",
    base="Win32GUI",
    icon="icon.ico"
)
#setup CX_Freeze
setup(
    name="Repotect Tecsep",
    version="1.9",
    description="Sistema de Gestão de Reportes",
    author="NETAG DEVELOPERS",
    options = {'build_exe': {'include_files': path}},
    executables = [target]
)
