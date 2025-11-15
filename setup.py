import sys
import os
from cx_Freeze import setup, Executable

# Ícone e base
icone = "Tela/logo_principal_cortada.ico"
base = "Win32GUI" if sys.platform == "win32" else None

# Arquivos adicionais
arquivos_incluidos = [
    'logo_principal.ico',
    'apresentacao.py',
    'tela_login.py',
    'login.py',
    'tela_recovery.py',
    'recovery.py',
    'cadastro.py',
    'tela_principal.py',
    'principal.py',
    'logo.py',
    'sprites.py',
    'sprites_menu.py',
    'LOGMARKET.db'
]

# Dependências
packages = [
    'PySide6',
    'os',
    'sys',
    'time',
    'dotenv'
]

includes = [
    'dotenv',
    'os',
    'sys',
    'time',
    'PySide6.QtWidgets',
    'PySide6.QtGui',
    'PySide6.QtCore'
]

setup(
    name="LogMarket",
    version="1.1.3",
    description="Terminal de Consulta",
    options={
        "build_exe": {
            "packages": packages,
            "includes": includes,
            "include_files": arquivos_incluidos,
            "excludes": []
        }
    },
    executables=[
        Executable("logmarket.py", icon=icone, base=base)
    ]
)

