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
- A planilha deve estar formatada como uma **Tabela**, o nome da tabela servirá para identificar a tabela que será utilizada no fluxo.

<img width="712" height="790" alt="image" src="https://github.com/user-attachments/assets/71e0fbd4-da32-4e95-9d3c-2ba332389910" />

### 3️) Aplicar a cada
- Processa cada linha retornada pela ação anterior.

<img width="727" height="254" alt="image" src="https://github.com/user-attachments/assets/a5a38fef-c5e1-479e-9aff-1ffd27123d2e" />

### 4️) Condição
- Utiliza os dados da coluna **"Prazo Remanescente (Dias)"** para fazer a comparação.

- Avalia regras como:
  - Data igual ou menor a 90, 60, 30 ou 7 dias.

**Caminhos:**
-  Verdadeiro → Executa envio de e-mail
-  Falso → Nenhuma ação

<img width="723" height="569" alt="image" src="https://github.com/user-attachments/assets/623a45f8-c937-42f8-b836-6284eb4efc2f" />

### 5️) Enviar um e-mail (V2)
- Envia mensagens automáticas utilizando dados dinâmicos extraídos da planilha do Excel.
- Os dados dinâmicos utilizados são respectivamente:
  - **"Document Name"**, o nome do documento
  - **"Document Number"**, o número do documento
  - **"Next Periodic Review Date"**, a data para a revisão do documento
  - **"Prazo Remanescente (Dias)"**, quantidade de dias que faltam para a próxima revisão

<img width="714" height="806" alt="image" src="https://github.com/user-attachments/assets/5d99f4b3-d4f3-4830-aad6-da6747a6c07d" />

---

##  Como acessar o fluxo

### 1) Baixar o arquivo `.zip`
Faça o download do arquivo **`fluxo-alerta-revisão-periódica.zip`**, localizado nesta pasta do repositório.

<img width="307" height="158" alt="image" src="https://github.com/user-attachments/assets/bdb0544f-429e-4c8c-a00f-6b17b94402d3" />

### 2) Acessar o Power Automate
Acesse o **Power Automate** pelo navegador e autentique-se com sua conta.

### 3) Importar o fluxo
1. No menu lateral, acesse a secção **Meus Fluxos**.  
2. Clique em **Importar** e selecione a opção **Importar Pacote (zip)**.
<img width="246" height="113" alt="image" src="https://github.com/user-attachments/assets/1b902b4c-9ace-4262-986a-ff2ec95025d0" />

### 4) Fazer upload do pacote e configurar as conexões
1. Faça o upload do arquivo `.zip` baixado anteriormente.  
2. Configure as conexões necessárias conforme solicitado pelo Power Automate.
<img width="1207" height="678" alt="image" src="https://github.com/user-attachments/assets/b5bffa3e-da03-4812-8b95-f5a44bd3b246" />

Na seção **Examinar conteúdo do pacote**, selecione as **configurações de importação** mais adequadas ao seu cenário (por exemplo, criar um novo fluxo ou atualizar um existente).

<img width="483" height="276" alt="image" src="https://github.com/user-attachments/assets/37b0cd73-2a38-48d3-a7ac-425868a3c014" />

### 5) Salve o fluxo
1. Após o fluxo ser importado, abra o mesmo e o salve
2. O fluxo aparece-rá nos na secção "Meus Fluxos" em "Compartilhados Comigo"

---

##  Estrutura do repositório

```text
📦 alerta-revisão-periódica
 ┣ 📄 README.md
 ┣ 📄 fluxo-alerta-revisão.zip
