<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

/* ── Live count ticker ── */
const count = ref(47)
let countInterval = null

/* ── Chat messages data ── */
const messages = [
  { from: 'user', text: 'Hola! Vi su anuncio de botox. ¿Cuánto cuesta?', delay: 100 },
  { from: 'bot', text: '¡Hola! Te comparto información. ¿Es tu primera vez o ya te has aplicado antes?', delay: 900 },
  { from: 'user', text: 'Primera vez, en frente 🙈', delay: 1800 },
  { from: 'bot', text: 'Perfecto. La consulta de valoración es gratis con la Dra. Pérez. ¿Te acomoda el jueves 11:30 am?', delay: 2700 },
]

const visibleMessages = ref([])
const showTyping = ref(true)
const timers = []

/* ── Floating stat badges around phone ── */
const floatingStats = [
  { icon: '⚡', label: '15s respuesta', x: '-65px', y: '80px', delay: 0.5 },
  { icon: '📅', label: 'Cita agendada', x: '-80px', y: '340px', delay: 1.1 },
  { icon: '🔁', label: '92% atendidos', x: '275px', y: '240px', delay: 1.7 },
]

const statVisible = ref({})

/* ── Trust strip data ── */
const trustItems = [
  { n: '15 seg', l: 'Tiempo de primera respuesta' },
  { n: '24/7', l: 'Sin horarios, sin excusas' },
  { n: '3.2×', l: 'Más citas vs respuesta manual' },
]

onMounted(() => {
  /* Count ticker */
  countInterval = setInterval(() => {
    if (Math.random() > 0.7) count.value++
  }, 3500)

  /* Staggered message reveals */
  messages.forEach((msg, i) => {
    const t = setTimeout(() => {
      visibleMessages.value = [...visibleMessages.value, i]
      /* Hide typing after last message */
      if (i === messages.length - 1) {
        const t2 = setTimeout(() => { showTyping.value = true }, 600)
        timers.push(t2)
      }
    }, msg.delay)
    timers.push(t)
  })

  /* Staggered stat badge reveals */
  floatingStats.forEach((s, i) => {
    const t = setTimeout(() => {
      statVisible.value = { ...statVisible.value, [i]: true }
    }, s.delay * 1000 + 600)
    timers.push(t)
  })
})

onUnmounted(() => {
  clearInterval(countInterval)
  timers.forEach(t => clearTimeout(t))
})
</script>

