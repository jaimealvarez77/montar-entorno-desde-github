# Montar el entorno desde GitHub

Programación I · Grado en Business Analytics · Universidad Francisco de Vitoria

Repositorio de partida para practicar lo que se hace con cualquier proyecto de Python descargado de GitHub: clonarlo, crear un entorno virtual e instalar las librerías a partir de `requirements.txt`.

## Qué hay en el repositorio

| Archivo | Para qué sirve |
|---|---|
| `requirements.txt` | Las librerías del proyecto: numpy, pandas, matplotlib y seaborn. |
| `ejemplo_numpy.py` | Cálculos con vectores de números: importes, totales y un descuento sobre cinco productos. |
| `ejemplo_pandas.py` | Crea una tabla con 240 ventas de cuatro tiendas y la resume por tienda, por categoría y por mes. |
| `ejemplo_seaborn.py` | Dibuja dos gráficos de esas ventas y los guarda en una carpeta `graficos`. |

## Antes de empezar

Necesitas VS Code con la extensión de Python, Python 3.10 o superior y Git. Abre en VS Code tu carpeta de la asignatura (**Archivo > Abrir carpeta**) y después una terminal (**Terminal > Nueva terminal**). La terminal ya arranca dentro de tu carpeta.

## Pasos en Windows (PowerShell)

```
git clone https://github.com/rprieto2809/montar_entorno_desde_github.git .
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python ejemplo_numpy.py
python ejemplo_pandas.py
python ejemplo_seaborn.py
```

## Pasos en Mac (Terminal)

```
git clone https://github.com/rprieto2809/montar_entorno_desde_github.git .
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python ejemplo_numpy.py
python ejemplo_pandas.py
python ejemplo_seaborn.py
```

El punto al final del `git clone` hace que el proyecto se descargue en tu carpeta, sin crear una subcarpeta. Después de activar el entorno debe aparecer `(venv)` al principio de la línea de la terminal.

Por último, en VS Code pulsa `Ctrl+Shift+P` (`Cmd+Shift+P` en Mac), escribe **Python: Select Interpreter** y elige el que tenga `venv` en su ruta.

`ejemplo_seaborn.py` abre una ventana con los gráficos. Ciérrala para que el programa termine.

## Si tu carpeta no está vacía

Si ya había algo dentro de tu carpeta, `git clone ... .` da el error `destination path '.' already exists and is not an empty directory`. En ese caso, en lugar del `git clone`, usa estos tres comandos (iguales en Windows y en Mac):

```
git init
git remote add origin https://github.com/rprieto2809/montar_entorno_desde_github.git
git pull origin main
```

## Problemas frecuentes

| Lo que ves | Qué hacer |
|---|---|
| Windows: `Activate.ps1 no se puede cargar porque la ejecución de scripts está deshabilitada` | Ejecuta una vez `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`, confirma con S y vuelve a activar el entorno. |
| Windows: `python` no se reconoce, o se abre la Microsoft Store | Reinstala Python desde python.org marcando *Add python.exe to PATH*, o usa `py -m venv venv`. |
| Mac: `python: command not found` | Antes de activar el entorno, en Mac se escribe `python3`. |
| `git` no se reconoce (Windows) o aviso de herramientas de línea de comandos (Mac) | En Windows, instala Git desde git-scm.com y reinicia VS Code. En Mac, acepta la instalación o escribe `xcode-select --install`. |
| Se ha creado una subcarpeta `montar_entorno_desde_github` | Faltó el punto al final del `git clone`. Abre esa subcarpeta en VS Code y sigue desde la creación del entorno. |
| `ModuleNotFoundError: No module named 'pandas'` | El entorno no está activo o VS Code usa otro intérprete. Comprueba que aparece `(venv)` y vuelve a elegir el intérprete. |
| `No matching distribution found` al instalar | Tu Python es anterior a la 3.10. Instala una versión más reciente y crea el entorno de nuevo. |

## Cuando vuelvas a abrir el proyecto

Abre la carpeta en VS Code y una terminal nueva. Si elegiste el intérprete del entorno, VS Code lo activa solo. Si no ves `(venv)`, actívalo como en el paso 3. Para descargar cambios que el profesor haya subido al repositorio, ejecuta `git pull` y después `pip install -r requirements.txt`.

La carpeta `venv` no se sube a GitHub: cada persona se crea la suya a partir de `requirements.txt`.
