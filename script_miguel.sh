#!/bin/bash

# ============================================================
# script_miguel.sh
#
# Que hace:
#   1. Recibe un .zip y una carpeta destino.
#   2. Descomprime el .zip en una carpeta temporal.
#   3. Ordena los archivos en documentos/, imagenes/, codigo/,
#      multimedia/ y otros/.
#   4. Revisa cada archivo .py buscando PySide6.
#   5. Imprime un resumen final.
#
# Uso:
#   ./script_miguel.sh <archivo.zip> <directorio_destino>
#
# Ejemplo:
#   ./script_miguel.sh proyecto_analisis.zip resultado
# ============================================================


# ------------------------------------------------------------
# PASO 1: revisar que lleguen exactamente 2 argumentos
# ------------------------------------------------------------
# "$#" es el numero de argumentos que escribiste en la terminal.
if [ "$#" -ne 2 ]; then
    echo "Uso: ./script_miguel.sh <archivo.zip> <directorio_destino>"
    exit 1
fi

ARCHIVO_ZIP="$1"
DESTINO="$2"


# ------------------------------------------------------------
# PASO 2: revisar que el .zip exista
# ------------------------------------------------------------
# -f pregunta: "existe y es un archivo normal?"
if [ ! -f "$ARCHIVO_ZIP" ]; then
    echo "Error: no existe el archivo '$ARCHIVO_ZIP'"
    exit 1
fi

# Revisar tambien que unzip este instalado en la computadora.
# "command -v unzip" devuelve la ruta del programa si existe.
if ! command -v unzip > /dev/null 2>&1; then
    echo "Error: el programa 'unzip' no esta instalado."
    exit 1
fi


# ------------------------------------------------------------
# PASO 3: descomprimir el .zip en una carpeta temporal
# ------------------------------------------------------------
# mktemp -d crea una carpeta temporal con nombre unico
# (asi no chocamos con carpetas que ya existan).
TEMPORAL=$(mktemp -d)

echo "Descomprimiendo '$ARCHIVO_ZIP' en una carpeta temporal..."

# -q = modo silencioso, -d = carpeta donde se descomprime.
# El "if !" significa: si el comando FALLA, haz esto.
if ! unzip -q "$ARCHIVO_ZIP" -d "$TEMPORAL"; then
    echo "Error: no se pudo descomprimir el archivo (revisa que sea un .zip valido)."
    rm -rf "$TEMPORAL"
    exit 1
fi


# ------------------------------------------------------------
# PASO 4: crear las subcarpetas en el destino
# ------------------------------------------------------------
# -p = crea la carpeta solo si no existe (y no da error si ya existe).
mkdir -p "$DESTINO/documentos"
mkdir -p "$DESTINO/imagenes"
mkdir -p "$DESTINO/codigo"
mkdir -p "$DESTINO/multimedia"
mkdir -p "$DESTINO/otros"

echo "Organizando archivos en '$DESTINO'..."


