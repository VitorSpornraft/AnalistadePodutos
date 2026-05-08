import requests
import xml.etree.ElementTree as ET

PALAVRAS_CHAVE = [
    "rtx", "ryzen", "intel", "amd", "nvidia", "radeon", 
    "ssd", "nvme", "notebook", "lenovo", "loq", "gamer", 
    "processador", "placa de vídeo", "hardware", "monitor"
]

def validar_nicho(titulo):
    titulo_formatado = titulo.lower()
    for palavra in PALAVRAS_CHAVE:
        if palavra in titulo_formatado:
            return True
    return False

def buscar_tendencias_oficiais():
    print("Conectando API...")
    
    url_rss = "https://trends.google.com/trending/rss?geo=BR"
    
    try:
        resposta = requests.get(url_rss)
        resposta.raise_for_status() # Verifica se a conexão foi bem sucedida (Status 200)
        
        root = ET.fromstring(resposta.content)
        items = root.findall('.//item')
        
        print("\nRESULTADOS FILTRADOS\n")

        encontrou_oportunidade = False

        for item in items:
            titulo = item.find('title').text
            
            if validar_nicho(titulo):
                 encontrou_oportunidade = True
                 trafego_tag = item.find('{https://trends.google.com/trending/rss}approx_traffic')
                 trafego = trafego_tag.text if trafego_tag is not None else "N/A"
                
                 print(f"[ALERTA] {titulo} (Volume: {trafego})")
                
        if not encontrou_oportunidade:
            print("Nenhum termo de hardware em alta no momento. O script continuará monitorando.")
            
    except Exception as e:
        print(f"Erro ao buscar dados na rota oficial: {e}")

if __name__ == "__main__":
    buscar_tendencias_oficiais()