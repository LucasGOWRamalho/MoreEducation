# MoreEducation 
 Teclado com os Olhos
MoreEducation é um projeto de acessibilidade cujo objetivo é permitir que pessoas com deficiência possam se comunicar usando apenas o movimento dos olhos. O sistema usa OpenCV e Dlib para capturar e analisar o olhar do usuário, e renderiza um teclado interativo no navegador com Next.js. Ao identificar onde o usuário está olhando, o sistema irá simular a digitação.

# 🚀 Objetivo
Criar um sistema onde:

- O usuário olha para a tela.

- O sistema detecta a direção do olhar com OpenCV + Dlib.

- O usuário pisca para confirmar uma tecla.

- Um teclado virtual é exibido em uma página Next.js (front/teclado/page.tsx).

- Comunicação entre front-end e back-end ocorre via WebSockets ou API REST.

# 🧠 Tecnologias
### 🎯 Back-End (Visão Computacional)
- Python

- OpenCV

- Dlib (shape predictor 68 pontos)

- WebSocket / FastAPI para comunicação com o front

- Módulo de detecção de piscar e direção do olhar

### 💻 Front-End
- Next.js (React)

- TypeScript

- Teclado virtual responsivo (dividido em seções por área da tela)

- Comunicação com back-end via WebSocket

# 🏗️ Arquitetura

### 📁 projeto-raiz
├── front                  
│       └── teclado
|               |
│               └── page.tsx        
├── backend
│   └── main.py            
│   └── gaze_tracker.py     
├── shape_predictor_68.dat 
├── README.md
🔮 Planejamento: Próximos Passos



### ✅ Etapa 1: Back-End com OpenCV
- Configurar main.py para capturar rosto e olhos ✅

- Modularizar detecção do olhar (gaze direction)

- Detectar em qual direção o usuário está olhando (esquerda, centro, direita)

- Detectar piscadas (confirmação de tecla)

- Criar comunicação WebSocket ou API para enviar resultado para o front

### ⌨️ Etapa 2: Front-End com Teclado Virtual
- Criar layout do teclado na página front/teclado/page.tsx

- Dividir tela em zonas correspondentes aos blocos do teclado

- Receber dados do back-end (posição do olhar) e destacar zona da tela

- Simular digitação com piscar (confirmação)

### 🔗 Etapa 3: Integração
- Conectar front e back usando WebSocket (ou REST para testes iniciais)

- Realizar testes de usabilidade com cursor visual (foco) e piscadas

### 🌍 Etapa 4: Acessibilidade Real
- Melhorar acurácia da detecção

- Adicionar configurações de acessibilidade (tamanho da fonte, contraste, etc.)

- Internacionalização (i18n)

- Feedback auditivo (opcional)

## 📸 Imagem Futuro
- O usuário poderá:

- Acessar o site via webcam

- Navegar no teclado com os olhos

- Piscar para selecionar letras e formar frases

- Enviar mensagens com autonomia

