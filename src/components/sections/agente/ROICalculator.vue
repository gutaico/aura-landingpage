<script setup>
import { ref, computed, onMounted, onUnmounted, nextTick } from 'vue'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

/* ── calculator ── */
const leads  = ref(80)
const ticket = ref(8000)
const lost   = ref(30)

const lostLeads = computed(() => leads.value * (lost.value / 100))
const monthly   = computed(() => lostLeads.value * 0.35 * ticket.value)
const recovered = computed(() => monthly.value * 0.45)
const agentCost = computed(() => Math.ceil(leads.value / 100) * 2000)
const net       = computed(() => recovered.value - agentCost.value)
const roi       = computed(() => agentCost.value === 0 ? '0.0' : (recovered.value / agentCost.value).toFixed(1))

const fmt    = (n) => Math.round(n).toLocaleString('es-MX')
const slFill = (v, lo, hi) => ((v - lo) / (hi - lo)) * 100

/* ── GSAP ── */
const sectionEl = ref(null)
const analyzeEl = ref(null)
const resultsEl = ref(null)
const wavePath  = ref(null)

const progress = ref(0)
let ctx = null

const stepLabel = computed(() => {
  const p = progress.value
  if (p < 18) return 'Mapeando tus datos'
  if (p < 42) return 'Calculando pérdidas'
  if (p < 68) return 'Estimando recuperación'
  if (p < 92) return 'Generando reporte'
  return 'Análisis completo'
})

onMounted(() => {
  nextTick(() => {
    const pathLen = wavePath.value?.getTotalLength() || 420
    const waveLines = analyzeEl.value.querySelectorAll('.ana-wave-line')

    /* initial states */
    waveLines.forEach(el => {
      el.setAttribute('stroke-dasharray', pathLen)
      el.setAttribute('stroke-dashoffset', pathLen)
    })
    gsap.set(resultsEl.value.children, { opacity: 0, y: 24 })

    ctx = gsap.context(() => {

      /* ── 1. Pin + wave animation (scrubbed to scroll) ── */
      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: analyzeEl.value,
          start: 'center center',
          end: '+=500',          // 500px of scroll to fill
          pin: true,
          scrub: 0.4,
          onUpdate: (self) => {
            progress.value = Math.round(self.progress * 100)
          },
        },
      })

      tl.fromTo(analyzeEl.value,
        { opacity: 0.15 },
        { opacity: 1, duration: 0.15, ease: 'none' },
        0,
      )

      tl.to(waveLines, {
        strokeDashoffset: 0,
        duration: 1,
        ease: 'none',
      }, 0)

      /* ── 2. Results stagger on enter ── */
      ScrollTrigger.create({
        trigger: resultsEl.value,
        start: 'top 85%',
        once: true,
        onEnter: () => {
          gsap.to(resultsEl.value.children, {
            opacity: 1,
            y: 0,
            stagger: 0.12,
            duration: 0.6,
            ease: 'power3.out',
          })
        },
      })

    })
  })
})

onUnmounted(() => ctx?.revert())
</script>

