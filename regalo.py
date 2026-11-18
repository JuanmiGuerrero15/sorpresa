
import streamlit as st

st.set_page_config(
    page_title="Pruebas de la agente Lola",
    page_icon="🕵️"
)

# Mensajes iniciales: respetan los print originales
st.write("Bienvenida, agente Lola")
st.write(
    "Es hora de validar si has superado las pruebas "
    "y tienes los datos correctos:"
)

# 1. Coordenadas
with st.form("form_coordenadas"):
    coordenadas = st.text_input("Coordenadas:")
    enviar = st.form_submit_button("Comprobar")

if enviar:
    if coordenadas == "37.336895, -5.853140":
        st.session_state["coordenadas_ok"] = True
    else:
        st.session_state["coordenadas_ok"] = False

if st.session_state.get("coordenadas_ok", False):
    st.success("Coordenadas correctas.")
elif st.session_state.get("coordenadas_ok") is False:
    st.error("Coordenadas incorrectas.")

# 2. Fecha
if st.session_state.get("coordenadas_ok", False):
    with st.form("form_fecha"):
        fecha = st.text_input("Fecha:")
        enviar_fecha = st.form_submit_button("Comprobar fecha")

    if enviar_fecha:
        if fecha == "21/11/2026" or fecha == "21-11-2026" or fecha == "21-11":
            st.session_state["fecha_ok"] = True
        else:
            st.session_state["fecha_ok"] = False

    if st.session_state.get("fecha_ok", False):
        st.success("Fecha correcta.")
    elif st.session_state.get("fecha_ok") is False:
        st.error("Fecha incorrecta.")

# 3. Hora
if st.session_state.get("fecha_ok", False):
    with st.form("form_hora"):
        hora = st.text_input("Hora:")
        enviar_hora = st.form_submit_button("Comprobar hora")

    if enviar_hora:
        if hora == "9:00" or hora == "9":
            st.session_state["hora_ok"] = True
        else:
            st.session_state["hora_ok"] = False

    if st.session_state.get("hora_ok", False):
        st.success("Hora correcta.")
    elif st.session_state.get("hora_ok") is False:
        st.error("Hora incorrecta.")

# 4. Transporte
if st.session_state.get("hora_ok", False):
    with st.form("form_transporte"):
        transporte = st.text_input("¿Cuál será el transporte?:")
        enviar_transporte = st.form_submit_button(
            "Comprobar transporte"
        )

    if enviar_transporte:
        if transporte.lower() in [
            "auto", "coche", "automóvil"
        ]:
            st.session_state["transporte_ok"] = True
        else:
            st.session_state["transporte_ok"] = False

    if st.session_state.get("transporte_ok", False):
        st.success("Transporte correcto.")
    elif st.session_state.get("transporte_ok") is False:
        st.error("Transporte incorrecto.")

# 5. Equipaje
if st.session_state.get("transporte_ok", False):
    maleta = [
        "pijama", "polar", "sudadera",
        "chándal", "blusa", "jersey", "altavoz"
    ]

    with st.form("form_equipaje"):
        equipaje = st.text_input(
            "¿Qué debes llevar? Escribe solo un objeto:"
        )
        enviar_equipaje = st.form_submit_button(
            "Comprobar equipaje"
        )

    if enviar_equipaje:
        if equipaje.lower() in maleta:
            st.session_state["equipaje_ok"] = True
        else:
            st.session_state["equipaje_ok"] = False

    if st.session_state.get("equipaje_ok", False):
        st.success("Equipaje correcto.")
    elif st.session_state.get("equipaje_ok") is False:
        st.error("Equipaje incorrecto.")

# Mensajes finales: se mantienen todos los print originales
if st.session_state.get("equipaje_ok", False):
    st.write("Has superado con éxito las pruebas, enhorabuena")
    st.write(
        "La operación queda autorizada. Mañana, sábado "
        "21 de noviembre a las 9:00, espera en las "
        "coordenadas indicadas con tu equipaje."
    )
    st.write(
        "Un agente de confianza te recogerá en un vehículo "
        "(AUTO). Añade a tu equipo el cargador y el neceser con tus productos y gotas. "
        "La misión terminará el domingo."
    )
    st.write(
        "Desayuna ligero, duerme bien y no hables con nadie."
    )
    st.write("La contraseña con el conductor será: 'HARTO'")

    if st.button("Volver a empezar"):
        for clave in [
            "coordenadas_ok",
            "fecha_ok",
            "hora_ok",
            "transporte_ok",
            "equipaje_ok"
        ]:
            st.session_state.pop(clave, None)
        st.rerun()
