// ============================================
// ESTADO
// ============================================
let mesAtual = new Date().getMonth();
let anoAtual = new Date().getFullYear();
let eventos = [];
let eventoEmEdicao = null;
let dataSelecionada = null;

const MESES = [
    'Janeiro','Fevereiro','Março','Abril','Maio','Junho',
    'Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'
];

// ============================================
// ELEMENTOS
// ============================================
const gridDias       = document.getElementById('grid-dias');
const mesAnoEl       = document.getElementById('mes-ano');
const btnAnt         = document.getElementById('btn-anterior');
const btnProx        = document.getElementById('btn-proximo');

const painel         = document.getElementById('painel-edicao');
const tituloPainel   = document.getElementById('titulo-painel');
const inputData      = document.getElementById('input-data');
const inputNome      = document.getElementById('input-nome');
const inputDescricao = document.getElementById('input-descricao');
const inputInicio    = document.getElementById('input-inicio');
const inputFim       = document.getElementById('input-fim');
const checkDoacao    = document.getElementById('check-doacao');
const checkVolunt    = document.getElementById('check-voluntario');
const btnSalvar      = document.getElementById('btn-salvar');
const btnExcluir     = document.getElementById('btn-excluir');
const btnCancelar    = document.getElementById('btn-cancelar');

// ============================================
// CSRF TOKEN
// ============================================
function getCsrfToken() {
    const input = document.querySelector('input[name="csrfmiddlewaretoken"]');
    return input ? input.value : '';
}

// ============================================
// API — CARREGAR EVENTOS
// ============================================
async function carregarEventos() {
    try {
        const resposta = await fetch('/administrador/api/eventos/');
        if (!resposta.ok) throw new Error('Erro ao carregar');
        eventos = await resposta.json();
    } catch (erro) {
        console.error('Erro ao carregar eventos:', erro);
        eventos = [];
    }
}

// ============================================
// API — SALVAR EVENTO
// ============================================
async function salvarEvento(dados) {
    const resposta = await fetch('/administrador/api/evento/salvar/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken(),
        },
        body: JSON.stringify(dados),
    });
    return resposta.json();
}

// ============================================
// API — EXCLUIR EVENTO
// ============================================
async function excluirEvento(id) {
    const resposta = await fetch(`/administrador/api/evento/excluir/${id}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCsrfToken(),
        },
    });
    return resposta.json();
}

// ============================================
// HELPERS
// ============================================
function classeDoDia(dataISO) {
    const ev = eventos.find(e => e.data === dataISO);
    if (!ev) return '';
    if (ev.aceita_doacao && ev.aceita_voluntariado) return 'ambos';
    if (ev.aceita_doacao) return 'doacao';
    if (ev.aceita_voluntariado) return 'voluntario';
    return '';
}

function eventoDaData(dataISO) {
    return eventos.find(e => e.data === dataISO);
}

// ============================================
// RENDERIZAR CALENDÁRIO
// ============================================
function renderizarCalendario() {
    gridDias.innerHTML = '';
    mesAnoEl.textContent = `${MESES[mesAtual]} ${anoAtual}`;

    const primeiroDia = new Date(anoAtual, mesAtual, 1).getDay();
    const totalDias   = new Date(anoAtual, mesAtual + 1, 0).getDate();

    for (let i = 0; i < primeiroDia; i++) {
        const vazio = document.createElement('div');
        vazio.className = 'dia vazio';
        gridDias.appendChild(vazio);
    }

    for (let dia = 1; dia <= totalDias; dia++) {
        const dataISO = `${anoAtual}-${String(mesAtual + 1).padStart(2,'0')}-${String(dia).padStart(2,'0')}`;

        const el = document.createElement('div');
        el.className = 'dia';
        el.textContent = dia;

        const classe = classeDoDia(dataISO);
        if (classe) el.classList.add(classe);

        el.addEventListener('click', () => abrirEdicao(dataISO));
        gridDias.appendChild(el);
    }
}

// ============================================
// PAINEL DE EDIÇÃO
// ============================================
function abrirEdicao(dataISO) {
    dataSelecionada = dataISO;
    const existente = eventoDaData(dataISO);

    painel.classList.remove('escondido');
    inputData.value = dataISO;

    if (existente) {
        eventoEmEdicao = existente;
        tituloPainel.textContent = 'Editar evento';
        inputNome.value = existente.nome_evento || '';
        inputDescricao.value = existente.descricao || '';
        inputInicio.value = existente.horario_inicio || '';
        inputFim.value = existente.horario_fim || '';
        checkDoacao.checked = !!existente.aceita_doacao;
        checkVolunt.checked = !!existente.aceita_voluntariado;
        btnExcluir.classList.remove('escondido');
    } else {
        eventoEmEdicao = null;
        tituloPainel.textContent = 'Novo evento';
        inputNome.value = '';
        inputDescricao.value = '';
        inputInicio.value = '';
        inputFim.value = '';
        checkDoacao.checked = false;
        checkVolunt.checked = false;
        btnExcluir.classList.add('escondido');
    }

    inputNome.focus();
}

function fecharPainel() {
    painel.classList.add('escondido');
    eventoEmEdicao = null;
    dataSelecionada = null;
}

// ============================================
// SALVAR / EXCLUIR
// ============================================
async function salvar() {
    if (!inputNome.value.trim()) {
        alert('Preencha o nome do evento.');
        return;
    }
    if (!checkDoacao.checked && !checkVolunt.checked) {
        alert('Marque pelo menos: doação ou voluntariado.');
        return;
    }

    const dados = {
        id: eventoEmEdicao ? eventoEmEdicao.id : null,
        nome_evento: inputNome.value.trim(),
        descricao: inputDescricao.value.trim(),
        data: dataSelecionada,
        horario_inicio: inputInicio.value,
        horario_fim: inputFim.value,
        aceita_doacao: checkDoacao.checked,
        aceita_voluntariado: checkVolunt.checked,
    };

    try {
        btnSalvar.disabled = true;
        btnSalvar.textContent = 'Salvando...';

        const resposta = await salvarEvento(dados);

        if (resposta.erro) {
            alert('Erro: ' + resposta.erro);
            return;
        }

        await carregarEventos();
        renderizarCalendario();
        fecharPainel();
    } catch (erro) {
        alert('Erro ao salvar. Tente novamente.');
        console.error(erro);
    } finally {
        btnSalvar.disabled = false;
        btnSalvar.textContent = 'Salvar';
    }
}

async function excluir() {
    if (!eventoEmEdicao) return;
    if (!confirm('Excluir este evento?')) return;

    try {
        await excluirEvento(eventoEmEdicao.id);
        await carregarEventos();
        renderizarCalendario();
        fecharPainel();
    } catch (erro) {
        alert('Erro ao excluir. Tente novamente.');
        console.error(erro);
    }
}

// ============================================
// NAVEGAÇÃO
// ============================================
btnAnt.addEventListener('click', () => {
    mesAtual--;
    if (mesAtual < 0) { mesAtual = 11; anoAtual--; }
    renderizarCalendario();
});

btnProx.addEventListener('click', () => {
    mesAtual++;
    if (mesAtual > 11) { mesAtual = 0; anoAtual++; }
    renderizarCalendario();
});

btnSalvar.addEventListener('click', salvar);
btnExcluir.addEventListener('click', excluir);
btnCancelar.addEventListener('click', fecharPainel);

// ============================================
// INICIALIZAÇÃO
// ============================================
async function iniciar() {
    await carregarEventos();
    renderizarCalendario();
}

iniciar();