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

      <!-- Testimonials — visual cards with metrics -->
      <div class="mt-16 lg:mt-24 grid md:grid-cols-3 gap-4 lg:gap-5">
        <div
          v-for="(t, i) in testimonials"
          :key="i"
          class="reveal rounded-xl lg:rounded-2xl bg-white border border-cream-200/60 p-6 lg:p-7
                 hover:shadow-[0_8px_32px_rgba(74,52,40,0.06)] transition-shadow duration-500"
          :class="'reveal-delay-' + (i + 1)"
        >
          <!-- Key metric -->
          <div class="mb-5">
            <p class="font-heading text-[1.8rem] lg:text-[2.2rem] font-bold text-terracotta-500 leading-none">
              {{ t.metric }}
            </p>
            <p class="font-secondary text-[0.68rem] text-brown-400 mt-1">{{ t.metricLabel }}</p>
          </div>

          <!-- Divider -->
          <div class="w-8 h-px bg-terracotta-300/40 mb-4"></div>

          <!-- Quote -->
          <p class="text-[0.88rem] leading-[1.7] text-brown-600 italic">
            "{{ t.quote }}"
          </p>

          <!-- Author -->
          <div class="mt-5 flex items-center gap-3">
            <div class="w-9 h-9 rounded-full flex items-center justify-center text-[0.7rem] font-bold"
                 :class="['bg-terracotta-100/60 text-terracotta-600', 'bg-cream-200 text-brown-500', 'bg-brown-100 text-brown-600'][i]">
              {{ t.initials }}
            </div>
            <div>
              <p class="font-secondary text-[0.78rem] font-semibold text-brown-700">{{ t.name }}</p>
              <p class="font-secondary text-[0.65rem] text-brown-400">{{ t.role }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Logo bar -->
      <div class="reveal mt-16 lg:mt-20">
        <p class="font-secondary text-[0.65rem] uppercase tracking-[0.2em] text-brown-300 text-center mb-8">
          Negocios que confían en nosotros
        </p>
        <div class="flex flex-wrap items-center justify-center gap-8 lg:gap-14">
          <div
            v-for="(logo, i) in logos"
            :key="i"
            class="flex items-center justify-center h-8 lg:h-9 opacity-30 hover:opacity-50 transition-opacity duration-300"
          >
            <!-- Placeholder logos — text-based -->
            <span class="font-heading text-[0.85rem] lg:text-[1rem] font-bold text-brown-400 tracking-wider uppercase"
                  :style="{ letterSpacing: logo.spacing || '0.1em' }">
              {{ logo.name }}
            </span>
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
  { value: '7', label: 'días hábiles para tener todo instalado' },
  { value: '$300', label: 'MXN costo máximo por paciente interesado' },
]

const testimonials = [
  {
    metric: '4x',
    metricLabel: 'más citas por semana en 6 semanas',
    quote: 'Pasamos de 3 citas por semana a 12. El sistema de seguimiento automático fue lo que más impacto tuvo.',
    name: 'Dra. Mariana Solís',
    role: 'Clínica de estética facial — CDMX',
    initials: 'MS',
  },
  {
    metric: '-62%',
    metricLabel: 'en costo por paciente nuevo',
    quote: 'Por fin veo exactamente cuánto me cuesta cada paciente y cuánto me genera. Dejé de tirar dinero.',
    name: 'Carlos Mendoza',
    role: 'Centro de depilación láser — Monterrey',
    initials: 'CM',
  },
  {
    metric: '38',
    metricLabel: 'pacientes recuperados en un mes',
    quote: 'Tenía una base de 200 pacientes que no regresaban. En un mes reactivaron 38 solo con el nurturing automático.',
    name: 'Lic. Andrea Reyes',
    role: 'Clínica capilar — Guadalajara',
    initials: 'AR',
  },
]

const logos = [
  { name: 'Dermaclinic', spacing: '0.12em' },
  { name: 'Bella Vita', spacing: '0.08em' },
  { name: 'Glow Studio', spacing: '0.1em' },
  { name: 'Vitae Spa', spacing: '0.15em' },
  { name: 'Estética Luxe', spacing: '0.08em' },
  { name: 'Nova Skin', spacing: '0.12em' },
]
</script>
