# Aura Landing Page

Landing page de Aura Marketing — la cara pública de la primera vertical de Gutai Co. Advertising, especializada en bienestar, estética y salud personal.

## Stack

- **Vue 3** (Composition API con `<script setup>`)
- **Vite 8** (build tool)
- **Tailwind CSS 4**

## Desarrollo

```bash
npm install
npm run dev       # servidor de desarrollo
npm run build     # build de producción → dist/
npm run preview   # preview del build
```

## Estructura

```
src/
├── App.vue                       ← layout principal
├── main.js                       ← entry point
├── style.css                     ← estilos globales + Tailwind
├── composables/
│   └── useReveal.js              ← animación de scroll reveal
├── components/
│   ├── NavHeader.vue
│   ├── FooterSection.vue
│   └── sections/                 ← secciones de la landing
│       ├── HeroSection.vue
│       ├── PainBar.vue
│       ├── WhyAura.vue
│       ├── HowItWorks.vue
│       ├── UnderstandPatient.vue
│       ├── Results.vue
│       ├── FullSystem.vue
│       ├── GuaranteeSection.vue
│       ├── FaqSection.vue
│       └── CtaForm.vue
└── assets/
```

## Deploy

Desplegada en Vercel. El build de producción vive en `dist/`.

## Relación con el proyecto

El contenido y el mensaje de esta landing están alineados con la documentación de Aura: el copy refleja los ángulos del proceso creativo (`../sector/`), la propuesta de valor del mecanismo autocorrectivo (`../../_compartido/metodologia/`), y la garantía de resultados (`../../_compartido/recursos-comerciales/garantia-de-resultados.md`).
