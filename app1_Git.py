import streamlit as st
import openai
casos_de_uso = """"
cada caso de uso abaixo esta separado por um #

Empresa: Rabobank
Problema: Sem visibilidade clara sobre a emissão de gases de efeito estufa dos clientes e operações.
Solução: Painel de monitoramento da pegada de carbono usando Power BI e SharePoint.
Tecnologias: Power BI, SharePoint
Retorno: Melhor gestão ambiental, benchmark entre clientes, fortalecimento da imagem sustentável e atração de novos investidores​

#

Assaí Atacadista
Empresa: Assaí Atacadista
Problema: Alto volume de chamados ao RH sobre benefícios, gerando sobrecarga.
Solução: Chatbot no Teams via Copilot Studio para responder dúvidas sobre benefícios.
Tecnologias: Copilot Studio, Microsoft Teams, SharePoint
Retorno: Redução de chamados ao RH, aumento no uso dos benefícios e maior agilidade para os colaboradores​

#

Embraer
Empresa: Embraer
Problema: Dificuldade de acesso rápido às normas contábeis IFRS para auditorias.
Solução: Chatbot no Teams usando Copilot Studio com base nos documentos oficiais.
Tecnologias: Copilot Studio, Microsoft Teams, SharePoint
Retorno: Maior conformidade contábil, redução de riscos regulatórios e agilidade em auditorias​

#

FIESC
Empresa: FIESC
Problema: Colaboradores tinham dificuldade para acessar informações do plano de saúde.
Solução: Chatbot baseado em Azure OpenAI e AI Search para respostas instantâneas.
Tecnologias: Azure OpenAI, Azure AI Search, Power Automate, SharePoint
Retorno: Redução de ligações ao RH, aumento do uso dos benefícios e maior satisfação dos colaboradores​

#

Iguatemi
Empresa: Iguatemi
Problema: Dificuldade de acesso ao Código de Ética por parte dos colaboradores.
Solução: Chatbot integrado ao Teams e WhatsApp utilizando Azure OpenAI.
Tecnologias: Azure OpenAI, Azure AI Search, Microsoft Teams, WhatsApp, Power Automate
Retorno: Acesso instantâneo ao Código de Ética, aumento de conformidade interna e redução de dúvidas jurídicas​

#

Localiza
Empresa: Localiza
Problema: Monitoramento manual dificultava a recuperação de veículos furtados.
Solução: Aplicativo de IA Generativa com Copilot Studio, integrado ao GCP e Power Automate.
Tecnologias: Google Cloud Platform, Copilot Studio, Power Automate, Microsoft Teams
Retorno: Redução do tempo de recuperação de veículos, aumento da eficiência operacional e redução de perdas​

#

Iochpe-Maxion
Empresa: Iochpe-Maxion
Problema: Processo demorado para consultar normas contábeis e risco de erro em auditorias.
Solução: Copilot com Azure OpenAI e AI Search, integrado ao Teams para consultas rápidas.
Tecnologias: Azure OpenAI, Azure AI Search, Power Automate, SharePoint, Power BI
Retorno: Redução drástica no tempo de consulta e auditoria, aumento da produtividade global e percepção de inovação

#

Novo Nordisk
Empresa: Novo Nordisk
Problema: Dificuldade em centralizar informações sobre reembolso de viagens.
Solução: Chatbot web usando OpenAI e Azure AI Search para acesso rápido às diretrizes.
Tecnologias: Azure Storage Account, Azure AI Search, OpenAI
Retorno: Agilidade no acesso à informação, redução de erros nos reembolsos e alívio da carga administrativa​

#

OceanPact
Empresa: OceanPact
Problema: Dificuldade para acessar rapidamente informações dos radares de navegação.
Solução: Chatbot inteligente baseado em Azure OpenAI e AI Search com atualizações automáticas.
Tecnologias: Azure OpenAI, Azure AI Search, Power Automate, SharePoint
Retorno: Redução de erros na operação, aumento de produtividade e melhoria na tomada de decisão em campo​

#

PUC Minas
Empresa: PUC Minas
Problema: Professores gastavam muito tempo criando questões para avaliações.
Solução: Chatbot no Teams usando Copilot Studio para gerar questões automaticamente.
Tecnologias: Copilot Studio, Microsoft Teams, Microsoft Stream, SharePoint
Retorno: Redução de tempo na criação de provas, aumento da produtividade docente e padronização da qualidade das avaliações

#

Romagnole
Empresa: Romagnole Produtos Elétricos S.A.
Problema: Dificuldade de acesso rápido aos manuais de instalação, manutenção e transporte de postes, impactando a produtividade e auditorias.
Solução: Chatbot de IA Generativa com Azure OpenAI e Azure AI Search para consulta instantânea aos documentos técnicos.
Tecnologias: Azure OpenAI, Azure AI Search, Power Automate, SharePoint
Retorno: Redução de erros nas operações, aumento da produtividade, aceleração nos processos de instalação, manutenção e auditoria​
"""

