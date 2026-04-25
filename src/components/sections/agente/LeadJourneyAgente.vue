<script setup>
import { ref, computed, onMounted, onUnmounted, nextTick } from 'vue'
import ChromaImage from '../../ChromaImage.vue'

/* ── Two separate sequential timelines ── */
const problemSteps = [
  { time: '10:47 pm', title: 'María envía un WhatsApp', desc: '"Hola, vi su anuncio de botox. ¿Cuánto cuesta?"' },
  { time: '10:48 pm', title: 'Visto ✓✓ — nadie contesta', desc: 'Tu clínica cerró a las 7. El mensaje queda en visto.' },
  { time: '11:30 pm', title: 'María cierra WhatsApp', desc: 'Busca "botox cerca de mí" y le escribe a otra clínica.', stall: true },
  { time: '9:15 am', title: 'La recepcionista responde', desc: '"Hola, tenemos disponibilidad esta semana..."', faded: true, lag: '+10 hrs después' },
  { title: '"Ya agendé en otro lado"', dead: true },
]

const solutionSteps = [
  { time: '10:47 pm', title: 'María envía el mismo WhatsApp', desc: '"Hola, vi su anuncio de botox. ¿Cuánto cuesta?"' },
  { time: '+15 seg', title: 'El agente responde', desc: 'Saluda por nombre, pregunta si es primera vez, resuelve dudas de precio.', highlight: true },
  { time: '10:52 pm', title: 'Cita agendada', desc: 'Jueves 11:30 AM con la Dra. Pérez. Sin intervención humana.' },
  { time: 'Miércoles', title: 'Recordatorio automático', desc: '"¡Hola María! Mañana tienes cita a las 11:30 AM"' },
  { time: 'Jueves', title: 'María llega y paga', desc: 'Primera sesión + paquete de 3. Paciente recurrente.', success: true },
]

const painPoints = [
  'Leads que llegan fuera de horario — sin respuesta hasta mañana',
  'Seguimiento que depende de "si alguien se acuerda"',
  'Cada hora de retraso = mayor probabilidad de perderlo',
]

const benefits = [
  'Responde en <30 seg, 24/7',
  'Agenda citas sin intervención',
  'Seguimiento: 2h, 24h, 7 días',
  'Maneja objeciones y upsell',
  'Retención: retoques, cumpleaños',
]

/* ══════════════════════════════════════════════════════
   Choreography — image first, then description, then timeline
   ──────────────────────────────────────────────────────
   0.00→0.04  Frustration IMAGE fades in (first thing)
   0.03→0.08  "El problema" narrative fades in
   0.06→0.10  "SIN AGENTE" header fades in
   0.10→0.18  Problem step 0
   0.18→0.25  Problem step 1
   0.25→0.32  Problem step 2 (stall)
   0.32→0.38  Problem step 3 (faded, +10hrs)
   0.38→0.43  Problem step 4 (dead end)
   0.43→0.55  Crossfade: image + narrative switch
   0.53→0.58  "CON AGENTE AURA" header fades in
   0.58→0.65  Solution step 0
   0.65→0.72  Solution step 1 (agent responds)
   0.72→0.80  Solution step 2 (appointment)
   0.80→0.88  Solution step 3 (reminder)
   0.88→0.96  Solution step 4 (success)
   ══════════════════════════════════════════════════════ */

const pTimings = [
  { start: 0.10, full: 0.18 },
  { start: 0.18, full: 0.25 },
  { start: 0.25, full: 0.32 },
  { start: 0.32, full: 0.38 },
  { start: 0.38, full: 0.43 },
]
const sTimings = [
  { start: 0.58, full: 0.65 },
  { start: 0.65, full: 0.72 },
  { start: 0.72, full: 0.80 },
  { start: 0.80, full: 0.88 },
  { start: 0.88, full: 0.96 },
]

/* ── Scroll engine ── */
const journeyRef = ref(null)
const progress = ref(0)
let ticking = false

