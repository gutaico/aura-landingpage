<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import ChromaImage from '../ChromaImage.vue'

const triggers = [
  { n: '01', t: 'Inseguridad', b: 'No venden tratamientos — venden dejar de esconderse. Tu paciente no busca un procedimiento, busca dejar de evitar espejos, fotos y reuniones.' },
  { n: '02', t: 'Desconfianza', b: 'Vio 10 anuncios iguales. Su defensa está alta. Necesita ver algo que se sienta real — no otro antes y después con filtro.' },
  { n: '03', t: 'Procrastinación', b: 'Lo quiere hace 2 años. Lo pospone con miedo disfrazado de dinero. El trigger correcto rompe la inercia en un solo scroll.' },
  { n: '04', t: 'Pertenencia', b: 'No quiere "verse bien". Quiere sentirse parte de algo aspiracional. Pertenecer a ese grupo de mujeres que sí se atreven.' },
]

const sectors = [
  'Medicina estética',
  'Depilación láser',
  'Barbería',
  'Wellness',
  'Pilates',
  'Medicina antiage',
  'Spa & masajes',
  'Odontología estética',
]

const activeIndex = ref(0)
const itemEls = []
let observer = null

function setItemRef(el, i) {
  if (el) itemEls[i] = el
}

onMounted(() => {
  observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const idx = itemEls.indexOf(entry.target)
          if (idx !== -1) activeIndex.value = idx
        }
      })
    },
    { rootMargin: '-35% 0px -35% 0px' },
  )

  itemEls.forEach(el => {
    if (el) observer.observe(el)
  })
})

onUnmounted(() => {
  if (observer) observer.disconnect()
})
</script>

