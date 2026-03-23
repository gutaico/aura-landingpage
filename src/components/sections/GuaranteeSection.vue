<template>
  <section class="relative py-16 lg:py-36 px-5 lg:px-10 overflow-hidden">
    <!-- Background: deep warm -->
    <div class="absolute inset-0 bg-brown-900"></div>
    <div class="absolute inset-0 grain"></div>

    <div class="relative mx-auto max-w-5xl">
      <!-- Two-column: illustration + text -->
      <div class="grid lg:grid-cols-2 gap-8 lg:gap-16 items-center">
        <!-- Image — guarantee shield -->
        <div class="reveal flex justify-center">
          <img
            src="/img/guarantee-shield.png"
            alt="Mujer profesional con escudo de garantía 90 días"
            class="w-full max-w-[18rem] sm:max-w-xs lg:max-w-md object-contain"
          />
        </div>

        <!-- Text -->
        <div class="reveal reveal-delay-1">
          <p class="font-secondary text-[0.68rem] font-medium uppercase tracking-[0.3em] text-terracotta-300/80 mb-6">
            Garantía de resultados
          </p>

          <h2 class="font-heading text-[clamp(2rem,4vw,3rem)] font-bold text-cream-50 leading-[1.08]">
            90 días.
            Si no cumplimos,
            <span class="text-terracotta-400">te devolvemos todo.</span>
          </h2>

          <p class="mt-8 text-cream-200/80 leading-[1.8] text-[1rem] max-w-lg">
            Si en 90 días desde el lanzamiento de tus campañas no alcanzamos el mínimo
            de prospectos calificados que definimos juntos, te reembolsamos el 100%.
            Setup, retainers, todo.
          </p>
        </div>
      </div>

      <!-- Divider -->
      <div class="mx-auto w-12 h-px bg-terracotta-500/25 my-14 reveal"></div>

      <!-- Three pillars — simple, no cards -->
      <div class="grid md:grid-cols-3 gap-8 lg:gap-16 reveal">
        <div v-for="(pillar, i) in pillars" :key="i" class="text-center md:text-left">
          <h3 class="font-heading text-[1rem] font-bold text-cream-100 leading-snug">{{ pillar.title }}</h3>
          <p class="mt-3 text-[0.85rem] leading-[1.75] text-cream-300/80">{{ pillar.description }}</p>
        </div>
      </div>

      <!-- Closing quote -->
      <div class="reveal mt-16 text-center">
        <p class="text-cream-200/80 text-[1.05rem] italic leading-relaxed max-w-2xl mx-auto">
          "Tu peor escenario es que te devolvamos todo el dinero.
          Tu mejor escenario es una máquina que te trae pacientes cada semana."
        </p>
      </div>

      <!-- CTA — text link, not button -->
      <div class="reveal mt-10 text-center">
        <a
          href="#agenda"
          class="group inline-flex items-center gap-2 font-secondary text-[0.85rem] font-semibold text-terracotta-400
                 hover:text-terracotta-300 transition-colors duration-300"
        >
          Agenda tu consultoría — sin riesgo
          <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3" />
          </svg>
        </a>
      </div>
    </div>
  </section>
</template>

<script setup>
const pillars = [
  {
    title: 'La meta la definimos juntos',
    description: 'Durante el onboarding cruzamos tu inversión, tu capacidad operativa y los benchmarks del sector. El número mínimo lo firmamos ambos.',
  },
  {
    title: 'Compromiso bilateral',
    description: 'Nosotros ponemos el mecanismo, tú pones la respuesta a los leads y el presupuesto acordado. Si ambos cumplimos y no llegan los resultados, el dinero es tuyo.',
  },
  {
    title: 'Ninguna agencia te ofrece esto',
    description: 'Podemos hacerlo porque confiamos en el mecanismo. Si no funciona, preferimos devolver el dinero y quedarnos con la reputación intacta.',
  },
]
</script>
