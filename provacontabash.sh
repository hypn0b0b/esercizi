#!/bin/bash

# Directory in cui cercare i file script
directory="$1"

# Verifica se è stata fornita una directory come argomento
if [ -z "$directory" ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

# Assicurati che la directory esista
if [ ! -d "$directory" ]; then
  echo "La directory $directory non esiste."
  exit 1
fi

# Inizializza un array associativo per conteggiare gli interpreti
declare -A interpreter_counts

# Utilizza il comando find per cercare tutti i file nella directory
# Poi usa il comando file per determinare il tipo di file
# E conta le occorrenze di ciascun interprete
while IFS= read -r -d '' script_file; do
  # Verifica se il file è di tipo binario
  if [ -n "$(file -b --mime-encoding "$script_file" | grep -E '^binary$')" ]; then
    continue
  fi

  shebang=$(head -n 1 "$script_file")
  if [[ "$shebang" =~ ^#!/ ]]; then
    interpreter="${shebang:2}"
    ((interpreter_counts["$interpreter"]++))
  fi
done < <(find "$directory" -type f -print0)

# Stampa il conteggio degli script per ciascun interprete
for interpreter in "${!interpreter_counts[@]}"; do
  count="${interpreter_counts["$interpreter"]}"
  echo "$count #!$interpreter"
done


