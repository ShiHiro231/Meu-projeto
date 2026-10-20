# 🌱 Painel Administrativo ONG

**Versão 1.0.0**

Sistema administrativo interno para ONG, com painel protegido por login, calendário editável de eventos e interface moderna em tema dark com detalhes neon roxo.

---

## 👨‍💻 Desenvolvimento

Este projeto está sendo desenvolvido em equipe, com auxílio de ferramentas de inteligência artificial para:

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
| Django 5.x | Framework web |
| SQLite | Banco de dados (desenvolvimento) |
| MySQL | Banco de dados (produção) |
| HTML5 + CSS3 | Interface |
| JavaScript (puro) | Interatividade do calendário |
| Inter (Google Fonts) | Tipografia |
| Git + GitHub | Versionamento |

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.11 ou superior
- Git
- VS Code (recomendado)

### Passo a passo

```bash
# 1. Clonar o repositório
git clone https://github.com/ShiHiro231/Meu-projeto.git
cd Meu-projeto

# 2. Criar ambiente virtual
python -m venv venv

# 3. Ativar o venv
venv\Scripts\activate          # Windows CMD
venv\Scripts\Activate.ps1      # Windows PowerShell
source venv/bin/activate        # Mac/Linux

# 4. Instalar dependências
pip install -r requirements.txt

# 5. Rodar migrações
python manage.py migrate
```

---

## 👤 Criar Administrador

O painel usa um modelo `Administrador` customizado. Para criar o primeiro:

```bash
python manage.py shell -c "from administrador.models import Administrador; from django.contrib.auth.hashers import make_password; Administrador.objects.create(nome='Admin', login='admin', senha=make_password('admin123')); print('OK')"
```

### Login padrão

```text
Login: admin
Senha: admin123
```

> ⚠️ **Importante:** altere a senha em produção!

---

## ▶️ Executar o Sistema

```bash
python manage.py runserver
```

Acesse no navegador:

```text
http://127.0.0.1:8000/administrador/login/
```

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

### Django Admin

| Rota | Descrição |
|------|-----------|
| `/admin/` | CRUD automático das tabelas |

---

## 🗄️ Modelos de Dados

### `Administrador`

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | AutoField | Chave primária |
| `nome` | CharField(100) | Nome completo |
| `login` | CharField(50) | Único |
| `senha` | CharField(128) | Hash da senha |

### `Evento`

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | AutoField | Chave primária |
| `nome_evento` | CharField(100) | Nome do evento |
| `descricao` | TextField | Detalhes (opcional) |
| `data` | DateField | Data do evento |
| `horario_inicio` | TimeField | Opcional |
| `horario_fim` | TimeField | Opcional |
| `aceita_doacao` | BooleanField | Se aceita doação |
| `aceita_voluntariado` | BooleanField | Se aceita voluntariado |
| `criado_em` | DateTimeField | Timestamp automático |

---

## 📂 Estrutura do Projeto

```text
Meu-projeto/
├── administrador/
│   ├── migrations/
│   ├── templates/
│   │   └── administrador/
│   │       ├── login.html
│   │       ├── painel.html
│   │       └── calendario.html
│   ├── static/
│   │   └── administrador/
│   │       ├── css/
│   │       │   ├── base.css
│   │       │   └── calendario.css
│   │       └── js/
│   │           └── calendario.js
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── ong/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
├── venv/
├── .gitignore
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🔄 Migrando para MySQL

O projeto está configurado para **SQLite** em desenvolvimento. Para migrar para **MySQL** em produção:

### 1. Instalar dependência

```bash
pip install mysqlclient
```

> Se der erro no Windows, use `pymysql` como alternativa:
> ```bash
> pip install pymysql
> ```
> E em `ong/__init__.py`:
> ```python
> import pymysql
> pymysql.install_as_MySQLdb()
> ```

### 2. Ajustar `settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ong_db',
        'USER': 'root',
        'PASSWORD': 'sua-senha',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}
```

### 3. Rodar migrações

```bash
python manage.py migrate
```

---

## 🌿 Fluxo de Trabalho Git

### Branches

| Branch | Propósito |
|--------|-----------|
| `main` | Produção (protegida) |
| `feature/*` | Novas funcionalidades |
| `fix/*` | Correções de bug |
| `style/*` | Ajustes visuais |
| `docs/*` | Documentação |

### Fluxo padrão

```bash
# 1. Atualizar main local
git checkout main
git pull origin main

# 2. Criar branch nova
git checkout -b feature/nome-da-feature

# 3. Codar...

# 4. Commitar
git add .
git commit -m "feat: descrição da funcionalidade"

# 5. Subir para o fork
git push meu feature/nome-da-feature

# 6. Abrir Pull Request no GitHub
```

### Padrão de commits

| Prefixo | Uso |
|---------|-----|
| `feat:` | Nova funcionalidade |
| `fix:` | Correção de bug |
| `style:` | Ajuste visual/CSS |
| `refactor:` | Refatoração sem mudar comportamento |
| `docs:` | Documentação |
| `chore:` | Tarefas diversas |

---

## 🔐 Segurança

- Senhas armazenadas como hash (usa `make_password` do Django)
- Bloqueio após 5 tentativas de login falhas
- Bloqueio temporário de 5 minutos
- Sessão por cookie (Django)
- CSRF token em todas as requisições POST
- Variáveis sensíveis em `.env` (ignorado no Git)
- `.gitignore` configurado para não versionar:
  - `venv/`
  - `db.sqlite3`
  - `.env`
  - `__pycache__/`

---

## 📝 Changelog

### v1.0.0 (Atual)

- ✅ Tela de login com tema dark neon roxo
- ✅ Bloqueio após 5 tentativas (5 min)
- ✅ Painel administrativo com topbar
- ✅ Card de acesso rápido ao calendário
- ✅ Calendário editável com CRUD completo
- ✅ Cores por categoria (doação / voluntariado / ambos)
- ✅ APIs REST (listar, salvar, excluir eventos)
- ✅ Tema dark com detalhes neon roxo
- ✅ Layout responsivo
- ✅ Migração preparada para MySQL

---

## 👥 Time

| Integrante | Responsabilidade |
|------------|------------------|
| **ShiHiro231** | Back-end Django e estrutura inicial |
| **chandyzera** | Painel admin, calendário, tema neon e CSS |
| **THIAGO NESI NUNES** | Modelos e banco de dados |

---

## 📚 Documentação Adicional

- [Guia de Comandos](COMANDOS.md) *(se existir)*
- [Documentação do Django](https://docs.djangoproject.com/)

---

## 📌 Roadmap

- [ ] Migração completa para MySQL
- [ ] Integração com WhatsApp (link direto)
- [ ] Integração com Instagram
- [ ] Integração com e-mail
- [ ] Formulário público de doação
- [ ] Formulário público de voluntariado
- [ ] Dashboard com estatísticas

---

## 📝 Licença

Projeto interno. Todos os direitos reservados à ONG.

---

**Desenvolvido com 💜 para uma causa maior.**
