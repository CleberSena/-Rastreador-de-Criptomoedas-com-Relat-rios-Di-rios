import sys
import os
from cx_Freeze import setup, Executable

# Definir o que deve ser incluído na pasta final

# Saida de arquivos
configuracao = Executable(
    script='app.py',
    icon='icon.ico'
)
# Configurar o executável
setup(
    name='Rastreador de Criptomoedas',
    version='1.0',
    description='Este programa automatizar rastreia os preços do Bitcoin usando uma API de mercado de criptomoedas (por exemplo, CoinGecko ou CoinMarketCap) e que, ao iniciar pede para o usuário enviar um e-mail quando ele cair abaixo de um certo valor',
    author='Cleber W. Sena',
    options={'build_exe':{        
        'include_msvcr': True
    }},
    executables=[configuracao]
)