# ------------------------------------------------------------
# PASO 5: recorrer los archivos y copiarlos a su carpeta
# ------------------------------------------------------------
# find busca TODOS los archivos dentro de la carpeta temporal,
# incluyendo los que estan dentro de subcarpetas.
#
# El "while read" lee una ruta a la vez. Usamos IFS= y -r para
# que los nombres con espacios (como "Describing People.jpeg")
# se lean completos y no se partan.
find "$TEMPORAL" -type f | while IFS= read -r RUTA; do

    # macOS a veces mete una carpeta "__MACOSX" con basura al comprimir.
    # La saltamos para no copiar archivos inutiles.
    case "$RUTA" in
        *__MACOSX*) continue ;;
    esac

    NOMBRE=$(basename "$RUTA")

    # Sacar la extension = lo que va despues del ultimo punto.
    # Si el nombre no tiene punto, no hay extension.
    if [ "$NOMBRE" = "${NOMBRE%.*}" ]; then
        EXTENSION=""
    else
        EXTENSION="${NOMBRE##*.}"
    fi

    # Pasar la extension a minusculas para que .JPG y .jpg
    # se traten igual. tr cambia letras mayusculas por minusculas.
    EXTENSION=$(echo "$EXTENSION" | tr 'A-Z' 'a-z')

    # Elegir la carpeta segun la extension.
    case "$EXTENSION" in
        py|pyw)
            CARPETA="$DESTINO/codigo" ;;
        txt|md|pdf|doc|docx|ppt|pptx|xls|xlsx|csv)
            CARPETA="$DESTINO/documentos" ;;
        jpg|jpeg|png|gif|bmp|webp|svg|ico|tif|tiff)
            CARPETA="$DESTINO/imagenes" ;;
        mp3|wav|mp4|mov|avi|mkv|m4a)
            CARPETA="$DESTINO/multimedia" ;;
        *)
            # Todo lo demas (zipped, ttf, sin extension, etc.)
            CARPETA="$DESTINO/otros" ;;
    esac

    # Ruta final del archivo dentro del destino.
    RUTA_FINAL="$CARPETA/$NOMBRE"

    # Si ya existe un archivo con ese nombre, le agregamos _1, _2...
    # para no sobrescribir nada.
    if [ -e "$RUTA_FINAL" ]; then
        BASE="${NOMBRE%.*}"
        CONTADOR=1
        while [ -e "$RUTA_FINAL" ]; do
            if [ "$EXTENSION" = "" ]; then
                RUTA_FINAL="$CARPETA/${BASE}_$CONTADOR"
            else
                RUTA_FINAL="$CARPETA/${BASE}_$CONTADOR.$EXTENSION"
            fi
            CONTADOR=$((CONTADOR + 1))
        done
    fi

    cp "$RUTA" "$RUTA_FINAL"
    echo "  $NOMBRE  ->  $(basename "$CARPETA")/"

done

# Ya no necesitamos la carpeta temporal.
rm -rf "$TEMPORAL"


# ------------------------------------------------------------
# PASO 6: auditar los archivos .py buscando PySide6
# ------------------------------------------------------------
echo ""
echo "=============================================="
echo " AUDITORIA DE CODIGO PYTHON"
echo "=============================================="

# Contadores para el resumen final.
TOTAL_PY=0
TOTAL_CON_PYSIDE6=0

# El patron "*.py" toma todos los .py de la carpeta codigo.
for ARCHIVO in "$DESTINO/codigo/"*.py; do

    # Si la carpeta esta vacia, el patron se queda como "*.py"
    # (un archivo que no existe). Este chequeo lo evita.
    if [ ! -f "$ARCHIVO" ]; then
        continue
    fi

    TOTAL_PY=$((TOTAL_PY + 1))
    echo ""
    echo "Archivo: $ARCHIVO"

    # grep busca texto dentro del archivo:
    #   -n  muestra el numero de linea
    #   -i  ignora mayusculas/minusculas (pyside6 = PySide6)
    # Guardamos el resultado para revisar si encontro algo.
    COINCIDENCIAS=$(grep -n -i "PySide6" "$ARCHIVO")

    # -n en el if significa: "el texto no esta vacio?".
    if [ -n "$COINCIDENCIAS" ]; then
        TOTAL_CON_PYSIDE6=$((TOTAL_CON_PYSIDE6 + 1))
        echo "  SI usa PySide6. Coincidencias (linea: texto):"
        echo "$COINCIDENCIAS"
    else
        echo "  NO usa PySide6."
    fi

done


# ------------------------------------------------------------
# PASO 7: resumen final
# ------------------------------------------------------------
echo ""
echo "=============================================="
echo " RESUMEN"
echo "=============================================="
echo "Archivos .py analizados:              $TOTAL_PY"
echo "Archivos .py que usan PySide6:        $TOTAL_CON_PYSIDE6"
echo ""
echo "Listo. Archivos organizados en: $DESTINO"
