<template>
  <section id="que-incluye" class="relative bg-cream-50 py-16 lg:py-32 px-5 lg:px-10 overflow-hidden">
    <div class="relative mx-auto max-w-6xl">
      <!-- Header -->
      <div class="max-w-2xl reveal">
        <p class="font-secondary text-[0.68rem] font-medium uppercase tracking-[0.25em] text-terracotta-500 mb-5">
          El sistema completo
        </p>
        <h2 class="font-heading text-[clamp(1.7rem,3vw,2.5rem)] font-bold text-brown-800 leading-[1.12]">
          No solo traemos pacientes.
          <span class="text-terracotta-600">Los cuidamos hasta que regresen.</span>
        </h2>
        <p class="mt-6 text-brown-400 leading-[1.8] text-[0.95rem]">
          La mayoría de las agencias te traen leads y ahí se acaban. Nosotros construimos
          un sistema completo: desde que alguien ve tu anuncio hasta que regresa a su siguiente cita.
        </p>
      </div>

      <!-- Journey illustration — full width -->
      <div class="reveal mt-14 lg:mt-16 flex justify-center">
        <img
          src="/img/system-complete.png"
          alt="Journey del paciente: anuncio, WhatsApp, agenda, clínica, paciente feliz"
          class="w-full max-w-3xl object-contain"
        />
      </div>

      <!-- Modules list below -->
      <div class="mt-16 lg:mt-20 grid sm:grid-cols-2 lg:grid-cols-5 gap-8 lg:gap-6">
        <div
          v-for="(mod, i) in modules"
          :key="i"
          class="reveal text-center"
          :class="'reveal-delay-' + Math.min(i + 1, 5)"
        >
          <div class="flex items-center justify-center gap-2 mb-3">
            <div class="w-6 h-px bg-terracotta-400"></div>
            <span class="font-secondary text-[0.65rem] font-medium uppercase tracking-[0.15em] text-terracotta-500">
              {{ String(i + 1).padStart(2, '0') }}
            </span>
            <div class="w-6 h-px bg-terracotta-400"></div>
          </div>
          <h3 class="font-heading text-[0.95rem] font-bold text-brown-800 leading-snug">{{ mod.title }}</h3>
          <p class="mt-2 text-[0.8rem] leading-relaxed text-brown-400">{{ mod.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const modules = [
  {
    title: 'Publicidad',
    description: 'Campañas que hablan el lenguaje emocional de tu paciente.',
  },
  {
    title: 'CRM',
    description: 'Pipeline completo: quién llegó, quién agendó, quién compró.',
  },
  {
    title: 'Recuperación',
    description: 'Seguimiento automático que rescata el 60-70% de leads perdidos.',
  },
  {
    title: 'Retención',
    description: 'Tu paciente no olvida regresar. Recordatorios y campañas de relación.',
  },
  {
    title: 'Producción',
    description: 'Video, foto y diseño que genera citas, no solo likes.',
  },
]
</script>
