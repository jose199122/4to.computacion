class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.paginas}")


# Ejemplo de uso
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 471)
libro1.mostrar_informacion()
