<template>
  <section id="resultados" class="bg-brown-800 py-24 px-6">
    <div class="mx-auto max-w-6xl">
      <h2 class="text-center font-heading text-3xl font-bold text-cream-50 sm:text-4xl">
        Lo que los datos dicen.
      </h2>

      <!-- Stats bar -->
      <div class="mt-16 grid grid-cols-2 gap-6 lg:grid-cols-4">
        <div v-for="stat in stats" :key="stat.label" class="text-center">
          <p class="font-heading text-4xl font-bold text-terracotta-400 lg:text-5xl">{{ stat.value }}</p>
          <p class="mt-2 text-sm text-cream-300 leading-snug">{{ stat.label }}</p>
        </div>
      </div>

      <!-- Testimonials placeholder -->
      <div class="mt-20 grid gap-6 md:grid-cols-2">
        <div
          v-for="(testimonial, i) in testimonials"
          :key="i"
          class="rounded-2xl border border-cream-200/10 bg-brown-700/50 p-8"
        >
          <p class="text-cream-200 leading-relaxed italic">"{{ testimonial.quote }}"</p>
          <div class="mt-6 flex items-center gap-3">
            <div class="h-10 w-10 rounded-full bg-terracotta-500/30"></div>
            <div>
              <p class="text-sm font-semibold text-cream-100">{{ testimonial.name }}</p>
              <p class="text-xs text-cream-400">{{ testimonial.role }}</p>
            </div>
          </div>
        </div>
      </div>

      <p class="mt-6 text-center text-xs text-cream-500">
        *Rango típico: 3x-8x según tipo de tratamiento y madurez del negocio.
      </p>
    </div>
  </section>
</template>

<script setup>
const stats = [
  { value: '5x', label: 'de retorno por cada peso invertido*' },
  { value: '60-70%', label: 'de leads perdidos recuperados con nuestro sistema' },
  { value: '21 días', label: 'para tener todo instalado y corriendo' },
  { value: '$50-$300', label: 'MXN costo por paciente interesado' },
]

const testimonials = [
  {
    quote: 'Pasamos de 3 citas por semana a 12 en solo 6 semanas. El sistema de seguimiento automático fue lo que más impacto tuvo.',
    name: 'Caso de estudio',
    role: 'Clínica de estética facial — CDMX',
  },
  {
    quote: 'Por fin veo en un dashboard exactamente cuánto me cuesta cada paciente y cuánto me genera. Antes solo veía likes.',
    name: 'Caso de estudio',
    role: 'Centro de depilación láser — Monterrey',
  },
]
</script>
