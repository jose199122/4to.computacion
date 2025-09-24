import flet as ft

# Vehículos disponibles
vehiculos = [
    {
        "id": 1,
        "nombre": "Auto Deportivo",
        "tipo": "auto",
        "precio": 120,
        "imagen": "camineta_blanca.jpg",
        "descripcion": "Velocidad y confort para largas distancias."
    },
    {
        "id": 2,
        "nombre": "Moto Urbana",
        "tipo": "moto",
        "precio": 60,
        "imagen": "mi_motocicleta.jpg",
        "descripcion": "Rápida y práctica para la ciudad."
    },
    {
        "id": 3,
        "nombre": "Bicicleta Montaña",
        "tipo": "bicicleta",
        "precio": 25,
        "imagen": "mi_ori_ls.jpg",
        "descripcion": "Perfecta para caminos difíciles y aventuras."
    }
]

# Estado de sesión y carrito
usuarios = {}
sesion = {"usuario": None}
carrito = []

def main(page: ft.Page):
    page.title = "Renta de Vehículos"
    page.window_width = 400
    page.window_height = 750
    page.scroll = ft.ScrollMode.AUTO

    # Campos compartidos
    email = ft.TextField(label="Correo electrónico", width=300)
    password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)
    estado = ft.Text("", size=14, color="red")

    # ======================= PANTALLAS PRINCIPALES ========================

    # --------- LOGIN ----------
    def pantalla_login():
        page.controls.clear()
        page.add(
            ft.Column([
                ft.Text("🚗 Iniciar Sesión", size=24, weight="bold"),
                email,
                password,
                ft.ElevatedButton("Entrar", on_click=procesar_login),
                ft.TextButton("¿No tienes cuenta? Regístrate aquí", on_click=lambda e: pantalla_registro()),
                estado
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER)
        )
        page.update()

    # --------- REGISTRO ----------
    def pantalla_registro():
        page.controls.clear()
        page.add(
            ft.Column([
                ft.Text("📝 Registro de Usuario", size=24, weight="bold"),
                email,
                password,
                ft.ElevatedButton("Registrarse", on_click=procesar_registro),
                ft.TextButton("¿Ya tienes cuenta? Inicia sesión", on_click=lambda e: pantalla_login()),
                estado
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER)
        )
        page.update()

    # --------- CATÁLOGO ----------
    def pantalla_catalogo():
        page.controls.clear()

        lista = []
        for v in vehiculos:
            item = ft.Container(
                content=ft.Column([
                    ft.Image(src=f"/assets/{v['imagen']}", width=350, height=180, fit=ft.ImageFit.COVER),
                    ft.Text(v["nombre"], size=18, weight="bold"),
                    ft.Text(v["descripcion"]),
                    ft.Text(f"💰 ${v['precio']} por día"),
                    ft.Row([
                        ft.ElevatedButton("Ver Detalles", on_click=lambda e, v=v: pantalla_detalles(v)),
                        ft.OutlinedButton("Agregar 🛒", on_click=lambda e, v=v: agregar_al_carrito(v))
                    ])
                ]),
                padding=10,
                margin=10,
                border=ft.border.all(1, "gray"),
                border_radius=8
            )
            lista.append(item)

        page.add(
            ft.Column([
                ft.Row([
                    ft.Text(f"👤 {sesion['usuario']}", weight="bold"),
                    ft.ElevatedButton("🛒 Carrito", on_click=pantalla_carrito),
                    ft.OutlinedButton("Salir", on_click=cerrar_sesion)
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Text("Catálogo de Vehículos", size=22, weight="bold"),
                ft.Column(lista, scroll=ft.ScrollMode.AUTO)
            ])
        )
        page.update()

    # --------- DETALLES DE VEHÍCULO ----------
    def pantalla_detalles(vehiculo):
        page.controls.clear()
        page.add(
            ft.Column([
                ft.Image(src=f"/assets/{vehiculo['imagen']}", width=380, height=220),
                ft.Text(vehiculo["nombre"], size=24, weight="bold"),
                ft.Text(vehiculo["descripcion"]),
                ft.Text(f"💰 Precio por día: ${vehiculo['precio']}"),
                ft.Row([
                    ft.ElevatedButton("Agregar al carrito 🛒", on_click=lambda e: agregar_al_carrito(vehiculo)),
                    ft.OutlinedButton("⬅️ Volver", on_click=lambda e: pantalla_catalogo())
                ])
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO)
        )
        page.update()

    # --------- CARRITO ----------
    def pantalla_carrito(e=None):
        page.controls.clear()

        if not carrito:
            page.add(
                ft.Column([
                    ft.Text("🛒 Tu carrito está vacío.", size=20),
                    ft.ElevatedButton("Volver al catálogo", on_click=lambda e: pantalla_catalogo())
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            )
        else:
            items = []
            total = 0
            for i, item in enumerate(carrito):
                total += item["precio"]
                items.append(
                    ft.Row([
                        ft.Text(f"{item['nombre']} - ${item['precio']}"),
                        ft.TextButton("❌ Quitar", on_click=lambda e, i=i: quitar_del_carrito(i))
                    ])
                )

            page.add(
                ft.Column([
                    ft.Text("🛒 Carrito de Renta", size=22, weight="bold"),
                    ft.Column(items),
                    ft.Text(f"Total: ${total}", weight="bold"),
                    ft.Row([
                        ft.ElevatedButton("❌ Cancelar compra", on_click=cancelar_compra),
                        ft.OutlinedButton("⬅️ Volver", on_click=lambda e: pantalla_catalogo())
                    ])
                ])
            )
        page.update()

    # ======================= FUNCIONES DE LÓGICA ========================

    def procesar_login(e):
        if email.value in usuarios and usuarios[email.value] == password.value:
            sesion["usuario"] = email.value
            email.value = ""
            password.value = ""
            estado.value = ""
            pantalla_catalogo()
        else:
            estado.value = "❌ Usuario o contraseña incorrecta."
            page.update()

    def procesar_registro(e):
        if email.value in usuarios:
            estado.value = "⚠️ Este correo ya está registrado."
        else:
            usuarios[email.value] = password.value
            estado.value = "✅ Registro exitoso. Inicia sesión."
        page.update()

    def cerrar_sesion(e):
        sesion["usuario"] = None
        carrito.clear()
        pantalla_login()

    def agregar_al_carrito(vehiculo):
        carrito.append(vehiculo)
        pantalla_catalogo()

    def quitar_del_carrito(index):
        del carrito[index]
        pantalla_carrito()

    def cancelar_compra(e):
        carrito.clear()
        pantalla_catalogo()

    # Mostrar pantalla inicial
    pantalla_login()

# Ejecutar con carpeta de imágenes
ft.app(target=main, assets_dir="assets")
