<script setup>
</script>

<template>
  <section class="aura-section-pad" :style="{
    background: 'var(--color-cream-50)',
    padding: 'clamp(4rem, 6vw, 6rem) 2.5rem 0',
    position: 'relative',
  }">
    <div :style="{ maxWidth: '1200px', margin: '0 auto' }">
      <div
        class="aura-hero-grid"
        :style="{
          display: 'grid',
          gridTemplateColumns: 'auto 1fr',
          gap: '2.5rem',
          alignItems: 'center',
          paddingBlock: '3rem',
          borderTop: '1px solid rgba(221,209,186,0.8)',
          borderBottom: '1px solid rgba(221,209,186,0.8)',
        }"
      >
        <!-- Vertical text -->
        <p class="pain-vertical" :style="{
          fontFamily: 'var(--font-ui)',
          fontSize: '0.68rem',
          fontWeight: 500,
          textTransform: 'uppercase',
          letterSpacing: '0.3em',
          color: 'var(--color-brown-400)',
          margin: 0,
          writingMode: 'vertical-rl',
          transform: 'rotate(180deg)',
          alignSelf: 'start',
        }">Seamos honestos</p>

        <!-- Editorial text -->
        <div>
          <p :style="{
            fontFamily: 'var(--font-display)',
            fontSize: 'clamp(1.4rem, 2.5vw, 2rem)',
            fontWeight: 400,
            lineHeight: 1.25,
            letterSpacing: '-0.015em',
            color: 'var(--color-brown-900)',
            margin: 0,
            maxWidth: '60ch',
          }">
            Probaste una agencia. <span :style="{ fontStyle: 'italic', color: 'var(--color-brown-400)' }">Te llenaron de leads fríos.</span>{{ ' ' }}Probaste a tu sobrino. <span :style="{ fontStyle: 'italic', color: 'var(--color-brown-400)' }">Te hizo reels lindos sin citas.</span>{{ ' ' }}Lo intentaste tú. <span :style="{ fontStyle: 'italic', color: 'var(--color-brown-400)' }">Ya no tienes tiempo.</span>
          </p>

          <!-- Accent line -->
          <div :style="{
            width: '64px',
            height: '1px',
            background: 'var(--color-terracotta-500)',
            marginTop: '1.5rem',
            marginBottom: '1rem',
          }" />

          <!-- Closing statement -->
          <p :style="{
            fontFamily: 'var(--font-body-alt)',
            fontStyle: 'italic',
            fontSize: '1.1rem',
            color: 'var(--color-terracotta-500)',
            margin: 0,
          }">
            El problema no eras tú. Era que nadie estaba mirando la cadena completa.
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
@media (max-width: 980px) {
  .pain-vertical {
    writing-mode: horizontal-tb !important;
    transform: none !important;
    margin-bottom: 0.5rem !important;
  }
}
</style>
