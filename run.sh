#!/bin/bash

# Nome do ambiente virtual
ENV_NAME=.venv

# Caminho para o arquivo PDF que deseja converter
PDF_FILE=src

# Caminho para o diretório do projeto
PROJECT_DIR=src

# Verifica se o ambiente virtual já existe
if [ ! -d "$ENV_NAME" ]; then
    echo "Criando ambiente virtual..."
    python -m venv $ENV_NAME
fi

# Ativa o ambiente virtual
source $ENV_NAME/bin/activate

# Navega até o diretório do projeto
cd $PROJECT_DIR

# Executa o script de conversão de PDF para MOBI
python app.py "$PDF_FILE"

# Desativa o ambiente virtual
deactivate