function update() {
  if (!journeyRef.value) return
  const r = journeyRef.value.getBoundingClientRect()
  progress.value = Math.max(0, Math.min(1, (window.innerHeight * 0.78 - r.top) / Math.max(r.height, 1)))
}
function onScroll() {
  if (!ticking) { requestAnimationFrame(() => { update(); ticking = false }); ticking = true }
}

/* ── Image appears FIRST ── */
const imgProblemOp = computed(() => {
  const p = progress.value
  if (p < 0.00) return 0
  if (p < 0.04) return p / 0.04
  if (p < 0.43) return 1
  if (p < 0.52) return 1 - (p - 0.43) / 0.09
  return 0
})
const imgProblemY = computed(() => {
  if (progress.value < 0.43) return 0
  return -12 * Math.min(1, (progress.value - 0.43) / 0.09)
})
const imgSolutionOp = computed(() => {
  const p = progress.value
  if (p < 0.47) return 0
  if (p < 0.55) return (p - 0.47) / 0.08
  return 1
})
const imgSolutionY = computed(() => {
  if (progress.value < 0.47) return 14
  if (progress.value < 0.55) return 14 * (1 - (progress.value - 0.47) / 0.08)
  return 0
})

/* ── Narrative panels (appear AFTER image) ── */
const problemOp = computed(() => {
  const p = progress.value
  if (p < 0.03) return 0
  if (p < 0.08) return (p - 0.03) / 0.05
  if (p < 0.43) return 1
  if (p < 0.52) return 1 - (p - 0.43) / 0.09
  return 0
})
const problemY = computed(() => {
  if (progress.value < 0.43) return 0
  return -12 * Math.min(1, (progress.value - 0.43) / 0.09)
})
const solutionOp = computed(() => {
  const p = progress.value
  if (p < 0.49) return 0
  if (p < 0.57) return (p - 0.49) / 0.08
  return 1
})
const solutionY = computed(() => {
  if (progress.value < 0.49) return 14
  if (progress.value < 0.57) return 14 * (1 - (progress.value - 0.49) / 0.08)
  return 0
})

/* ── Timeline section headers (appear AFTER description) ── */
const pHeaderOp = computed(() => {
  const p = progress.value
  if (p < 0.06) return 0
  if (p < 0.10) return (p - 0.06) / 0.04
  return 1
})
const sHeaderOp = computed(() => {
  const p = progress.value
  if (p < 0.53) return 0
  if (p < 0.58) return (p - 0.53) / 0.05
  return 1
})

/* ── Easing ── */
function ease(t) {
  return t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2
}

/* ── Row progress helpers ── */
function rp(timings, i) {
  const t = timings[i]
  return Math.max(0, Math.min(1.5, (progress.value - t.start) / (t.full - t.start)))
}
function dot(timings, i) { return ease(Math.min(1, rp(timings, i) / 0.25)) }
function cop(timings, i) { return ease(Math.min(1, Math.max(0, (rp(timings, i) - 0.05) / 0.4))) }
function csh(timings, i) { return (1 - cop(timings, i)) * 18 }
function lgr(timings, i) { return ease(Math.min(1, Math.max(0, (rp(timings, i) - 0.3) / 0.7))) }

onMounted(async () => {
  await nextTick()
  window.addEventListener('scroll', onScroll, { passive: true })
  window.addEventListener('resize', onScroll, { passive: true })
  onScroll()
})
onUnmounted(() => {
  window.removeEventListener('scroll', onScroll)
  window.removeEventListener('resize', onScroll)
})

/* ── Line styles ── */
const solidMuted = 'rgba(170,149,120,0.45)'
const dashedMuted = 'repeating-linear-gradient(180deg, rgba(170,149,120,0.22) 0px, rgba(170,149,120,0.22) 3px, transparent 3px, transparent 7px)'
const ghostMuted = 'rgba(170,149,120,0.12)'
</script>

