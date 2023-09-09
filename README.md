![clipboard.png](image/Amazon-Kindle-app-Mac.jpeg)

# Conversor de PDF para MOBI

## Sumário

- [Introdução](#introdução)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Sistemas Operacionais Principais](#sistemas-operacionais-principais)
- [Propósito](#propósito)
- [Baixando as libs](#baixando-as-libs)
- [Ambiente Isolado](#ambiente-isolado)
- [Bibliotecas Usadas](#bibliotecas-usadas)
- [Arquitetura de Pasta e Arquivos](#arquitetura-de-pasta-e-arquivos)
- [Princípios SOLID Utilizados](#princípios-solid-utilizados)
- [Programação Orientada a Objetos](#programação-orientada-a-objetos)
- [Como Usar](#como-usar)

## Introdução

Este projeto é um conversor de arquivos PDF para o formato MOBI, amplamente usado em dispositivos Kindle. O objetivo principal é fornecer uma ferramenta simples para converter documentos PDF em um formato compatível com leitores de e-books Kindle.

## Tecnologias Utilizadas

- Python
- Calibre (ebook-convert)
- PyQt6
- BeautifulSoup4 (bs4)
- Pillow (PIL)
- Sistema Operacional Linux (Ubuntu)

## Pré-requisitos

Antes de usar este projeto, é necessário ter os seguintes pré-requisitos instalados:

- Python 3.x
- Calibre
- PyQt6
- BeautifulSoup4
- Pillow

## Sistemas Operacionais Principais

Este projeto foi desenvolvido e testado principalmente no seguinte sistema operacional:

- Ubuntu Linux

## Propósito

O propósito deste projeto é oferecer uma maneira fácil e eficaz de converter arquivos PDF em MOBI para que eles possam ser lidos em dispositivos Kindle ou em aplicativos de leitura compatíveis com MOBI.

## Baixando as libs

### Introdução

O arquivo `requirements.txt` é uma maneira eficaz de gerenciar as dependências de um projeto Python. Ele permite que você especifique as bibliotecas e suas versões exatas que são necessárias para garantir que o projeto seja executado de forma consistente em diferentes ambientes. O processo de utilização do `requirements.txt` envolve a criação, atualização e instalação das dependências listadas no arquivo.
#### Passo 1: Criando o arquivo `requirements.txt` 
1. Crie um arquivo chamado `requirements.txt` na raiz do seu projeto. 
2. Liste todas as bibliotecas que seu projeto depende, uma por linha, no seguinte formato:

```makefile
biblioteca==versão
```

Por exemplo, para incluir a biblioteca `requests` na versão `2.26.0`, adicione a seguinte linha:

```makefile
requests==2.26.0
``` 
3. Adicione todas as outras bibliotecas utilizadas no seu projeto, especificando suas versões conforme necessário.
#### Passo 2: Atualizando o arquivo `requirements.txt` 
1. À medida que você adiciona ou atualiza bibliotecas em seu projeto, certifique-se de manter o arquivo `requirements.txt` atualizado. 
2. Sempre especifique versões exatas das bibliotecas para garantir a consistência em diferentes ambientes. Você pode usar comandos como `pip freeze` para gerar uma lista das bibliotecas atualizadas em seu ambiente virtual e copiá-las para o arquivo `requirements.txt`.
#### Passo 3: Instalando as dependências 
1. Antes de executar o projeto em um novo ambiente, certifique-se de que o Python e o gerenciador de pacotes `pip` estejam instalados. 
2. Crie um ambiente virtual Python usando `venv`, `virtualenv` ou outro método de sua escolha:

```bash
python -m venv myenv
source myenv/bin/activate  # Ative o ambiente virtual (Linux/macOS)
``` 
3. Para instalar todas as dependências listadas no arquivo `requirements.txt`, execute o seguinte comando:

```bash
pip install -r requirements.txt
```

Isso garantirá que todas as bibliotecas e suas versões correspondentes sejam instaladas no ambiente virtual.

#### Passo 4: Executando o Projeto

Agora que todas as dependências estão instaladas no ambiente virtual, você pode executar o projeto de forma consistente em qualquer ambiente. Ative o ambiente virtual, navegue até a raiz do projeto e execute o código conforme necessário.

```bash
source myenv/bin/activate  # Ative o ambiente virtual (Linux/macOS)
cd /caminho/para/seu/projeto
python seu_script.py
```

Isso garante que seu projeto funcione com as versões específicas das bibliotecas listadas no `requirements.txt`, proporcionando uma experiência consistente para você e outros colaboradores.---

Você pode criar um arquivo `utilizando_requirements.md` com essas informações e incluí-lo na documentação do seu projeto. Este guia ajudará a garantir que as dependências do seu projeto sejam gerenciadas de forma eficaz, facilitando o desenvolvimento e a colaboração.

## Ambiente Isolado

É altamente recomendável configurar um ambiente virtual Python para isolar este projeto das bibliotecas globais do sistema. Você pode usar `venv` ou `virtualenv` para criar um ambiente virtual.

```bash
python3 -m venv .venv
source .venv/bin/activate  # Ativar o ambiente virtual
```

## Bibliotecas Usadas

Este projeto utiliza várias bibliotecas Python, incluindo:
- Calibre: Para realizar a conversão de PDF para MOBI.
- PyQt6: Requerido pelo Calibre.
- BeautifulSoup4 (bs4): Utilizado para análise HTML.
- Pillow (PIL): Utilizado para manipulação de imagens.
## Arquitetura de Pasta e Arquivos 
- `conversor_pdf_mobi.py`: O script principal para a conversão de PDF para MOBI. 
- `converted_mobi/`: Pasta onde os arquivos MOBI resultantes são salvos.
- Outros arquivos e pastas relacionados ao ambiente virtual, se configurado.
## Princípios SOLID Utilizados

Neste projeto, seguimos os princípios SOLID da seguinte maneira: 
- **Single Responsibility Principle (SRP)** : O código do script `conversor_pdf_mobi.py` é focado na conversão de PDF para MOBI, mantendo uma única responsabilidade. 
- **Open/Closed Principle (OCP)** : O código pode ser estendido para suportar mais funcionalidades ou tipos de conversão sem modificar a lógica existente. 
- **Liskov Substitution Principle (LSP)** : Não aplicável neste contexto. 
- **Interface Segregation Principle (ISP)** : Não aplicável neste contexto. 
- **Dependency Inversion Principle (DIP)** : O código depende de abstrações (ex: `subprocess.run`) em vez de implementações concretas.
## Programação Orientada a Objetos

O projeto utiliza a programação orientada a objetos (OOP) para organizar e encapsular a funcionalidade de conversão de PDF para MOBI. 
- `PDFConverter`: Uma classe que representa um conversor de PDF para MOBI, encapsulando a lógica de conversão. 
- `main()`: A função principal que interage com o usuário para fornecer o caminho do arquivo PDF a ser convertido.
## Como Usar

Para iniciar a conversão de um arquivo PDF para MOBI, siga estas etapas: 
1. Certifique-se de que todos os pré-requisitos estejam instalados, incluindo Python 3.x, Calibre, PyQt6, BeautifulSoup4 e Pillow. 
2. Clone ou baixe este repositório em seu sistema. 
3. Abra um terminal ou prompt de comando e navegue até o diretório onde você baixou/clonou o projeto. 
4. Ative um ambiente virtual Python, se desejar isolar o projeto do ambiente global.

```bash
source myenv/bin/activate  # Substitua "myenv" pelo nome do seu ambiente virtual, se aplicável
```
 
1. Execute o script `conversor_pdf_mobi.py` digitando o seguinte comando:

```bash
python conversor_pdf_mobi.py /caminho/para/seu/arquivo.pdf
```

Substitua `/caminho/para/seu/arquivo.pdf` pelo caminho completo do arquivo PDF que você deseja converter. 
1. Aguarde o processo de conversão ser concluído. O arquivo MOBI resultante será salvo na pasta `converted_mobi/`.

Agora você pode transferir o arquivo MOBI para seu dispositivo Kindle ou usar um aplicativo de leitura de e-books compatíveis com o formato MOBI para ler o livro no seu dispositivo.

**Nota:**  Certifique-se de que o Calibre esteja instalado e configurado corretamente em seu sistema, juntamente com suas dependências, para garantir que a conversão ocorra sem problemas.
## Automatização

Você pode automatizar o processo de conversão usando o script `run.sh`. Certifique-se de dar permissão de execução ao script com o seguinte comando:

```bash
chmod +x run.sh
```

Depois, execute o script para converter um arquivo PDF em MOBI.

```bash
./run.sh
```

Este script realiza todas as etapas, desde a criação e ativação do ambiente virtual até a execução do projeto.

```javascript
Com estas adições, o `README.md` inclui instruções claras sobre como usar o projeto, incluindo a automação do processo com o script `run.sh`. Certifique-se de substituir `/caminho/para/seu/arquivo.pdf` pelo caminho real do arquivo PDF que deseja converter e `/caminho/para/seu/projeto/src` pelo caminho real do diretório do projeto.
```