import os
import time
import requests

# Caminho onde o Sentinela joga os pacotes suspeitos
WATCH_DIR = "/tmp/traffic_buffer"
MODELO = "qwen2.5-coder:3b"

def analisar_trafego(payload):
    prompt = (
        "Você é um motor de inspeção profunda de pacotes (DPI). "
        "Analise o payload de rede abaixo. Identifique se é um ataque (XSS, SQLi, Exploit) ou tráfego legítimo. "
        "Responda APENAS: 'ATAQUE: [tipo]' ou 'NORMAL'.\n\n"
        f"Payload: {payload}"
    )
    try:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": MODELO, "stream": False, "prompt": prompt
        }, timeout=10)
        return response.json().get('response', 'NORMAL')
    except: return "ERRO_IA"

def monitorar():
    if not os.path.exists(WATCH_DIR): os.makedirs(WATCH_DIR)
    
    print(f"[*] Auditor Ativo online. Monitorando {WATCH_DIR}...")
    while True:
        for arquivo in os.listdir(WATCH_DIR):
            caminho = os.path.join(WATCH_DIR, arquivo)
            with open(caminho, 'r') as f:
                payload = f.read()
                
            veredito = analisar_trafego(payload)
            print(f"[*] Payload: {arquivo} | Veredito: {veredito}")
            
            if "ATAQUE" in veredito:
                # Aqui você integra com o seu bloqueio de firewall
                print(f"[!] AÇÃO: Banindo origem do payload {arquivo}")
            
            os.remove(caminho) # Limpa após análise
        time.sleep(0.5)

if __name__ == "__main__":
    monitorar()
