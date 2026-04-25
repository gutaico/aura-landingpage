<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  activeTab: { type: String, default: 'agencia' },
})
const emit = defineEmits(['switchPage'])

const hidden = ref(false)

const agenciaLinks = [
  { label: 'Diagnóstico', href: '#diagnostico' },
  { label: 'Metodología', href: '#metodologia' },
  { label: 'Portfolio', href: '#portfolio' },
  { label: 'FAQ', href: '#faq' },
]

const agenteLinks = [
  { label: 'Comparativa', href: '#comparativa' },
  { label: 'Mecanismo', href: '#como-funciona' },
  { label: 'ROI', href: '#roi' },
  { label: 'Preguntas', href: '#faq' },
]

const links = computed(() => props.activeTab === 'agente' ? agenteLinks : agenciaLinks)

const ctaLabel = computed(() => props.activeTab === 'agente' ? 'Probar el agente' : 'Agendar diagnóstico')

function onScroll() {
  hidden.value = window.scrollY > 80
}

function switchTo(key) {
  if (key !== props.activeTab) {
    emit('switchPage', key)
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
}

onMounted(() => window.addEventListener('scroll', onScroll, { passive: true }))
onUnmounted(() => window.removeEventListener('scroll', onScroll))
</script>

<template>
  <nav :style="{
    position: 'fixed', top: 0, left: 0, right: 0, zIndex: 50,
    transform: hidden ? 'translateY(-100%)' : 'translateY(0)',
    transition: 'transform .5s cubic-bezier(0.16,1,0.3,1), opacity .4s ease',
    opacity: hidden ? 0 : 1,
  }">
    <div :style="{
      maxWidth: '1200px', margin: '0 auto',
      padding: '1.05rem clamp(1rem, 4vw, 2.5rem)', display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: '1rem',
    }">
      <!-- Logo -->
      <a href="#" :style="{ display: 'flex', alignItems: 'center', gap: '0.55rem', textDecoration: 'none' }">
        <img src="/logo-dark.webp" alt="Aura" :style="{ height: '22px', display: 'block' }" />
      </a>

      <!-- Tab switcher -->
      <div :style="{
        display: 'inline-flex', alignItems: 'center',
        position: 'relative',
        padding: '2.5px',
        background: 'rgba(255,255,255,0.5)',
        border: '1px solid rgba(221, 209, 186, 0.45)',
        borderRadius: '999px',
      }">
        <!-- Sliding pill -->
        <div :style="{
          position: 'absolute',
          top: '2.5px',
          bottom: '2.5px',
          left: '2.5px',
          width: 'calc(50% - 2.5px)',
          borderRadius: '999px',
          background: 'var(--color-brown-900)',
          transition: 'transform .35s cubic-bezier(0.16,1,0.3,1)',
          transform: activeTab === 'agencia' ? 'translateX(100%)' : 'translateX(0)',
        }" />
        <button
          v-for="t in [{ key: 'agente', label: 'Agente IA' }, { key: 'agencia', label: 'Agencia' }]"
          :key="t.key"
          @click="switchTo(t.key)"
          :style="{
            fontFamily: 'var(--font-ui)',
            fontSize: '0.6rem',
            fontWeight: 600,
            textTransform: 'uppercase',
            letterSpacing: '0.1em',
            padding: '0.28rem 0.7rem',
            borderRadius: '999px',
            border: 'none',
            cursor: 'pointer',
            background: 'transparent',
            color: activeTab === t.key ? 'var(--color-cream-50)' : 'var(--color-brown-400)',
            transition: 'color .25s ease',
            position: 'relative',
            zIndex: 1,
          }"
        >{{ t.label }}</button>
      </div>

      <!-- Nav links -->
      <ul class="aura-nav-links" :style="{
        display: 'flex', gap: '1.8rem', listStyle: 'none', margin: 0, padding: 0,
      }">
        <li v-for="link in links" :key="link.label">
          <a
            :href="link.href"
            :style="{
              fontFamily: 'var(--font-ui)', fontSize: '0.72rem', fontWeight: 500,
              textTransform: 'uppercase', letterSpacing: '0.14em',
              color: 'var(--color-brown-400)', textDecoration: 'none', transition: 'color .3s',
            }"
            @mouseenter="$event.target.style.color = 'var(--color-terracotta-500)'"
            @mouseleave="$event.target.style.color = 'var(--color-brown-400)'"
          >{{ link.label }}</a>
        </li>
      </ul>

      <!-- CTA link -->
      <a href="#cta" class="aura-nav-cta" :style="{
        display: 'inline-flex', alignItems: 'center', gap: '0.5rem',
        fontFamily: 'var(--font-ui)', fontSize: '0.82rem', fontWeight: 600,
        letterSpacing: '0.02em', color: 'var(--color-terracotta-500)',
        textDecoration: 'none', cursor: 'pointer',
        transition: 'color .3s cubic-bezier(0.16,1,0.3,1)',
      }">
        {{ ctaLabel }}
        <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.75" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
        </svg>
      </a>
    </div>
  </nav>
</template>
