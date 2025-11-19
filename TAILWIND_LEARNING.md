# Guía de Aprendizaje de TailwindCSS

Esta guía te ayudará a entender TailwindCSS mientras trabajas en tu página personal.

## ¿Qué es TailwindCSS?

TailwindCSS es un framework CSS "utility-first" (utilidad primero). En lugar de escribir CSS personalizado, usas clases predefinidas directamente en tu HTML.

### Ventajas

- **Desarrollo rápido**: No necesitas saltar entre archivos CSS y HTML
- **Consistencia**: Los espaciados y colores siguen un sistema de diseño
- **Responsive**: Fácil hacer diseños responsive
- **Personalizable**: Puedes extender y personalizar todo

## Conceptos Fundamentales

### 1. Sistema de Espaciado

Tailwind usa una escala numérica donde cada número representa múltiplos de 0.25rem (4px):

| Clase | Tamaño | Píxeles |
|-------|--------|---------|
| p-0   | 0      | 0px     |
| p-1   | 0.25rem| 4px     |
| p-2   | 0.5rem | 8px     |
| p-4   | 1rem   | 16px    |
| p-8   | 2rem   | 32px    |
| p-12  | 3rem   | 48px    |

#### Direcciones de Espaciado

```html
<!-- Padding en todos los lados -->
<div class="p-4">...</div>

<!-- Padding horizontal (izquierda + derecha) -->
<div class="px-4">...</div>

<!-- Padding vertical (arriba + abajo) -->
<div class="py-4">...</div>

<!-- Padding individual -->
<div class="pt-4 pr-2 pb-4 pl-2">...</div>
<!-- pt = padding-top, pr = padding-right, etc. -->

<!-- Lo mismo aplica para margin (m-4, mx-4, my-4, etc.) -->
```

### 2. Sistema de Colores

Tailwind tiene colores predefinidos en diferentes tonalidades (50-900):

```html
<!-- Fondo azul -->
<div class="bg-blue-500">...</div>

<!-- Texto rojo -->
<div class="text-red-600">...</div>

<!-- Borde verde -->
<div class="border border-green-400">...</div>
```

Colores disponibles: gray, red, yellow, green, blue, indigo, purple, pink, etc.

### 3. Flexbox

Flexbox es fundamental para layouts modernos:

```html
<!-- Contenedor flex básico -->
<div class="flex">
    <div>Item 1</div>
    <div>Item 2</div>
</div>

<!-- Centrar elementos -->
<div class="flex justify-center items-center">
    Centrado horizontal y vertical
</div>

<!-- Espacio entre elementos -->
<div class="flex justify-between">
    <div>Izquierda</div>
    <div>Derecha</div>
</div>

<!-- Dirección de columna -->
<div class="flex flex-col">
    <div>Arriba</div>
    <div>Abajo</div>
</div>

<!-- Espaciado entre elementos flex -->
<div class="flex gap-4">
    <div>Item 1</div>
    <div>Item 2</div>
</div>
```

### 4. Grid

Grid CSS para layouts más complejos:

```html
<!-- 3 columnas iguales -->
<div class="grid grid-cols-3 gap-4">
    <div>1</div>
    <div>2</div>
    <div>3</div>
</div>

<!-- Responsive grid: 1 col en móvil, 2 en tablet, 3 en desktop -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
    <div>1</div>
    <div>2</div>
    <div>3</div>
</div>
```

### 5. Diseño Responsive

Tailwind usa breakpoints (puntos de quiebre) para responsive design:

| Prefijo | Tamaño Mínimo | Dispositivo |
|---------|---------------|-------------|
| (ninguno) | 0px        | Móvil       |
| sm:     | 640px         | Móvil grande|
| md:     | 768px         | Tablet      |
| lg:     | 1024px        | Laptop      |
| xl:     | 1280px        | Desktop     |
| 2xl:    | 1536px        | Desktop XL  |

