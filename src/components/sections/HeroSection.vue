<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

/* ── Floating reactions data ── */
const reactions = [
  { icon: '♥', label: '284 likes', x: '-18%', y: '6%', delay: 0, color: '#e85a6e', variant: 'reaction' },
  { icon: '💬', label: '47 mensajes', x: '-22%', y: '40%', delay: 0.3, color: 'var(--color-terracotta-500)', variant: 'reaction' },
  { icon: '✦', label: '3.2× ROI', x: '78%', y: '10%', delay: 0.6, color: 'var(--color-terracotta-500)', variant: 'stat' },
  { icon: '📅', label: '12 citas nuevas', x: '82%', y: '48%', delay: 0.9, color: 'var(--color-terracotta-500)', variant: 'stat' },
]

/* ── Trust strip data ── */
const trustItems = [
  { n: '7 días', l: 'al aire' },
  { n: '30 días', l: 'garantía total' },
  { n: '+40', l: 'clínicas activas' },
]

/* ── Floating reaction mount state ── */
const mounted = ref({})
const timers = []

onMounted(() => {
  reactions.forEach((r, i) => {
    const t = setTimeout(() => {
      mounted.value = { ...mounted.value, [i]: true }
    }, r.delay * 1000 + 400)
    timers.push(t)
  })
})

onUnmounted(() => {
  timers.forEach(t => clearTimeout(t))
})

function getReactionStyles(r, i) {
  const isMounted = mounted.value[i]

  const base = {
    position: 'absolute',
    left: r.x,
    top: r.y,
    display: 'inline-flex',
    alignItems: 'center',
    gap: '0.55rem',
    whiteSpace: 'nowrap',
    borderRadius: '999px',
    fontFamily: 'var(--font-ui)',
    fontSize: '0.82rem',
    fontWeight: 600,
    letterSpacing: '0.01em',
    opacity: isMounted ? 1 : 0,
    transform: isMounted ? 'translateY(0)' : 'translateY(12px)',
    transition: 'all 600ms cubic-bezier(0.16,1,0.3,1)',
    animation: isMounted ? 'auraFloat 6s ease-in-out infinite' : 'none',
    animationDelay: `${r.delay}s`,
    zIndex: 3,
  }

  return {
    ...base,
    background: 'white',
    color: 'var(--color-brown-900)',
    padding: '0.65rem 1.15rem',
    boxShadow: '0 10px 30px rgba(74, 52, 40, 0.16)',
    border: '1px solid rgba(0,0,0,0.04)',
  }
}
</script>

