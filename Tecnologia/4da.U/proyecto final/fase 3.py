import flet as ft
import json
import os
from datetime import datetime

# Archivos de persistencia
CLIENTES_FILE = "clientes.json"
VEHICULOS_FILE = "vehiculos.json"
PRESTAMOS_FILE = "prestamos.json"
PAGOS_FILE = "pagos.json"

# Funciones de persistencia
def load_data(file):
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_data(file, data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# Datos cargados al inicio
clientes = load_data(CLIENTES_FILE)
vehiculos = load_data(VEHICULOS_FILE)
prestamos = load_data(PRESTAMOS_FILE)
pagos = load_data(PAGOS_FILE)

# Funciones de lógica
def registrar_cliente(nombre, cedula, telefono):
    if not nombre or not cedula.isdigit() or not telefono.isdigit():
        return "Datos inválidos"
    clientes.append({"nombre": nombre, "cedula": cedula, "telefono": telefono})
    save_data(CLIENTES_FILE, clientes)
    return "Cliente registrado con éxito"

def registrar_vehiculo(marca, modelo, anio, estado):
    if not marca or not modelo or not anio.isdigit():
        return "Datos de vehículo inválidos"
    vehiculos.append({"marca": marca, "modelo": modelo, "anio": anio, "estado": estado})
    save_data(VEHICULOS_FILE, vehiculos)
    return "Vehículo registrado con éxito"

def crear_prestamo(cedula, vehiculo_idx, monto, interes, plazo):
    try:
        cliente = next((c for c in clientes if c["cedula"] == cedula), None)
        if not cliente:
            return "Cliente no encontrado"
        if vehiculo_idx < 0 or vehiculo_idx >= len(vehiculos):
            return "Índice de vehículo inválido"
        vehiculo = vehiculos[vehiculo_idx]
        if vehiculo["estado"] != "disponible":
            return "Vehículo no disponible"
        total_interes = monto * (interes / 100) * plazo
        total_pagar = monto + total_interes
        prestamo = {
            "cliente": cedula,
            "vehiculo": vehiculo,
            "monto": monto,
            "interes": interes,
            "plazo": plazo,
            "total_pagar": total_pagar,
            "saldo": total_pagar,
            "fecha": datetime.now().strftime("%Y-%m-%d")
        }
        prestamos.append(prestamo)
        vehiculo["estado"] = "prestado"
        save_data(PRESTAMOS_FILE, prestamos)
        save_data(VEHICULOS_FILE, vehiculos)
        return f"Préstamo creado. Total a pagar: {total_pagar:.2f}"
    except Exception as e:
        return f"Error al crear préstamo: {str(e)}"

def registrar_pago(cedula, monto):
    try:
        prestamo = next((p for p in prestamos if p["cliente"] == cedula and p["saldo"] > 0), None)
        if not prestamo:
            return "No se encontró préstamo activo"
        if monto <= 0 or monto > prestamo["saldo"]:
            return "Monto inválido"
        prestamo["saldo"] -= monto
        pago = {"cedula": cedula, "monto": monto, "fecha": datetime.now().strftime("%Y-%m-%d")}
        pagos.append(pago)
        save_data(PRESTAMOS_FILE, prestamos)
        save_data(PAGOS_FILE, pagos)
        return f"Pago registrado. Saldo restante: {prestamo['saldo']:.2f}"
    except Exception as e:
        return f"Error al registrar pago: {str(e)}"

# Interfaz con Flet
def main(page: ft.Page):
    page.title = "Sistema de Préstamos"
    page.window_width = 850
    page.window_height = 650
    output = ft.Text("Bienvenido al sistema", size=14,)

    # ==== Vista de Clientes ====
    nombre = ft.TextField(label="Nombre")
    cedula = ft.TextField(label="Cédula")
    telefono = ft.TextField(label="Teléfono")
    btn_cliente = ft.ElevatedButton("Registrar Cliente", on_click=lambda e: output.update(registrar_cliente(nombre.value, cedula.value, telefono.value)))
    cliente_view = ft.Column([
        ft.Image(src="cliente.png", width=150, height=150),
        nombre, cedula, telefono, btn_cliente
    ])

    # ==== Vista de Vehículos ====
    marca = ft.TextField(label="Marca")
    modelo = ft.TextField(label="Modelo")
    anio = ft.TextField(label="Año")
    estado = ft.Dropdown(
        label="Estado",
        options=[ft.dropdown.Option("disponible"), ft.dropdown.Option("prestado")],
        value="disponible"
    )
    btn_vehiculo = ft.ElevatedButton("Registrar Vehículo", on_click=lambda e: output.update(registrar_vehiculo(marca.value, modelo.value, anio.value, estado.value)))
    

    imagenes_vehiculos = ft.Row([
        ft.Image(src="R1.jpg", width=120, height=100),
        ft.Image(src="RT_V_972b48e3b42549a8b8011ee1fd85c76a.jpg", width=120, height=100),
        ft.Image(src="XTZ125.jpg", width=120, height=100),
        ft.Image(src="yamaha-xsr-900-2023.jpg", width=120, height=100),
        ft.Image(src="lanzamiento-toyota-hilux-gr-sport.jpg", width=120, height=100),
        ft.Image(src="10-yamaha-r125-2025-estudio-azul-12-210-150.jpg", width=120, height=100),
        ft.Image(src="2024_Toyota_Tacoma_TRDsport_049-1500x1000-1.jpg", width=120, height=100),
        ft.Image(src="BMW-520i-Edicion-M-2026.jpg", width=120, height=100),
        ft.Image(src="bmw-8-series-gran-coupe-ms-g16.jpg", width=120, height=100),
        ft.Image(src="vw-promociones-virtus-2.jpg", width=120, height=100),
        ft.Image(src="Toyota-Hilux-GR-SPORT.jpg", width=120, height=100),
        ft.Image(src="2024_Toyota_Tacoma_TRD_PreRunner_002.jpg", width=120, height=100),
    ])

    vehiculo_view = ft.Column([
        imagenes_vehiculos,
        marca, modelo, anio, estado, btn_vehiculo
    ])

    # ==== Vista de Préstamos ====
    prestamo_cedula = ft.TextField(label="Cédula del Cliente")
    vehiculo_idx = ft.TextField(label="Índice del Vehículo (0..n)")
    monto = ft.TextField(label="Monto")
    interes = ft.TextField(label="Interés (%)")
    plazo = ft.TextField(label="Plazo (meses)")
    def crear_prestamo_click(e):
        try:
            idx = int(vehiculo_idx.value)
            m = float(monto.value)
            i = float(interes.value)
            p = int(plazo.value)
            output.update(crear_prestamo(prestamo_cedula.value, idx, m, i, p))
        except:
            output.update("Datos inválidos. Verifica los campos.")
    btn_prestamo = ft.ElevatedButton("Crear Préstamo", on_click=crear_prestamo_click)

    prestamo_view = ft.Column([
        ft.Image(src="prestamo.png", width=150, height=150),
        prestamo_cedula, vehiculo_idx, monto, interes, plazo, btn_prestamo
    ])

    # ==== Vista de Pagos ====
    pago_cedula = ft.TextField(label="Cédula del Cliente")
    pago_monto = ft.TextField(label="Monto a Pagar")
    def pago_click(e):
        try:
            output.update(registrar_pago(pago_cedula.value, float(pago_monto.value)))
        except:
            output.update("Error en el monto.")
    btn_pago = ft.ElevatedButton("Registrar Pago", on_click=pago_click)

    pago_view = ft.Column([
        ft.Image(src="https://cdn-icons-png.flaticon.com/512/1086/1086741.png", width=150, height=150),
        pago_cedula, pago_monto, btn_pago
    ])

    # ==== Vista de Reportes ====
    reporte_clientes = ft.TextButton("Clientes", on_click=lambda e: output.update(json.dumps(clientes, indent=2, ensure_ascii=False)))
    reporte_vehiculos = ft.TextButton("Vehículos", on_click=lambda e: output.update(json.dumps(vehiculos, indent=2, ensure_ascii=False)))
    reporte_prestamos = ft.TextButton("Préstamos", on_click=lambda e: output.update(json.dumps(prestamos, indent=2, ensure_ascii=False)))
    reporte_pagos = ft.TextButton("Pagos", on_click=lambda e: output.update(json.dumps(pagos, indent=2, ensure_ascii=False)))

    reportes_view = ft.Column([
        ft.Image(src="reportes.png", width=150, height=150),
        reporte_clientes, reporte_vehiculos, reporte_prestamos, reporte_pagos
    ])

    # ==== Tabs ====
    tabs = ft.Tabs(
        selected_index=0,
        on_change=lambda e: switch_tab(),
        tabs=[
            ft.Tab(text="Clientes"),
            ft.Tab(text="Vehículos"),
            ft.Tab(text="Préstamos"),
            ft.Tab(text="Pagos"),
            ft.Tab(text="Reportes"),
        ]
    )

    views = [cliente_view, vehiculo_view, prestamo_view, pago_view, reportes_view]

    def switch_tab():
        page.controls.clear()
        page.add(tabs, views[tabs.selected_index], output)
        page.update()

    # Inicializar vista
    page.add(tabs, cliente_view, output)

# Ejecutar la app
ft.app(target=main)
