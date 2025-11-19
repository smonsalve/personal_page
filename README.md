# Personal Page - Aprende TailwindCSS

Una página web personal moderna construida con FastAPI y TailwindCSS. Incluye portfolio de proyectos, sobre mí, CV y formulario de contacto.

## Stack Tecnológico

- **Python 3.13+** - Lenguaje de programación
- **FastAPI** - Framework web moderno y rápido
- **uv** - Gestor de paquetes Python ultrarrápido
- **TailwindCSS** - Framework CSS utility-first
- **Jinja2** - Motor de plantillas HTML

## Estructura del Proyecto

```
personal_page/
├── main.py                 # Aplicación FastAPI principal
├── templates/              # Plantillas HTML con Jinja2
│   ├── base.html          # Plantilla base (nav, footer)
│   ├── index.html         # Página de inicio
│   ├── portfolio.html     # Portfolio de proyectos
│   ├── about.html         # Sobre mí
│   ├── contact.html       # Formulario de contacto
│   └── cv.html            # Currículum vitae
├── static/                # Archivos estáticos
│   ├── css/
│   │   ├── input.css      # CSS de entrada con directivas Tailwind
│   │   └── output.css     # CSS compilado (generado automáticamente)
│   ├── js/
│   │   └── main.js        # JavaScript personalizado
│   └── images/            # Tus imágenes, fotos, screenshots
├── tailwind.config.js     # Configuración de TailwindCSS
├── package.json           # Dependencias de Node.js (Tailwind)
├── pyproject.toml         # Dependencias de Python
└── README.md              # Este archivo
```

## Instalación y Configuración

### 1. Requisitos Previos

Asegúrate de tener instalado:

- Python 3.13 o superior
- Node.js y npm (para TailwindCSS)
- uv (gestor de paquetes Python)

Para instalar uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Instalar Dependencias de Python

```bash
# Las dependencias ya están instaladas, pero si necesitas reinstalar:
uv sync
```

### 3. Instalar TailwindCSS

```bash
npm install
```

### 4. Compilar CSS de Tailwind

En una terminal, ejecuta:
```bash
npm run build:css
```

Esto compilará el CSS de TailwindCSS. Para desarrollo con auto-reload:
```bash
npm run dev:css
```

Mantén esta terminal abierta durante el desarrollo para que Tailwind recompile automáticamente cuando hagas cambios.

## Ejecutar el Proyecto

### Desarrollo (con auto-reload)

1. En una terminal, ejecuta TailwindCSS en modo watch:
```bash
npm run dev:css
```

2. En otra terminal, ejecuta el servidor FastAPI:
```bash
uv run uvicorn main:app --reload
```

3. Abre tu navegador en: http://localhost:8000

### Producción

```bash
# Compilar CSS minificado
npm run build:css

# Ejecutar servidor
uv run uvicorn main:app --host 0.0.0.0 --port 8000
```

## Aprendiendo TailwindCSS

### Conceptos Básicos

TailwindCSS es un framework "utility-first" que te permite construir diseños usando clases predefinidas directamente en tu HTML.

#### Ejemplo Básico:
```html
<!-- Sin Tailwind -->
<div style="background-color: blue; color: white; padding: 16px; border-radius: 8px;">
    Hola Mundo
</div>

<!-- Con Tailwind -->
<div class="bg-blue-500 text-white p-4 rounded-lg">
    Hola Mundo
</div>
```

### Clases Más Comunes

#### Colores
- `bg-blue-500` - Fondo azul
- `text-white` - Texto blanco
- `border-gray-300` - Borde gris

#### Espaciado (padding/margin)
- `p-4` - Padding en todos los lados (1rem = 16px)
- `px-4` - Padding horizontal (left + right)
- `py-2` - Padding vertical (top + bottom)
- `m-4` - Margin en todos los lados
- `mt-8` - Margin top

#### Layout (Flexbox/Grid)
- `flex` - Display flex
- `grid` - Display grid
- `grid-cols-3` - 3 columnas en grid
- `justify-center` - Centrar horizontalmente
- `items-center` - Centrar verticalmente

#### Responsive Design
TailwindCSS usa prefijos para diferentes tamaños de pantalla:

- Sin prefijo: móvil (por defecto)
- `sm:` - ≥ 640px
- `md:` - ≥ 768px
- `lg:` - ≥ 1024px
- `xl:` - ≥ 1280px

