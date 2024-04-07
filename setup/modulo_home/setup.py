from cx_Freeze import setup, Executable
import sys

build_exe_options = {"packages": ["os","PyQt5","reportlab","fitz"], "includes": ["os","PyQt5","reportlab","fitz","psycopg2"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"


setup(
    name="TecPro",
    version="1.0",
    description="Software de Geração de Report",
    options={"build_exe": build_exe_options},
    executables=[Executable("C:\\Users\\Acer\\Documents\\repotec\\setup\\modulo_home\\login.py", base=base, icon="icon.ico")]
)