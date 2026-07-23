import streamlit as st
import os
import base64

# Page configuration
st.set_page_config(
    page_title="Jornada sobre ética na pesquisa",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Constants & Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STYLE_FILE = os.path.join(BASE_DIR, "style.css")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# Helper function to get image as base64
def get_image_base64(filename):
    file_path = os.path.join(ASSETS_DIR, filename)
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
            return base64.b64encode(data).decode()
    return ""

# Helper to load external CSS
def load_css():
    if os.path.exists(STYLE_FILE):
        with open(STYLE_FILE, "r", encoding="utf-8") as f:
            css = f.read()
            st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    else:
        st.error("Arquivo style.css não encontrado!")

# Load styles
load_css()

# Session State Initialization
if "jornada" not in st.session_state:
    st.session_state.jornada = 0  # 0: Intro, 1: Perg. Fundamental, 2: J3 (Filósofos), 3: J4 (Termos), 4: J5 (Dilema 1), 5: J5 (Dilema 2), 6: Fim

if "quiz_q1" not in st.session_state:
    st.session_state.quiz_q1 = None
if "quiz_q2" not in st.session_state:
    st.session_state.quiz_q2 = None
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

if "j4_visited" not in st.session_state:
    st.session_state.j4_visited = {"tcle": False, "tale": False, "lgpd": False, "cep": False}
if "j4_current_open" not in st.session_state:
    st.session_state.j4_current_open = None

if "dilema1_choice" not in st.session_state:
    st.session_state.dilema1_choice = None
if "dilema2_choice" not in st.session_state:
    st.session_state.dilema2_choice = None

# Custom rendering components
def render_teacher_speech(text):
    avatar_b64 = get_image_base64("avatar_professora.jpg")
    img_src = f"data:image/jpeg;base64,{avatar_b64}" if avatar_b64 else "https://via.placeholder.com/180"
    
    html = f"""
    <div class="teacher-speech-container">
        <img src="{img_src}" class="teacher-avatar" alt="Professora">
        <div class="speech-bubble">
            <div class="teacher-name">Professora Maria</div>
            <div>{text}</div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_progress_bar(current_step, total_steps=6):
    pct = int((current_step / total_steps) * 100)
    html = f"""
    <div class="game-progress-bar">
        <div class="game-progress-inner" style="width: {pct}%;"></div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# Navigation Actions
def next_step():
    st.session_state.jornada += 1

def prev_step():
    st.session_state.jornada -= 1

def restart_game():
    st.session_state.jornada = 0
    st.session_state.quiz_q1 = None
    st.session_state.quiz_q2 = None
    st.session_state.quiz_submitted = False
    st.session_state.j4_visited = {"tcle": False, "tale": False, "lgpd": False, "cep": False}
    st.session_state.j4_current_open = None
    st.session_state.dilema1_choice = None
    st.session_state.dilema2_choice = None

# Main Interface Routing
render_progress_bar(st.session_state.jornada)

# ----------------- TELA 0: ABERTURA -----------------
if st.session_state.jornada == 0:
    render_teacher_speech(
        "Olá, futuro(a) pesquisador(a)! Bem-vindo(a) à nossa jornada interativa sobre <b>Ética na Pesquisa</b>. "
        "A palavra ética está em toda parte, mas você sabe como ela se aplica quando pesquisamos na área da Educação? "
        "Vamos começar nossa jornada de conhecimento?!"
    )
    
    st.markdown("""
    <div class="glass-card">
        <div class="gradient-text">Ética e Pesquisa Educacional</div>
        <div class="subtitle-text">
            <p>Se as discussões sobre ética costumam ser travadas de forma distante, no cotidiano da pesquisa ela é uma prática VIVA! 
            A ética não se resume a uma lista de "pode/não pode" ditada por comitês distantes do dia a dia.</p>
            <p>Mais do que dizer simplesmente "o que fazer", a ética é uma <b>reflexão crítica sobre o que nós fazemos</b> e como nossas investigações afetam as pessoas à nossa volta.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.button("Iniciar Jornada ▶", on_click=next_step, type="primary")

# ----------------- TELA 1: PERGUNTA FUNDAMENTAL -----------------
elif st.session_state.jornada == 1:
    render_teacher_speech(
    "Antes de conversarmos com estudantes, professores(as), gestores(as) ou familiares no campo, "
    "precisamos refletir sobre uma questão fundamental e norteadora..."
)
    st.markdown("""
    <div class="glass-card" style="text-align: center; padding: 40px 20px;">
        <h2 style="color: #1e3a8a; margin-bottom: 20px;">O que é ética na pesquisa educacional?
       
        Como agir de forma ética durante uma pesquisa?</h2>
        <p style="color: #475569; max-width: 600px; margin: 0 auto 30px auto; font-size: 1.1rem;">
            Pense sobre isso! A ética nasce da preocupação genuína com a dignidade e a vulnerabilidade das pessoas envolvidas no seu estudo.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Simple reflection block
    reflection_opt = st.radio(
        "Para você, qual é o núcleo do comportamento ético na pesquisa?",
        [
            "Selecione uma opção...",
            "Cumprir exigências burocráticas e assinar documentos obrigatórios.",
            "Refletir de maneira crítica e empática sobre o impacto das minhas ações nas pessoas reais da pesquisa.",
            "Focar apenas nos resultados acadêmicos, garantindo a neutralidade total."
        ],
        index=0
    )
    
    if reflection_opt and reflection_opt != "Selecione uma opção...":
        if "Refletir" in reflection_opt:
            st.success("Exatamente! A ética exige reflexão crítica, engajamento e empatia cotidiana.")
        else:
            st.info("Uma visão comum, mas lembre-se: a ética vai muito além de meros protocolos ou distanciamento técnico!")
            
        st.button("Continuar para a Jornada 3 ▶", on_click=next_step, type="primary")
    else:
        st.button("Voltar", on_click=prev_step)

# ----------------- TELA 2: JORNADA 3 (FILÓSOFOS & QUIZ) -----------------
elif st.session_state.jornada == 2:
    render_teacher_speech(
        "Na <b>Jornada 3</b>, você assume o papel de pesquisador(a)! "
        "Leia com atenção as reflexões de três grandes pensadores para compreender as bases da ética na pesquisa educacional. "
        "Depois, responda ao quiz de avanço!"
    )
    
    st.markdown("<h2 class='gradient-text'>Jornada 3: O/A Pesquisador(a) e os Pensadores</h2>", unsafe_allow_html=True)
    
    # Columns for Aristóteles, Saviani, Paulo Freire
    col1, col2, col3 = st.columns(3)
    
    # Base64 values for philosophers
    aristoteles_b64 = get_image_base64("aristoteles.png")
    saviani_b64 = get_image_base64("saviani.png")
    freire_b64 = get_image_base64("paulo_freire.png")
    
    aristoteles_src = f"data:image/png;base64,{aristoteles_b64}" if aristoteles_b64 else "https://via.placeholder.com/150"
    saviani_src = f"data:image/png;base64,{saviani_b64}" if saviani_b64 else "https://via.placeholder.com/150"
    freire_src = f"data:image/png;base64,{freire_b64}" if freire_b64 else "https://via.placeholder.com/150"
    
    with col1:
        st.markdown(f"""
        <div class="philosopher-card">
            <img src="{aristoteles_src}" class="philosopher-avatar" alt="Aristóteles">
            <div class="philosopher-name">Aristóteles</div>
            <div class="philosopher-quote">
                "A ética está ligada ao caráter de uma pessoa, construído na relação, no diálogo e no convívio prático com os outros."
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
        <div class="philosopher-card">
            <img src="{saviani_src}" class="philosopher-avatar" alt="Saviani">
            <div class="philosopher-name">Dermeval Saviani</div>
            <div class="philosopher-quote">
                "A educação se inscreve na esfera pública, ligando a ética à política. Cabe ao pesquisador refletir sobre sua ação e intervir conscientemente."
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown(f"""
        <div class="philosopher-card">
            <img src="{freire_src}" class="philosopher-avatar" alt="Paulo Freire">
            <div class="philosopher-name">Paulo Freire</div>
            <div class="philosopher-quote">
                "A ética na educação envolve o respeito profundo à autonomia progressiva, à subjetividade e à dignidade do educando, promovendo a proteção e o diálogo."
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br><hr style='border-color: rgba(255,255,255,0.4)'><br>", unsafe_allow_html=True)
    
    # Quiz section
    st.markdown("### 📝 Quiz de Avanço")
    
    q1 = st.radio(
        "1. De acordo com Aristóteles, o que constitui a base da ética?",
        [
            "Selecione uma opção...",
            "A) Um conjunto de regras estritas e burocráticas definidas por comitês.",
            "B) O caráter de uma pessoa, construído e moldado na relação prática com os outros.",
            "C) A neutralidade absoluta de um cientista isolado de influências sociais."
        ],
        index=0 if st.session_state.quiz_q1 is None else ["A", "B", "C"].index(st.session_state.quiz_q1) + 1
    )
    
    q2 = st.radio(
        "2. Para Saviani e Paulo Freire, qual o compromisso ético-político do pesquisador na educação?",
        [
            "Selecione uma opção...",
            "A) O pesquisador deve ser um agente neutro que apenas observa, sem intervir ou se importar com os sentimentos do educando.",
            "B) A ética na pesquisa restringe-se a obter assinaturas formais, sem compromisso social ou intervenção crítica.",
            "C) A ética exige engajamento social, escuta sensível da realidade educacional e profundo respeito pela dignidade e autonomia do educando."
        ],
        index=0 if st.session_state.quiz_q2 is None else ["A", "B", "C"].index(st.session_state.quiz_q2) + 1
    )
    
    # Validate and submit
    if st.button("Verificar Respostas", type="secondary"):
        if not q1 or not q2 or q1 == "Selecione uma opção..." or q2 == "Selecione uma opção...":
            st.warning("Por favor, responda a ambas as perguntas para prosseguir.")
        else:
            st.session_state.quiz_q1 = "A" if "A)" in q1 else ("B" if "B)" in q1 else "C")
            st.session_state.quiz_q2 = "A" if "A)" in q2 else ("B" if "B)" in q2 else "C")
            st.session_state.quiz_submitted = True
            st.rerun()
 
    # Feedback display
    if st.session_state.quiz_submitted:
        correct_q1 = (st.session_state.quiz_q1 == "B")
        correct_q2 = (st.session_state.quiz_q2 == "C")
        
        if correct_q1:
            st.success("✅ Pergunta 1 Correta! Excelente. Aristóteles foca no caráter construído no convívio com os outros.")
        else:
            st.error("❌ Pergunta 1 Incorreta. Lembre-se: Aristóteles associa a ética ao caráter moldado nas relações cotidianas, e não a regras burocráticas.")
            
        if correct_q2:
            st.success("✅ Pergunta 2 Correta! Saviani e Freire apoiam a ação engajada e o respeito à autonomia do participante.")
        else:
            st.error("❌ Pergunta 2 Incorreta. Para Saviani e Freire, a pesquisa em educação deve superar a falsa neutralidade e zelar pela dignidade e autonomia do estudante.")
            
        if correct_q1 and correct_q2:
            st.success("🎉 Parabéns! Você acertou todas as perguntas da Jornada 3.")
            st.button("Avançar para a Jornada 4 ▶", on_click=next_step, type="primary")
        else:
            st.info("Revise as alternativas incorretas e tente novamente clicando em 'Verificar Respostas'.")
            
    st.button("Voltar", on_click=prev_step, key="back_j3")

# ----------------- TELA 3: JORNADA 4 (TERMOS IMPORTANTES) -----------------
elif st.session_state.jornada == 3:
    render_teacher_speech(
        "Seja bem-vindo(a) à <b>Sala dos Termos Importantes</b>! "
        "Aqui estão as siglas e conceitos legais que materializam a ética no cotidiano da pesquisa. "
        "Clique em cada um dos cartões abaixo para ler suas definições. <b>Você precisa explorar todos os 4 termos para liberar a próxima fase!</b>"
    )
    
    st.markdown("<h2 class='gradient-text'>Jornada 4: Os Termos da Ética na Pesquisa</h2>", unsafe_allow_html=True)
    
    terms_info = {
        "tcle": {
            "title": "📄 TCLE – Termo de Consentimento Livre e Esclarecido",
            "emoji": "📄",
            "content": """
            Documento por meio do qual os participantes (ou seus responsáveis legais) autorizam voluntariamente sua participação na pesquisa. 
            Ele deve detalhar todos os objetivos, métodos, riscos e benefícios potenciais do estudo de forma transparente antes da assinatura.
            """
        },
        "tale": {
            "title": "📄 TALE – Termo de Assentimento Livre e Esclarecido",
            "emoji": "📄",
            "content": """
            Documento destinado a crianças, adolescentes ou pessoas temporariamente impedidas de consentir juridicamente. 
            Manifesta a concordância do participante em linguagem clara, simples e adequada à sua idade e compreensão, complementando o consentimento dos responsáveis.
            """
        },
        "lgpd": {
            "title": "🔒 LGPD – Lei Geral de Proteção de Dados Pessoais",
            "emoji": "🔒",
            "content": """
            Legislação brasileira (Lei nº 13.709/2018) que rege a coleta, tratamento e guarda de dados pessoais. 
            Na pesquisa educacional, exige cuidado especial com dados de alunos, pais e professores, além de dados sensíveis (origem racial, convicção religiosa, etc.). 
            O planejamento da pesquisa deve prever a segurança e a <b>anonimização</b> dos dados nas publicações.
            """
        },
        "cep": {
            "title": "⚖️ CEP – Comitê de Ética em Pesquisa",
            "emoji": "⚖️",
            "content": """
            Colegiado interdisciplinar responsável por analisar e acompanhar os aspectos éticos das pesquisas envolvendo seres humanos. 
            Sua missão é garantir a integridade dos procedimentos de pesquisa, a proteção integral de todos os envolvidos e o cumprimento das diretrizes éticas nacionais.
            """
        }
    }
    
    # Render clickable term cards
    for key, info in terms_info.items():
        is_visited = st.session_state.j4_visited[key]
        status_text = "Explorado ✓" if is_visited else "Clique para Ler"
        badge_class = "visited" if is_visited else "unvisited"
        card_class = "visited" if is_visited else "unvisited"
        
        # We can implement a clean expander or trigger action by clicking a button
        col_c1, col_c2 = st.columns([4, 1])
        with col_c1:
            st.markdown(f"""
            <div class="term-header">
                <span>{info['title']}</span>
            </div>
            """, unsafe_allow_html=True)
        with col_c2:
            if st.button(f"{status_text}", key=f"btn_{key}", type="secondary" if is_visited else "primary"):
                st.session_state.j4_visited[key] = True
                st.session_state.j4_current_open = key
                st.rerun()
        
        # Display open content
        if st.session_state.j4_current_open == key:
            st.markdown(f"""
            <div class="term-card visited">
                <div class="term-body">{info['content']}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)
            
    # Check if all terms are visited
    all_visited = all(st.session_state.j4_visited.values())
    
    if all_visited:
        st.success("🎉 Excelente! Você examinou todos os termos éticos e procedimentais da pesquisa.")
        st.button("Continuar para os Dilemas (Jornada 5) ▶", on_click=next_step, type="primary")
    else:
        st.info("Explore todos os quatro termos acima para liberar a continuação do jogo.")
        
    st.button("Voltar", on_click=prev_step, key="back_j4")

# ----------------- TELA 4: JORNADA 5 - DILEMA 1 (CRIANÇAS NA ESCOLA) -----------------
elif st.session_state.jornada == 4:
    render_teacher_speech(
        "Chegamos à <b>Jornada 5: Dilemas Éticos na Educação</b>. "
        "Aqui a teoria encontra a realidade! Enfrente o primeiro dilema e decida qual caminho seguir."
    )
    
    st.markdown("<h2 class='gradient-text'>Jornada 5: Dilema 1 - Pesquisa com Crianças na Escola</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="dilemma-card">
        <h4 style="color: #1e3a8a;">O Cenário:</h4>
        <p style="font-size: 1.05rem; line-height: 1.6; color: #334155;">
            Uma pesquisadora realiza uma investigação sobre as formas de participação das crianças nas decisões escolares. 
            O estudo envolve observações e entrevistas individuais com alunos. 
            A escola e os responsáveis assinaram o <b>TCLE</b>, e as crianças assinaram o <b>TALE</b>. 
            <br><br>
            Durante uma entrevista individual gravada, uma aluna compartilha de forma espontânea informações delicadas sobre <b>conflitos familiares graves</b> e seus profundos sentimentos de exclusão e sofrimento.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    choice = st.radio(
        "Como a pesquisadora deve agir diante desta situação?",
        [
            "Selecione uma opção...",
            "Opção A: Registrar e analisar o relato no relatório científico, pois é um dado de alta relevância para compreender a dimensão emocional e a exclusão na vida escolar.",
            "Opção B: Suprimir o trecho delicado da análise pública para proteger o bem-estar emocional da aluna, mantendo o sigilo e evitando exposição inadequada."
        ],
        index=0 if st.session_state.dilema1_choice is None else ["A", "B"].index(st.session_state.dilema1_choice) + 1
    )
    
    if choice and choice != "Selecione uma opção...":
        st.session_state.dilema1_choice = "A" if "Opção A" in choice else "B"
        
        if st.session_state.dilema1_choice == "A":
            st.warning("""
            ⚠️ **Reflexão Crítica (Cuidado necessário):**
            Embora o dado seja cientificamente interessante para compreender a exclusão, o princípio fundamental aqui é o respeito à vulnerabilidade e dignidade da criança.
            O cuidado, a privacidade e a segurança emocional da aluna devem prevalecer sobre o interesse acadêmico do pesquisador.
            """)
        else:
            st.success("""
            ✅ **Decisão Ética Exemplar!**
            Exatamente! A ética vai muito além de protocolos formais assinados — exige escuta sensível, prudência e empatia.
            Conforme o Estatuto da Criança e do Adolescente (ECA, 1990) e os princípios de Paulo Freire (1996), a ética envolve respeitar a subjetividade do educando, garantindo a sua proteção integral.
            """)
            
        st.button("Avançar para o Dilema 2 ▶", on_click=next_step, type="primary")
    else:
        st.button("Voltar", on_click=prev_step, key="back_d1")

# ----------------- TELA 5: JORNADA 5 - DILEMA 2 (DADOS DIGITAIS) -----------------
elif st.session_state.jornada == 5:
    render_teacher_speech(
        "Ótimo progresso! Agora vamos para o segundo e último dilema, "
        "focando na complexa relação entre o público e o privado no ambiente digital."
    )
    
    st.markdown("<h2 class='gradient-text'>Jornada 5: Dilema 2 - Pesquisa em Plataformas e Redes Sociais</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="dilemma-card">
        <h4 style="color: #1e3a8a;">O Cenário:</h4>
        <p style="font-size: 1.05rem; line-height: 1.6; color: #334155;">
            Um grupo de pesquisadores em educação analisa a expressão de emoções de alunos em ambientes virtuais de aprendizagem 
            (como fóruns do Moodle, grupos de WhatsApp da turma ou comentários em plataformas escolares). 
            Os dados são coletados a partir de postagens públicas, sem identificação nominal dos estudantes.
            <br><br>
            Durante a análise, os pesquisadores deparam-se com mensagens textuais que revelam situações graves de <b>sofrimento psíquico, bullying escolar e conflitos interpessoais profundos</b>.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    choice = st.radio(
        "Como a equipe de pesquisadores deve proceder em relação a essas postagens?",
        [
            "Selecione uma opção...",
            "Opção A: É eticamente legítimo analisar e publicar trechos literais dessas mensagens diretamente (sem os nomes), uma vez que elas são publicamente acessíveis na rede.",
            "Opção B: É necessário evitar a publicação direta de trechos literais que permitam reidentificação via buscas web e buscar consentimento informado ampliado, reconhecendo que os alunos escreveram as mensagens em um contexto interpessoal de confiança."
        ],
        index=0 if st.session_state.dilema2_choice is None else ["A", "B"].index(st.session_state.dilema2_choice) + 1
    )
    
    if choice and choice != "Selecione uma opção...":
        st.session_state.dilema2_choice = "A" if "Opção A" in choice else "B"
        
        if st.session_state.dilema2_choice == "A":
            st.warning("""
            ⚠️ **Reflexão Crítica (Cuidado necessário):**
            Atenção! Em ambientes virtuais, a fronteira entre público e privado é ambígua. 
            Publicar trechos literais de fóruns ou grupos fechados (mesmo sem nomes) permite que as pessoas e seus autores sejam reidentificados através de buscas na internet. Isso rompe a relação de confiança e pode expor o participante a novos episódios de bullying.
            """)
        else:
            st.success("""
            ✅ **Decisão Ética Exemplar!**
            Parabéns! De acordo com Boaventura de Sousa Santos (2008) e Maria Cecília Minayo (2012), a ética digital deve basear-se no cuidado e no consentimento. 
            Dados publicamente acessíveis na internet não significam dados livres de cuidado ético.
            """)
            
        st.button("Concluir o Jogo 🏁", on_click=next_step, type="primary")
    else:
        st.button("Voltar", on_click=prev_step, key="back_d2")

# ----------------- TELA 6: ENCERRAMENTO (FINAL) -----------------
elif st.session_state.jornada == 6:
    render_teacher_speech(
        "Parabéns! Você concluiu com sucesso todas as jornadas do jogo sobre <b>Ética na Pesquisa</b>! "
        "Você demonstrou compreender a importância do compromisso social, das bases filosóficas, "
        "das regulamentações legais e da sensibilidade diária necessária para proteger os participantes."
    )
    
    st.markdown("<h2 class='gradient-text' style='text-align: center;'>Conquista Desbloqueada! 🏆</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="glass-card" style="text-align: center; border-color: rgba(16, 185, 129, 0.4); background: rgba(240, 253, 244, 0.85);">
        <h3 style="color: #065f46; margin-bottom: 10px;">Pesquisador(a) Consciente & Ético(a)</h3>
        <p style="color: #047857; font-size: 1.05rem;">
            Você completou o percurso formativo das Jornadas 3, 4 e 5, superando os dilemas escolares e digitais com foco na dignidade humana!
        </p>
        <hr style="border-color: rgba(16, 185, 129, 0.2); margin: 20px 0;">
        <div style="text-align: left; max-width: 600px; margin: 0 auto; color: #1f2937;">
            <p><b>Recapitulando as Aprendizagens:</b></p>
            <div class="lgpd-point"><b>Caráter e Relação:</b> A ética é construída na convivência e na relação com o outro (Aristóteles).</div>
            <div class="lgpd-point"><b>Engajamento Social:</b> A pesquisa educacional tem responsabilidade política e não é neutra (Saviani e Freire).</div>
            <div class="lgpd-point"><b>Amparo Burocrático:</b> Documentos como TCLE e TALE asseguram consentimento e assentimento formais.</div>
            <div class="lgpd-point"><b>Proteção de Dados:</b> A LGPD orienta o tratamento ético dos dados, resguardando o sigilo e segurança.</div>
            <div class="lgpd-point"><b>Cuidado Digital:</b> Dados públicos em redes digitais exigem cautela e anonimização rigorosa.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.button("Jogar Novamente 🔄", on_click=restart_game, type="primary")
