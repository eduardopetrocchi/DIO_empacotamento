# Address Corrector

This is a simple Python module for address correction. It provides the `substituicao()` function, which replaces all occurrences of '\\' with '/' in an address.

## Installation

You can install the module using the following pip command:

```bash
pip install corretor_de_enderecos
```

## Usage

The `substituicao` function can be used as follows:

```python
from corretor_de_enderecos import substituicao

endereco = "C:\\Users\\MeuUsuario\\Desktop"
endereco_corrigido = substituicao(endereco)
print(f"Original address: {endereco}")
print(f"Corrected address: {endereco_corrigido}")
```

Output:
```
Original address: C:\\Users\\MeuUsuario\\Desktop
Corrected address: C:/Users/MeuUsuario/Desktop
```

## Contributions

Contributions are welcome! If you want to contribute to the development of this module, follow the steps below:

1. Fork the repository.
2. Create a branch: `git checkout -b feature/new-feature`.
3. Make changes and commit.
4. Push to the branch: `git push origin feature/new-feature`.
5. Open a Pull Request.

## License

Distributed under the [MIT License](LICENSE).

## Authors

- [Eduardo Petroccchi](https://www.github.com/eduardopetrocchi)

I hope this README is helpful and provides clear information about the usage and contribution to the Address Corrector module.