Ejemplo:
```html
<!-- 1 columna en móvil, 2 en tablet, 3 en desktop -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
    ...
</div>
```

#### Estados Interactivos
- `hover:` - Al pasar el mouse
- `focus:` - Al hacer focus
- `active:` - Al hacer click

Ejemplo:
```html
<button class="bg-blue-500 hover:bg-blue-700 text-white px-4 py-2 rounded">
    Click Me
</button>
```

### Ejemplos en el Proyecto

Todos los archivos HTML en `templates/` tienen comentarios explicando las clases de TailwindCSS usadas. Busca comentarios como:

```html
<!--
    TailwindCSS Learning Notes:
    - bg-white: white background
    - shadow-md: medium shadow
    ...
-->
```

### Recursos de Aprendizaje

- [Documentación Oficial de TailwindCSS](https://tailwindcss.com/docs)
- [TailwindCSS Cheat Sheet](https://nerdcave.com/tailwind-cheat-sheet)
- [Tailwind Play](https://play.tailwindcss.com/) - Experimenta en el navegador

## Personalización

### Cambiar Colores

Edita `tailwind.config.js`:

```javascript
theme: {
    extend: {
        colors: {
            'primary': '#3B82F6',  // Cambia este color
            'secondary': '#10B981',
        },
    },
}
```

### Agregar tus Propios Datos

1. **Portfolio**: Edita los datos en `main.py` en la función `portfolio()`
2. **CV**: Edita los datos en `main.py` en la función `cv()`
3. **Información Personal**: Edita directamente en los archivos HTML de `templates/`

### Agregar Imágenes

1. Coloca tus imágenes en `static/images/`
2. Úsalas en HTML: `<img src="/static/images/tu-foto.jpg" alt="...">`

## Despliegue en AWS

Para desplegar tu aplicación en AWS, puedes usar:

- **AWS Elastic Beanstalk** - Más fácil para empezar
- **AWS ECS/Fargate** - Usando Docker
- **AWS EC2** - Más control manual
- **AWS Lambda + API Gateway** - Serverless con Mangum

### Ejemplo con Elastic Beanstalk:

1. Instala AWS CLI y EB CLI
2. Crea un archivo `requirements.txt`:
   ```bash
   uv pip compile pyproject.toml -o requirements.txt
   ```
3. Inicializa y despliega:
   ```bash
   eb init
   eb create
   eb deploy
   ```

## Comandos Útiles

```bash
# Instalar nueva dependencia Python
uv add nombre-paquete

# Instalar dependencia de desarrollo
uv add --dev nombre-paquete

# Ejecutar servidor de desarrollo
uv run uvicorn main:app --reload

# Ver rutas disponibles
uv run uvicorn main:app --reload
# Luego visita: http://localhost:8000/docs

# Compilar CSS de Tailwind (una vez)
npm run build:css

# Compilar CSS de Tailwind (watch mode)
npm run dev:css
```

## Próximos Pasos

1. **Personaliza tu información**: Cambia los textos de ejemplo por tu información real
2. **Agrega tus imágenes**: Sube fotos tuyas y capturas de tus proyectos
3. **Experimenta con Tailwind**: Prueba diferentes clases y combinaciones
4. **Conecta un formulario real**: Implementa el envío de emails en `/contact`
5. **Agrega más secciones**: Blog, testimonios, etc.
6. **Optimiza para SEO**: Meta tags, sitemap, etc.
7. **Implementa analytics**: Google Analytics, Plausible, etc.

## Problemas Comunes

### CSS no se actualiza
- Asegúrate de que `npm run dev:css` esté corriendo
- Refresca el navegador con Ctrl+F5 (hard refresh)
- Verifica que `output.css` se haya generado en `static/css/`

### Error al iniciar el servidor
- Verifica que el puerto 8000 no esté en uso
- Activa el virtual environment: `source .venv/bin/activate`

### Las clases de Tailwind no funcionan
- Verifica que las rutas en `tailwind.config.js` sean correctas
- Asegúrate de que `output.css` esté siendo cargado en `base.html`

## Contacto y Contribuciones

Este es tu proyecto personal. ¡Diviértete aprendiendo y construyendo!

Para preguntas sobre TailwindCSS: https://tailwindcss.com/docs
Para preguntas sobre FastAPI: https://fastapi.tiangolo.com/

---

**¡Feliz coding!** 🚀
