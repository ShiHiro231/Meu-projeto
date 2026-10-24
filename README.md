# 🌱 Painel Administrativo ONG

**Versão 2.0.0**

Sistema administrativo interno para ONG, com painel protegido por login nativo, calendário editável de eventos, API pública para integração com o site principal e interface moderna em tema dark com detalhes neon roxo.

---

## 👨‍💻 Desenvolvimento

Este projeto está sendo desenvolvido em equipe (3 integrantes), com auxílio de ferramentas de inteligência artificial para:
- Auxílio na geração e boas práticas de código Python/Django.
- Documentação e comentários explicativos.
- Depuração e correção de bugs.
- Criação do tema visual dark + neon.

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
| Django 4.2+ (ou 6.1) | Framework web |
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
source venv/bin/activate       # Mac/Linux

# 3. Instalar dependências
pip install -r requirements.txt
