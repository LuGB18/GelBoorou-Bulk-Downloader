# GelBooru Bulk Downloader

Bulk downloader de imagens e videos do **GelBooru**, escrito em **Python**, com foco em:

- Facilidade de uso  

---

## Funcionalidades

- Download em massa de posts do GelBooru  
- Filtro por tags  
- Suporte a múltiplas páginas  
- Downloads paralelos (multithreading)  
- Configuração externa (API e comportamento pelo config.json)   
- Prevenção de sobrecarga do sistema  

---

## 📁 Estrutura do Projeto

```
GelBooru-Bulk-Downloader/
├── main.py            # Lógica principal / interface CLI
├── configlib.py       # Configurações e carregamento de dados
├── gelboorulib.py     # Comunicação com a API e download
├── requirements.txt   # Dependências do projeto
└── README.md
```

---

## Requisitos

- Python **3.10** ou superior  
- Conexão com a internet  
- Conta no GelBooru (para API Key)  

### Dependências

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuração

Antes de executar o projeto, configure seus dados no arquivo `configlib.py`.

```python
{
    "gelbooru": {
        "endpoint": "https://gelbooru.com/index.php"
    },
    "credentials": {
        "userid": "<SEU USER ID>",
        "apikey": "<SUA CHAVE API>"
    },
    "downloads": {
        "folder": "<SEU LOCAL DE DOWNLOAD>"
    },
    "system": {
        "allow_cpu_get_overwhelmed_by_downloads": false
    }
}
```

---

## Como Usar

```bash
python main.py
```
