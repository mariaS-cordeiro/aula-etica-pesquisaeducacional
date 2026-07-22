# Jogo Interativo: Ética na Pesquisa Educacional

Este é um ambiente interativo e gamificado construído com **Streamlit** e **CSS customizado** (com efeitos de glassmorphism e design responsivo) para guiar estudantes e pesquisadores nas reflexões éticas essenciais na pesquisa educacional.

## 🚀 Como Executar o Jogo Localmente

Siga o passo a passo abaixo para rodar o aplicativo na sua máquina:

### 1. Pré-requisitos
Certifique-se de ter o **Python** (versão 3.8 ou superior) instalado em seu computador.

### 2. Instalar as Dependências
Abra o seu terminal na pasta do projeto e execute o comando abaixo para instalar as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

### 3. Executar o Streamlit
Inicie o servidor de desenvolvimento do Streamlit com o seguinte comando:
```bash
streamlit run app.py
```

O jogo abrirá automaticamente no seu navegador padrão no endereço `http://localhost:8501`.

---

## 📂 Estrutura do Projeto

*   `app.py`: Contém a lógica de controle das jornadas do jogo, as telas e perguntas.
*   `style.css`: Estilização customizada premium com efeito *glassmorphic*, importação de fontes modernas e responsividade.
*   `requirements.txt`: Dependências do Python.
*   `assets/`: Diretório contendo as imagens dos pensadores e o avatar da professora.

---

## 🎨 Lógica Visual e Design

- **Avatar Integrado**: O avatar de professora enviado por você guia o aluno de forma acolhedora.
- **Filósofos & Teóricos**: Cartões visuais contendo os retratos e trechos teóricos (Aristóteles, Dermeval Saviani, Paulo Freire).
- **Termos Importantes**: Uma sala com cartões que registram a leitura interativa de cada sigla (TCLE, TALE, LGPD e CEP).
- **Dilemas Reais**: Cenários práticos em escola e redes digitais com feedbacks construtivos baseados no ECA, Paulo Freire, Boaventura de Sousa Santos e Minayo.
