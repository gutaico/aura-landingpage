<script setup>
const cases = [
  { name: 'Estudio Lumen', cat: 'Depilación láser', bg: '#a87968', big: '284K', big2: 'views', q: 'El reel que generó $340K en ventas', tall: true },
  { name: 'Clínica Serena', cat: 'Medicina estética', bg: '#c4a887', big: '47', big2: 'citas / 30 días', q: 'De 4 consultas al mes a 47', tall: false },
  { name: 'Casa Mellado', cat: 'Barbería premium', bg: '#8e6f5a', big: '2.8×', big2: 'LTV', q: 'Sistema de retención que multiplica', tall: false },
  { name: 'Estudio Raíz', cat: 'Wellness · Pilates', bg: '#b89780', big: '68%', big2: 'menos no-shows', q: 'Confirmación automática 24h + 2h', tall: true },
  { name: 'Botánica MD', cat: 'Medicina antiage', bg: '#9d7f6b', big: '$2.3K', big2: 'ticket promedio', q: 'Posicionamiento premium real', tall: false },
  { name: 'Vera Spa', cat: 'Spa & masajes', bg: '#b08a72', big: '+41', big2: 'socias nuevas', q: 'Comunidad en 60 días', tall: false },
]

function onCardEnter(e) {
  e.currentTarget.style.transform = 'translateY(-4px)'
}
function onCardLeave(e) {
  e.currentTarget.style.transform = 'translateY(0)'
}
</script>

<template>
  <section
    id="portfolio"
    class="aura-section-pad"
    :style="{
      background: 'var(--color-cream-50)',
      padding: 'clamp(5rem, 8vw, 9rem) 2.5rem',
      borderTop: '1px solid rgba(221,209,186,0.8)',
    }"
  >
    <div :style="{ maxWidth: '1200px', margin: '0 auto' }">
      <!-- Header -->
      <div class="reveal">
        <div
          class="aura-hero-grid"
          :style="{
            display: 'grid',
            gridTemplateColumns: '1fr 1.5fr',
            gap: '4rem',
            alignItems: 'end',
            marginBottom: '4rem',
          }"
        >
          <div>
            <p :style="{
              fontFamily: 'var(--font-ui)',
              fontSize: '0.7rem',
              fontWeight: 500,
              textTransform: 'uppercase',
              letterSpacing: '0.28em',
              color: 'var(--color-terracotta-500)',
              margin: '0 0 1.25rem',
            }">
              &sect; VII &middot; Portfolio
            </p>
            <h2 :style="{
              fontFamily: 'var(--font-display)',
              fontWeight: 400,
              fontSize: 'clamp(2rem, 4vw, 3rem)',
              lineHeight: 1.05,
              letterSpacing: '-0.022em',
              margin: 0,
              color: 'var(--color-brown-900)',
            }">
              Creativos que<br /><span :style="{ fontStyle: 'italic', color: 'var(--color-terracotta-500)' }">generaron resultados</span>.
            </h2>
          </div>
          <p :style="{
            fontFamily: 'var(--font-body-alt)',
            fontStyle: 'italic',
            fontSize: '1.05rem',
            lineHeight: 1.55,
            color: 'var(--color-brown-400)',
            margin: 0,
          }">
            Piezas producidas por nuestro equipo para cl&iacute;nicas reales. Cada una con la m&eacute;trica que import&oacute; detr&aacute;s.
          </p>
        </div>
      </div>

      <!-- Masonry grid -->
      <div
        class="aura-masonry"
        :style="{ columnCount: 3, columnGap: '1.25rem' }"
      >
        <article
          v-for="(c, i) in cases"
          :key="i"
          :style="{
            breakInside: 'avoid',
            marginBottom: '1.25rem',
            position: 'relative',
            borderRadius: '18px',
            overflow: 'hidden',
            aspectRatio: c.tall ? '9/16' : '4/5',
            background: `linear-gradient(160deg, ${c.bg}, ${c.bg}cc 50%, #4a342c 100%)`,
            boxShadow: '0 20px 50px rgba(74,52,40,0.18)',
            cursor: 'pointer',
            transition: 'transform .4s cubic-bezier(0.16,1,0.3,1)',
          }"
          @mouseenter="onCardEnter"
          @mouseleave="onCardLeave"
        >
          <!-- Noise overlay -->
          <div
            aria-hidden="true"
            class="poster-noise"
          ></div>

          <!-- Gradient floor -->
          <div
            aria-hidden="true"
            :style="{
              position: 'absolute',
              bottom: 0,
              left: 0,
              right: 0,
              height: '55%',
              background: 'linear-gradient(to top, rgba(0,0,0,0.55), transparent)',
              pointerEvents: 'none',
            }"
          ></div>

          <!-- Play button -->
          <div :style="{
            position: 'absolute',
            top: '1rem',
            right: '1rem',
            width: '34px',
            height: '34px',
            borderRadius: '50%',
            background: 'rgba(255,255,255,0.18)',
            backdropFilter: 'blur(6px)',
            border: '1px solid rgba(255,255,255,0.25)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
          }">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="white">
              <path d="M8 5v14l11-7z" />
            </svg>
          </div>

          <!-- Top label: category -->
          <div :style="{ position: 'absolute', top: '1.1rem', left: '1.25rem', color: 'white' }">
            <p :style="{
              fontFamily: 'var(--font-ui)',
              fontSize: '0.6rem',
              fontWeight: 500,
              textTransform: 'uppercase',
              letterSpacing: '0.2em',
              margin: 0,
              opacity: 0.85,
            }">
              {{ c.cat }}
            </p>
          </div>

          <!-- Bottom content -->
          <div :style="{
            position: 'absolute',
            bottom: '1.1rem',
            left: '1.25rem',
            right: '1.25rem',
            color: 'white',
          }">
            <!-- Big number -->
            <p :style="{
              fontFamily: 'var(--font-display)',
              fontWeight: 400,
              fontStyle: 'italic',
              fontSize: 'clamp(2.8rem, 5vw, 4.2rem)',
              lineHeight: 0.95,
              letterSpacing: '-0.025em',
              margin: '0 0 0.2rem',
              textShadow: '0 2px 18px rgba(0,0,0,0.35)',
            }">
              {{ c.big }}
            </p>

            <!-- Big2 label -->
            <p :style="{
              fontFamily: 'var(--font-ui)',
              fontSize: '0.72rem',
              fontWeight: 500,
              textTransform: 'uppercase',
              letterSpacing: '0.2em',
              margin: '0 0 0.85rem',
              opacity: 0.85,
            }">
              {{ c.big2 }}
            </p>

            <!-- Quote -->
            <p :style="{
              fontFamily: 'var(--font-body-alt)',
              fontStyle: 'italic',
              fontSize: '0.95rem',
              lineHeight: 1.35,
              margin: '0 0 0.85rem',
              opacity: 0.95,
              maxWidth: '24ch',
            }">
              "{{ c.q }}"
            </p>

            <!-- Name -->
            <div :style="{ paddingTop: '0.65rem', borderTop: '1px solid rgba(255,255,255,0.2)' }">
              <p :style="{
                fontFamily: 'var(--font-ui)',
                fontSize: '0.74rem',
                fontWeight: 600,
                color: 'white',
                margin: 0,
                letterSpacing: '0.02em',
              }">
                {{ c.name }}
              </p>
            </div>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>

<style scoped>
.poster-noise {
  position: absolute;
  inset: 0;
  opacity: 0.18;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  background-size: 180px;
  pointer-events: none;
}
</style>