<template>
  <section
    id="expertise"
    class="aura-section-pad"
    :style="{
      background: 'var(--color-cream-100)',
      padding: 'clamp(5rem, 8vw, 9rem) 2.5rem',
      position: 'relative',
    }"
  >
    <div :style="{ maxWidth: '1200px', margin: '0 auto', position: 'relative' }">
      <!-- Header -->
      <div class="reveal">
        <div :style="{ textAlign: 'center', maxWidth: '780px', margin: '0 auto 4rem' }">
          <p :style="{
            fontFamily: 'var(--font-ui)',
            fontSize: '0.7rem',
            fontWeight: 500,
            textTransform: 'uppercase',
            letterSpacing: '0.28em',
            color: 'var(--color-terracotta-500)',
            margin: '0 0 1.25rem',
          }">
            § II · Expertise sectorial
          </p>
          <h2 :style="{
            fontFamily: 'var(--font-display)',
            fontWeight: 400,
            fontSize: 'clamp(2rem, 4.5vw, 3.2rem)',
            lineHeight: 1.05,
            letterSpacing: '-0.022em',
            margin: 0,
            color: 'var(--color-brown-900)',
          }">
            Tu paciente no compra<br/>
            un tratamiento.<br/>
            Compra <span :style="{ fontStyle: 'italic', color: 'var(--color-terracotta-500)' }">la versión de sí misma</span><br/>
            que ve en el espejo.
          </h2>
        </div>
      </div>

      <!-- Two-column layout -->
      <div
        class="aura-expertise-layout"
        :style="{
          display: 'grid',
          gridTemplateColumns: '1fr 1fr',
          gap: '5rem',
          alignItems: 'start',
        }"
      >
        <!-- Left: sticky image -->
        <div :style="{
          position: 'sticky',
          top: '15vh',
          alignSelf: 'start',
        }">
          <div :style="{ position: 'relative' }">
            <ChromaImage
              src="/espejo.webp"
              alt="Paciente y su versión aspiracional"
              :threshold="40"
              :feather="20"
              :style="{
                width: '100%',
                maxWidth: '420px',
                height: 'auto',
                display: 'block',
                margin: '0 auto',
                filter: 'drop-shadow(0 30px 60px rgba(74,52,40,0.15))',
              }"
            />
            <svg
              aria-hidden="true"
              :style="{
                position: 'absolute',
                inset: '-6%',
                width: '112%',
                height: '112%',
                pointerEvents: 'none',
              }"
              viewBox="0 0 100 100"
              preserveAspectRatio="xMidYMid meet"
            >
              <circle
                cx="50" cy="50" r="48"
                fill="none"
                stroke="var(--color-terracotta-500)"
                stroke-width="0.2"
                stroke-dasharray="0.5 1.5"
                opacity="0.35"
              />
            </svg>
          </div>
        </div>

        <!-- Right: scroll-driven accordion -->
        <div class="expertise-accordion" :style="{ paddingBottom: '30vh' }">
          <div
            v-for="(trigger, i) in triggers"
            :key="trigger.n"
            :ref="el => setItemRef(el, i)"
            :style="{
              borderTop: i === 0 ? '1px solid rgba(221,209,186,0.8)' : 'none',
              borderBottom: '1px solid rgba(221,209,186,0.8)',
              paddingTop: i === 0 ? '0' : '2rem',
              marginTop: i === 0 ? '0' : '2rem',
            }"
          >
            <!-- Header row -->
            <div
              :style="{
                display: 'flex',
                alignItems: 'baseline',
                gap: '1rem',
                padding: '1.5rem 0',
                cursor: 'pointer',
                transition: 'opacity .5s ease',
                opacity: activeIndex === i ? 1 : 0.3,
              }"
              @click="activeIndex = i"
            >
              <span :style="{
                fontFamily: 'var(--font-ui-alt)',
                fontStyle: 'italic',
                fontSize: '0.82rem',
                color: 'var(--color-terracotta-500)',
                flexShrink: 0,
              }">{{ trigger.n }}</span>

              <span :style="{
                width: activeIndex === i ? '32px' : '0px',
                height: '1px',
                background: 'var(--color-terracotta-500)',
                transition: 'width .5s cubic-bezier(0.16,1,0.3,1)',
                flexShrink: 0,
              }" />

              <span :style="{
                fontFamily: 'var(--font-display)',
                fontWeight: 400,
                fontStyle: 'italic',
                fontSize: 'clamp(1.3rem, 2vw, 1.65rem)',
                color: activeIndex === i ? 'var(--color-brown-900)' : 'var(--color-brown-400)',
                letterSpacing: '-0.01em',
                transition: 'color .5s ease',
              }">{{ trigger.t }}</span>
            </div>

            <!-- Collapsible body -->
            <div :style="{
              maxHeight: activeIndex === i ? '160px' : '0',
              opacity: activeIndex === i ? 1 : 0,
              overflow: 'hidden',
              transition: 'max-height .6s cubic-bezier(0.16,1,0.3,1), opacity .5s ease',
            }">
              <p class="expertise-body" :style="{
                fontFamily: 'var(--font-body)',
                fontSize: '0.95rem',
                lineHeight: 1.6,
                color: 'var(--color-brown-400)',
                margin: '0 0 1.75rem',
                paddingLeft: '3.8rem',
                maxWidth: '42ch',
              }">{{ trigger.b }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Bottom strip — sectors -->
      <div class="reveal">
        <div
          class="aura-hero-grid"
          :style="{
            marginTop: '3.5rem',
            paddingTop: '2.5rem',
            borderTop: '1px solid rgba(221,209,186,0.8)',
            display: 'grid',
            gridTemplateColumns: '1.2fr 2fr',
            gap: '3rem',
            alignItems: 'center',
          }"
        >
          <p :style="{
            fontFamily: 'var(--font-display)',
            fontWeight: 400,
            fontSize: 'clamp(1.4rem, 2.2vw, 1.85rem)',
            lineHeight: 1.15,
            letterSpacing: '-0.015em',
            color: 'var(--color-brown-900)',
            margin: 0,
            fontStyle: 'italic',
          }">
            Un solo sector. <br/>Desde 2021.
          </p>
          <div :style="{
            display: 'flex',
            flexWrap: 'wrap',
            gap: '0.5rem 1.5rem',
            alignItems: 'center',
          }">
            <template v-for="(sector, i) in sectors" :key="i">
              <span :style="{
                fontFamily: 'var(--font-body)',
                fontSize: '0.95rem',
                color: 'var(--color-brown-400)',
              }">{{ sector }}</span>
              <span
                v-if="i < sectors.length - 1"
                :style="{
                  color: 'var(--color-brown-300)',
                  fontSize: '0.7rem',
                  userSelect: 'none',
                }"
              >·</span>
            </template>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
@media (max-width: 900px) {
  .expertise-accordion {
    padding-bottom: 2rem !important;
  }
  .expertise-body {
    padding-left: 0 !important;
  }
}
</style>
