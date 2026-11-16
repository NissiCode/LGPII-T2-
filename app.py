"""Catálogo de productos de tecnología - Flask + Quicksort + Búsqueda binaria."""
import json
import random
import time
from pathlib import Path

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
RUTA_JSON = Path(__file__).parent / "productos.json"
CLAVES_VALIDAS = {"id", "nombre", "categoria", "precio", "stock"}


def cargar_productos():
    with open(RUTA_JSON, encoding="utf-8") as f:
        return json.load(f)


def valor(item, clave):
    v = item[clave]
    return v.lower() if isinstance(v, str) else v


def quicksort(items, clave, reverse=False):
    if len(items) <= 1:
        return items
    pivote = valor(items[len(items) // 2], clave)
    izq = [x for x in items if (valor(x, clave) > pivote if reverse else valor(x, clave) < pivote)]
    centro = [x for x in items if valor(x, clave) == pivote]
    der = [x for x in items if (valor(x, clave) < pivote if reverse else valor(x, clave) > pivote)]
    return quicksort(izq, clave, reverse) + centro + quicksort(der, clave, reverse)



def burbuja(items, clave):
    arr = items[:]
    n = len(arr)
    for i in range(n - 1):
        cambio = False
        for j in range(n - 1 - i):
            if valor(arr[j], clave) > valor(arr[j + 1], clave):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                cambio = True
        if not cambio:
            break
    return arr


def busqueda_binaria(items, objetivo, clave="id"):
    """Precondición: 'items' ordenado ascendentemente por 'clave'."""
    bajo, alto, pasos = 0, len(items) - 1, 0
    while bajo <= alto:
        pasos += 1
        medio = (bajo + alto) // 2
        actual = items[medio][clave]
        if actual == objetivo:
            return medio, pasos
        if actual < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1, pasos


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/productos")
def get_productos():
    sort_by = request.args.get("sort_by", "precio")
    desc = request.args.get("order", "asc") == "desc"
    categoria = request.args.get("categoria", "")

    if sort_by not in CLAVES_VALIDAS:
        return jsonify(error=f"sort_by inválido. Use: {sorted(CLAVES_VALIDAS)}"), 400

    productos = cargar_productos()
    if categoria:
        productos = [p for p in productos if p["categoria"].lower() == categoria.lower()]
    return jsonify(quicksort(productos, sort_by, reverse=desc))


@app.route("/api/productos/buscar")
def buscar_producto():
    try:
        objetivo = int(request.args.get("id", ""))
    except ValueError:
        return jsonify(error="Debe enviar ?id=<número entero>"), 400

    
    ordenado = quicksort(cargar_productos(), "id")
    pos, pasos = busqueda_binaria(ordenado, objetivo, "id")

    if pos == -1:
        return jsonify(encontrado=False, id=objetivo, pasos=pasos,
                       mensaje="Producto no encontrado"), 404
    return jsonify(encontrado=True, posicion=pos, pasos=pasos, producto=ordenado[pos])


@app.route("/api/categorias")
def categorias():
    return jsonify(sorted({p["categoria"] for p in cargar_productos()}))


@app.route("/api/benchmark")
def benchmark():
    try:
        n = max(10, min(int(request.args.get("n", 1000)), 3000))
    except ValueError:
        n = 1000

    datos = [{"id": i, "nombre": f"Producto {i}", "categoria": "Demo",
              "precio": round(random.uniform(1, 2000), 2), "stock": random.randint(0, 300)}
             for i in range(n)]
    random.shuffle(datos)

    t0 = time.perf_counter()
    r_quick = quicksort(datos, "precio")
    ms_quick = (time.perf_counter() - t0) * 1000

    t0 = time.perf_counter()
    r_burb = burbuja(datos, "precio")
    ms_burb = (time.perf_counter() - t0) * 1000

    p_q = [x["precio"] for x in r_quick]
    p_b = [x["precio"] for x in r_burb]
    return jsonify(
        n=n,
        quicksort_ms=round(ms_quick, 3),
        burbuja_ms=round(ms_burb, 3),
        veces_mas_rapido=round(ms_burb / ms_quick, 1) if ms_quick else None,
        correcto=(p_q == p_b == sorted(p_q)),
    )


if __name__ == "__main__":
    app.run(debug=True)
