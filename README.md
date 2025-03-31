# Painel Administrativo - Quiz do mengão

O **Painel Administrativo** do Quiz do Mengão é uma aplicação desenvolvida para gerenciar as perguntas do quiz interativo sobre o Clube de Regatas do Flamengo. Este painel permite adicionar, editar e excluir perguntas de forma prática e eficiente, integrando-se diretamente ao backend do projeto.

---

## 📋 Objetivos Principais

- Fornecer uma interface administrativa para gerenciar as perguntas do - quiz.
- Garantir uma integração eficiente com o backend (Supabase).
- Facilitar a manutenção e atualização do banco de perguntas do quiz.

---

## 🚀 Tecnologias Utilizadas

- **Painel Administrativo:** Python (Streamlit)
- **Backend:** Supabase (banco de dados)
- **Gerenciamento de Dependências:** Python (pip)
- **Gestão do Projeto:** Trello (tarefas)

---

## 📋 Funcionalidades

- Adicionar novas perguntas ao banco de dados.
- Editar perguntas existentes (enunciado, opções e resposta correta).
- Excluir perguntas do banco de dados.

---

## 🛠️ Como Rodar o Projeto

### 1. Pré-requisitos
Certifique-se de ter instalado:
- **Python** (versão 3.10 ou superior)
- **pip** (gerenciador de pacotes do Python)


### 2. Clone o repositório
```bash
git clone https://github.com/raphaelFF/quiz_flamengo.git
```

### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as Variáveis de Ambiente
Crie um arquivo .env no diretório raiz do projeto e adicione as seguintes variáveis:
- **const supabaseUrl** = 'https://sua-url.supabase.co';
- **const supabaseKey** = 'sua-chave-publica';

### 5. Inicie o Painel Administrativo

```bash
python -m streamlit run app.py
```
OBS: 




 
