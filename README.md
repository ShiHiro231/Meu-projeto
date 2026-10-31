# 🌱 Painel Administrativo ONG

**Versão 2.1.0**

Sistema administrativo interno e site institucional para ONG, com painel protegido, calendário de eventos, integração com API pública e fluxos de contato via WhatsApp e PIX. Interface moderna em tema dark com detalhes neon roxo no admin, e design clean no site público.

---

## 👨‍💻 Desenvolvimento

Este projeto está sendo desenvolvido em equipe (3 integrantes), com auxílio de ferramentas de inteligência artificial (DeepSeek) para:

- Auxílio na geração e boas práticas de código Python/Django.
- Documentação e comentários explicativos.
- Depuração e correção de bugs.
- Criação dos temas visuais (Dark/Neon no admin e Clean no público).

> **Nota de Arquitetura:** O código gerado por IA passou por uma auditoria e refatoração profunda para garantir segurança (uso do Auth nativo do Django) e organização (separação de views, criação de API RESTful e lógica de redirecionamento externo).

---

## ✨ Funcionalidades

### 🔐 Sistema de Login e Segurança (Admin)

- **Autenticação Nativa:** Uso do sistema de usuários nativo do Django (`django.contrib.auth`). Senhas criptografadas automaticamente.
- **Proteção de Rotas:** Views do painel e APIs de edição protegidas com `@login_required`.
- **CSRF Token:** Proteção ativada em todas as requisições POST.
- **Logout Seguro:** Implementado via método POST (exigência das versões recentes do Django).

### 📊 Painel Administrativo

- Tela inicial com boas-vindas ao administrador.
- Topbar com navegação entre seções.
- Card de acesso rápido ao calendário.

### 📅 Calendário Editável (Admin)

- Visualização mensal com navegação entre meses.
- Criação, edição e exclusão de eventos por clique no dia.
- **Cores por categoria:** 🟢 Verde (Doação), 🔵 Azul (Voluntariado), 🟣 Roxo (Ambos).
- Painel lateral de edição com campos de texto, data, horário e flags de categoria.

### 🌐 Site Institucional (Público)

- **Home:** Design responsivo, carrossel de projetos, seção "Quem Somos" e links de navegação.
- **Calendário Público:** Integrado via API, exibe apenas eventos futuros para os visitantes.
- **Voluntariado:** Formulário com nome, telefone e seleção de evento (puxado da API). O envio redireciona o usuário diretamente para o WhatsApp da ONG com a mensagem pré-formatada.
- **Doação:** Página dedicada com chave PIX para cópia rápida.

---

## 🏗️ Arquitetura e Banco de Dados

Para manter o repositório limpo, as imagens dos diagramas (Arquitetura do Sistema e DER) estão disponíveis na pasta [`/docs`](./docs) deste projeto.

- **Diagrama de Arquitetura:** Explica o fluxo entre Apresentação, Negócio, Dados e Serviços Externos.
- **Diagrama de Banco (DER):** Ilustra as tabelas, chaves primárias e relacionamentos (Eventos, Inscrições, Admin, etc.).

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
| JavaScript (puro) | Interatividade (calendário, carrossel, fetch API) |
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
source venv/bin/activate       # Mac/Linux

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

4. Rode as migrações para criar as tabelas:

```bash
python manage.py migrate
```

### 👤 Criar Administrador (Superusuário)

O painel usa o sistema de autenticação nativo do Django. Para criar o primeiro acesso, rode:

```bash
python manage.py createsuperuser
```

O terminal pedirá um nome de usuário, e-mail (opcional) e senha.

### ▶️ Executar o Sistema

```bash
python manage.py runserver
```

Acesse no navegador:
- **Site Público:** http://127.0.0.1:8000/
- **Painel Admin:** http://127.0.0.1:8000/administrador/login/

---

## 🔗 Rotas do Sistema

### Painel e Páginas (HTML)

| Rota | Descrição | Proteção |
|------|-----------|----------|
| `/` | Home do site público | Pública |
| `/pagamento/` | Página de doação (PIX) | Pública |
| `/voluntario/` | Formulário de voluntariado (redireciona pro WhatsApp) | Pública |
| `/administrador/login/` | Tela de login | Pública |
| `/administrador/painel/` | Painel principal | `@login_required` |
| `/administrador/calendario/` | Calendário de eventos | `@login_required` |

### APIs (JSON)

| Método | Rota | Descrição | Proteção |
|--------|------|-----------|----------|
| `GET` | `/administrador/api/eventos/` | Lista todos os eventos (Admin) | `@login_required` |
| `POST` | `/administrador/api/evento/salvar/` | Cria ou atualiza evento | `@login_required` + CSRF |
| `POST` | `/administrador/api/evento/excluir/<id>/` | Exclui evento | `@login_required` + CSRF |
| `GET` | `/administrador/api/publica/eventos/` | Lista eventos futuros (Público) | Pública (sem login) |

---

## 📂 Estrutura do Projeto

```text
Meu-projeto/
├── administrador/
│   ├── migrations/
│   ├── templates/
│   │   ├── administrador/         (login.html, painel.html, calendario.html)
│   │   └── site_publico/          (home.html, pagamento.html, voluntario.html)
│   ├── static/administrador/      (css/, js/, img/)
│   ├── views/                     (Pasta de views modularizadas)
│   │   ├── __init__.py
│   │   ├── paginas.py             (Views HTML e lógica do WhatsApp)
│   │   └── api.py                 (APIs JSON)
│   ├── admin.py
│   ├── forms.py                   (UserForm para validação)
│   ├── models.py                  (Evento, Voluntario, Inscricao, etc.)
│   └── urls.py
├── docs/                          (Pasta contendo as imagens dos diagramas)
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
- **Senhas com Hash:** Gerenciadas nativamente pelo sistema de autenticação do Django.
- **CSRF Ativado:** Proteção em todas as requisições POST.
- **Rotas Blindadas:** Uso generalizado de `@login_required` para impedir acesso não autorizado ao painel.

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
| `refactor:` | Refatoração de código |
| `chore:` | Tarefas diversas |

---

## 👥 Time

| Integrante | Responsabilidade |
|------------|------------------|
| **ShiHiro231** | Back-end Django, Refatoração de Segurança e API Pública |
| **chandyzera** | Painel admin, calendário, tema neon e integração JS |
| **THIAGO NESI NUNES** | Modelos, banco de dados e diagramas |

---

Desenvolvido com 💜 para uma causa maior.