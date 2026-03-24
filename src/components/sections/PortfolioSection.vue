<script setup>
import { ref, computed, onMounted, nextTick } from 'vue'

const showAll = ref(false)
const loaded = ref(new Set())
const sectionVisible = ref(false)

const INITIAL_COUNT = 6

const works = [
  { id: 1, type: 'video', aspect: 'tall', label: 'Reel — Clínica facial', category: 'Video' },
  { id: 2, type: 'photo', aspect: 'wide', label: 'Campaña — Depilación láser', category: 'Fotografía' },
  { id: 3, type: 'design', aspect: 'square', label: 'Carrusel — Medicina estética', category: 'Diseño' },
  { id: 4, type: 'video', aspect: 'tall', label: 'Testimonial — Clínica capilar', category: 'Video' },
  { id: 5, type: 'photo', aspect: 'wide', label: 'Antes/Después — Tratamiento corporal', category: 'Fotografía' },
  { id: 6, type: 'design', aspect: 'square', label: 'Stories — Centro de wellness', category: 'Diseño' },
  { id: 7, type: 'video', aspect: 'wide', label: 'Reel — Spa day experience', category: 'Video' },
  { id: 8, type: 'photo', aspect: 'tall', label: 'Branding — Consultorio dental', category: 'Fotografía' },
  { id: 9, type: 'design', aspect: 'square', label: 'Anuncio — Promoción temporada', category: 'Diseño' },
]

const visibleWorks = computed(() => showAll.value ? works : works.slice(0, INITIAL_COUNT))

// Placeholder colors matching brand
const placeholderColors = [
  'bg-gradient-to-br from-terracotta-200/60 to-terracotta-300/40',
  'bg-gradient-to-br from-cream-300/80 to-cream-400/60',
  'bg-gradient-to-br from-brown-200/60 to-brown-300/40',
  'bg-gradient-to-br from-terracotta-100/70 to-cream-200/50',
  'bg-gradient-to-br from-brown-100/80 to-cream-300/60',
  'bg-gradient-to-br from-terracotta-300/30 to-brown-200/40',
]

function getColor(i) {
  return placeholderColors[i % placeholderColors.length]
}

function getAspect(aspect) {
  if (aspect === 'tall') return 'aspect-[3/4]'
  if (aspect === 'wide') return 'aspect-[4/3]'
  return 'aspect-square'
}

function onItemVisible(id) {
  loaded.value.add(id)
}

function loadMore() {
  showAll.value = true
  nextTick(() => {
    // Trigger reveal on new items
    document.querySelectorAll('.portfolio-item:not(.item-visible)').forEach((el, i) => {
      setTimeout(() => {
        el.classList.add('item-visible')
      }, i * 80)
    })
  })
}

onMounted(() => {
  // Staggered reveal of initial items
  const observer = new IntersectionObserver(
    ([entry]) => {
      if (entry.isIntersecting) {
        sectionVisible.value = true
        observer.disconnect()
        // Stagger initial items
        document.querySelectorAll('.portfolio-item').forEach((el, i) => {
          setTimeout(() => {
            el.classList.add('item-visible')
            onItemVisible(i)
          }, i * 100)
        })
      }
    },
    { threshold: 0.1 }
  )
  const section = document.getElementById('portfolio-grid')
  if (section) observer.observe(section)
})
</script>

