# 🌱 Painel Administrativo ONG

**Versão 2.0.0**

Sistema administrativo interno para ONG, com painel protegido por login nativo, calendário editável de eventos, API pública para integração com o site principal e interface moderna em tema dark com detalhes neon roxo.

---

## 👨‍💻 Desenvolvimento

Este projeto está sendo desenvolvido em equipe (3 integrantes), com auxílio de ferramentas de inteligência artificial para:
- Auxílio na geração e boas práticas de código Python/Django.
- Documentação e comentários explicativos.
- Depuração e correção de bugs.
- Criação do tema visual CSS.

> **Nota de Arquitetura:** O código gerado por IA passou por uma auditoria e refatoração profunda para garantir segurança (uso do Auth nativo do Django) e organização (separação de views e criação de API RESTful).

---

## ✨ Funcionalidades

### 🔐 Sistema de Login e Segurança
- **Autenticação Nativa:** Uso do sistema de usuários nativo do Django (`django.contrib.auth`). Senhas são criptografadas automaticamente (hash nativo).
- **Proteção de Rotas:** Todas as views do painel e APIs de edição estão protegidas com o decorator `@login_required`.
- **CSRF Token:** Proteção nativa do Django ativada em todas as requisições POST (tanto nos formulários HTML quanto no JavaScript via `fetch`).
- **Logout Seguro:** Implementado via método POST (exigência das versões recentes do Django).

### 📊 Painel Administrativo
- Tela inicial com boas-vindas ao administrador.
- Topbar com navegação entre seções.
- Card de acesso rápido ao calendário.

### 📅 Calendário Editável
- Visualização mensal com navegação entre meses.
- Criação, edição e exclusão de eventos por clique no dia.
- **Cores por categoria:**
  - 🟢 Verde: Aceita doação
  - 🔵 Azul: Aceita voluntariado
  - 🟣 Roxo: Aceita ambos
- Painel lateral de edição com campos de texto, data, horário e flags de categoria.

### 🌐 API Pública (Integração)
- Rota pública e otimizada (`GET /administrador/api/publica/eventos/`) que retorna apenas eventos futuros.
- Retorno em formato JSON, pronto para ser consumido pelo site principal (front-end institucional).

### 🎨 Design
- Tema dark com accent neon roxo (`#a855f7`).
- Efeitos de glow sutis em hover/focus.
- Cards com borda neon animada.
- Layout responsivo (mobile-friendly) e tipografia Inter.

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|------------|-----|
| Python 3.11+ | Linguagem principal |
| Django 4.2+ | Framework web |
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
- MySQL Workbench (opcional)
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
source venv/bin/activate       # Mac/Linux

# 3. Instalar dependências
pip install -r requirements.txt
```

### Configuração do Banco e Segurança
O projeto utiliza variáveis de ambiente para proteger os dados do banco.

1. Abra o `.env` e preencha com as credenciais do seu MySQL local:

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

### 👤 Criar Administrador (Superusuário)
Como o sistema agora utiliza o Auth nativo do Django, a criação do usuário administrador é feita pelo próprio framework. Para criar o primeiro acesso, rode no terminal (com a `venv` ativa):

```bash
python manage.py createsuperuser
```
O terminal pedirá um nome de usuário, e-mail (opcional) e senha.

### ▶️ Executar o Sistema
```bash
python manage.py runserver
```
Acesse no navegador: `http://127.0.0.1:8000/administrador/login/`

---

## 🔗 Rotas do Sistema

### Painel e Páginas (HTML)
| Rota | Descrição | Proteção |
|------|-----------|----------|
| `/administrador/login/` | Tela de login | Pública |
| `/administrador/painel/` | Painel principal | `@login_required` |
| `/administrador/calendario/` | Calendário de eventos | `@login_required` |

### APIs do Calendário (JSON) - Restritas
| Método | Rota | Descrição | Proteção |
|--------|------|-----------|----------|
| `GET` | `/administrador/api/eventos/` | Lista todos os eventos | `@login_required` |
| `POST` | `/administrador/api/evento/salvar/` | Cria ou atualiza evento | `@login_required` + CSRF |
| `POST` | `/administrador/api/evento/excluir/<id>/` | Exclui evento | `@login_required` + CSRF |

### API Pública (JSON) - Integração
| Método | Rota | Descrição | Proteção |
|--------|------|-----------|----------|
| `GET` | `/administrador/api/publica/eventos/` | Lista eventos futuros para o site principal | Pública (sem login) |

---

## 📂 Estrutura do Projeto

```text
Meu-projeto/
├── administrador/
│   ├── migrations/
│   ├── templates/administrador/   (login.html, painel.html, calendario.html)
│   ├── static/administrador/      (css/, js/)
│   ├── views/                     (Pasta de views modularizadas)
│   │   ├── __init__.py
│   │   ├── paginas.py             (Views HTML)
│   │   └── api.py                 (APIs JSON)
│   ├── admin.py
│   ├── models.py                  (Apenas model Evento)
│   ├── urls.py
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
- **Senhas com Hash:** Gerenciadas nativamente pelo sistema de autenticação do Django (PBKDF2).
- **CSRF Ativado:** Proteção em todas as requisições POST.
- **Rotas Blindadas:** Uso generalizado de `@login_required` para impedir acesso não autorizado às views e APIs de edição.

---

## 🌿 Fluxo de Trabalho Git

- `main`: Produção (protegida).
- `feature/*`: Novas funcionalidades.
- `fix/*`: Correções de bug.
- `refactor/*`: Refatorações e melhorias de arquitetura.

### Padrão de commits
| Prefixo | Uso |
|---------|-----|
| `feat:` | Nova funcionalidade |
| `fix:` | Correção de bug |
| `style:` | Ajuste visual/CSS |
| `docs:` | Documentação |
| `refactor:` | Refatoração de código sem mudar comportamento |
| `chore:` | Tarefas diversas |

---

## 👥 Time

| Integrante | Responsabilidade |
|------------|------------------|
| **ShiHiro231** | Back-end Django, Sistema de Login |
| **chandyzera** | Painel admin, calendário, CSS, integração JS, Refatoração de Segurança e API Pública |
| **THIAGO NESI NUNES** | Modelos e banco de dados |

---

<p align="center">Desenvolvido com 💜 para uma causa maior.</p>