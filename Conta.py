import os
import datetime

def conta_script(directory, log_file):
    # Dizionario per conteggiare gli interpreti
    interpreter_counts = {}

    # Scansione dei file nella directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Percorso completo del file
            file_path = os.path.join(root, file)

            # Apertura del file e lettura della prima riga (shebang)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    first_line = f.readline().strip()
            except Exception as e:
                continue

            # Verifica se la prima riga inizia con #!
            if first_line.startswith("#!"):
                interpreter = first_line[2:].strip()
                # Incremento del conteggio dell'interprete
                interpreter_counts[interpreter] = interpreter_counts.get(interpreter, 0) + 1

    # Stampa il conteggio degli script
    with open(log_file, 'a') as log:
        log.write(f"Data e Ora dell'Esecuzione: {datetime.datetime.now()}\n")
        log.write(f"Numero di File Trovati: {sum(interpreter_counts.values())}\n")
        log.write("Conteggio per Interprete:\n")
        # Stampa il conteggio degli script per ciascun interprete
        for interpreter, count in sorted(interpreter_counts.items(), key=lambda x: x[1], reverse=True):
            log.write(f"{count} {interpreter}\n")

if __name__ == "__main__":
    import sys

    # Assicurarsi che siano stati forniti due argomenti: la directory e il file di log
    if len(sys.argv) != 3:
        print("Usage: python conta_script.py <directory> <log_file>")
        sys.exit(1)

    directory = sys.argv[1]
    log_file = sys.argv[2]

    # Verifica se la directory esiste
    if not os.path.exists(directory):
        print(f"La directory '{directory}' non esiste.")
        sys.exit(1)

    conta_script(directory, log_file)


