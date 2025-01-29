# 3D Print Log
Este script Python lista arquivos em um diretório, organiza-os em um formato estruturado e salva a saída em um arquivo de texto. É particularmente útil para gerenciar arquivos de impressão 3D (por exemplo, .stl, .gcode, .obj) e fornece um resumo do número total de arquivos e o número total de arquivos a serem impressos.

## Funcionalidades
- Lista arquivos em um diretório e seus subdiretórios.
- Ignora arquivos com extensões específicas (por exemplo, .txt, .py).
- Organiza os arquivos em uma estrutura hierárquica.
- Salva a saída em um arquivo de texto (impressao_3d.txt).
- Fornece um resumo do número total de arquivos e o número total de arquivos a serem impressos.
- Inclui um menu para interação fácil.

## Arquivos no Repositório
- 3DPrintLog.py: O script Python.
- 3DPrintLog.exe: O arquivo executável (para usuários que não têm o Python instalado).

## Como Usar

### Rodando o Script Python (3DPrintLog.py)

Pré-requisitos:
1. Certifique-se de ter o Python instalado. Você pode baixá-lo em python.org.

Passos:
1. Clone este repositório ou baixe o arquivo 3DPrintLog.py.
2. Clique no arquivo para iniciar-lo
3. Siga o menu na tela para iniciar o processo ou sair.

Saída:
1. O script gerará um arquivo chamado impressao_3d.txt no mesmo diretório.
2. O terminal exibirá uma mensagem de sucesso e aguardará você pressionar uma tecla antes de fechar.

### Rodando o Arquivo Executável (3DPrintLog.exe)

Pré-requisitos:
1. Não é necessário instalar o Python. O arquivo .exe é um executável independente.

Passos:
1. Baixe o arquivo 3DPrintLog.exe deste repositório.
2. Dê um duplo clique no arquivo .exe para executá-lo.
3. Siga o menu na tela para iniciar o processo ou sair.

Saída:
O programa gerará um arquivo chamado impressao_3d.txt no mesmo diretório do arquivo .exe.
O terminal exibirá uma mensagem de sucesso e aguardará você pressionar uma tecla antes de fechar.


```
folder1
    1x file1.stl
    2x file2.obj
folder2
    1x file3.gcode

Resumo:
Total de tipos de arquivos: 3
Total de arquivos a serem impressos: 4
Construindo o Executável (Opcional)
```

## Se você quiser construir o arquivo .exe por conta própria ou depois de alguma mudança no .py:


1. Instale o PyInstaller:
```
pip install pyinstaller
```
2. Navegue até o diretório do script:

```
cd caminho\para\diretório
```
3. Construa o executável:

```
pyinstaller --onefile 3DPrintLog.py
```
4. O arquivo .exe será localizado na pasta dist.

## Licença
Este projeto está licenciado sob a Licença MIT.

## Contribuindo
Se você deseja contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Suporte
Se você encontrar algum problema ou tiver dúvidas, abra uma issue no GitHub.
