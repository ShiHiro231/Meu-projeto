
# 🌱 PROCRED - Sistema de Gestão e Site Institucional

**Versão 3.0.0**

Plataforma completa (Full-Stack) desenvolvida para a ONG PROCRED. O sistema é dividido em duas frentes: um **Painel Administrativo seguro** para gestão interna de eventos e um **Site Institucional responsivo** para o público geral, com integração de voluntariado via WhatsApp e doações via PIX.

---

## 👨‍💻 Desenvolvimento

Este projeto está sendo desenvolvido em equipe (6 integrantes), com auxílio de ferramentas de inteligência artificial para:

- Auxílio na geração e boas práticas de código Python/Django.
- Documentação e comentários explicativos.
- Depuração e correção de bugs.
- Criação dos temas visuais.

> **Nota de Arquitetura:**  
> O código passou por uma auditoria profunda. Refatoramos o sistema de autenticação para o padrão nativo do Django, separamos as views por responsabilidade, criamos uma API RESTful para integração do front-end e aplicamos lógica de redirecionamento dinâmico para WhatsApp.

---

## ✨ Funcionalidades

### 🌐 Site Institucional (Público)

- **Home:** Design responsivo, carrossel de projetos, seção "Quem Somos" e navegação suave.
- **Calendário Público:** Integrado dinamicamente via JavaScript (Fetch API), exibe apenas eventos futuros puxados do banco de dados.
- **Página de Doação:** Layout dedicado para doações via PIX, com botão de "Copiar Chave" e exibição de QR Code.
- **Página de Voluntariado:** Formulário dinâmico onde o usuário seleciona um evento cadastrado no banco. Ao enviar, o sistema monta uma mensagem pré-formatada e redireciona o usuário para o WhatsApp da ONG.

### 🔐 Painel Administrativo (Restrito)

- **Autenticação Nativa:** Uso do sistema de usuários do Django (`django.contrib.auth`), garantindo senhas criptografadas e sessões seguras.
- **Proteção de Rotas:** Todas as views do painel e APIs de edição estão protegidas com `@login_required`.
- **Calendário Editável:** Interface para criar, editar e excluir eventos. Os eventos são categorizados por cores (Doação, Voluntariado ou Ambos).
- **Tema Dark/Neon:** Interface moderna com detalhes em roxo neon e efeitos de glow.

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|------------|-----|
| Python 3.11+ | Linguagem principal |
| Django 6.1 | Framework web (Back-end) |
| MySQL 8.4 | Banco de dados principal |
| PyMySQL | Driver de conexão do banco |
| python-dotenv | Proteção de credenciais (.env) |
| HTML5 + CSS3 | Interface (Site Público e Admin) |
| JavaScript (Vanilla) | Interatividade (Carrossel, Calendário, Fetch API) |
| Git + GitHub | Versionamento |

---

## 🏗️ Arquitetura do Sistema

O projeto segue o padrão MVT (Model-View-Template) do Django para o Admin e uma arquitetura API-First para o Site Público.

- **Apresentação:** Templates HTML separados em `administrador/` e `site_publico/`.
- **Negócio:** Views modulares separadas em `paginas.py` (renderização e lógica do WhatsApp) e `api.py` (endpoints JSON).
- **Dados:** Models para Eventos, Admin (nativo) e Inscrições.
- **Integrações:** API do WhatsApp (via redirecionamento `wa.me`).

---

## 🚀 Instalação e Configuração

### Pré-requisitos

- Python 3.11 ou superior
- MySQL Server 8.4+ (em execução local)
- Git

### Passo a passo

#### 1. Clonar o repositório

```bash
git clone https://github.com/chandyzera/ProjetoWEB.git
cd ProjetoWEB
```

#### 2. Criar e ativar o ambiente virtual

**Windows CMD:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Mac/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

Caso o `python-dotenv` não esteja no `requirements.txt`, instale manualmente:

```bash
pip install python-dotenv
```

### Configuração do Banco e Segurança

1. Preencha com as credenciais do seu MySQL local:

```env
DB_NAME=projeto_ong
DB_USER=projeto
DB_PASSWORD=projeto
DB_HOST=127.0.0.1
DB_PORT=3306
```

3. Crie o banco e o usuário no MySQL (via terminal ou Workbench):