<template>
  <section class="relative bg-cream-100 py-16 lg:py-32 px-5 lg:px-10 overflow-hidden">
    <div class="relative mx-auto max-w-6xl">
      <!-- Header -->
      <div class="reveal max-w-2xl mb-12 lg:mb-16">
        <p class="font-secondary text-[0.68rem] font-medium uppercase tracking-[0.25em] text-terracotta-500 mb-5">
          Nuestro trabajo
        </p>
        <h2 class="font-heading text-[clamp(1.7rem,3vw,2.5rem)] font-bold text-brown-800 leading-[1.12]">
          Contenido que genera citas,
          <span class="text-terracotta-500">no solo likes.</span>
        </h2>
      </div>

      <!-- Masonry grid -->
      <div id="portfolio-grid" class="columns-2 lg:columns-3 gap-3 lg:gap-4 space-y-3 lg:space-y-4">
        <div
          v-for="(work, i) in visibleWorks"
          :key="work.id"
          class="portfolio-item break-inside-avoid opacity-0 translate-y-6 transition-all duration-500"
          style="transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);"
        >
          <div
            class="group relative overflow-hidden rounded-lg lg:rounded-xl cursor-pointer"
            :class="getAspect(work.aspect)"
          >
            <!-- Placeholder -->
            <div :class="['absolute inset-0', getColor(i)]">
              <!-- Decorative inner elements -->
              <div class="absolute inset-0 flex items-center justify-center">
                <div v-if="work.type === 'video'" class="w-12 h-12 lg:w-14 lg:h-14 rounded-full bg-white/20 flex items-center justify-center backdrop-blur-sm">
                  <svg class="w-5 h-5 lg:w-6 lg:h-6 text-white/70 ml-0.5" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M8 5v14l11-7z" />
                  </svg>
                </div>
                <div v-else-if="work.type === 'photo'" class="w-10 h-10 lg:w-12 lg:h-12 rounded-full bg-white/15 flex items-center justify-center">
                  <svg class="w-5 h-5 lg:w-6 lg:h-6 text-white/60" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M6.827 6.175A2.31 2.31 0 015.186 7.23c-.38.054-.757.112-1.134.175C2.999 7.58 2.25 8.507 2.25 9.574V18a2.25 2.25 0 002.25 2.25h15A2.25 2.25 0 0021.75 18V9.574c0-1.067-.75-1.994-1.802-2.169a47.865 47.865 0 00-1.134-.175 2.31 2.31 0 01-1.64-1.055l-.822-1.316a2.192 2.192 0 00-1.736-1.039 48.774 48.774 0 00-5.232 0 2.192 2.192 0 00-1.736 1.039l-.821 1.316z" />
                    <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 12.75a4.5 4.5 0 11-9 0 4.5 4.5 0 019 0z" />
                  </svg>
                </div>
                <div v-else class="w-10 h-10 lg:w-12 lg:h-12 rounded-full bg-white/15 flex items-center justify-center">
                  <svg class="w-5 h-5 lg:w-6 lg:h-6 text-white/60" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M9.53 16.122a3 3 0 00-5.78 1.128 2.25 2.25 0 01-2.4 2.245 4.5 4.5 0 008.4-2.245c0-.399-.078-.78-.22-1.128zm0 0a15.998 15.998 0 003.388-1.62m-5.043-.025a15.994 15.994 0 011.622-3.395m3.42 3.42a15.995 15.995 0 004.764-4.648l3.876-5.814a1.151 1.151 0 00-1.597-1.597L14.146 6.32a15.996 15.996 0 00-4.649 4.763m3.42 3.42a6.776 6.776 0 00-3.42-3.42" />
                  </svg>
                </div>
              </div>
            </div>

            <!-- Hover overlay -->
            <div class="absolute inset-0 bg-brown-900/0 group-hover:bg-brown-900/60 transition-all duration-300 flex items-end p-4 lg:p-5">
              <div class="opacity-0 group-hover:opacity-100 translate-y-2 group-hover:translate-y-0 transition-all duration-300">
                <span class="font-secondary text-[0.6rem] lg:text-[0.65rem] uppercase tracking-wider text-terracotta-300">{{ work.category }}</span>
                <p class="text-cream-50 text-[0.78rem] lg:text-[0.85rem] font-medium mt-0.5 leading-snug">{{ work.label }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Load more -->
      <div v-if="!showAll" class="mt-10 lg:mt-12 text-center">
        <button
          @click="loadMore"
          class="group inline-flex items-center gap-2 font-secondary text-[0.82rem] font-semibold text-terracotta-500
                 hover:text-terracotta-600 transition-colors duration-300
                 bg-transparent border-none cursor-pointer"
        >
          Ver más trabajos
          <svg class="w-4 h-4 group-hover:translate-y-0.5 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
          </svg>
        </button>
      </div>
    </div>
  </section>
</template>

<style scoped>
.portfolio-item.item-visible {
  opacity: 1;
  transform: translateY(0);
}
</style>
