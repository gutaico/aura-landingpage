<template>
  <section id="resultados" class="relative bg-cream-50 py-16 lg:py-32 px-5 lg:px-10 overflow-hidden">
    <div class="relative mx-auto max-w-6xl">
      <!-- Header + stats -->
      <div class="grid lg:grid-cols-[3fr_2fr] gap-12 lg:gap-20 items-start">
        <div>
          <div class="reveal">
            <p class="font-secondary text-[0.68rem] font-medium uppercase tracking-[0.25em] text-terracotta-500 mb-5">
              Resultados reales
            </p>
            <h2 class="font-heading text-[clamp(1.7rem,3vw,2.5rem)] font-bold text-brown-800 leading-[1.12]">
              Lo que los datos dicen.
            </h2>
          </div>

          <!-- Stats -->
          <div class="mt-12 grid grid-cols-2 gap-8 reveal">
            <div v-for="(stat, i) in stats" :key="stat.label" :class="'reveal-delay-' + (i + 1)">
              <p class="font-heading text-[clamp(2.2rem,4vw,3rem)] font-bold text-terracotta-500 leading-none">
                {{ stat.value }}
              </p>
              <p class="font-secondary mt-2 text-[0.75rem] text-brown-400 leading-snug max-w-[10rem]">{{ stat.label }}</p>
            </div>
          </div>
        </div>

        <!-- Image — full agenda -->
        <div class="reveal flex justify-center lg:pt-8">
          <img
            src="/img/results-full-agenda.png"
            alt="Agenda llena de citas con notificación de nueva cita agendada"
            class="w-full max-w-[18rem] sm:max-w-xs lg:max-w-md object-contain"
          />
        </div>
      </div>

      <!-- Testimonials -->
      <div class="mt-16 lg:mt-20 grid lg:grid-cols-2 gap-10 lg:gap-20">
        <div
          v-for="(testimonial, i) in testimonials"
          :key="i"
          class="reveal"
          :class="'reveal-delay-' + (i + 1)"
        >
          <p class="text-[1.05rem] leading-[1.8] text-brown-700 italic">
            "{{ testimonial.quote }}"
          </p>
          <div class="mt-5 flex items-center gap-3">
            <div class="w-8 h-px bg-terracotta-400"></div>
            <div>
              <p class="font-secondary text-[0.78rem] font-semibold text-brown-700">{{ testimonial.name }}</p>
              <p class="font-secondary text-[0.68rem] text-brown-400">{{ testimonial.role }}</p>
            </div>
          </div>
        </div>
      </div>

      <p class="reveal mt-10 font-secondary text-[0.68rem] text-brown-300">
        *Rango típico: 3x-8x según tipo de tratamiento y madurez del negocio.
      </p>
    </div>
  </section>
</template>

<script setup>
const stats = [
  { value: '5x', label: 'de retorno por cada peso invertido*' },
  { value: '60%', label: 'de leads perdidos recuperados' },
  { value: '21', label: 'días para tener todo instalado' },
  { value: '$300', label: 'MXN costo máximo por paciente interesado' },
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