<template>
  <section class="aura-section-pad" :style="{
    background: 'var(--color-cream-50)',
    padding: 'clamp(7rem, 11vw, 10rem) 2.5rem 0',
    position: 'relative',
    overflow: 'hidden',
  }">
    <div :style="{ maxWidth: '1200px', margin: '0 auto' }">
      <div
        class="aura-hero-grid"
        :style="{
          display: 'grid',
          gridTemplateColumns: '1.35fr 1fr',
          gap: '3.5rem',
          alignItems: 'start',
        }"
      >
        <!-- ═══ Left — editorial headline ═══ -->
        <div>
          <!-- Eyebrow -->
          <p :style="{
            fontFamily: 'var(--font-ui)',
            fontSize: '0.72rem',
            fontWeight: 500,
            textTransform: 'uppercase',
            letterSpacing: '0.28em',
            color: 'var(--color-terracotta-500)',
            margin: '0 0 2rem',
          }">
            ╱ Carta abierta a dueños de clínicas
          </p>

          <!-- Headline -->
          <h1 :style="{
            fontFamily: 'var(--font-display)',
            fontWeight: 400,
            fontSize: 'clamp(2.4rem, 6vw, 4.8rem)',
            lineHeight: 1,
            letterSpacing: '-0.025em',
            margin: '0 0 2.5rem',
            color: 'var(--color-brown-900)',
          }">
            Tus anuncios<br />
            traen <span :style="{ fontStyle: 'italic', color: 'var(--color-terracotta-500)' }">curiosos</span>.<br />
            Nosotros traemos<br />
            <span :style="{
              fontStyle: 'italic',
              color: 'var(--color-terracotta-500)',
              position: 'relative',
            }">
              pacientes que pagan
              <svg
                aria-hidden="true"
                :style="{
                  position: 'absolute',
                  bottom: '-0.15em',
                  left: 0,
                  width: '100%',
                  height: '0.2em',
                }"
                viewBox="0 0 300 12"
                preserveAspectRatio="none"
              >
                <path d="M2,8 Q75,2 150,6 T298,5" stroke="currentColor" stroke-width="2" fill="none" opacity="0.4" />
              </svg>
            </span>.
          </h1>

          <!-- Pull quote -->
          <div :style="{
            maxWidth: '48ch',
            display: 'grid',
            gridTemplateColumns: 'auto 1fr',
            gap: '1.25rem',
            marginBottom: '2.5rem',
          }">
            <span :style="{
              fontFamily: 'var(--font-display)',
              fontSize: '4.5rem',
              fontWeight: 400,
              lineHeight: 0.85,
              color: 'var(--color-terracotta-500)',
              fontStyle: 'italic',
              alignSelf: 'start',
            }">&ldquo;</span>
            <p :style="{
              fontFamily: 'var(--font-body-alt)',
              fontStyle: 'italic',
              fontSize: 'clamp(1.05rem, 1.4vw, 1.2rem)',
              lineHeight: 1.55,
              color: 'var(--color-brown-900)',
              margin: 0,
            }">
              El 92% de las agencias te venden tráfico. Nosotros llevamos
              a esa persona desde el primer anuncio hasta el momento en que
              paga su tercera cita. Medimos lo que te importa: ventas.
            </p>
          </div>

          <!-- CTA row -->
          <div :style="{
            display: 'flex',
            gap: '2rem',
            alignItems: 'center',
            flexWrap: 'wrap',
            marginBottom: '3rem',
          }">
            <!-- Primary CTA button -->
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
              <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
                <rect x="3" y="5" width="18" height="16" rx="2" />
                <path d="M3 10h18M8 3v4M16 3v4" />
              </svg>
              Diagnóstico gratuito
            </a>

            <!-- Secondary link -->
            <a href="#mecanismo" :style="{
              fontFamily: 'var(--font-ui)',
              fontSize: '0.78rem',
              fontWeight: 600,
              letterSpacing: '0.04em',
              color: 'var(--color-brown-400)',
              textDecoration: 'none',
              display: 'inline-flex',
              alignItems: 'center',
              gap: '0.5rem',
              borderBottom: '1px solid var(--color-cream-300)',
              paddingBottom: '2px',
            }">
              Ver cómo lo hacemos
              <span :style="{ fontSize: '0.9rem' }">↓</span>
            </a>
          </div>

          <!-- Trust strip -->
          <div :style="{
            display: 'grid',
            gridTemplateColumns: 'repeat(3, auto)',
            gap: '2rem',
            paddingTop: '2rem',
            borderTop: '1px solid rgba(221,209,186,0.8)',
            maxWidth: '520px',
          }">
            <div v-for="s in trustItems" :key="s.l">
              <p :style="{
                fontFamily: 'var(--font-display)',
                fontSize: '1.5rem',
                fontWeight: 400,
                color: 'var(--color-brown-900)',
                margin: 0,
                letterSpacing: '-0.01em',
              }">{{ s.n }}</p>
              <p :style="{
                fontFamily: 'var(--font-ui-alt)',
                fontStyle: 'italic',
                fontSize: '0.78rem',
                color: 'var(--color-brown-400)',
                margin: '0.2rem 0 0',
              }">{{ s.l }}</p>
            </div>
          </div>
        </div>

        <!-- ═══ Right — media column ═══ -->
        <div :style="{
          position: 'relative',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'flex-start',
          paddingTop: '1rem',
        }">
          <!-- Floating reactions -->
          <div
            v-for="(r, i) in reactions"
            :key="i"
            class="hero-float-badge"
            :style="getReactionStyles(r, i)"
          >
            <span :style="{
              color: r.color || 'var(--color-terracotta-500)',
              fontSize: '1.05rem',
              lineHeight: 1,
            }">{{ r.icon }}</span>
            <span>{{ r.label }}</span>
          </div>

          <!-- Reel mockup -->
          <div class="hero-reel" :style="{
            width: '280px',
            aspectRatio: '9 / 16',
            borderRadius: '20px',
            background: 'linear-gradient(160deg, var(--color-brown-800), var(--color-brown-900))',
            position: 'relative',
            overflow: 'hidden',
            transform: 'rotate(-2deg)',
            boxShadow: '0 24px 64px rgba(74, 52, 40, 0.28)',
            zIndex: 2,
          }">
            <!-- Fake IG top bar -->
            <div :style="{
              position: 'absolute',
              top: 0,
              left: 0,
              right: 0,
              padding: '1rem 1rem 0.5rem',
              background: 'linear-gradient(180deg, rgba(0,0,0,0.4) 0%, transparent 100%)',
              zIndex: 2,
              display: 'flex',
              alignItems: 'center',
              gap: '0.5rem',
            }">
              <div :style="{
                width: '24px',
                height: '24px',
                borderRadius: '50%',
                background: 'linear-gradient(135deg, var(--color-terracotta-500), var(--color-terracotta-400))',
                border: '1.5px solid rgba(255,255,255,0.6)',
              }" />
              <span :style="{
                fontFamily: 'var(--font-ui)',
                fontSize: '0.68rem',
                fontWeight: 600,
                color: 'white',
                letterSpacing: '0.02em',
              }">aura.marketing</span>
              <span :style="{
                fontFamily: 'var(--font-ui)',
                fontSize: '0.58rem',
                fontWeight: 500,
                color: 'rgba(255,255,255,0.5)',
                marginLeft: 'auto',
              }">Reel</span>
            </div>

            <!-- Play button center -->
            <div :style="{
              position: 'absolute',
              top: '50%',
              left: '50%',
              transform: 'translate(-50%, -50%)',
              width: '48px',
              height: '48px',
              borderRadius: '50%',
              background: 'rgba(255,255,255,0.15)',
              backdropFilter: 'blur(8px)',
              WebkitBackdropFilter: 'blur(8px)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              zIndex: 2,
            }">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="white">
                <path d="M8 5v14l11-7z" />
              </svg>
            </div>

            <!-- Text overlay at bottom -->
            <div :style="{
              position: 'absolute',
              bottom: 0,
              left: 0,
              right: 0,
              padding: '2.5rem 1rem 1.2rem',
              background: 'linear-gradient(0deg, rgba(0,0,0,0.5) 0%, transparent 100%)',
              zIndex: 2,
            }">
              <p :style="{
                fontFamily: 'var(--font-body)',
                fontSize: '0.78rem',
                color: 'white',
                margin: '0 0 0.5rem',
                lineHeight: 1.4,
              }">Cómo conseguimos 42 citas en 7 días para una clínica de estética 🔥</p>
              <p :style="{
                fontFamily: 'var(--font-ui)',
                fontSize: '0.62rem',
                color: 'rgba(255,255,255,0.5)',
                margin: 0,
              }">♫ Sonido original · 28.4K vistas</p>
            </div>

            <!-- Action rail right side -->
            <div :style="{
              position: 'absolute',
              right: '0.75rem',
              bottom: '5rem',
              display: 'flex',
              flexDirection: 'column',
              gap: '1.2rem',
              alignItems: 'center',
              zIndex: 2,
            }">
              <div v-for="action in [
                { icon: '♥', count: '2.8K' },
                { icon: '💬', count: '47' },
                { icon: '↗', count: '' },
                { icon: '⋯', count: '' },
              ]" :key="action.icon" :style="{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                gap: '0.15rem',
              }">
                <span :style="{ fontSize: '1rem', color: 'white' }">{{ action.icon }}</span>
                <span v-if="action.count" :style="{
                  fontFamily: 'var(--font-ui)',
                  fontSize: '0.58rem',
                  color: 'rgba(255,255,255,0.7)',
                }">{{ action.count }}</span>
              </div>
            </div>
          </div>

          <!-- ═══ Chat overlay ═══ -->
          <div class="hero-chat-overlay" :style="{
            position: 'absolute',
            left: '-8%',
            bottom: '-2%',
            width: '240px',
            background: 'white',
            borderRadius: '16px',
            padding: '0.9rem 1rem',
            boxShadow: '0 16px 44px rgba(74, 52, 40, 0.18)',
            border: '1px solid rgba(0,0,0,0.04)',
            zIndex: 4,
            transform: 'rotate(-3deg)',
          }">
            <!-- Chat header -->
            <div :style="{
              display: 'flex',
              alignItems: 'center',
              gap: '0.55rem',
              marginBottom: '0.65rem',
            }">
              <div :style="{
                width: '28px',
                height: '28px',
                borderRadius: '50%',
                background: 'linear-gradient(135deg, var(--color-terracotta-500), var(--color-terracotta-400))',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: 'white',
                fontSize: '0.72rem',
                fontWeight: 600,
              }">A</div>
              <div>
                <p :style="{
                  fontFamily: 'var(--font-ui)',
                  fontSize: '0.72rem',
                  fontWeight: 600,
                  margin: 0,
                  color: 'var(--color-brown-900)',
                }">Aura · WhatsApp</p>
                <p :style="{
                  fontFamily: 'var(--font-ui-alt)',
                  fontStyle: 'italic',
                  fontSize: '0.62rem',
                  margin: 0,
                  color: 'var(--color-brown-400)',
                }">en línea · responde en 28s</p>
              </div>
            </div>

            <!-- Chat bubble -->
            <div :style="{
              background: 'var(--color-cream-100)',
              borderRadius: '10px 10px 10px 2px',
              padding: '0.55rem 0.75rem',
              fontFamily: 'var(--font-body)',
              fontSize: '0.75rem',
              lineHeight: 1.4,
              color: 'var(--color-brown-900)',
              marginBottom: '0.35rem',
            }">
              Hola Ana 👋 Vi que viste el reel. ¿Quieres agendar tu valoración gratis esta semana?
            </div>

            <!-- Timestamp -->
            <p :style="{
              fontFamily: 'var(--font-ui-alt)',
              fontStyle: 'italic',
              fontSize: '0.62rem',
              color: 'var(--color-brown-300)',
              margin: 0,
              textAlign: 'right',
            }">
              13:42 · Leído
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
@media (max-width: 980px) {
  .hero-float-badge {
    display: none !important;
  }
  .hero-reel {
    width: 240px !important;
    margin: 0 auto;
    transform: rotate(0deg) !important;
  }
  .hero-chat-overlay {
    left: 50% !important;
    transform: translateX(-50%) rotate(-2deg) !important;
    bottom: -2rem !important;
    width: 220px !important;
  }
}
@media (max-width: 480px) {
  .hero-reel {
    width: 200px !important;
  }
  .hero-chat-overlay {
    width: 190px !important;
  }
}
</style>
