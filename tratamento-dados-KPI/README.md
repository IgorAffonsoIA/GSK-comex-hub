# Tratamento e validação de Dados em Planilhas Excel para o KPI

![Python](https://img.shields.io/badge/Python-blue)
![Excel](https://img.shields.io/badge/Excel-green)

##  Descrição

Este repositório contém um **script em Python** desenvolvido para realizar o **tratamento e validação de dados em planilhas Excel**.  
O objetivo é automatizar verificações de qualidade dos dados, identificar inconsistências e padronizar informações antes de seu uso em análises, relatórios ou processos operacionais.

O projeto é especialmente útil como etapa de **pré-processamento de dados**, reduzindo erros manuais e aumentando a confiabilidade das informações.

---

##  Arquitetura do Script

O fluxo do script segue a seguinte sequência:

1. Seleção do arquivo Excel pelo usuário    
2. Substituição de valores nulos  
3. Validação de colunas de data  
4. Validação da coluna *Freight Forward*   
5. Salvamento da planilha tratada  

---

##  Detalhamento das Etapas

### 1️) Seleção do Arquivo
- Abre uma janela para o usuário selecionar um arquivo Excel.
- Suporta arquivos `.xlsx` e `.xls`.

### 2️) Substituição de Valores Nulos
- Todos os valores `NaN` são substituídos por **string vazia**.
- Garante consistência no tratamento dos dados.

### 3️) Validação de Datas
- Identifica automaticamente colunas cujo nome contenha o termo **\"data\"**.
- Para cada valor:
  - Tenta converter para `datetime`
  - Verifica se o ano está entre **1900 e 2100**
- Datas inválidas são reportadas com:
  - Linha
  - Coluna
  - Valor
  - Motivo do erro

### 4️) Validação de Freight Forward
- Valida se a coluna **`Freight Forward`** contém apenas valores permitidos.
- Valores válidos:
  - CARGOLUX  
  - DHL  
  - Expeditors  
  - KN  
  - Lufttansa  
  - Yusen  

### 5️) Salvamento do Arquivo
- A planilha é salva **no mesmo arquivo**, já com os dados tratados.

---

##  Exemplo de Uso

- Usuário recebe uma planilha com dados operacionais
- Executa o script
- O sistema:
  - Corrige valores nulos
  - Aponta datas inválidas
  - Identifica valores incorretos em *Freight Forward*
- A planilha final fica pronta para uso ou análise

---

##  Estrutura do repositório

```text
📦 tratamento-dados-KPI
 ┣ 📄 README.md
 ┣ 📄 Tratamento.py
 ┣ 📄 requirements.txt

