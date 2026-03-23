<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const visible = ref(true)
const scrolled = ref(false)
const mobileOpen = ref(false)
let lastY = 0

function onScroll() {
  const y = window.scrollY
  scrolled.value = y > 60

  // Hide on scroll down, show on scroll up (after first 100px)
  if (y > 100) {
    visible.value = y < lastY
  } else {
    visible.value = true
  }
  lastY = y
}

function scrollTo(id) {
  mobileOpen.value = false
  const el = document.getElementById(id)
  if (el) el.scrollIntoView({ behavior: 'smooth' })
}

onMounted(() => window.addEventListener('scroll', onScroll, { passive: true }))
onUnmounted(() => window.removeEventListener('scroll', onScroll))
</script>

<template>
  <header
    :class="[
      'fixed top-0 inset-x-0 z-50 transition-all duration-500',
      visible ? 'translate-y-0' : '-translate-y-full',
      'bg-transparent'
    ]"
  >
    <nav class="mx-auto flex max-w-7xl items-center justify-between px-5 lg:px-10 py-4 lg:py-5">
      <a href="#" class="block">
        <img
          :src="scrolled ? '/img/logo-dark.png' : '/img/logo-light.png'"
          alt="Aura Marketing"
          class="h-5 lg:h-6 w-auto transition-opacity duration-500"
        />
      </a>

      <!-- Desktop -->
      <div class="hidden items-center gap-9 md:flex">
        <button
          v-for="link in [
            { id: 'como-funciona', label: 'Cómo funciona' },
            { id: 'que-incluye', label: 'Sistema' },
            { id: 'resultados', label: 'Resultados' },
          ]"
          :key="link.id"
          @click="scrollTo(link.id)"
          class="font-secondary text-[0.72rem] font-medium uppercase bg-transparent border-none cursor-pointer transition-colors duration-300"
          :class="scrolled ? 'text-brown-400 hover:text-brown-700' : 'text-cream-300/70 hover:text-cream-100'"
          style="letter-spacing: 0.12em;"
        >
          {{ link.label }}
        </button>
        <button
          @click="scrollTo('agenda')"
          class="font-secondary text-[0.72rem] font-semibold uppercase bg-transparent border-none cursor-pointer transition-colors duration-300"
          :class="scrolled ? 'text-terracotta-600 hover:text-terracotta-700' : 'text-terracotta-400 hover:text-terracotta-300'"
          style="letter-spacing: 0.1em;"
        >
          Agendar →
        </button>
      </div>

      <!-- Mobile -->
      <div class="flex items-center gap-3 md:hidden">
        <button
          @click="scrollTo('agenda')"
          class="font-secondary text-[0.68rem] font-semibold uppercase bg-transparent border-none cursor-pointer transition-colors duration-300"
          :class="scrolled ? 'text-terracotta-600' : 'text-terracotta-400'"
          style="letter-spacing: 0.1em;"
        >
          Agendar
        </button>
        <button
          @click="mobileOpen = !mobileOpen"
          :class="[
            'p-1 bg-transparent border-none cursor-pointer transition-colors',
            scrolled ? 'text-brown-600' : 'text-cream-200'
          ]"
        >
          <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5">
            <path v-if="!mobileOpen" stroke-linecap="round" stroke-linejoin="round" d="M3.75 9h16.5M3.75 15.75h16.5" />
            <path v-else stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>
    </nav>

    <Transition
      enter-active-class="transition-all duration-300 ease-out"
      enter-from-class="opacity-0 -translate-y-2"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition-all duration-200 ease-in"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 -translate-y-2"
    >
      <div
        v-if="mobileOpen"
        class="bg-cream-50/95 backdrop-blur-lg px-5 pb-5 pt-2 md:hidden"
      >
        <button
          v-for="link in [
            { id: 'como-funciona', label: 'Cómo funciona' },
            { id: 'que-incluye', label: 'Qué incluye' },
            { id: 'resultados', label: 'Resultados' },
            { id: 'agenda', label: 'Agendar consultoría' },
          ]"
          :key="link.id"
          @click="scrollTo(link.id)"
          class="block w-full text-left py-3 text-sm text-brown-600 font-medium bg-transparent border-none cursor-pointer"
        >
          {{ link.label }}
        </button>
      </div>
    </Transition>
  </header>
</template>
