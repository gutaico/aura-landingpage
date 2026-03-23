<template>
  <section class="relative py-16 lg:py-32 px-5 lg:px-10 bg-cream-50">
    <div class="mx-auto max-w-6xl">
      <!-- Two-column: illustration + pain points -->
      <div class="grid lg:grid-cols-[2fr_3fr] gap-8 lg:gap-20 items-center">
        <!-- Image -->
        <div class="reveal flex justify-center">
          <img
            src="/img/pain-empty-chair.png"
            alt="Sala de espera vacía con notificaciones sin contestar"
            class="w-full max-w-[18rem] sm:max-w-xs lg:max-w-md object-contain"
          />
        </div>

        <!-- Pain points -->
        <div class="space-y-8 lg:space-y-14">
          <div
            v-for="(pain, i) in pains"
            :key="i"
            class="reveal flex gap-5 lg:gap-8 items-start"
            :class="'reveal-delay-' + (i + 1)"
          >
            <span class="font-heading text-[2.5rem] lg:text-[3rem] font-bold text-terracotta-200/50 leading-none shrink-0 pt-1">
              {{ String(i + 1).padStart(2, '0') }}
            </span>
            <div>
              <h3 class="font-heading text-[1.1rem] lg:text-[1.25rem] font-bold text-brown-800 leading-snug">
                {{ pain.title }}
              </h3>
              <p class="mt-2 text-[0.9rem] leading-[1.75] text-brown-400 max-w-md">
                {{ pain.description }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const pains = [
  {
    title: 'Inviertes en publicidad pero no ves pacientes nuevos.',
    description: 'Te reportan alcance e impresiones. Tú necesitas gente que agende, llegue y pague. Son cosas muy distintas.',
  },
  {
    title: 'Tus leads se enfrían antes de que alguien conteste.',
    description: 'Alguien te escribe por WhatsApp, tu equipo tarda en responder, y el lead se fue con la competencia.',
  },
  {
    title: 'Tus pacientes no regresan — y no es porque no quieran.',
    description: 'Les diste un gran servicio pero no volvieron. No porque no les gustó — porque nadie les recordó.',
  },
]
</script>