<template>
  <section ref="sectionEl" class="roi grain grain-05 aura-section-pad">
    <div class="roi-wrap">

      <!-- ── Header ── -->
      <div class="reveal roi-header">
        <p class="roi-eyebrow">&sect; &middot; Calculadora</p>
        <h2 class="roi-title">
          Ponle <em>números</em> a lo<br />que estás perdiendo.
        </h2>
        <p class="roi-sub">Ajusta los valores de tu clínica. Nosotros hacemos las cuentas.</p>
      </div>

      <!-- ── Sliders ── -->
      <div class="reveal roi-sliders">
        <div class="sl">
          <div class="sl-head">
            <span class="sl-label">Leads / mes</span>
            <span class="sl-num">{{ leads }}</span>
          </div>
          <input type="range" v-model.number="leads" min="10" max="300" step="5"
            class="sl-range" :style="{ '--f': slFill(leads, 10, 300) + '%' }" />
        </div>
        <div class="sl">
          <div class="sl-head">
            <span class="sl-label">Ticket promedio</span>
            <span class="sl-num">${{ fmt(ticket) }}</span>
          </div>
          <input type="range" v-model.number="ticket" min="500" max="60000" step="500"
            class="sl-range" :style="{ '--f': slFill(ticket, 500, 60000) + '%' }" />
        </div>
        <div class="sl">
          <div class="sl-head">
            <span class="sl-label">% que se enfrían</span>
            <span class="sl-num">{{ lost }}%</span>
          </div>
          <input type="range" v-model.number="lost" min="10" max="60" step="5"
            class="sl-range" :style="{ '--f': slFill(lost, 10, 60) + '%' }" />
        </div>
      </div>

      <!-- ── Analysis (GSAP pins this) ── -->
      <div ref="analyzeEl" class="ana">
        <p class="ana-heading">Analizando tus números</p>
        <p class="ana-step">{{ stepLabel }}</p>

        <svg class="ana-wave" viewBox="0 0 400 12" preserveAspectRatio="none">
          <!-- ghost path -->
          <path d="M0,6 C55,2 110,10 200,6 C290,2 345,10 400,6"
            stroke="rgba(212,154,120,0.08)" stroke-width="1.5" fill="none" stroke-dasharray="4 6" />
          <!-- glow -->
          <path d="M0,6 C55,2 110,10 200,6 C290,2 345,10 400,6"
            stroke="var(--color-terracotta-400)" stroke-width="6" fill="none"
            stroke-linecap="round" opacity="0.12" class="ana-wave-line" />
          <!-- main -->
          <path ref="wavePath" d="M0,6 C55,2 110,10 200,6 C290,2 345,10 400,6"
            stroke="var(--color-terracotta-400)" stroke-width="2.5" fill="none"
            stroke-linecap="round" class="ana-wave-line" />
        </svg>

        <span class="ana-pct">{{ Math.round(progress) }}%</span>
      </div>

      <!-- ── Results (GSAP staggers in) ── -->
      <div ref="resultsEl" class="roi-results">
        <div class="res-row">
          <span class="res-label">Estás dejando ir</span>
          <span class="res-val res-val--loss">${{ fmt(monthly) }}<small>/mes</small></span>
        </div>
        <hr class="res-line" />
        <div class="res-row">
          <span class="res-label">El agente recuperaría</span>
          <span class="res-val res-val--gain">${{ fmt(recovered) }}<small>/mes</small></span>
        </div>
        <hr class="res-line" />
        <div class="res-row">
          <span class="res-label res-label--strong">Recuperación potencial</span>
          <span class="res-val res-val--gain">+${{ fmt(recovered) }}<small>/mes</small></span>
        </div>
        <hr class="res-line res-line--thick" />
        <div class="res-row">
          <span class="res-label res-label--strong">Inversión del agente</span>
          <span class="res-val">${{ fmt(agentCost) }}<small>/mes</small></span>
        </div>
        <div class="res-roi">
          <span class="res-roi-label">ROI</span>
          <span class="res-roi-num">{{ roi }}<em>&times;</em></span>
        </div>
      </div>

    </div>
  </section>
</template>

<style scoped>
/* ═══════════════════════
   Section
   ═══════════════════════ */
.roi {
  background: var(--color-brown-900);
  padding: clamp(5rem, 9vw, 10rem) 2.5rem 0;
  position: relative;
}
.roi-wrap {
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
}

/* ═══════════════════════
   Header
   ═══════════════════════ */
.roi-header { text-align: center; margin-bottom: clamp(3.5rem, 6vw, 5rem); }
.roi-eyebrow {
  font-family: var(--font-ui); font-size: 0.68rem; font-weight: 500;
  text-transform: uppercase; letter-spacing: 0.28em;
  color: var(--color-terracotta-300); margin: 0 0 1.25rem; opacity: .8;
}
.roi-title {
  font-family: var(--font-display); font-weight: 400;
  font-size: clamp(2rem, 4vw, 3rem); line-height: 1.08;
  letter-spacing: -0.022em; color: var(--color-cream-50); margin: 0 0 1rem;
}
.roi-title em { font-style: italic; color: var(--color-terracotta-300); }
.roi-sub {
  font-family: var(--font-body-alt); font-style: italic;
  font-size: clamp(0.95rem, 1.3vw, 1.1rem);
  color: rgba(234,225,208,0.45); margin: 0;
}

/* ═══════════════════════
   Sliders
   ═══════════════════════ */
