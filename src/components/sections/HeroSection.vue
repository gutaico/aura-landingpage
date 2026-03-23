<template>
  <section class="relative min-h-[100svh] flex items-center overflow-hidden">
    <div class="absolute inset-0 bg-brown-900"></div>
    <div class="absolute inset-0 grain"></div>

    <div class="relative z-10 mx-auto w-full max-w-7xl grid lg:grid-cols-2 gap-8 lg:gap-8 px-5 lg:px-10 pt-24 pb-12 lg:pt-32 lg:pb-24">
      <!-- Text -->
      <div class="flex flex-col justify-center">
        <p class="font-secondary text-[0.62rem] lg:text-[0.68rem] font-medium uppercase tracking-[0.25em] text-terracotta-300/80 mb-5 lg:mb-7">
          Publicidad especializada en belleza y bienestar
        </p>

        <h1 class="font-heading font-bold leading-[1.08] text-cream-50" style="letter-spacing: 0.01em;">
          <span class="block text-[clamp(1.8rem,8vw,3.8rem)]">Tu negocio merece</span>
          <span class="block text-[clamp(1.8rem,8vw,3.8rem)]">más que likes.</span>
          <span class="block text-[clamp(2rem,9vw,4.2rem)] text-terracotta-300 mt-1">
            Merece pacientes.
          </span>
        </h1>

        <p class="mt-5 lg:mt-8 max-w-md text-[0.9rem] lg:text-[1rem] leading-[1.7] text-cream-200/85">
          Publicidad para clínicas de estética y centros de bienestar que se mide
          en citas agendadas, pacientes que llegan y ventas que cierran.
        </p>

        <div class="mt-7 lg:mt-10">
          <a
            href="#agenda"
            class="group inline-flex items-center gap-3 font-secondary text-[0.82rem] font-semibold text-terracotta-300
                   hover:text-terracotta-200 transition-colors duration-300"
          >
            Agenda tu consultoría gratuita
            <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3" />
            </svg>
          </a>
        </div>

        <p class="mt-3 font-secondary text-[0.68rem] text-cream-300/50 tracking-wide">
          Sin compromiso · 30 minutos · Diagnóstico real
        </p>
      </div>

      <!-- Image — visible on ALL screens -->
      <div class="relative flex items-center justify-center mt-4 lg:mt-0">
        <img
          src="/img/hero-wellness-social.png"
          alt="Mujer en calma rodeada de notificaciones sociales"
          class="w-full max-w-[20rem] sm:max-w-sm lg:max-w-xl object-contain drop-shadow-[0_8px_32px_rgba(145,65,38,0.15)]"
        />
      </div>
    </div>

    <div class="absolute bottom-5 left-5 lg:left-10 hidden lg:block">
      <p class="font-secondary text-[0.62rem] uppercase tracking-[0.2em] text-cream-500/30 [writing-mode:vertical-lr]">
        Scroll
      </p>
    </div>
  </section>
</template>
