# Alerta de Revisão Periódica

![Power Automate](https://img.shields.io/badge/Power%20Automate-blue)
![Excel](https://img.shields.io/badge/Excel-green)

##  Descrição

Este repositório documenta um **fluxo do Microsoft Power Automate** responsável por **ler dados de uma tabela do Excel de forma recorrente** e **enviar e-mails automaticamente** quando uma condição definida é atendida.

O projeto é voltado para automações simples e eficazes, como lembretes, notificações e alertas baseados em dados de planilhas.

---

##  Arquitetura do Fluxo

O fluxo segue a seguinte sequência:

1. **Recorrência** – Define a periodicidade de execução do fluxo.
2. **Listar linhas presentes em uma tabela** – Lê os dados de cada linha de uma planilha no Excel.
3. **Aplicar a cada** – Itera sobre cada linha da tabela.
4. **Condição** – Avalia um critério lógico definido pelo usuário.
5. **Enviar um e-mail (V2)** – Dispara o e-mail quando a condição é verdadeira.

<img width="574" height="739" alt="image" src="https://github.com/user-attachments/assets/9558be71-2b80-4156-a29f-3b1a9d1b134d" />

---

##  Detalhamento das Etapas

### 1️) Recorrência
- Gatilho do fluxo.
- Configurável para execução diária, semanal ou em horários específicos.

<img width="888" height="812" alt="image" src="https://github.com/user-attachments/assets/43f9159b-c2ad-469e-a519-91d7fe64bc80" />

### 2️) Listar linhas presentes em uma tabela 
- Conecta-se a um arquivo Excel armazenado no **SharePoint**.
- A planilha deve estar formatada como uma **Tabela**, o nome da tabela servirá como parâmetro para a acão.

<img width="712" height="790" alt="image" src="https://github.com/user-attachments/assets/71e0fbd4-da32-4e95-9d3c-2ba332389910" />

### 3️) Aplicar a cada
- Processa cada linha retornada pela ação anterior.

<img width="727" height="254" alt="image" src="https://github.com/user-attachments/assets/a5a38fef-c5e1-479e-9aff-1ffd27123d2e" />

### 4️) Condição
- Utiliza os dados da coluna **"Prazo Remanescente (Dias)"** para fazer a comparação.

- Avalia regras como:
  - Data igual ou menor ao dia atual

**Caminhos:**
-  Verdadeiro → Executa envio de e-mail
-  Falso → Nenhuma ação

<img width="723" height="569" alt="image" src="https://github.com/user-attachments/assets/623a45f8-c937-42f8-b836-6284eb4efc2f" />

### 5️) Enviar um e-mail (V2)
- Envia mensagens automáticas utilizando dados dinâmicos do Excel.
- Os dados dinâmicos utilizados são respectivamente:
  - **"Document Name"**, o nome do documento
  - **"Document Number"**, o número do documento
  - **"Next Periodic Review Date"**, a data para a revisão do documento
  - **"Prazo Remanescente (Dias)"**, quantidade de dias que faltam para a próxima revisão

<img width="714" height="806" alt="image" src="https://github.com/user-attachments/assets/5d99f4b3-d4f3-4830-aad6-da6747a6c07d" />

---

##  Exemplo de Cenário

- Planilha com coluna **"Prazo Remanescente (Dias)"**
- Fluxo executado diariamente
- Quando a data for igual ao dia atual:
  - Um e-mail de lembrete é enviado automaticamente

---

##  Estrutura do repositório

```text
📦 alerta-revisão-periódica
 ┣ 📄 README.md
