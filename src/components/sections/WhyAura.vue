<template>
  <section class="relative bg-cream-50 py-16 lg:py-32 px-5 lg:px-10 overflow-hidden">
    <div class="relative mx-auto max-w-5xl">
      <!-- Header -->
      <div class="reveal max-w-2xl">
        <p class="font-secondary text-[0.68rem] font-medium uppercase tracking-[0.25em] text-terracotta-500 mb-5">
          Por qué nosotros
        </p>
        <h2 class="font-heading text-[clamp(1.7rem,3vw,2.5rem)] font-bold text-brown-800 leading-[1.12]">
          No somos la agencia del sobrino.
        </h2>
      </div>

      <!-- Grid — clean list, checkmarks, no containers -->
      <div class="mt-14 lg:mt-16 grid sm:grid-cols-2 lg:grid-cols-3 gap-x-12 lg:gap-x-16 gap-y-10">
        <div
          v-for="(d, i) in differentiators"
          :key="d.title"
          class="reveal"
          :class="'reveal-delay-' + Math.min(i + 1, 3)"
        >
          <div class="flex items-center gap-2.5 mb-3">
            <svg class="h-4 w-4 text-terracotta-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
            </svg>
            <h3 class="font-heading text-[0.92rem] font-bold text-brown-800">{{ d.title }}</h3>
          </div>
          <p class="text-[0.85rem] text-brown-400 leading-[1.7] pl-[1.62rem]">{{ d.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const differentiators = [
  { title: 'Especializados en belleza y wellness', description: 'No somos una agencia que le hace de todo a todos. Solo trabajamos con negocios como el tuyo.' },
  { title: 'Mecanismo autocorrectivo', description: 'Tu inversión mejora cada semana. No prometemos — convergemos.' },
  { title: 'CRM y automatización incluidos', description: 'Pipeline, seguimiento, nurturing y retención. Desde el día uno.' },
  { title: 'Producción profesional', description: 'Contenido que conecta con la emoción de tu paciente. No diseños genéricos.' },
  { title: '7 días hábiles de implementación', description: 'En una semana tienes todo el sistema instalado y generando resultados.' },
  { title: 'Transparencia total', description: 'Dashboard en tiempo real. Sin reportes mensuales que oculten. Los datos cuando quieras.' },
]
</script>
