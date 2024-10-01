import pdfplumber
import os

# Specifica il percorso del tuo file PDF
pdf_path = 'C:\\Users\\agvgica\\Pictures\\OdP.pdf'

# Specifica il percorso del file di testo nella stessa cartella dello script
script_dir = os.path.dirname(os.path.realpath(__file__))  # Ottieni la cartella dello script
txt_path = os.path.join(script_dir, 'output.txt')  # Crea il percorso completo per il file di output

# Apri il PDF e leggi il contenuto
try:
    with pdfplumber.open(pdf_path) as pdf:
        with open(txt_path, 'w', encoding='utf-8') as txt_file:  # Apri il file di testo in scrittura
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:  # Controlla se c'è del testo estratto
                    txt_file.write(f"Testo dalla pagina {i + 1}:\n")
                    txt_file.write(text + "\n\n")  # Scrivi il testo nel file
                else:
                    txt_file.write(f"Pagina {i + 1} non contiene testo leggibile.\n\n")
    print(f"Il contenuto è stato salvato in {txt_path}.")
except Exception as e:
    print(f"Si è verificato un errore: {e}")