**Mobile-first**: Sin prefijo = móvil, luego agregas prefijos para pantallas más grandes.

```html
<!-- Texto pequeño en móvil, grande en desktop -->
<h1 class="text-2xl md:text-4xl lg:text-6xl">
    Título Responsive
</h1>

<!-- Oculto en móvil, visible en desktop -->
<div class="hidden md:block">
    Solo visible en tablet y más grande
</div>

<!-- Visible en móvil, oculto en desktop -->
<div class="block md:hidden">
    Solo visible en móvil
</div>
```

### 6. Estados Interactivos

Pseudo-clases para interacciones:

```html
<!-- Hover (al pasar el mouse) -->
<button class="bg-blue-500 hover:bg-blue-700">
    Hover me
</button>

<!-- Focus (al hacer foco, ej. en inputs) -->
<input class="border focus:border-blue-500 focus:ring-2 focus:ring-blue-300">

<!-- Active (al hacer click) -->
<button class="bg-blue-500 active:bg-blue-900">
    Click me
</button>

<!-- Combinados -->
<button class="bg-blue-500 hover:bg-blue-700 active:bg-blue-900 transition duration-300">
    Botón con transiciones
</button>
```

### 7. Tipografía

```html
<!-- Tamaño de texto -->
<p class="text-xs">Extra pequeño</p>
<p class="text-sm">Pequeño</p>
<p class="text-base">Base (16px)</p>
<p class="text-lg">Grande</p>
<p class="text-xl">Extra grande</p>
<p class="text-2xl">2XL</p>
<p class="text-4xl">4XL</p>

<!-- Peso de fuente -->
<p class="font-light">Light</p>
<p class="font-normal">Normal</p>
<p class="font-semibold">Semi Bold</p>
<p class="font-bold">Bold</p>

<!-- Alineación -->
<p class="text-left">Izquierda</p>
<p class="text-center">Centro</p>
<p class="text-right">Derecha</p>

<!-- Altura de línea -->
<p class="leading-tight">Líneas juntas</p>
<p class="leading-relaxed">Líneas espaciadas</p>
```

### 8. Bordes y Sombras

```html
<!-- Bordes -->
<div class="border">Borde básico</div>
<div class="border-2">Borde grueso</div>
<div class="border-t-4">Borde superior extra grueso</div>

<!-- Bordes redondeados -->
<div class="rounded">Ligeramente redondeado</div>
<div class="rounded-lg">Redondeado grande</div>
<div class="rounded-full">Círculo completo</div>

<!-- Sombras -->
<div class="shadow-sm">Sombra pequeña</div>
<div class="shadow-md">Sombra mediana</div>
<div class="shadow-lg">Sombra grande</div>
<div class="shadow-xl">Sombra extra grande</div>
```

### 9. Efectos y Transiciones

```html
<!-- Transiciones -->
<button class="transition duration-300 ease-in-out hover:scale-110">
    Hover para agrandar
</button>

<!-- Opacidad -->
<div class="opacity-50">50% opaco</div>
<div class="opacity-100">100% opaco</div>

<!-- Transform -->
<div class="transform rotate-45">Rotado 45°</div>
<div class="transform scale-150">Agrandado 150%</div>
```

## Ejercicios Prácticos

### Ejercicio 1: Crear una Tarjeta (Card)

```html
<div class="bg-white rounded-lg shadow-lg p-6 max-w-sm">
    <h2 class="text-2xl font-bold mb-4">Título de la Tarjeta</h2>
    <p class="text-gray-600 mb-4">
        Esta es una tarjeta básica con Tailwind CSS.
    </p>
    <button class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-700 transition">
        Acción
    </button>
</div>
```

### Ejercicio 2: Navbar Responsive

