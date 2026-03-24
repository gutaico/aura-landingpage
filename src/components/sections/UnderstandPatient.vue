<template>
  <section class="relative py-16 lg:py-32 px-5 lg:px-10 overflow-hidden">
    <div class="absolute inset-0 bg-cream-50"></div>

    <div class="relative mx-auto max-w-6xl">
      <div class="grid lg:grid-cols-2 gap-8 lg:gap-20 items-center">
        <!-- Image — mirror transformation -->
        <div class="reveal flex justify-center order-2 lg:order-1">
          <img
            src="/img/patient-journey.png"
            alt="Mujer mirándose al espejo viendo una versión más confiada de sí misma"
            class="w-full max-w-[18rem] sm:max-w-xs lg:max-w-lg object-contain"
          />
        </div>

        <!-- Text -->
        <div class="reveal reveal-delay-1 order-1 lg:order-2">
          <p class="font-secondary text-[0.68rem] font-medium uppercase tracking-[0.25em] text-terracotta-500 mb-5">
            Expertise del sector
          </p>
          <h2 class="font-heading text-[clamp(1.7rem,3vw,2.5rem)] font-bold text-brown-800 leading-[1.12]">
            No somos una agencia genérica.
            <span class="text-terracotta-600">Entendemos por qué tu paciente compra.</span>
          </h2>
          <p class="mt-6 text-brown-400 leading-[1.8] text-[0.95rem] max-w-lg">
            Cada anuncio, cada mensaje, cada toque de seguimiento está diseñado
            desde la psicología de compra de tu paciente.
          </p>

          <div class="mt-8 lg:mt-10 space-y-5 lg:space-y-6">
            <div
              v-for="item in transformations"
              :key="item.before"
              class="flex items-baseline gap-2 sm:gap-4"
            >
              <span class="font-secondary text-[0.65rem] sm:text-[0.72rem] uppercase tracking-wider text-brown-300 w-20 sm:w-28 shrink-0">{{ item.before }}</span>
              <span class="text-terracotta-500 text-xs sm:text-sm shrink-0">→</span>
              <div class="min-w-0">
                <span class="font-secondary text-[0.65rem] sm:text-[0.72rem] uppercase tracking-wider text-terracotta-600 font-semibold">{{ item.after }}</span>
                <p class="mt-1 text-[0.82rem] sm:text-[0.85rem] leading-relaxed text-brown-400">{{ item.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const transformations = [
  {
    before: 'Inseguridad',
    after: 'Confianza',
    description: 'Tu paciente busca sentirse bien consigo mismo. Nosotros hablamos a esa emoción.',
  },
  {
    before: 'Miedo',
    after: 'Curiosidad',
    description: 'Nuestro contenido desmitifica el proceso y convierte el miedo en ganas de agendar.',
  },
  {
    before: 'Desconfianza',
    after: 'Autoridad',
    description: 'Posicionamos a tu especialista como la figura de confianza: en cámara, con resultados.',
  },
  {
    before: '"Algún día"',
    after: 'Ahora',
    description: 'Convertimos la intención en acción con urgencia suave y facilitadores reales.',
  },
]
</script>
