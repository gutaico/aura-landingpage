<template>
  <section id="como-funciona" class="bg-brown-800 py-24 px-6">
    <div class="mx-auto max-w-4xl">
      <div class="text-center">
        <h2 class="font-heading text-3xl font-bold text-cream-50 sm:text-4xl">
          Cada semana, tu inversión rinde más.
        </h2>
        <p class="mx-auto mt-5 max-w-2xl text-cream-300 leading-relaxed">
          No prometemos resultados mágicos. Prometemos un sistema que cada semana entiende
          mejor qué funciona para tu negocio — y corrige lo que no.
        </p>
      </div>

      <div class="mt-16 space-y-0">
        <div v-for="(step, i) in steps" :key="i" class="relative flex gap-6">
          <!-- Timeline line -->
          <div class="flex flex-col items-center">
            <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-terracotta-500 text-white font-bold text-sm">
              {{ i + 1 }}
            </div>
            <div v-if="i < steps.length - 1" class="w-px grow bg-terracotta-500/30 my-2"></div>
          </div>

          <div class="pb-12">
            <h3 class="font-heading text-xl font-semibold text-cream-50">{{ step.title }}</h3>
            <p class="mt-2 text-cream-300 text-sm leading-relaxed">{{ step.description }}</p>
          </div>
        </div>
      </div>

      <div class="mt-8 rounded-2xl border border-terracotta-500/20 bg-terracotta-500/10 p-6 text-center">
        <p class="text-cream-100 font-medium">
          El resultado: una espiral que se aprieta. Más pacientes del perfil correcto,
          por menos inversión. Semana tras semana.
        </p>
      </div>

      <div class="mt-10 text-center">
        <a
          href="#agenda"
          class="inline-flex items-center gap-2 rounded-full bg-terracotta-500 px-8 py-4 font-semibold text-white shadow-lg hover:bg-terracotta-400 transition-colors"
        >
          Quiero ver cómo aplicaría en mi negocio
          <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
          </svg>
        </a>
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