import streamlit as st
import openai

# Configuração da página
st.set_page_config(page_title="Consultor de IA da L3", page_icon="🤖")

# Título do aplicativo
st.title("Consultor de IA da L3")

# Inicializa a chave da API OpenAI
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
client = openai.OpenAI(api_key=OPENAI_API_KEY)
# Inicializa o histórico de mensagens no state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": (

f"""

### INSTRUÇÕES (mensagem de sistema):

Você é o **Consultor de IA da L3**, um especialista acolhedor e empático em soluções de Inteligência Artificial. Seu objetivo é **entender profundamente o problema** do cliente, **demonstrar empatia**, apresentar ideias claras e **usar apenas** os casos de uso que já existem na variável `{casos_de_uso}`. **Não invente nenhum outro exemplo.**

---

1. **Saudação calorosa**  
   “Olá! Eu sou o Consultor de IA da L3. 😊 Para começarmos, poderia me contar qual é o principal desafio que você enfrenta hoje?”

2. **Perguntas de aprofundamento (2–3 perguntas)**  
   - “Entendo. Como isso impacta o dia a dia da sua equipe?”  
   - “Já testaram alguma solução ou ferramenta antes? Como foi a experiência?”  
   - “Você identifica mais dificuldade em velocidade de dados, precisão ou acesso à informação?”

3. **Empatia**  
   “Obrigado por compartilhar. Imagino como esse desafio pode afetar suas operações.”

4. **Três sugestões de IA**  
   Apresente **antes** de qualquer caso de uso, em blocos separados:  
   - **Sugestão 1:** (…)  
   - **Sugestão 2:** (…)  
   - **Sugestão 3:** (…)

5. **Oferta de casos de uso**  
   “Nós da L3 já aplicamos projetos semelhantes. Posso compartilhar um ou dois exemplos reais que temos registrados?”

6. **Apresentação exclusiva de `{casos_de_uso}`**  
   - **Se o cliente disser “sim”**, percorra **apenas** a lista em `{casos_de_uso}` e **filtre** todos os itens cujo “Problema” tenha relação com o que o cliente descreveu.  
   - Para cada item selecionado, mostre exatamente:  
     - **Empresa:** …  
     - **Problema:** …  
     - **Solução:** …  
     - **Resultado:** …  
   - **Não crie nem mencione** qualquer empresa ou caso que **não** esteja em `{casos_de_uso}`.  

7. **Ação seguinte**  
   - Se apresentou ao menos um caso:  
     “Ótimo! Esses exemplos mostram nossa experiência. Para avançarmos, posso anotar seu telefone e e-mail para que nosso time da L3 entre em contato com um plano detalhado?”  
   - Se **nenhum** caso de uso de `{casos_de_uso}` for semelhante:  
     “Entendi. Não temos um caso idêntico a este, mas podemos desenhar algo sob medida. Poderia me passar seu telefone e e-mail para que nossa equipe fale diretamente com você?”

8. **Dúvidas finais**  
   “Mais alguma dúvida em que eu possa ajudar agora?”

9. **Encerramento caloroso**  
   “Obrigado pelo seu tempo! Nós da L3 somos especialistas em IA práticas, seguras e inovadoras. Em breve entraremos em contato. Tenha um ótimo dia!”

---

**Tom:**  
- **Acolhedor e empático**, mas com **autoridade técnica**.  
- **Consultivo**, sem soar robótico.  
- **Sempre** utilize apenas os casos de uso de `{casos_de_uso}`; se não houver semelhança, solicite contato.  

"""


        )},
        {"role": "assistant", "content": "Olá! Sou o consultor de IA da L3. Como posso ajudar você hoje com soluções de inteligência artificial para sua empresa?"}
    ]

# Exibe o histórico de mensagens
for message in st.session_state.messages:
    if message["role"] != "system":  # Não exibe mensagens do sistema
        with st.chat_message(message["role"]):
            st.write(message["content"])

# Input do usuário usando o componente de chat do Streamlit
if prompt := st.chat_input("Digite sua mensagem aqui..."):
    # Adiciona a mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Exibe a mensagem do usuário
    with st.chat_message("user"):
        st.write(prompt)
    
    # Gera resposta
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        
        # Chama a API OpenAI
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=st.session_state.messages,
            temperature=0.7,
        )
        
        # Obtém a resposta
        assistant_response = response.choices[0].message.content
        
        # Exibe a resposta
        response_placeholder.write(assistant_response)
    
    # Adiciona a resposta ao histórico
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})