"""
Módulo para correção de endereços.

Este módulo fornece a função `substituicao()`,
que substitui todas as ocorrências de '\\' por '/' em um endereço.

Exemplo de uso:

```python
from corretor_de_enderecos import substituicao

endereco = "C:\\Users\\MeuUsuario\\Desktop"
endereco_corrigido = substituicao(endereco)
print(f"Endereço original: {endereco}")
print(f"Endereço corrigido: {endereco_corrigido}")

# Saída:
# Endereço original: C:\\Users\\MeuUsuario\\Desktop
# Endereço corrigido: C:/Users/MeuUsuario/Desktop
"""


def substituicao(endereco):
    """
    Substitui todas as ocorrências de '\\' por '/' em um endereço.

    Args:
        endereco: O endereço que contém as barras invertidas.

    Returns:
        O endereço com as barras invertidas substituídas por barras normais.
    """
    endereco_correto = endereco.replace("\\", "/")
    return endereco_correto
