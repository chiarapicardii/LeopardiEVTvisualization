import os
import requests

API_URL = "https://wikileopardi.altervista.org/wiki_leopardi/api.php"

params = {
    "action": "query",
    "list": "allimages",
    "aiprefix": "F31",    
    "ailimit": "500",     
    "format": "json"
}

# CORREZIONE: La cartella esatta che si vede nei log di Angular
cartella_destinazione = os.path.join("src", "assets", "images")
os.makedirs(cartella_destinazione, exist_ok=True)

print(f"Download mirato per EVT in corso...")

try:
    response = requests.get(API_URL, params=params).json()
    immagini = response.get("query", {}).get("allimages", [])

    if not immagini:
        print("Nessuna immagine trovata.")
    else:
        for img in immagini:
            nome_file = img["name"]
            url_file = img["url"]
            
            # CORREZIONE: Forza tutto in minuscolo .jpg come richiesto dalla console
            nome_base, _ = os.path.splitext(nome_file)
            nome_file = nome_base + ".jpg"

            print(f"Scaricando: {nome_file}...")

            img_data = requests.get(url_file).content
            percorso_salvataggio = os.path.join(cartella_destinazione, nome_file)

            with open(percorso_salvataggio, "wb") as f:
                f.write(img_data)

        print(f"\n✅ File pronti nella cartella richiesta da EVT!")

except Exception as e:
    print(f"Errore: {e}")