#  Passaporte Rota Certa

Aplicação web que simula um **passaporte digital para eventos**, permitindo que participantes coletem **vistos** ao acessar atividades específicas.  
Ideal para feiras, workshops e eventos gamificados.

O projeto é totalmente **front-end**, sem backend, utilizando `localStorage` para persistência de dados.

---

##  Funcionalidades

- Cadastro simples do participante
- Geração de passaporte digital personalizado
- Coleta de vistos via parâmetro na URL
- Barra de progresso automática
- Tela de conclusão ao completar todos os vistos
- Persistência de dados no navegador
- Layout responsivo

---

## 🚀 Como usar

### 1️⃣ Abrir o projeto
Basta abrir o arquivo `index.html` em qualquer navegador.

### 2️⃣ Criar o passaporte
Informe o nome do participante para gerar o passaporte digital.

### 3️⃣ Conceder vistos
Os vistos são concedidos automaticamente ao acessar a página com o parâmetro ?activity=NomeDaAtividade. Um QR Code pode ser utilizado para tal.

Exemplo: index.html?activity=Importacao

- Cada atividade concede **1 visto**
- Atividades duplicadas não são registradas
- O nome da atividade é limitado a 30 caracteres

---

##  Progresso

- Total de vistos padrão: **3**
- Barra de progresso exibida no passaporte
- Ao completar todos os vistos:
  - Mensagem de sucesso
  - Tela final de conclusão 

---

##  Armazenamento

Os dados são salvos no localStorage do navegador, ou seja 

| Chave               | Descrição                 |
| ------------------- | ------------------------- |
| `usuario`           | Nome do participante      |
| `vistos`            | Lista de vistos coletados |
| `conclusaoMostrada` | Controle da tela final    |

---

##  Configurações rápidas

### Alterar número total de vistos
Procurar a constante TOTAL_VISTOS no `index.html`:

```js
const TOTAL_VISTOS = 3;
```

---

##  Tecnologias

- **HTML5** – Estrutura da aplicação
- **CSS3** – Estilização, layout responsivo e animações
- **JavaScript** – Lógica da aplicação e interatividade
- **LocalStorage** – Persistência de dados no navegador