```html
<nav class="bg-white shadow-md">
    <div class="container mx-auto px-4 py-4">
        <div class="flex justify-between items-center">
            <!-- Logo -->
            <div class="text-2xl font-bold">Logo</div>

            <!-- Menú Desktop -->
            <div class="hidden md:flex space-x-6">
                <a href="#" class="hover:text-blue-600">Inicio</a>
                <a href="#" class="hover:text-blue-600">Servicios</a>
                <a href="#" class="hover:text-blue-600">Contacto</a>
            </div>

            <!-- Botón Mobile -->
            <button class="md:hidden">
                ☰
            </button>
        </div>
    </div>
</nav>
```

### Ejercicio 3: Grid de Productos

```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    <!-- Producto 1 -->
    <div class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition">
        <div class="h-48 bg-blue-500"></div>
        <div class="p-6">
            <h3 class="text-xl font-bold mb-2">Producto 1</h3>
            <p class="text-gray-600 mb-4">Descripción del producto</p>
            <div class="flex justify-between items-center">
                <span class="text-2xl font-bold">$99</span>
                <button class="bg-blue-500 text-white px-4 py-2 rounded">Comprar</button>
            </div>
        </div>
    </div>

    <!-- Repite para más productos... -->
</div>
```

## Tips y Mejores Prácticas

### 1. Usa @apply para Componentes Repetidos

En `static/css/input.css`, puedes crear clases personalizadas:

```css
@layer components {
    .btn-primary {
        @apply bg-blue-500 text-white font-semibold py-2 px-6 rounded-lg hover:bg-blue-700 transition duration-300;
    }
}
```

Luego úsala en HTML:
```html
<button class="btn-primary">Mi Botón</button>
```

### 2. Container y Max-Width

```html
<!-- Contenedor centrado con max-width -->
<div class="container mx-auto px-4">
    Contenido centrado
</div>

<!-- O con max-width personalizado -->
<div class="max-w-4xl mx-auto px-4">
    Contenido con ancho máximo
</div>
```

### 3. Aspectos Importantes

- **Mobile-first**: Diseña para móvil primero, luego agrega clases para pantallas grandes
- **Consistencia**: Usa el sistema de espaciado de Tailwind (4, 8, 12, 16, etc.)
- **Reutilización**: Si repites las mismas clases, considera crear un componente
- **Legibilidad**: Organiza tus clases (layout → espaciado → tipografía → colores → efectos)

## Recursos Adicionales

### Documentación Oficial
- [Tailwind Docs](https://tailwindcss.com/docs) - Documentación completa
- [Tailwind Play](https://play.tailwindcss.com/) - Playground online

### Herramientas Útiles
- [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss) - Extension VS Code
- [Tailwind Cheat Sheet](https://nerdcave.com/tailwind-cheat-sheet)
- [Heroicons](https://heroicons.com/) - Iconos SVG optimizados

### Componentes Listos
- [Tailwind UI](https://tailwindui.com/) - Componentes oficiales (algunos gratis)
- [Flowbite](https://flowbite.com/) - Componentes gratuitos
- [DaisyUI](https://daisyui.com/) - Plugin con componentes

## Práctica en Tu Proyecto

Ahora que conoces los conceptos básicos, explora los archivos en `templates/`:

1. **base.html** - Mira el navbar y footer
2. **index.html** - Hero section y cards
3. **portfolio.html** - Grid de proyectos
4. **contact.html** - Formularios con Tailwind
5. **cv.html** - Timeline y layouts complejos

Todos tienen comentarios explicando las clases usadas.

## Desafíos para Practicar

1. **Cambia los colores** del theme en `tailwind.config.js`
2. **Crea una nueva sección** en index.html (ej. testimonios)
3. **Haz el navbar sticky** con `sticky top-0 z-50`
4. **Agrega animaciones** con `animate-pulse` o `animate-bounce`
5. **Crea un dark mode** (busca "dark mode tailwind" en la documentación)

---

**¡Experimenta, prueba y diviértete aprendiendo!** 🎨