```sql
CREATE DATABASE IF NOT EXISTS projeto_ong CHARACTER SET utf8mb4;

CREATE USER IF NOT EXISTS 'projeto'@'localhost' IDENTIFIED BY 'projeto';

GRANT ALL PRIVILEGES ON projeto_ong.* TO 'projeto'@'localhost';

FLUSH PRIVILEGES;
```

4. Rode as migrações:

```bash
python manage.py migrate
```

---

## 👤 Criar Administrador

Para acessar o painel restrito, crie o superusuário nativo do Django:

```bash
python manage.py createsuperuser
```

O terminal pedirá um nome de usuário, e-mail (opcional) e senha.

---

## ▶️ Executar o Sistema

```bash
python manage.py runserver
```

Acesse no navegador:

- 🌐 **Site Público:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- 🔐 **Painel Admin:** [http://127.0.0.1:8000/administrador/login/](http://127.0.0.1:8000/administrador/login/)

---

## 🔗 Rotas do Sistema

### Site Público (HTML)

| Rota | Descrição | Proteção |
|------|-----------|----------|
| `/` | Home do site institucional | Pública |
| `/pagamento/` | Página de doação (PIX) | Pública |
| `/voluntario/` | Formulário de voluntariado (WhatsApp) | Pública |

### Painel Admin (HTML)

| Rota | Descrição | Proteção |
|------|-----------|----------|
| `/administrador/login/` | Tela de login | Pública |
| `/administrador/painel/` | Painel principal | `@login_required` |
| `/administrador/calendario/` | Calendário de eventos | `@login_required` |

### APIs (JSON)

| Método | Rota | Descrição | Proteção |
|--------|------|-----------|----------|
| GET | `/administrador/api/eventos/` | Lista todos os eventos | `@login_required` |
| POST | `/administrador/api/evento/salvar/` | Cria ou atualiza evento | `@login_required` + CSRF |
| POST | `/administrador/api/evento/excluir/<id>/` | Exclui evento | `@login_required` + CSRF |
| GET | `/administrador/api/publica/eventos/` | Lista eventos futuros (Público) | Pública (sem login) |

---

## 📂 Estrutura do Projeto

```text
Meu-projeto/
├── administrador/
│   ├── migrations/
│   ├── templates/
│   │   ├── administrador/
│   │   │   ├── login.html
│   │   │   ├── painel.html
│   │   │   └── calendario.html
│   │   └── site_publico/
│   │       ├── home.html
│   │       ├── pagamento.html
│   │       └── voluntario.html
│   ├── static/
│   │   └── administrador/
│   │       ├── css/
│   │       ├── img/
│   │       └── js/
│   ├── views/
│   │   ├── __init__.py
│   │   ├── paginas.py
│   │   └── api.py
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   └── urls.py
├── docs/
│   └── (Imagens dos diagramas de Arquitetura e DER)
├── ong/
│   ├── settings.py
│   └── urls.py
├── .env                 # NÃO versionado - local
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🔐 Segurança

- **Credenciais Protegidas:** Senhas do banco movidas para o arquivo `.env` (não versionado no Git).
- **Senhas com Hash:** Gerenciadas nativamente pelo sistema de autenticação do Django.
- **CSRF Ativado:** Proteção em todas as requisições POST (tanto nos formulários quanto no fetch do JS).
- **Rotas Blindadas:** Uso generalizado de `@login_required` para impedir acesso não autorizado ao painel.
- **Logout Seguro:** Implementado via método POST (exigência das versões recentes do Django).

---

## 🌿 Fluxo de Trabalho Git

- `main`: Produção (protegida).
- `feature/*`: Novas funcionalidades.
- `fix/*`: Correções de bug.
- `refactor/*`: Refatorações e melhorias de arquitetura.

### Padrão de commits

| Prefixo | Uso |
|----------|-----|
| `feat:` | Nova funcionalidade |
| `fix:` | Correção de bug |
| `style:` | Ajuste visual/CSS |
| `docs:` | Documentação |
| `refactor:` | Refatoração de código |
| `chore:` | Tarefas diversas |

---

## 👥 Time

| Integrante | Responsabilidade |
|------------|-----------------|
| ShiHiro231 | Back-end Django, Refatoração de Segurança e API Pública |
| chandyzera | Painel admin, calendário, tema e integração JS |
| THIAGO NESI NUNES | Modelos, banco de dados e diagramas |
| Tiago Morimoto | Front-end |
| Carol| Estilização CSS |
| Daiane| Estilização CSS |

---

<div align="center">

**Desenvolvido com 💜 para uma causa maior.**

</div>