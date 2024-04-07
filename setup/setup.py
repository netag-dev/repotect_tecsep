from cx_Freeze import setup, Executable
import sys
import os

# Obtém o caminho absoluto para o diretório de imagens
img_path = os.path.abspath("../img")

# Define as opções para a criação do executável
build_exe_options = {
    "packages": ["os"],
    "includes": ["PyQt5","fitz"],
    # Inclui o diretório de imagens
    "include_files": [(img_path, "img")]
}

icon_file = "icon.ico"

# Define a base dependendo do sistema operacional
base = "Console"
#if sys.platform == "win32":
#    base = "Win32GUI"

# Configuração do setup
setup(
    name="Meu App",
    version="0.1",
    description="Minha 1 Aplicação!",
    options={"build_exe": build_exe_options},
    executables=[Executable("Run.py", base=base,icon=icon_file)]
)
