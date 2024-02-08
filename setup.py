"""
corretor_de_enderecos - Módulo para correção de endereços

Este módulo oferece a funcionalidade de correção de endereços, substituindo todas as ocorrências
de '\\' por '/' em um endereço.

Exemplo de uso:

```python
from correcao_endereco import substituicao

endereco = "C:\\Users\\MeuUsuario\\Desktop"
endereco_corrigido = substituicao(endereco)
print(f"Endereço original: {endereco}")
print(f"Endereço corrigido: {endereco_corrigido}")




from setuptools import setup

Para obter mais detalhes e informações sobre o módulo, consulte a documentação no GitHub:
https://github.com/eduardopetrocchi/DIO_empacotamento

Autor: Eduardo Petrocchi
Email: eduardo.petrocchi@gmail.com
License: MIT
"""

from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="corretor_de_endereco",
    version="1.1",
    author="Eduardo Petroccchi",
    author_email="eduardo.petrocchi@gmail.com",
    description="Um módulo Python simples para corrigir endereços substituindo '\\' por '/'.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eduardopetrocchi/DIO_empacotamento",
    install_requires=requirements,
    packages=find_packages(),
    python_requires=">=3.6",
)

