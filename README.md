# LGPII-T2-

PAGINA WEB
⚡ NovaNissi - Catálogo de Productos de Tecnología

Aplicación web desacoplada compuesta por un backend en Flask que expone una API REST con algoritmos de ordenamiento y búsqueda, y un frontend en HTML5 + CSS + JavaScript que consume los datos con y los dibuja dinámicamente en el navegador sin recargar la página.fetch()

Proyecto académico de la asignatura Lenguaje de Programación II (LPII).

📸 Vista previa
Búsqueda binaria (ID 27)	Producto no encontrado (ID 999)
Búsqueda encontrada	No existe
Ordenado por nombre	Versión móvil
Orden por nombre	Móvil
✨ Características
Ordenamiento con Quicksort implementado desde cero (sin ni ), con soporte para orden ascendente y descendente.sorted().sort()
Búsqueda binaria por ID, con la precondición de ordenar la lista antes de buscar.
Benchmark de rendimiento: Quicksort vs Ordenamiento Burbuja con 1.000 elementos, medido en milisegundos.
Frontend responsivo (escritorio y celular) que consume la API con y actualiza la vista sin recargar.fetch()
Filtro por categoría y varios criterios de orden (precio, nombre, stock).
Validación de parámetros y respuestas de error en JSON ( y ).400404
🧰 Tecnologías
Capa	Tecnología
Backend	Python 3, Flask
Frontend	HTML5, CSS3, JavaScript (API de recolección)
Datos	Archivo JSON (productos.json)
📁 Estructura del proyecto
catalogo_tecnologia/
├── app.py               # Backend Flask: API + algoritmos
├── productos.json       # Catálogo de 20 productos de tecnología
├──── index.html       # Interfaz web (consume la API con fetch)
└── README.md
🚀 Instalación y ejecución
Requisitos
Python 3.8+
pip (viene con Python)
Pasos
Bash
# 1. Clonar el repositorio
git clone https://github.com/TU-USUARIO/NOMBRE-DEL-REPO.git
cd NOMBRE-DEL-REPO

# 2. Crear y activar un entorno virtual (recomendado)
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # Mac / Linux

# 4. Ejecutar la aplicación
python app.py

Luego abre en el navegador: http://127.0.0.1:5000

En Windows, si no funciona, usa . En Mac/Linux, usa .pythonpypython3


🧠 Algoritmos implementados
Quicksort

Divide y vencerás: elige un pivote (elemento central) y separa la lista en tres grupos (menores, iguales y mayores), ordenando recursivamente los extremos.

Complejidad promedio: O(n log n)
Peor caso: O(n²)
Búsqueda binaria

Divide el rango de búsqueda a la mitad en cada paso. Requiere una lista ordenada, por eso el endpoint ordena por con Quicksort antes de buscar.id

Complejidad: O(log n)
Ordenamiento burbuja (solo benchmark)

Compara pares adyacentes e intercambia los que están desordenados. Se usa únicamente para demostrar la diferencia de rendimiento.

Complejidad: O(n²)
🧪 Cómo probar
Abre y usa los botones de orden y el filtro por categoría.http://127.0.0.1:5000
Escribe un ID (por ejemplo) en el buscador para ver la búsqueda binaria en acción.27
Abre para ver la comparación de tiempos.http://127.0.0.1:5000/api/benchmark?n=1000
