# app.py
# Versión web (Streamlit) del simplificador.
# La lógica es la misma que en simplificador_simple.py;
# solo cambia cómo se pide el texto y cómo se muestra el resultado.

from pathlib import Path
import pandas as pd
import streamlit as st

# --- 1. Cargar el diccionario (igual que antes) -------------------------
ruta = Path(__file__).parent / "candidatos_con_explicacion.csv"
df = pd.read_csv(ruta, encoding="utf-8-sig")
df = df.dropna(subset=["explicación sencilla"])

# --- 2. La interfaz: título, cuadro de texto y botón --------------------
st.title("📄 Entiende tus papeles")

# Esto sustituye al input(): crea un cuadro grande donde pegar el texto
texto = st.text_area("Pegue aquí el texto que no entiende:", height=250)

# Esto crea el botón. El código de dentro solo se ejecuta cuando se pulsa.
if st.button("Explicar con palabras sencillas"):

    if texto.strip() == "":
        st.warning("Primero escriba o pegue un texto.")
    else:
        # --- 3. Preparar el texto (igual que antes) ----------------------
        texto_limpio = texto.lower()

        for signo in ',.;:()¿?¡!"':
            texto_limpio = texto_limpio.replace(signo, " ")

        palabras_pequeñas = ["de", "del", "la", "el", "los", "las", "en", "y", "a", "para", "por", "con"]
        palabras = [p for p in texto_limpio.split() if p not in palabras_pequeñas]
        texto_limpio = " " + " ".join(palabras) + " "

        # --- 4. Buscar las palabras difíciles (igual que antes) ----------
        encontradas = []

        for _, fila in df.iterrows():
            termino = fila["termino"]
            explicacion = fila["explicación sencilla"]

            formas = [termino, termino + "s", termino + "es"]
            if termino.endswith("ón"):
                formas.append(termino[:-2] + "ones")

            for forma in formas:
                if " " + forma + " " in texto_limpio:
                    encontradas.append((termino, explicacion))
                    break

        # --- 5. Mostrar el resultado (aquí st.* sustituye a print) -------
        if encontradas:
            st.subheader("Palabras que pueden resultar difíciles")
            for termino, explicacion in encontradas:
                st.write(f"**{termino}**: {explicacion}")
        else:
            st.info("No he encontrado palabras difíciles en este texto.")
