<template>
  <section class="relative min-h-screen flex items-center justify-center bg-gradient-to-br from-brown-800 via-brown-900 to-brown-800 px-6 pt-20">
    <!-- Overlay pattern -->
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_30%_40%,rgba(194,106,61,0.15),transparent_60%)]"></div>

    <div class="relative z-10 mx-auto max-w-3xl text-center">
      <h1 class="font-heading text-4xl font-bold leading-tight text-cream-50 sm:text-5xl lg:text-6xl">
        Tu negocio merece más que likes.
        <span class="block text-terracotta-400">Merece pacientes.</span>
      </h1>

      <p class="mx-auto mt-6 max-w-2xl text-lg text-cream-300 leading-relaxed">
        Publicidad para clínicas de estética y centros de bienestar que se mide
        en citas agendadas, pacientes que llegan y ventas que cierran. No en impresiones.
      </p>

      <div class="mt-10">
        <a
          href="#agenda"
          class="inline-flex items-center gap-2 rounded-full bg-terracotta-500 px-8 py-4 text-lg font-semibold text-white shadow-lg hover:bg-terracotta-600 transition-all hover:shadow-xl hover:scale-[1.02]"
        >
          Agenda tu consultoría gratuita
          <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
          </svg>
        </a>
      </div>

      <p class="mt-4 text-sm text-cream-400">
        Sin compromiso. 30 minutos. Diagnóstico real de tu situación actual.
      </p>
    </div>
  </section>
</template>
