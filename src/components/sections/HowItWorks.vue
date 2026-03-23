<template>
  <section id="como-funciona" class="relative bg-cream-50 py-16 lg:py-32 px-5 lg:px-10 overflow-hidden">
    <div class="relative mx-auto max-w-7xl">
      <div class="grid lg:grid-cols-2 gap-8 lg:gap-20">
        <!-- Text -->
        <div>
          <p class="font-secondary text-[0.68rem] font-medium uppercase tracking-[0.25em] text-terracotta-500 mb-5 reveal">
            El mecanismo
          </p>
          <h2 class="font-heading text-[clamp(1.7rem,3vw,2.5rem)] font-bold text-brown-800 leading-[1.12] reveal">
            Cada semana, tu inversión rinde más.
          </h2>
          <p class="mt-6 text-brown-400 leading-[1.8] text-[0.95rem] max-w-lg reveal">
            No prometemos resultados mágicos. Prometemos un sistema que cada semana entiende
            mejor qué funciona para tu negocio — y corrige lo que no.
          </p>

          <div class="mt-10 lg:mt-12 space-y-7 lg:space-y-8">
            <div
              v-for="(step, i) in steps"
              :key="i"
              class="reveal flex gap-4 lg:gap-5"
              :class="'reveal-delay-' + (i + 1)"
            >
              <span class="font-heading text-[1.6rem] lg:text-[1.8rem] font-bold text-terracotta-300/40 leading-none pt-0.5">{{ i + 1 }}</span>
              <div>
                <h3 class="font-heading text-[1rem] lg:text-[1.05rem] font-bold text-brown-800">{{ step.title }}</h3>
                <p class="mt-1.5 text-brown-400 text-[0.85rem] lg:text-[0.88rem] leading-relaxed">{{ step.description }}</p>
              </div>
            </div>
          </div>

          <div class="mt-10 lg:mt-12 reveal">
            <a
              href="#agenda"
              class="group inline-flex items-center gap-2 font-secondary text-[0.82rem] font-semibold text-terracotta-500
                     hover:text-terracotta-600 transition-colors duration-300"
            >
              Quiero ver cómo aplicaría en mi negocio
              <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3" />
              </svg>
            </a>
          </div>
        </div>

        <!-- Image -->
        <div class="reveal flex items-center justify-center mt-4 lg:mt-0">
          <img
            src="/img/mechanism-dashboard.png"
            alt="Dashboard mostrando métricas que mejoran semana tras semana"
            class="w-full max-w-[18rem] sm:max-w-sm lg:max-w-lg object-contain"
          />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const steps = [
  { title: 'Lanzamos', description: 'Campañas basadas en lo que mueve a tu paciente. Con hipótesis claras, no adivinanzas.' },
  { title: 'Medimos', description: 'Resultados reales: citas agendadas, leads calificados, cierres. No vanidad.' },
  { title: 'Analizamos', description: 'Qué ángulo conectó, qué mensaje convirtió, qué hay que ajustar.' },
  { title: 'Corregimos', description: 'Ajustes semanales. Con cada ciclo, el costo por paciente baja y la calidad sube.' },
]
</script>
