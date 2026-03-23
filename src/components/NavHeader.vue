<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const scrolled = ref(false)
const mobileOpen = ref(false)

function onScroll() {
  scrolled.value = window.scrollY > 20
}

onMounted(() => window.addEventListener('scroll', onScroll))
onUnmounted(() => window.removeEventListener('scroll', onScroll))
</script>

<template>
  <header
    :class="[
      'fixed top-0 inset-x-0 z-50 transition-all duration-300',
      scrolled ? 'bg-cream-50/95 backdrop-blur-md shadow-sm' : 'bg-transparent'
    ]"
  >
    <nav class="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
      <!-- Logo -->
      <a href="#" class="font-heading text-2xl font-bold text-terracotta-700 tracking-tight">
        AURA
      </a>

      <!-- Desktop nav -->
      <div class="hidden items-center gap-8 md:flex">
        <a href="#como-funciona" class="text-sm font-medium text-brown-600 hover:text-terracotta-600 transition-colors">
          Cómo funciona
        </a>
        <a href="#que-incluye" class="text-sm font-medium text-brown-600 hover:text-terracotta-600 transition-colors">
          Qué incluye
        </a>
        <a href="#resultados" class="text-sm font-medium text-brown-600 hover:text-terracotta-600 transition-colors">
          Resultados
        </a>
        <a
          href="#agenda"
          class="rounded-full bg-terracotta-600 px-5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-terracotta-700 transition-colors"
        >
          Agenda tu consultoría gratuita
        </a>
      </div>

      <!-- Mobile CTA + hamburger -->
      <div class="flex items-center gap-3 md:hidden">
        <a
          href="#agenda"
          class="rounded-full bg-terracotta-600 px-4 py-2 text-xs font-semibold text-white"
        >
          Agendar
        </a>
        <button @click="mobileOpen = !mobileOpen" class="text-brown-700 p-1">
          <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path v-if="!mobileOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>
    </nav>

    <!-- Mobile menu -->
    <div
      v-if="mobileOpen"
      class="border-t border-cream-200 bg-cream-50/95 backdrop-blur-md px-6 pb-4 md:hidden"
    >
      <a href="#como-funciona" @click="mobileOpen = false" class="block py-3 text-sm text-brown-600">Cómo funciona</a>
      <a href="#que-incluye" @click="mobileOpen = false" class="block py-3 text-sm text-brown-600">Qué incluye</a>
      <a href="#resultados" @click="mobileOpen = false" class="block py-3 text-sm text-brown-600">Resultados</a>
    </div>
  </header>
</template>
