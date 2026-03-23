<template>
  <section class="bg-cream-100 py-24 px-6">
    <div class="mx-auto max-w-6xl">
      <h2 class="text-center font-heading text-3xl font-bold text-brown-800 sm:text-4xl">
        No somos la agencia del sobrino.
      </h2>

      <div class="mt-16 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
        <div v-for="d in differentiators" :key="d.title" class="rounded-2xl bg-white p-6 shadow-sm">
          <div class="mb-3 flex h-8 w-8 items-center justify-center rounded-lg bg-terracotta-100 text-terracotta-600">
            <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7" />
            </svg>
          </div>
          <h3 class="font-heading text-base font-semibold text-brown-800">{{ d.title }}</h3>
          <p class="mt-2 text-sm text-brown-500 leading-relaxed">{{ d.description }}</p>
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
  { title: '21 días de implementación', description: 'En 3 semanas tienes todo el sistema instalado y generando resultados.' },
  { title: 'Transparencia total', description: 'Dashboard en tiempo real. Sin reportes mensuales que oculten. Los datos cuando quieras.' },
]
</script>
