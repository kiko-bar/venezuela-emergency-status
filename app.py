### APPLICATION CODE TO HELP THE VENEZUELAN PEOPLE SITUATION TO FIND THEIR LOVE ONE """
# Usefull lybraries
import streamlit as st
import pandas as pd
import json 
import os
from datetime import datetime

# 1. Configuration and page setup (hyper lightwaight UI)
st.set_page_config(
    page_title = "Vargas & Caracas - Disasster Status Board",
    page_icon = "❤️‍🩹",
    layout = "wide"
)

DB_FILE = "disaster_data.jason"
SECTORS = ["Caraballeda", "Macuto", "Catia_La_Mar", "Maiquetia", "Tanaguarena", "Caracas_East", "Caracas_West", "Altamira", "Los_Palos_Grande", "Playa_Grande", "Other"]
STATUS_OPTIONS = ["Missing_(Desaparecido)", "Trapped_(Atrapado)", "Safe_(A_Salvo)", "Rescued_(Rescatado)"]

# 2. Database helper functions
def load_data():
    if not os.path.exists(DB_FILE):
        # Create an empty database if it doesn't exist yet
        with open(DB_FILE, "w") as f:
            json.dump([], f)
        return []
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_record(new_record):
    data = load_data()
    data.append(new_record)
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent = 4)

# Load existing records into session state
records = load_data()

# 3. Application headers
st.title("🤕 Tablon de Personas Desaparecidas y Estatus de Emergencia")
st.subheader("Respuesta a Terremoto-Venezuela - Vargas / Caracas")
st. caption("Esto es un registro simple, banda-baja para cruzar referencias de individuos perdidos y estatus de rescate.")

# 4. Interface Split: Left side (Report) | Right side (Search/View) 
col1, col2 = st.columns([1, 2])

with col1:
    st.header("📝 Meter Estatus / Petición")
    with st.form("formulario_estatus", clear_on_submit = True):
        full_name = st.text_input("Nombre Completo (Full Name of Person) *")
        status = st.selectbox("Estatus Actual", STATUS_OPTIONS)
        sector = st.selectbox("Zona / Becindario *", SECTORS)
        address = st.text_input("Especificar Dirección / Ultima Localización Conocida")
        notes = st.text_area("Detalles Críticos (Lesionados, tapeado, estatus bateria movil, etc.)")
        reporter = st.text_input("Su Nombre & Info de Contacto (Quien lo reporta)")

        submitted = st.form_submit_button("ENVIAR Estatus de Reporte")

        if submitted:
            if not full_name:
                st.error("Error: Requerido su 'Nombre Completo'.")
            else:
                new_entry = {
                    "report_id": f"REQ-{int(datetime.utcnow().timestamp())}",
                    "full_name": full_name.strip(),
                    "status": status,
                    "sector": sector,
                    "specific_address": address.strip(),
                    "notes": notes.strip(),
                    "reported_by": reporter.strip(),
                    "timestamp": datetime.utcnow().strftime("%d-%m-%Y %H:%M:%S UTC")
                }    
                save_record(new_entry)
                st.success(f"Reporte Exitosamente Cargado por {full_name}!")
                st.rerun()

with col2:
    st.header("🔎 Tablon de Busqueda & Rescate")

    # Simple, fast filtering mechanics
    search_query = st.text_input("Busqueda por Nombre (Search by Name)").strip().lower()
    filter_sector = st.selectbox("Filtro por Zona", ["Todos_los_Sectores"] + SECTORS)

    if records:
        




