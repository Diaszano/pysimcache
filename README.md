# PySimCache

Simulador de Caches implementado em Python como parte do trabalho acadêmico de Arquitetura e Organização de Computadores II.

## Descrição

O **PySimCache** é um simulador parametrizável de caches que permite configurar aspectos como número de conjuntos, tamanho do bloco, associatividade e política de substituição. Ele aceita parâmetros via linha de comando e simula o comportamento de uma cache endereçada a bytes, utilizando um arquivo de entrada com endereços de 32 bits.

## Funcionalidades

- Simulação de diferentes configurações de cache:
  - Número de conjuntos (`nsets`)
  - Tamanho do bloco (`bsize`)
  - Associatividade (`assoc`)
  - Políticas de substituição:
    - **Random (R)**
    - **FIFO (F)** (bônus)
    - **LRU (L)** (bônus)
- Relatório de estatísticas de desempenho:
  - Número total de acessos
  - Taxa de hits e misses (compulsórios, capacidade e conflito)
- Suporte a dois formatos de saída (detalhado ou padrão).

## Linha de Comando

O simulador é executado com a seguinte sintaxe:

```
cache_simulator <nsets> <bsize> <assoc> <substituição> <flag_saida> <arquivo_de_entrada>
```

- `nsets`: Número de conjuntos na cache.
- `bsize`: Tamanho do bloco (em bytes).
- `assoc`: Grau de associatividade (número de vias por conjunto).
- `substituição`: Política de substituição (`R` para Random, `F` para FIFO, `L` para LRU).
- `flag_saida`: Define o formato de saída (`0` para formato livre, `1` para formato padrão).
- `arquivo_de_entrada`: Arquivo binário contendo os endereços (32 bits em formato big endian).

## Exemplo de Execução

Considerando o arquivo de entrada `bin_100.bin` e uma cache com 256 conjuntos, blocos de 4 bytes, associatividade de 1 via, política de substituição Random e saída no formato padrão:

```
cache_simulator 256 4 1 R 1 bin_100.bin
```

Resultado esperado:

```
100, 0.92, 0.08, 1.00, 0.00, 0.00
```

## Arquivo de Entrada

O arquivo de entrada contém endereços em formato binário, cada um com 32 bits. Exemplos de arquivos de teste disponíveis:

- [`bin_100.bin`](./address/bin_100.bin) (100 endereços)
- [`bin_1000.bin`](./address/bin_1000.bin) (1000 endereços)
- [`bin_10000.bin`](./address/bin_10000.bin) (10.000 endereços)
- [`vortex.in.sem.persons.bin`](./address/vortex.in.sem.persons.bin) (186.676 endereços)

## Como Compilar e Executar

Certifique-se de ter o [Python 3.12](https://www.python.org/) e o [Poetry](https://python-poetry.org/) instalados. Caso não tenha, siga estes tutoriais:

- [Instalando Python](https://realpython.com/installing-python/)
- [Instalando Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)

### Passos para Executar

1. Clone este repositório:
    ```bash
    git clone https://github.com/Diaszano/pysimcache
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd pysimcache
    ```
3. Ative o ambiente virtual:
    ```bash
    poetry shell
    ```
4. Compile o projeto:
    ```bash
    poetry build
    ```
5. Execute o simulador:
   ```bash
   cache_simulator <nsets> <bsize> <assoc> <substituição> <flag_saida> <arquivo_de_entrada>
   ```

## Funcionalidades Extras

- Implementação das políticas FIFO e LRU para substituição de blocos.

## Autores

- **Lucas Dias**
- **Luis Eduardo Rasch**
