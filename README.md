# 🌱 Painel Administrativo ONG

**Versão 1.1.0**

Sistema administrativo interno para ONG, com painel protegido por login, calendário editável de eventos e interface moderna em tema dark com detalhes neon roxo.

---

## 👨‍💻 Desenvolvimento

Este projeto está sendo desenvolvido em equipe (3 integrantes), com auxílio de ferramentas de inteligência artificial (DeepSeek) para:

- Auxílio na geração e boas práticas de código Python/Django
- Documentação e comentários explicativos
- Depuração e correção de bugs
- Criação do tema visual dark + neon

Toda a lógica de negócio, estrutura do banco de dados e fluxos do sistema estão sendo projetados e validados pelo time.

---

## ✨ Funcionalidades

### 🔐 Sistema de Login
- Tela de login customizada com tema dark neon
- Senha com hash (usa hasher nativo do Django)
- Bloqueio após 5 tentativas falhas (5 minutos)
- Sessão protegida por cookie

### 📊 Painel Administrativo
- Tela inicial com boas-vindas ao administrador
- Topbar com navegação entre seções
- Card de acesso rápido ao calendário
- Link de logout

### 📅 Calendário Editável
- Visualização mensal com navegação entre meses
- Criação de eventos por clique no dia
- Edição e exclusão de eventos
- **Cores por categoria:**

| Cor | Significado |
|-----|-------------|
| 🟢 Verde | Aceita doação |
| 🔵 Azul | Aceita voluntariado |
| 🟣 Roxo | Aceita ambos |

- Painel lateral de edição com campos:
  - Nome do evento
  - Descrição
  - Data
  - Horário de início e fim
  - Checkboxes de doação/voluntariado

### 🎨 Design
- Tema dark com accent neon roxo (`#a855f7`)
- Efeitos de glow sutis em hover/focus
- Cards com borda neon animada
- Layout responsivo (mobile-friendly)
- Tipografia Inter

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|------------|-----|
| Python 3.11+ | Linguagem principal |
| Django 6.1 | Framework web |
| MySQL 8.4 | Banco de dados principal |
| PyMySQL | Driver de conexão do banco |
| python-dotenv | Proteção de credenciais (.env) |
| HTML5 + CSS3 | Interface |
| JavaScript (puro) | Interatividade do calendário |
| Inter (Google Fonts) | Tipografia |
| Git + GitHub | Versionamento |

---

## 🚀 Instalação e Configuração

### Pré-requisitos

- Python 3.11 ou superior
- MySQL Server 8.4+ (em execução local)
- Git

### Passo a passo

```bash
# 1. Clonar o repositório
git clone https://github.com/ShiHiro231/Meu-projeto.git
cd Meu-projeto

# 2. Criar e ativar o ambiente virtual
python -m venv venv
venv\Scripts\activate          # Windows CMD
.\venv\Scripts\Activate.ps1    # Windows PowerShell
source venv/bin/activate        # Mac/Linux

# 3. Instalar dependências
pip install -r requirements.txt
```

### Configuração do Banco e Segurança

O projeto utiliza variáveis de ambiente para proteger os dados do banco.

1. Renomeie o arquivo `.env.example` para `.env`.
2. Abra o `.env` e preencha com as credenciais do seu MySQL local:
   ```env
   DB_NAME=projeto_ong
   DB_USER=projeto
   DB_PASSWORD=projeto
   DB_HOST=localhost
   DB_PORT=3306
   ```

3. Crie o banco e o usuário no MySQL (via terminal ou Workbench):
   ```sql
   CREATE DATABASE IF NOT EXISTS projeto_ong CHARACTER SET utf8mb4;
   CREATE USER IF NOT EXISTS 'projeto'@'localhost' IDENTIFIED BY 'projeto';
   GRANT ALL PRIVILEGES ON projeto_ong.* TO 'projeto'@'localhost';
   FLUSH PRIVILEGES;
   ```

4. Rode as migrações para criar as tabelas:
   ```bash
   python manage.py migrate
   ```

---

## 👤 Criar Administrador

O painel usa um modelo `Administrador` customizado. Para criar o primeiro acesso, rode:

```bash
python manage.py shell -c "from administrador.models import Administrador; from django.contrib.auth.hashers import make_password; Administrador.objects.create(nome='Admin', login='admin', senha=make_password('admin123')); print('Admin criado!')"
```

**Login padrão:** `admin` | **Senha:** `admin123`
> ⚠️ **Importante:** altere a senha em produção!

---

## ▶️ Executar o Sistema

```bash
python manage.py runserver
```

Acesse no navegador: `http://127.0.0.1:8000/administrador/login/`

---

## 🔗 Rotas do Sistema

### Painel (HTML)

| Rota | Descrição |
|------|-----------|
| `/administrador/login/` | Tela de login |
| `/administrador/painel/` | Painel principal |
| `/administrador/calendario/` | Calendário de eventos |
| `/administrador/logout/` | Sair da conta |

### APIs (JSON)

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/administrador/api/eventos/` | Lista todos os eventos |
| POST | `/administrador/api/evento/salvar/` | Cria ou atualiza evento |
| POST | `/administrador/api/evento/excluir/<id>/` | Exclui evento |

---

## 📂 Estrutura do Projeto

```text
Meu-projeto/
├── administrador/
│   ├── migrations/
│   ├── templates/administrador/   (login.html, painel.html, calendario.html)
│   ├── static/administrador/      (css/, js/)
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── ong/
│   ├── settings.py
│   └── urls.py
├── .env                  (NÃO versionado - local)
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🔐 Segurança

- **Credenciais Protegidas:** Senhas do banco movidas para o arquivo `.env` (não versionado no Git).
- Senhas de login armazenadas como hash (usa `make_password` do Django).
- Bloqueio após 5 tentativas de login falhas.
- CSRF token ativado em todas as requisições POST.

---

## 🌿 Fluxo de Trabalho Git

- **`main`**: Produção (protegida).
- **`feature/*`**: Novas funcionalidades.
- **`fix/*`**: Correções de bug.

### Padrão de commits

| Prefixo | Uso |
|---------|-----|
| `feat:` | Nova funcionalidade |
| `fix:` | Correção de bug |
| `style:` | Ajuste visual/CSS |
| `docs:` | Documentação |
| `chore:` | Tarefas diversas |

---

## 👥 Time

| Integrante | Responsabilidade |
|------------|------------------|
| **ShiHiro231** | Back-end Django e estrutura inicial |
| **chandyzera** | Painel admin, calendário, tema neon e segurança |
| **THIAGO NESI NUNES** | Modelos e banco de dados |

---

**Desenvolvido com 💜 para uma causa maior.**