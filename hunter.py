import requests
import xml.etree.ElementTree as ET

def buscar_tendencias_oficiais():
    print("Conectando API...")
    
    url_rss = "https://trends.google.com/trending/rss?geo=BR"
    
    try:
        resposta = requests.get(url_rss)
        resposta.raise_for_status() # Verifica se a conexão foi bem sucedida (Status 200)
        
        root = ET.fromstring(resposta.content)
        
        print("\nTOP ASSUNTOS EM ALTA HOJE\n")

        items = root.findall('.//item')
        
        for item in items[:10]:
            titulo = item.find('title').text
            
            trafego_tag = item.find('{https://trends.google.com/trending/rss}approx_traffic')
            trafego = trafego_tag.text if trafego_tag is not None else "N/A"
            
            print(f" {titulo} (Volume: {trafego})")
            
    except Exception as e:
        print(f"Erro ao buscar dados na rota oficial: {e}")

if __name__ == "__main__":
    buscar_tendencias_oficiais()