<template>
  <section class="grain grain-05 aura-section-pad" :style="{
    background: 'var(--color-brown-900)',
    color: 'var(--color-cream-50)',
    position: 'relative',
    overflow: 'hidden',
    padding: 'clamp(7rem, 12vw, 10rem) 2.5rem clamp(5rem, 7vw, 8rem)',
  }">

    <!-- Decorative radial glow top-right -->
    <div aria-hidden="true" :style="{
      position: 'absolute',
      top: '-15%',
      right: '-10%',
      width: '55%',
      height: '70%',
      background: 'radial-gradient(ellipse at center, rgba(145,65,38,0.28), transparent 65%)',
      pointerEvents: 'none',
    }" />

    <!-- Main grid -->
    <div class="aura-hero-grid" :style="{
      maxWidth: '1200px',
      margin: '0 auto',
      position: 'relative',
      display: 'grid',
      gridTemplateColumns: '1.15fr 1fr',
      gap: '4rem',
      alignItems: 'center',
    }">

      <!-- ═══ Left column ═══ -->
      <div>
        <!-- Eyebrow with pulse dot -->
        <div :style="{
          display: 'flex',
          alignItems: 'center',
          gap: '0.6rem',
          marginBottom: '1.5rem',
        }">
          <span :style="{
            width: '8px',
            height: '8px',
            borderRadius: '50%',
            background: '#6bcf7f',
            boxShadow: '0 0 12px rgba(107,207,127,0.6)',
            animation: 'auraPulse 2s ease-in-out infinite',
            display: 'inline-block',
          }" />
          <p :style="{
            fontFamily: 'var(--font-ui)',
            fontSize: '0.68rem',
            fontWeight: 500,
            textTransform: 'uppercase',
            letterSpacing: '0.25em',
            color: 'rgb(212 154 120 / 0.95)',
            margin: 0,
          }">Agente IA · En vivo 24/7</p>
        </div>

        <!-- Headline -->
        <h1 :style="{
          fontFamily: 'var(--font-display)',
          fontWeight: 400,
          fontSize: 'clamp(2.4rem, 6vw, 4.8rem)',
          lineHeight: 1,
          letterSpacing: '-0.025em',
          margin: '0 0 1.75rem',
          color: 'var(--color-cream-50)',
        }">
          El agente que no <span :style="{ fontStyle: 'italic', color: 'var(--color-terracotta-300)' }">pierde</span> un solo paciente.
        </h1>

        <!-- Lead paragraph -->
        <p :style="{
          fontFamily: 'var(--font-body)',
          fontSize: 'clamp(1.02rem, 1.35vw, 1.15rem)',
          lineHeight: 1.65,
          color: 'rgba(234, 225, 208, 0.82)',
          maxWidth: '44ch',
          margin: '0 0 2.5rem',
        }">
          Responde en segundos. Califica, agenda y da seguimiento. Recuerda a tus pacientes cuándo regresar. <span :style="{ fontFamily: 'var(--font-body-alt)', fontStyle: 'italic', color: 'var(--color-terracotta-300)' }">Configurado en 3 días</span> con el know-how comercial de Aura.
        </p>

        <!-- CTA row -->
        <div :style="{
          display: 'flex',
          gap: '1.5rem',
          alignItems: 'center',
          flexWrap: 'wrap',
          marginBottom: '3rem',
        }">
          <!-- Primary CTA pill -->
          <a href="#cta" class="aura-cta-pill" :style="{
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
          }">
            <!-- WhatsApp icon -->
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
            </svg>
            Probar el agente
          </a>

          <!-- Secondary link -->
          <a href="#como-funciona" :style="{
            fontFamily: 'var(--font-ui)',
            fontSize: '0.8rem',
            fontWeight: 500,
            color: 'rgba(234, 225, 208, 0.7)',
            textDecoration: 'none',
            letterSpacing: '0.04em',
            display: 'inline-flex',
            alignItems: 'center',
            gap: '0.5rem',
          }">
            Ver cómo funciona ↓
          </a>
        </div>

        <!-- Trust strip -->
        <div :style="{
          display: 'flex',
          gap: '2.5rem',
          flexWrap: 'wrap',
          paddingTop: '1.5rem',
          borderTop: '1px solid rgba(102,48,30,0.55)',
        }">
          <div v-for="s in trustItems" :key="s.l">
            <p :style="{
              fontFamily: 'var(--font-display)',
              fontSize: '1.5rem',
              fontWeight: 400,
              color: 'var(--color-cream-50)',
              margin: 0,
              letterSpacing: '-0.01em',
            }">{{ s.n }}</p>
            <p :style="{
              fontFamily: 'var(--font-ui-alt)',
              fontStyle: 'italic',
              fontSize: '0.72rem',
              color: 'rgba(206, 190, 162, 0.55)',
              margin: '0.2rem 0 0',
            }">{{ s.l }}</p>
          </div>
        </div>
      </div>

      <!-- ═══ Right column — Phone chat mockup ═══ -->
      <div :style="{
        position: 'relative',
        display: 'flex',
        justifyContent: 'center',
      }">
        <!-- Floating stat badges -->
        <div
          v-for="(s, i) in floatingStats"
          :key="'stat-'+i"
          class="agente-float-badge"
          :style="{
            position: 'absolute',
            left: s.x,
            top: s.y,
            display: 'inline-flex',
            alignItems: 'center',
            gap: '0.55rem',
            background: 'white',
            border: '1px solid rgba(0,0,0,0.04)',
            borderRadius: '999px',
            padding: '0.65rem 1.15rem',
            boxShadow: '0 10px 30px rgba(74, 52, 40, 0.16)',
            zIndex: 10,
            opacity: statVisible[i] ? 1 : 0,
            transform: statVisible[i] ? 'translateY(0)' : 'translateY(12px)',
            transition: 'all 700ms cubic-bezier(0.16,1,0.3,1)',
            animation: statVisible[i] ? 'auraFloat 6s ease-in-out infinite' : 'none',
            animationDelay: `${s.delay}s`,
            whiteSpace: 'nowrap',
            fontFamily: 'var(--font-ui)',
            fontSize: '0.82rem',
            fontWeight: 600,
            color: 'var(--color-brown-900)',
            letterSpacing: '0.01em',
          }"
        >
          <span :style="{ fontSize: '1.05rem', lineHeight: 1 }">{{ s.icon }}</span>
          <span>{{ s.label }}</span>
        </div>

        <!-- Phone frame -->
        <div class="agente-phone" :style="{
          width: '310px',
          background: 'linear-gradient(160deg, #2a2018, #1e1610)',
          borderRadius: '36px',
          padding: '0.6rem',
          boxShadow: '0 32px 80px rgba(0,0,0,0.45)',
          position: 'relative',
        }">
          <!-- Phone interior -->
          <div :style="{
            background: 'var(--color-cream-50)',
            borderRadius: '30px',
            overflow: 'hidden',
            display: 'flex',
            flexDirection: 'column',
            minHeight: '520px',
          }">

            <!-- Status bar -->
            <div :style="{
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              padding: '0.6rem 1.2rem 0.3rem',
              fontSize: '0.7rem',
              fontFamily: 'var(--font-ui)',
              fontWeight: 600,
              color: 'var(--color-brown-900)',
            }">
              <span>10:43</span>
              <div :style="{ display: 'flex', alignItems: 'center', gap: '0.35rem' }">
                <!-- Signal bars -->
                <svg width="14" height="10" viewBox="0 0 14 10" fill="var(--color-brown-900)">
                  <rect x="0" y="7" width="2.5" height="3" rx="0.5"/>
                  <rect x="3.5" y="4.5" width="2.5" height="5.5" rx="0.5"/>
                  <rect x="7" y="2" width="2.5" height="8" rx="0.5"/>
                  <rect x="10.5" y="0" width="2.5" height="10" rx="0.5"/>
                </svg>
                <!-- Battery -->
                <svg width="18" height="10" viewBox="0 0 18 10" fill="none" stroke="var(--color-brown-900)" stroke-width="1">
                  <rect x="0.5" y="1" width="14" height="8" rx="1.5"/>
                  <rect x="2" y="2.5" width="10" height="5" rx="0.5" fill="var(--color-brown-900)" stroke="none"/>
                  <path d="M15.5 3.5v3" stroke-linecap="round"/>
                </svg>
              </div>
            </div>

            <!-- WhatsApp header -->
            <div :style="{
              display: 'flex',
              alignItems: 'center',
              gap: '0.65rem',
              padding: '0.55rem 1rem',
              borderBottom: '1px solid rgba(221,209,186,0.5)',
              background: 'white',
            }">
              <!-- Back arrow -->
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--color-brown-400)" stroke-width="2">
                <path d="M15 18l-6-6 6-6"/>
              </svg>
              <!-- Avatar -->
              <div :style="{
                width: '32px',
                height: '32px',
                borderRadius: '50%',
                background: 'linear-gradient(135deg, var(--color-terracotta-500), var(--color-terracotta-400))',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: 'white',
                fontSize: '0.8rem',
                fontWeight: 600,
                fontFamily: 'var(--font-ui)',
                flexShrink: 0,
              }">A</div>
              <div :style="{ flex: 1 }">
                <p :style="{
                  fontFamily: 'var(--font-ui)',
                  fontSize: '0.78rem',
                  fontWeight: 600,
                  margin: 0,
                  color: 'var(--color-brown-900)',
                }">Clínica Aura · Atención</p>
                <p :style="{
                  fontFamily: 'var(--font-ui)',
                  fontSize: '0.62rem',
                  fontWeight: 500,
                  margin: 0,
                  color: '#25d366',
                }">en línea</p>
              </div>
            </div>

            <!-- Chat messages area -->
            <div :style="{
              flex: 1,
              padding: '1rem 0.75rem',
              display: 'flex',
              flexDirection: 'column',
              gap: '0.5rem',
              overflowY: 'auto',
              background: 'linear-gradient(180deg, var(--color-cream-50) 0%, #ece5d8 100%)',
            }">
              <div
                v-for="(msg, i) in messages"
                :key="i"
                :class="{ 'chat-msg-visible': visibleMessages.includes(i) }"
                :style="{
                  maxWidth: '82%',
                  padding: '0.55rem 0.7rem',
                  borderRadius: msg.from === 'user' ? '10px 10px 2px 10px' : '10px 10px 10px 2px',
                  fontFamily: 'var(--font-body)',
                  fontSize: '0.75rem',
                  lineHeight: 1.45,
                  color: 'var(--color-brown-900)',
                  alignSelf: msg.from === 'user' ? 'flex-end' : 'flex-start',
                  background: msg.from === 'user' ? '#d9fdd3' : 'white',
                  boxShadow: '0 1px 2px rgba(0,0,0,0.06)',
                  opacity: visibleMessages.includes(i) ? 1 : 0,
                  transform: visibleMessages.includes(i) ? 'translateY(0)' : 'translateY(8px)',
                  transition: 'opacity 0.4s ease-out, transform 0.4s ease-out',
                }"
              >{{ msg.text }}</div>

              <!-- Typing indicator -->
              <div v-if="showTyping" :style="{
                alignSelf: 'flex-start',
                background: 'white',
                borderRadius: '10px 10px 10px 2px',
                padding: '0.6rem 0.85rem',
                display: 'flex',
                gap: '0.25rem',
                alignItems: 'center',
                boxShadow: '0 1px 2px rgba(0,0,0,0.06)',
              }">
                <span class="typing-dot" :style="{
                  width: '6px', height: '6px', borderRadius: '50%',
                  background: 'var(--color-brown-300)',
                  animationDelay: '0s',
                }" />
                <span class="typing-dot" :style="{
                  width: '6px', height: '6px', borderRadius: '50%',
                  background: 'var(--color-brown-300)',
                  animationDelay: '0.15s',
                }" />
                <span class="typing-dot" :style="{
                  width: '6px', height: '6px', borderRadius: '50%',
                  background: 'var(--color-brown-300)',
                  animationDelay: '0.3s',
                }" />
              </div>
            </div>

            <!-- Input bar -->
            <div :style="{
              display: 'flex',
              alignItems: 'center',
              gap: '0.5rem',
              padding: '0.5rem 0.75rem',
              borderTop: '1px solid rgba(221,209,186,0.4)',
              background: 'white',
            }">
              <div :style="{
                flex: 1,
                height: '32px',
                borderRadius: '16px',
                background: 'var(--color-cream-50)',
                border: '1px solid rgba(221,209,186,0.6)',
                padding: '0 0.75rem',
                display: 'flex',
                alignItems: 'center',
                fontFamily: 'var(--font-ui)',
                fontSize: '0.68rem',
                color: 'var(--color-brown-300)',
              }">Escribe un mensaje...</div>
              <div :style="{
                width: '32px',
                height: '32px',
                borderRadius: '50%',
                background: '#25d366',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
              }">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="white">
                  <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/>
                </svg>
              </div>
            </div>
          </div>
        </div>

        <!-- Floating badge: "X citas hoy" -->
        <div class="agente-citas-badge" :style="{
          position: 'absolute',
          top: '-12px',
          right: '-8px',
          background: 'var(--color-cream-50)',
          borderRadius: '999px',
          padding: '0.55rem 1.1rem',
          display: 'flex',
          alignItems: 'center',
          gap: '0.5rem',
          boxShadow: '0 8px 28px rgba(74,52,40,0.22)',
          border: '1px solid rgba(221,209,186,0.6)',
          animation: 'auraFloat 5s ease-in-out infinite',
          zIndex: 5,
        }">
          <span :style="{
            width: '7px',
            height: '7px',
            borderRadius: '50%',
            background: '#6bcf7f',
            boxShadow: '0 0 8px rgba(107,207,127,0.5)',
            animation: 'auraPulse 2s ease-in-out infinite',
            display: 'inline-block',
          }" />
          <span :style="{
            fontFamily: 'var(--font-ui)',
            fontSize: '0.72rem',
            fontWeight: 600,
            color: 'var(--color-brown-900)',
          }">{{ count }} citas hoy</span>
        </div>
      </div>
    </div>

    <!-- Scroll indicator -->
    <div class="agente-scroll-hint" :style="{
      position: 'absolute',
      bottom: '2rem',
      left: '2rem',
      writingMode: 'vertical-rl',
      transform: 'rotate(180deg)',
      fontFamily: 'var(--font-ui)',
      fontSize: '0.65rem',
      textTransform: 'uppercase',
      letterSpacing: '0.3em',
      color: 'rgba(206, 190, 162, 0.4)',
    }">Scroll ↓</div>
  </section>
</template>

<style scoped>
@keyframes auraFadeIn {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes auraTyping {
  0%, 80%, 100% { opacity: 0.3; transform: translateY(0); }
  40% { opacity: 1; transform: translateY(-4px); }
}

.typing-dot {
  animation: auraTyping 1.4s ease-in-out infinite;
}

@media (max-width: 980px) {
  .agente-float-badge {
    display: none !important;
  }
  .agente-phone {
    width: 260px !important;
  }
  .agente-phone > div {
    min-height: 440px !important;
  }
  .agente-citas-badge {
    right: auto !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    top: -16px !important;
  }
  .agente-scroll-hint {
    display: none !important;
  }
}

@media (max-width: 480px) {
  .agente-phone {
    width: 220px !important;
  }
  .agente-phone > div {
    min-height: 380px !important;
  }
}
</style>
