<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const time = ref({ d: 3, h: 11, m: 42, s: 18 })
let timer = null

onMounted(() => {
  timer = setInterval(() => {
    let { d, h, m, s } = time.value
    s -= 1
    if (s < 0) { s = 59; m -= 1 }
    if (m < 0) { m = 59; h -= 1 }
    if (h < 0) { h = 23; d -= 1 }
    if (d < 0) { d = 0; h = 0; m = 0; s = 0 }
    time.value = { d, h, m, s }
  }, 1000)
})

onUnmounted(() => {
  if (timer) clearInterval(timer)
})

const pad = (n) => String(n).padStart(2, '0')

const countdownUnits = [
  { key: 'd', label: 'días' },
  { key: 'h', label: 'hrs' },
  { key: 'm', label: 'min' },
  { key: 's', label: 'seg' },
]

const grainBg = "url(\"data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E\")"
</script>

<template>
  <section
    id="cta"
    class="aura-section-pad"
    :style="{
      background: 'var(--color-brown-900)',
      color: 'var(--color-cream-50)',
      padding: 'clamp(6rem, 10vw, 10rem) 2.5rem',
      position: 'relative',
      overflow: 'hidden',
    }"
  >
    <!-- Grain overlay -->
    <div
      aria-hidden="true"
      :style="{
        position: 'absolute',
        inset: 0,
        backgroundImage: grainBg,
        backgroundSize: '180px',
        opacity: 0.05,
        pointerEvents: 'none',
      }"
    ></div>

    <!-- Decorative radial gradient -->
    <div
      aria-hidden="true"
      :style="{
        position: 'absolute',
        bottom: '-40%',
        right: '-10%',
        width: '60%',
        height: '90%',
        background: 'radial-gradient(ellipse at center, rgba(212,154,120,0.12) 0%, transparent 70%)',
        pointerEvents: 'none',
      }"
    ></div>

    <div :style="{ maxWidth: '1200px', margin: '0 auto', position: 'relative' }">
      <div
        class="aura-hero-grid"
        :style="{
          display: 'grid',
          gridTemplateColumns: '1.3fr 1fr',
          gap: '5rem',
          alignItems: 'center',
        }"
      >
        <!-- Left - copy -->
        <div class="reveal">
          <p
            :style="{
              fontFamily: 'var(--font-ui)',
              fontSize: '0.7rem',
              fontWeight: 500,
              textTransform: 'uppercase',
              letterSpacing: '0.28em',
              color: 'var(--color-terracotta-300)',
              margin: '0 0 1.25rem',
              opacity: 0.8,
            }"
          >
            &sect; X &middot; Último paso
          </p>

          <h2
            :style="{
              fontFamily: 'var(--font-display)',
              fontWeight: 400,
              fontSize: 'clamp(2.2rem, 5vw, 4rem)',
              lineHeight: 1.02,
              letterSpacing: '-0.025em',
              margin: '0 0 2rem',
              color: 'var(--color-cream-50)',
            }"
          >
            30 minutos.<br />
            Te decimos si podemos
            <span :style="{ fontStyle: 'italic', color: 'var(--color-terracotta-300)' }">ayudarte</span>.<br />
            O si no.
          </h2>

          <p
            :style="{
              fontFamily: 'var(--font-body-alt)',
              fontStyle: 'italic',
              fontSize: 'clamp(1.05rem, 1.4vw, 1.2rem)',
              lineHeight: 1.55,
              color: 'rgba(234,225,208,0.8)',
              margin: '0 0 2.5rem',
              maxWidth: '48ch',
            }"
          >
            Sin compromiso, sin venta agresiva. Si no somos un fit, te lo decimos en la llamada --
            y te damos 2 tips accionables para tu negocio antes de colgar.
          </p>

          <div :style="{ display: 'flex', gap: '1.5rem', alignItems: 'center', flexWrap: 'wrap' }">
            <!-- Big pill CTA button -->
            <a
              href="https://wa.me/5215525642721"
              class="aura-cta-pill"
              :style="{
                display: 'inline-flex',
                alignItems: 'center',
                gap: '0.65rem',
                padding: '1.25rem 2.5rem',
                fontFamily: 'var(--font-ui)',
                fontSize: '0.9rem',
                fontWeight: 600,
                letterSpacing: '0.06em',
                textTransform: 'uppercase',
                background: 'var(--color-terracotta-500)',
                color: 'var(--color-cream-50)',
                borderRadius: '999px',
                textDecoration: 'none',
                border: '1px solid var(--color-terracotta-500)',
                transition: 'all .3s cubic-bezier(0.16,1,0.3,1)',
                boxShadow: '0 8px 32px rgba(145, 65, 38, 0.25)',
              }"
            >
              <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
                <rect x="3" y="5" width="18" height="16" rx="2" />
                <path d="M3 10h18M8 3v4M16 3v4" />
              </svg>
              Agendar diagnóstico
            </a>

            <a
              href="#"
              :style="{
                fontFamily: 'var(--font-ui)',
                fontSize: '0.78rem',
                fontWeight: 500,
                color: 'rgba(234,225,208,0.65)',
                textDecoration: 'none',
                letterSpacing: '0.04em',
                borderBottom: '1px solid rgba(234,225,208,0.25)',
                paddingBottom: '2px',
              }"
            >
              o empezar solo con el agente &rarr;
            </a>
          </div>
        </div>

        <!-- Right - urgency card with countdown -->
        <div class="reveal reveal-delay-2">
          <div
            class="cta-urgency-card"
            :style="{
              background: 'rgba(58,40,33,0.55)',
              border: '1px solid rgba(212,154,120,0.2)',
              borderRadius: '16px',
              padding: '2rem',
            }"
          >
            <!-- Pulsing dot + cupos -->
            <div :style="{ display: 'flex', alignItems: 'center', gap: '0.6rem', marginBottom: '1.5rem' }">
              <span
                :style="{
                  width: '8px',
                  height: '8px',
                  borderRadius: '50%',
                  background: '#ffaa56',
                  boxShadow: '0 0 10px rgba(255,170,86,0.6)',
                  animation: 'auraPulse 2s infinite',
                }"
              ></span>
              <span
                :style="{
                  fontFamily: 'var(--font-ui)',
                  fontSize: '0.7rem',
                  fontWeight: 500,
                  textTransform: 'uppercase',
                  letterSpacing: '0.14em',
                  color: 'rgba(234,225,208,0.85)',
                }"
              >
                Cupos Mayo &middot; 4 de 6
              </span>
            </div>

            <p
              :style="{
                fontFamily: 'var(--font-ui-alt)',
                fontStyle: 'italic',
                fontSize: '0.82rem',
                color: 'rgba(234,225,208,0.6)',
                margin: '0 0 0.75rem',
              }"
            >
              Cierra el ciclo en:
            </p>

            <!-- 4-column countdown grid -->
            <div
              :style="{
                display: 'grid',
                gridTemplateColumns: 'repeat(4, 1fr)',
                gap: '0.5rem',
                marginBottom: '1.5rem',
              }"
            >
              <div
                v-for="unit in countdownUnits"
                :key="unit.key"
                :style="{
                  textAlign: 'center',
                  padding: '0.85rem 0.5rem',
                  background: 'rgba(255,255,255,0.03)',
                  borderRadius: '8px',
                  border: '1px solid rgba(212,154,120,0.12)',
                }"
              >
                <span
                  :style="{
                    fontFamily: 'var(--font-display)',
                    fontSize: '1.4rem',
                    color: 'var(--color-terracotta-300)',
                    fontVariantNumeric: 'tabular-nums',
                    display: 'block',
                  }"
                >
                  {{ pad(time[unit.key]) }}
                </span>
                <span
                  :style="{
                    fontFamily: 'var(--font-ui-alt)',
                    fontStyle: 'italic',
                    fontSize: '0.65rem',
                    color: 'rgba(234,225,208,0.5)',
                  }"
                >
                  {{ unit.label }}
                </span>
              </div>
            </div>

            <!-- Bottom checklist -->
            <div :style="{ paddingTop: '1.25rem', borderTop: '1px solid rgba(212,154,120,0.15)' }">
              <p
                :style="{
                  fontFamily: 'var(--font-body)',
                  fontSize: '0.82rem',
                  color: 'rgba(234,225,208,0.7)',
                  margin: '0 0 0.5rem',
                  lineHeight: 1.5,
                }"
              >
                &#10003; 30 min de llamada, sin pitch
              </p>
              <p
                :style="{
                  fontFamily: 'var(--font-body)',
                  fontSize: '0.82rem',
                  color: 'rgba(234,225,208,0.7)',
                  margin: '0 0 0.5rem',
                  lineHeight: 1.5,
                }"
              >
                &#10003; Demo en vivo del Dashboard
              </p>
              <p
                :style="{
                  fontFamily: 'var(--font-body)',
                  fontSize: '0.82rem',
                  color: 'rgba(234,225,208,0.7)',
                  margin: 0,
                  lineHeight: 1.5,
                }"
              >
                &#10003; 2 tips accionables aunque no trabajemos juntos
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
@media (max-width: 640px) {
  .cta-urgency-card {
    padding: 1.5rem 1.25rem !important;
  }
}
</style>
