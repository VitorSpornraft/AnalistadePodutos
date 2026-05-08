#  TrendHunter Bot

## Visão Geral
O **TrendHunter** é um sistema de automação inteligente desenvolvido em Python para o mercado de hardware e marketing de afiliados. O objetivo do projeto é monitorar picos de interesse em componentes de tecnologia, validar oportunidades reais de preço e automatizar a divulgação em canais de ofertas.

##  Arquitetura do Sistema
O projeto é dividido em três módulos principais para garantir modularidade e facilidade de manutenção:

1.  **Monitor de Tendências (The Hunter):** Consome o feed RSS oficial do Google Trends para identificar termos em ascensão no Brasil em tempo real.
2.  **Validador de Preços (The Scraper):** Realiza web scraping em e-commerces de hardware para verificar se o item em alta está com preço competitivo.
3.  **Distribuidor (Telegram Bot):** Formata os dados, gera links de afiliado e dispara alertas automáticos via API do Telegram.

##  Tecnologias e Ferramentas
* **Linguagem:** Python 3.12+
* **Ambiente:** WSL (Windows Subsystem for Linux) - Ubuntu 24.04
* **Bibliotecas Principais:**
    * `requests`: Comunicação com APIs e feeds externos.
    * `xml.etree.ElementTree`: Processamento de dados estruturados do Google.
    * `python-dotenv`: Gerenciamento seguro de credenciais (em implementação).

##  Como Executar o Projeto

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/VitorSpornraft/AnalistadePodutos
   cd AnalistadePodutos
2. **Configurar o ambiente virtual:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
3. **Instalar dependências:**
    ```bash
    pip install -r requirements.txt
4. **Rodar o monitor inicial**
    ```bash
    python hunter.py
