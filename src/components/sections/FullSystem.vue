<template>
  <section id="que-incluye" class="bg-cream-50 py-24 px-6">
    <div class="mx-auto max-w-6xl">
      <div class="text-center">
        <h2 class="font-heading text-3xl font-bold text-brown-800 sm:text-4xl">
          No solo traemos pacientes.<br>
          <span class="text-terracotta-600">Los cuidamos hasta que regresen.</span>
        </h2>
        <p class="mx-auto mt-5 max-w-2xl text-brown-500 leading-relaxed">
          La mayoría de las agencias te traen leads y ahí se acaban. Nosotros construimos
          un sistema completo: desde que alguien ve tu anuncio hasta que regresa a su siguiente cita.
        </p>
      </div>

      <div class="mt-16 space-y-6">
        <div
          v-for="(mod, i) in modules"
          :key="i"
          class="flex flex-col gap-6 rounded-2xl border border-cream-200 bg-white p-8 md:flex-row md:items-start"
          :class="i % 2 === 1 ? 'md:flex-row-reverse' : ''"
        >
          <div class="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-terracotta-100 text-terracotta-600">
            <div v-html="mod.icon"></div>
          </div>
          <div>
            <h3 class="font-heading text-xl font-semibold text-brown-800">{{ mod.title }}</h3>
            <p class="mt-3 text-brown-500 leading-relaxed">{{ mod.description }}</p>
            <p v-if="mod.highlight" class="mt-3 text-sm font-medium text-terracotta-600">{{ mod.highlight }}</p>
            <div v-if="mod.tags" class="mt-4 flex flex-wrap gap-2">
              <span
                v-for="tag in mod.tags"
                :key="tag"
                class="rounded-full bg-cream-100 px-3 py-1 text-xs font-medium text-brown-600"
              >
                {{ tag }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const modules = [
  {
    title: 'Publicidad que convierte',
    description: 'Campañas diseñadas para tu sector. No vendemos tratamientos — vendemos la transformación emocional que viene después. Cada pieza de contenido habla el lenguaje de tu paciente, no jerga de marketing.',
    highlight: 'Los videos de pacientes reales generan hasta 4x más respuesta que las fotos de stock.',
    icon: '<svg class="h-7 w-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M11 5.882V19.24a1.76 1.76 0 01-3.417.592l-2.147-6.15M18 13a3 3 0 100-6M5.436 13.683A4.001 4.001 0 017 6h1.832c4.1 0 7.625-1.234 9.168-3v14c-1.543-1.766-5.067-3-9.168-3H7a3.988 3.988 0 01-1.564-.317z"/></svg>',
    tags: null,
  },
  {
    title: 'Tu CRM dedicado',
    description: 'Adiós al cuaderno y al WhatsApp personal. Te montamos un sistema donde ves exactamente quién llegó, quién agendó, quién fue a consulta y quién compró. Todo registrado, con seguimiento automático, en tiempo real.',
    highlight: null,
    icon: '<svg class="h-7 w-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 17V7m0 10a2 2 0 01-2 2H5a2 2 0 01-2-2V7a2 2 0 012-2h2a2 2 0 012 2m0 10a2 2 0 002 2h2a2 2 0 002-2M9 7a2 2 0 012-2h2a2 2 0 012 2m0 10V7m0 10a2 2 0 002 2h2a2 2 0 002-2V7a2 2 0 00-2-2h-2a2 2 0 00-2 2"/></svg>',
    tags: ['Seguimiento completo', 'WhatsApp automático', 'Dashboard en vivo', 'Automatizaciones'],
  },
  {
    title: 'Recuperación de leads',
    description: 'Un lead que no contesta no es un lead perdido. Seguimiento automatizado con el mensaje correcto en el momento correcto. No es spam — son toques estratégicos basados en el estado de cada persona.',
    highlight: 'Un negocio típico pierde el 60-70% de los leads que nunca contestan. Nuestro sistema los recupera.',
    icon: '<svg class="h-7 w-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 10h10a8 8 0 018 8v2M3 10l6 6m-6-6l6-6"/></svg>',
    tags: null,
  },
  {
    title: 'Retención de pacientes',
    description: 'Que tu paciente no olvide regresar. Tu negocio vive de la recurrencia. Montamos un sistema que se encarga de recordarles cuándo es su siguiente cita.',
    highlight: null,
    icon: '<svg class="h-7 w-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>',
    tags: ['Recordatorios de recurrencia', 'Campañas de relación', 'Recuperación win-back'],
  },
  {
    title: 'Producción profesional',
    description: 'Producimos contenido que habla el lenguaje emocional de tu paciente: video, fotografía, diseño y reels. Cada pieza está pensada desde lo que genera citas, no desde lo que se ve bonito.',
    highlight: null,
    icon: '<svg class="h-7 w-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg>',
    tags: ['Video testimonial', 'Antes/después', 'Reels del especialista', 'Diseño profesional'],
  },
]
</script>