<template>
  <section class="aura-section-pad" :style="{
    background: 'var(--color-cream-50)',
    padding: 'clamp(5rem, 9vw, 9rem) 2.5rem clamp(5rem, 8vw, 7rem)',
    position: 'relative',
    borderTop: '1px solid rgba(221,209,186,0.5)',
  }">
    <div :style="{ maxWidth: '1200px', margin: '0 auto' }">

      <!-- ═══ Section header ═══ -->
      <div class="reveal" :style="{
        display: 'flex', alignItems: 'center', gap: '1rem',
        justifyContent: 'center', marginBottom: '1.5rem',
      }">
        <span :style="{ width: '2rem', height: '1px', background: 'rgba(221,209,186,0.8)' }" />
        <span :style="{
          fontFamily: 'var(--font-ui)', fontSize: '0.68rem', fontWeight: 500,
          textTransform: 'uppercase', letterSpacing: '0.25em', color: 'var(--color-terracotta-500)',
        }">01 &middot; Por qu&eacute; pierdes pacientes</span>
        <span :style="{ width: '2rem', height: '1px', background: 'rgba(221,209,186,0.8)' }" />
      </div>

      <div class="reveal" :style="{ textAlign: 'center', marginBottom: '4.5rem' }">
        <h2 :style="{
          fontFamily: 'var(--font-display)', fontWeight: 400,
          fontSize: 'clamp(1.7rem, 3.5vw, 2.6rem)', lineHeight: 1.1,
          letterSpacing: '-0.022em', margin: '0 auto',
          color: 'var(--color-brown-900)', maxWidth: '28ch',
        }">
          Mismo anuncio. Misma Mar&iacute;a.<br />
          <span :style="{ fontStyle: 'italic', color: 'var(--color-terracotta-500)' }">Distinto desenlace.</span>
        </h2>
      </div>

      <!-- ═══ Three-column sequential layout ═══ -->
      <div ref="journeyRef" class="journey-layout" :style="{
        display: 'grid',
        gridTemplateColumns: '2fr 4fr 3fr',
        gap: 'clamp(1.5rem, 3vw, 3rem)',
        alignItems: 'start',
      }">

        <!-- ─── LEFT: Sticky narrative (vertically centered) ─── -->
        <div class="narrative-col" :style="{
          position: 'sticky', top: '0',
          height: '100vh',
          display: 'flex', alignItems: 'center',
        }">
          <div :style="{ display: 'grid', width: '100%' }">

            <!-- PROBLEM panel -->
            <div :style="{
              gridArea: '1 / 1',
              opacity: problemOp,
              transform: `translateY(${problemY}px)`,
              pointerEvents: problemOp > 0.5 ? 'auto' : 'none',
            }">
              <span :style="{
                display: 'inline-block',
                fontFamily: 'var(--font-ui)', fontSize: '0.62rem', fontWeight: 600,
                textTransform: 'uppercase', letterSpacing: '0.18em',
                color: '#b04040', background: 'rgba(176,64,64,0.06)',
                padding: '0.35rem 0.75rem', borderRadius: '999px',
                marginBottom: '1.25rem',
              }">El problema</span>

              <h3 :style="{
                fontFamily: 'var(--font-display)', fontWeight: 400,
                fontSize: 'clamp(1.2rem, 2vw, 1.5rem)', lineHeight: 1.2,
                letterSpacing: '-0.015em', color: 'var(--color-brown-900)',
                margin: '0 0 0.75rem',
              }">
                Cada minuto sin respuesta es un paciente perdido.
              </h3>

              <p :style="{
                fontFamily: 'var(--font-body)', fontSize: '0.82rem',
                lineHeight: 1.55, color: 'var(--color-brown-400)',
                margin: '0 0 1.25rem',
              }">
                El lead lleg&oacute;. Pero es de noche y nadie contest&oacute;. A las 9 AM ya es tarde.
              </p>

              <div :style="{
                background: 'rgba(176,64,64,0.04)',
                border: '1px solid rgba(176,64,64,0.1)',
                borderRadius: '12px', padding: '0.85rem 1rem',
              }">
                <span :style="{
                  fontFamily: 'var(--font-display)', fontSize: '1.6rem',
                  fontStyle: 'italic', color: '#b04040', lineHeight: 1,
                }">78%</span>
                <p :style="{
                  fontFamily: 'var(--font-body)', fontSize: '0.78rem',
                  color: 'var(--color-brown-400)', margin: '0.2rem 0 0', lineHeight: 1.4,
                }">agenda con la primera cl&iacute;nica que responde.</p>
              </div>
            </div>

            <!-- SOLUTION panel -->
            <div :style="{
              gridArea: '1 / 1',
              opacity: solutionOp,
              transform: `translateY(${solutionY}px)`,
              pointerEvents: solutionOp > 0.5 ? 'auto' : 'none',
            }">
              <span :style="{
                display: 'inline-block',
                fontFamily: 'var(--font-ui)', fontSize: '0.62rem', fontWeight: 600,
                textTransform: 'uppercase', letterSpacing: '0.18em',
                color: 'var(--color-terracotta-500)', background: 'rgba(145,65,38,0.06)',
                padding: '0.35rem 0.75rem', borderRadius: '999px',
                marginBottom: '1.25rem',
              }">La soluci&oacute;n</span>

              <h3 :style="{
                fontFamily: 'var(--font-display)', fontWeight: 400,
                fontSize: 'clamp(1.2rem, 2vw, 1.5rem)', lineHeight: 1.2,
                letterSpacing: '-0.015em', color: 'var(--color-brown-900)',
                margin: '0 0 0.75rem',
              }">
                Un agente que nunca cierra y sabe vender.
              </h3>

              <p :style="{
                fontFamily: 'var(--font-body)', fontSize: '0.82rem',
                lineHeight: 1.55, color: 'var(--color-brown-400)',
                margin: '0 0 1.25rem',
              }">
                Entrenado con la estrategia que ya gener&oacute; +2,000 citas para cl&iacute;nicas.
              </p>

              <div :style="{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }">
                <div v-for="(benefit, idx) in benefits" :key="idx" :style="{
                  display: 'flex', alignItems: 'flex-start', gap: '0.5rem',
                }">
                  <svg width="12" height="12" fill="none" stroke="var(--color-terracotta-500)" stroke-width="2" viewBox="0 0 24 24" :style="{ flexShrink: 0, marginTop: '0.2rem' }">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M5 12l5 5L20 7" />
                  </svg>
                  <span :style="{
                    fontFamily: 'var(--font-body)', fontSize: '0.8rem',
                    color: 'var(--color-brown-700)', lineHeight: 1.4, fontWeight: 500,
                  }">{{ benefit }}</span>
                </div>
              </div>
            </div>

          </div>
        </div>

        <!-- ─── CENTER: Sticky image divider ─── -->
        <div class="image-col" :style="{
          position: 'sticky', top: '0',
          height: '100vh',
          display: 'flex', alignItems: 'center', justifyContent: 'center',
        }">
          <div :style="{ display: 'grid', width: '100%' }">
            <ChromaImage
              src="/img/frustracion.webp"
              alt="Frustración por leads perdidos"
              :threshold="40"
              :feather="20"
              :style="{
                gridArea: '1 / 1',
                width: '100%',
                objectFit: 'contain',
                opacity: imgProblemOp,
                transform: `translateY(${imgProblemY}px)`,
              }"
            />
            <ChromaImage
              src="/img/agenteia.webp"
              alt="Agente IA respondiendo"
              :threshold="40"
              :feather="20"
              :style="{
                gridArea: '1 / 1',
                width: '100%',
                objectFit: 'contain',
                opacity: imgSolutionOp,
                transform: `translateY(${imgSolutionY}px)`,
              }"
            />
          </div>
        </div>

        <!-- ─── RIGHT: Sequential timelines ─── -->
        <div :style="{ maxWidth: '420px', margin: '0 auto' }">

          <!-- ▸ PROBLEM TIMELINE ── -->
          <div :style="{
            marginBottom: '1.5rem',
            opacity: pHeaderOp,
            transform: `translateY(${(1 - pHeaderOp) * 8}px)`,
          }">
            <span :style="{
              fontFamily: 'var(--font-ui)', fontSize: '0.65rem', fontWeight: 600,
              textTransform: 'uppercase', letterSpacing: '0.18em', color: 'var(--color-brown-300)',
            }">Sin agente</span>
          </div>

          <div
            v-for="(step, i) in problemSteps"
            :key="'p' + i"
            :style="{
              display: 'flex',
              gap: '1.25rem',
              minHeight: i < problemSteps.length - 1 ? '100px' : 'auto',
            }"
          >
            <!-- Track -->
            <div :style="{ position: 'relative', width: '12px', flexShrink: 0 }">
              <!-- Dot -->
              <div v-if="!step.dead" :style="{
                position: 'absolute', top: '2px', left: '50%',
                transform: `translateX(-50%) scale(${dot(pTimings, i)})`,
                width: '10px', height: '10px', borderRadius: '50%',
                background: step.stall ? 'rgba(170,149,120,0.25)' : (step.faded ? 'rgba(170,149,120,0.15)' : 'var(--color-brown-300)'),
                border: '2px solid var(--color-cream-50)', boxSizing: 'border-box',
              }" />
              <!-- Dead X -->
              <div v-else :style="{
                position: 'absolute', top: '0', left: '50%',
                transform: `translateX(-50%) scale(${dot(pTimings, i)})`,
                width: '16px', height: '16px', borderRadius: '50%',
                background: 'rgba(176,64,64,0.1)',
                display: 'flex', alignItems: 'center', justifyContent: 'center',
              }">
                <span :style="{ color: '#b04040', fontSize: '0.55rem', fontWeight: 800, lineHeight: 1 }">&#10005;</span>
              </div>
              <!-- Line -->
              <div v-if="i < problemSteps.length - 1 && !step.dead" :style="{
                position: 'absolute', left: '50%', top: '14px', bottom: 0, width: '2px',
                transform: `translateX(-50%) scaleY(${lgr(pTimings, i)})`,
                transformOrigin: 'top',
                background: step.stall ? dashedMuted : (step.faded ? ghostMuted : solidMuted),
              }" />
            </div>

            <!-- Content -->
            <div :style="{
              paddingBottom: i < problemSteps.length - 1 ? '2.5rem' : '0',
              opacity: cop(pTimings, i) * (step.faded ? 0.45 : (step.dead ? 0.8 : 1)),
              transform: `translateY(${csh(pTimings, i)}px)`,
            }">
              <span v-if="step.lag" :style="{
                display: 'inline-block', fontFamily: 'var(--font-ui)',
                fontSize: '0.55rem', fontWeight: 600, color: '#b04040',
                background: 'rgba(176,64,64,0.08)', padding: '0.15rem 0.55rem',
                borderRadius: '999px', marginBottom: '0.3rem',
              }">{{ step.lag }}</span>
              <span v-if="step.time" :style="{
                display: 'block', fontFamily: 'var(--font-ui)',
                fontSize: '0.65rem', fontWeight: 500,
                color: step.faded ? 'var(--color-brown-300)' : 'var(--color-brown-400)',
                marginBottom: '0.15rem',
              }">{{ step.time }}</span>
              <p :style="{
                fontFamily: 'var(--font-ui)', fontSize: '0.88rem',
                fontWeight: step.dead ? 600 : 500,
                color: step.dead ? '#b04040' : 'var(--color-brown-700)',
                margin: '0 0 0.15rem', lineHeight: 1.35,
              }">{{ step.title }}</p>
              <p v-if="step.desc" :style="{
                fontFamily: 'var(--font-body)', fontSize: '0.78rem',
                color: 'var(--color-brown-400)', margin: 0, lineHeight: 1.5,
                maxWidth: '34ch',
              }">{{ step.desc }}</p>
            </div>
          </div>

          <!-- ▸ SPACER ── -->
          <div :style="{
            height: '120px',
            display: 'flex', alignItems: 'center',
            paddingLeft: '0.25rem',
          }">
            <span :style="{
              fontFamily: 'var(--font-ui-alt)', fontStyle: 'italic',
              fontSize: '0.7rem', color: 'var(--color-brown-200)',
              letterSpacing: '0.3em',
            }">&middot; &middot; &middot;</span>
          </div>

          <!-- ▸ SOLUTION TIMELINE ── -->
          <div :style="{
            marginBottom: '1.5rem',
            opacity: sHeaderOp,
            transform: `translateY(${(1 - sHeaderOp) * 8}px)`,
          }">
            <span :style="{
              fontFamily: 'var(--font-ui)', fontSize: '0.65rem', fontWeight: 600,
              textTransform: 'uppercase', letterSpacing: '0.18em', color: 'var(--color-terracotta-500)',
            }">Con agente Aura</span>
          </div>

          <div
            v-for="(step, i) in solutionSteps"
            :key="'s' + i"
            :style="{
              display: 'flex',
              gap: '1.25rem',
              minHeight: i < solutionSteps.length - 1 ? '100px' : 'auto',
            }"
          >
            <!-- Track -->
            <div :style="{ position: 'relative', width: '12px', flexShrink: 0 }">
              <!-- Dot -->
              <div v-if="!step.success" :style="{
                position: 'absolute', top: '2px', left: '50%',
                transform: `translateX(-50%) scale(${dot(sTimings, i)})`,
                width: '10px', height: '10px', borderRadius: '50%',
                background: step.highlight ? 'var(--color-terracotta-500)' : 'var(--color-terracotta-400)',
                border: '2px solid var(--color-cream-50)', boxSizing: 'border-box',
                boxShadow: step.highlight ? '0 0 12px rgba(145,65,38,0.45)' : 'none',
              }" />
              <!-- Success check -->
              <div v-else :style="{
                position: 'absolute', top: '0', left: '50%',
                transform: `translateX(-50%) scale(${dot(sTimings, i)})`,
                width: '16px', height: '16px', borderRadius: '50%',
                background: 'rgba(74,158,90,0.15)',
                display: 'flex', alignItems: 'center', justifyContent: 'center',
                boxShadow: '0 0 10px rgba(74,158,90,0.25)',
              }">
                <span :style="{ color: '#4a9e5a', fontSize: '0.6rem', fontWeight: 800, lineHeight: 1 }">&#10003;</span>
              </div>
              <!-- Line -->
              <div v-if="i < solutionSteps.length - 1" :style="{
                position: 'absolute', left: '50%', top: '14px', bottom: 0, width: '2px',
                transform: `translateX(-50%) scaleY(${lgr(sTimings, i)})`,
                transformOrigin: 'top',
                background: 'var(--color-terracotta-400)',
              }" />
            </div>

            <!-- Content -->
            <div :style="{
              paddingBottom: i < solutionSteps.length - 1 ? '2.5rem' : '0',
              opacity: cop(sTimings, i),
              transform: `translateY(${csh(sTimings, i)}px)`,
            }">
              <span v-if="step.time" :style="{
                display: 'block', fontFamily: 'var(--font-ui)',
                fontSize: '0.65rem', fontWeight: 500,
                color: step.highlight ? 'var(--color-terracotta-500)' : 'var(--color-brown-400)',
                marginBottom: '0.15rem',
              }">{{ step.time }}</span>
              <p :style="{
                fontFamily: 'var(--font-ui)', fontSize: '0.88rem',
                fontWeight: step.success ? 600 : 500,
                color: step.success ? '#3a8a4a' : 'var(--color-brown-900)',
                margin: '0 0 0.15rem', lineHeight: 1.35,
              }">{{ step.title }}</p>
              <p v-if="step.desc" :style="{
                fontFamily: 'var(--font-body)', fontSize: '0.78rem',
                color: 'var(--color-brown-500)', margin: 0, lineHeight: 1.5,
                maxWidth: '34ch',
              }">{{ step.desc }}</p>
            </div>
          </div>

        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
@media (max-width: 840px) {
  .journey-layout {
    grid-template-columns: 1fr !important;
  }
  .narrative-col {
    position: relative !important;
    top: auto !important;
    height: auto !important;
    margin-bottom: 3rem;
  }
  .image-col {
    display: none !important;
  }
}
</style>
