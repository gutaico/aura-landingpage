<script setup>
const pains = [
  'Leads que llegan a las 11 pm y nadie contesta',
  'Pacientes que nunca regresaron a su retoque',
  'Mensajes sin seguimiento en WhatsApp',
  'Citas confirmadas que no llegan',
  'Ofertas que no se vuelven a mencionar',
]

/* Triple items for seamless loop */
const tripled = [...pains, ...pains, ...pains]
</script>

<template>
  <section :style="{
    background: 'var(--color-brown-900)',
    padding: '1.75rem 0',
    overflow: 'hidden',
    position: 'relative',
    borderTop: '1px solid rgba(102,48,30,0.4)',
    borderBottom: '1px solid rgba(102,48,30,0.4)',
  }">
    <!-- Marquee track -->
    <div class="marquee-track" :style="{
      display: 'flex',
      width: 'max-content',
    }">
      <span
        v-for="(pain, i) in tripled"
        :key="i"
        :style="{
          display: 'inline-flex',
          alignItems: 'center',
          gap: '1.5rem',
          paddingRight: '1.5rem',
          whiteSpace: 'nowrap',
        }"
      >
        <span :style="{
          fontFamily: 'var(--font-display)',
          fontStyle: 'italic',
          fontSize: 'clamp(1rem, 1.6vw, 1.25rem)',
          fontWeight: 400,
          color: 'rgba(234, 225, 208, 0.55)',
          letterSpacing: '-0.01em',
        }">{{ pain }}</span>
        <span :style="{
          color: 'var(--color-terracotta-500)',
          fontSize: '0.55rem',
          opacity: 0.6,
        }">✦</span>
      </span>
    </div>
  </section>
</template>

<style scoped>
@keyframes auraMarquee {
  0% { transform: translateX(0); }
  100% { transform: translateX(-33.333%); }
}

.marquee-track {
  animation: auraMarquee 42s linear infinite;
}

.marquee-track:hover {
  animation-play-state: paused;
}
</style>
