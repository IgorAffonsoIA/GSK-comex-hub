# Power Automate – Envio Automático de E-mails

![Power Automate](https://img.shields.io/badge/Power%20Automate-blue)
![Excel](https://img.shields.io/badge/Excel-green)

##  Descrição

Este repositório documenta um **fluxo do Microsoft Power Automate** responsável por **ler dados de uma tabela do Excel de forma recorrente** e **enviar e-mails automaticamente** quando uma condição definida é atendida.

O projeto é voltado para automações simples e eficazes, como lembretes, notificações e alertas baseados em dados de planilhas.

---

##  Arquitetura do Fluxo

O fluxo segue a seguinte sequência:

1. **Recorrência** – Define a periodicidade de execução do fluxo.
2. **Listar linhas presentes em uma tabela** – Lê os dados de uma planilha do Excel.
3. **Aplicar a cada** – Itera sobre cada linha da tabela.
4. **Condição** – Avalia um critério lógico definido pelo usuário.
5. **Enviar um e-mail (V2)** – Dispara o e-mail quando a condição é verdadeira.

---

##  Detalhamento das Etapas

### 1️) Recurrence
- Gatilho do fluxo.
- Configurável para execução diária, semanal ou em horários específicos.

<img width="888" height="812" alt="image" src="https://github.com/user-attachments/assets/43f9159b-c2ad-469e-a519-91d7fe64bc80" />

### 2️) Listar linhas presentes em uma tabela 
- Conecta-se a um arquivo Excel armazenado no **OneDrive** ou **SharePoint**.
- A planilha deve estar formatada como **Tabela**.

### 3️) Aplicar a cada
- Processa cada linha retornada pela ação anterior.

### 4️) Condição
- Avalia regras como:
  - Data igual ao dia atual

**Caminhos:**
-  Verdadeiro → Executa envio de e-mail
-  Falso → Nenhuma ação

### 5️) Enviar um e-mail (V2)
- Envia mensagens automáticas utilizando dados dinâmicos do Excel.

---

##  Exemplo de Cenário

- Planilha com coluna **Data de Vencimento**
- Fluxo executado diariamente
- Quando a data for igual ao dia atual:
  - Um e-mail de lembrete é enviado automaticamente