.roi-sliders {
  max-width: 760px; margin: 0 auto;
  display: flex; flex-direction: column; gap: 2.25rem;
}
.sl { display: flex; flex-direction: column; gap: 0.65rem; }
.sl-head { display: flex; justify-content: space-between; align-items: baseline; }
.sl-label {
  font-family: var(--font-body); font-size: 0.92rem;
  color: rgba(234,225,208,0.65);
}
.sl-num {
  font-family: var(--font-display); font-size: 1.6rem; font-weight: 400;
  color: var(--color-cream-50); font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em;
}
.sl-range {
  -webkit-appearance: none; appearance: none;
  height: 2px; border-radius: 999px; width: 100%; outline: none;
  background: linear-gradient(to right,
    var(--color-terracotta-400) var(--f,0%),
    rgba(212,154,120,0.15) var(--f,0%));
}
.sl-range::-webkit-slider-thumb {
  -webkit-appearance: none; width: 16px; height: 16px; border-radius: 50%;
  background: var(--color-terracotta-400); border: 2px solid var(--color-cream-100);
  box-shadow: 0 1px 5px rgba(0,0,0,0.3); cursor: pointer;
  transition: transform .15s cubic-bezier(.16,1,.3,1);
}
.sl-range::-webkit-slider-thumb:active { transform: scale(1.25); }
.sl-range::-moz-range-thumb {
  width: 16px; height: 16px; border-radius: 50%;
  background: var(--color-terracotta-400); border: 2px solid var(--color-cream-100);
  box-shadow: 0 1px 5px rgba(0,0,0,0.3); cursor: pointer;
}
.sl-range::-moz-range-track {
  height: 2px; background: rgba(212,154,120,0.15); border: none; border-radius: 999px;
}
.sl-range::-moz-range-progress {
  height: 2px; background: var(--color-terracotta-400); border-radius: 999px;
}

/* ═══════════════════════
   Analysis (pinned by GSAP)
   ═══════════════════════ */
.ana {
  max-width: 520px;
  margin: 0 auto;
  padding: clamp(5rem, 10vh, 8rem) 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  opacity: 0.15;
}

.ana-heading {
  font-family: var(--font-display); font-weight: 400;
  font-size: clamp(1.3rem, 2.2vw, 1.6rem);
  color: var(--color-cream-50); letter-spacing: -0.015em;
  margin: 0 0 0.6rem; text-align: center;
}
.ana-step {
  font-family: var(--font-body-alt); font-style: italic;
  font-size: 0.88rem; color: rgba(234,225,208,0.4);
  margin: 0 0 2rem; min-height: 1.3em;
}
.ana-wave {
  width: 100%; height: 14px;
  margin-bottom: 1.5rem;
}
.ana-pct {
  font-family: var(--font-display);
  font-size: clamp(2.2rem, 4vw, 3rem);
  font-weight: 400; color: var(--color-terracotta-300);
  font-variant-numeric: tabular-nums; letter-spacing: -0.02em;
  line-height: 1;
}

/* ═══════════════════════
   Results
   ═══════════════════════ */
.roi-results {
  max-width: 760px; margin: 0 auto;
  padding-bottom: clamp(5rem, 9vw, 10rem);
}
.res-row {
  display: flex; justify-content: space-between;
  align-items: baseline; padding: 1.35rem 0;
}
.res-label {
  font-family: var(--font-body); font-size: 0.95rem;
  color: rgba(234,225,208,0.6); line-height: 1.4;
}
.res-label--strong {
  font-family: var(--font-display); font-size: 1.05rem;
  color: var(--color-cream-50);
}
.res-val {
  font-family: var(--font-display);
  font-size: clamp(1.4rem, 2.5vw, 1.8rem);
  font-weight: 400; color: var(--color-cream-50);
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em; white-space: nowrap;
}
.res-val small { font-size: .5em; opacity: .45; margin-left: .1em; letter-spacing: 0; }
.res-val--loss { color: #c97b6e; }
.res-val--gain { color: #7db88a; }
.res-line { border: none; height: 1px; background: rgba(212,154,120,0.12); margin: 0; }
.res-line--thick { height: 2px; background: rgba(212,154,120,0.25); }

.res-roi {
  display: flex; justify-content: space-between;
  align-items: baseline; padding: 2rem 0 0.5rem;
}
.res-roi-label {
  font-family: var(--font-ui); font-size: 0.78rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: 0.22em;
  color: rgba(234,225,208,0.35);
}
.res-roi-num {
  font-family: var(--font-display);
  font-size: clamp(2.8rem, 5vw, 3.8rem);
  font-weight: 400; color: var(--color-terracotta-300);
  font-variant-numeric: tabular-nums; letter-spacing: -0.03em;
  line-height: 1;
}
.res-roi-num em { font-style: italic; font-size: .6em; opacity: .7; }

/* ═══════════════════════
   Responsive
   ═══════════════════════ */
@media (max-width: 600px) {
  .roi-sliders, .roi-results { max-width: 100%; }
  .ana { max-width: 100%; padding-left: 1rem; padding-right: 1rem; }
  .res-row { flex-direction: column; gap: 0.3rem; }
  .res-val { font-size: 1.4rem; }
}
</style>
