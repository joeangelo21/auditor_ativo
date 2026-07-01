## ⚙️ Configuração do Ambiente Local

Para que o Auditor Ativo funcione corretamente em sua máquina Kali Linux, siga estes passos:

1. **Instalação do Motor Cognitivo (Ollama):**
   - Certifique-se de ter o [Ollama](https://ollama.com/) instalado.
   - Puxe o modelo Coder necessário para a análise:
     ```bash
     ollama pull qwen2.5-coder:3b
     ```

2. **Preparação do Buffer de Tráfego:**
   O sistema utiliza um sistema de arquivos para comunicação entre módulos. Garanta que o diretório de comunicação exista:
   ```bash
   sudo mkdir -p /tmp/traffic_buffer
   sudo chmod 777 /tmp/traffic_buffer
Dependências do Python:
Certifique-se de estar com seu ambiente virtual (venv) ativo e as bibliotecas instaladas:

Bash
pip install requests
Execução:
Inicie o auditor no terminal:

Bash
python3 auditor_ativo.py

# Auditor Ativo (Motor Cognitivo)

O **Auditor Ativo** é o módulo de inspeção profunda de pacotes (DPI) e análise cognitiva do ecossistema de defesa cibernética *SegurancaComIA*. Ele foi projetado para atuar como uma camada de análise inteligente, capaz de ler o conteúdo bruto do tráfego de rede e emitir vereditos de segurança utilizando modelos de linguagem local.

## 🏗️ Arquitetura de Defesa

O sistema opera de forma desacoplada para garantir performance e resiliência:

1. **Ingestão:** O tráfego suspeito é capturado e depositado em um buffer de comunicação (`/tmp/traffic_buffer`).
2. **Análise Cognitiva:** O `auditor_ativo.py` monitora esse diretório em tempo real, lendo payloads e submetendo-os ao motor de IA (Ollama/Qwen2.5-coder).
3. **Decisão:** Com base na análise semântica do payload, o sistema classifica a ameaça (XSS, SQLi, Exploit, Normal) e gera um feedback para bloqueio imediato.

## 🚀 Funcionalidades
- **Inspeção Profunda (DPI):** Analisa o conteúdo real do payload, não apenas assinaturas fixas.
- **Análise Semântica:** Uso de LLMs (Qwen2.5-coder) para identificar intenções maliciosas em padrões sutis.
- **Baixa Latência:** Processamento assíncrono para não impactar o fluxo de rede.
- **Fácil Integração:** Comunicação via sistema de arquivos (Unix Way), permitindo integração com qualquer Firewall/IDS.

## 🛠️ Requisitos
- **Ollama:** Rodando localmente com o modelo `qwen2.5-coder:3b`.
- **Python 3.x:** Dependências listadas no `requirements.txt`.
- **Permissões:** Acesso de leitura/escrita em `/tmp/traffic_buffer/`.

## ⚙️ Como utilizar
1. Garanta que o Ollama esteja rodando: `ollama serve`.
2. Certifique-se de que o diretório de buffer exista: `mkdir -p /tmp/traffic_buffer`.
3. Inicie o auditor:
   ```bash
   python3 auditor_ativo.py
🛡️ Aviso Legal
Este software é uma ferramenta experimental. O uso de automação para bloqueio de tráfego deve ser configurado com White-lists para evitar a negação de serviço de recursos legítimos da rede.

Autor: Joelson Angelo | Systems Developer
