<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import ChromaImage from '../../ChromaImage.vue'

const args = [
  { n: '01', t: 'Retorno inmediato', sub: 'Se paga en la primera semana.', body: 'Si perdías el 30% de leads por no contestar, el agente recupera eso desde el día 1. Hasta 10\u00d7 retorno en clínicas de alto ticket.', icon: '/img/iconos/datos.webp' },
  { n: '02', t: 'Ahorro en nómina', sub: 'Fracción del costo de una recepcionista.', body: 'No sustituye a tu equipo \u2014 hace lo que tu equipo no puede hacer. Contesta a las 11pm, los domingos, y en vacaciones.', icon: '/img/iconos/crm.webp' },
  { n: '03', t: 'Calidad consistente', sub: 'Nunca tiene un mal día.', body: 'A las 3am y a las 3pm. El lunes y el sábado. Tu paciente siempre recibe el mismo trato. Sin rotación, sin capacitar de nuevo.', icon: '/img/iconos/garantia.webp' },
  { n: '04', t: 'Disponible 24/7', sub: 'Cuando tu competencia duerme.', body: 'La gente busca tratamientos a las 11pm scrolleando Instagram. El agente responde en segundos. Tu competencia, al día siguiente.', icon: '/img/iconos/conversaciones.webp' },
  { n: '05', t: 'Nutrición + retención', sub: 'El paciente regresa solo.', body: 'Seguimiento inteligente a los que no contestaron. Recordatorio a los que les toca regresar. Cumpleaños, post-tratamiento, win-back.', icon: '/img/iconos/anuncios.webp' },
  { n: '06', t: 'Tú decides, él ejecuta', sub: 'Human-in-the-loop.', body: 'Cuando necesita tu criterio, te avisa al celular. Un toque y continúa. Dejas de operar, empiezas a dirigir.', icon: '/img/iconos/dashboard.webp' },
  { n: '07', t: 'Escala sin fricción', sub: 'De 50 a 500 conversaciones.', body: 'No es contratar a otra persona \u2014 es subir de plan. Sin capacitación, sin rotación, sin perder calidad.', icon: '/img/iconos/datos.webp' },
]

const active = ref(0)
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
          if (idx !== -1) active.value = idx
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
    class="aura-section-pad"
    :style="{
      background: 'var(--color-cream-100)',
      padding: 'clamp(5rem, 8vw, 9rem) 2.5rem',
      borderTop: '1px solid rgba(221,209,186,0.8)',
    }"
  >
    <div :style="{ maxWidth: '820px', margin: '0 auto' }">
      <!-- Header -->
      <div class="reveal" :style="{ textAlign: 'center', marginBottom: '4rem' }">
        <div :style="{
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          gap: '1.25rem', marginBottom: '1.25rem',
        }">
          <span :style="{ flex: '0 1 80px', height: '1px', background: 'rgba(221,209,186,0.8)' }" />
          <span :style="{
            fontFamily: 'var(--font-ui-alt)', fontStyle: 'italic',
            fontSize: '0.85rem', color: 'var(--color-terracotta-500)',
          }">04</span>
          <span :style="{ flex: '0 1 80px', height: '1px', background: 'rgba(221,209,186,0.8)' }" />
        </div>
        <p :style="{
          fontFamily: 'var(--font-ui)', fontSize: '0.7rem', fontWeight: 500,
          textTransform: 'uppercase', letterSpacing: '0.28em',
          color: 'var(--color-terracotta-500)', margin: '0 0 1.25rem',
        }">Por qu&eacute; funciona</p>
        <h2 :style="{
          fontFamily: 'var(--font-display)', fontWeight: 400,
          fontSize: 'clamp(2rem, 4vw, 3rem)', lineHeight: 1.05,
          letterSpacing: '-0.022em', margin: 0, color: 'var(--color-brown-900)',
        }">
          Siete razones para
          <span :style="{ fontStyle: 'italic', color: 'var(--color-terracotta-500)' }">dejar de dudar</span>.
        </h2>
      </div>

      <!-- Scroll-driven accordion -->
      <div>
        <div
          v-for="(arg, i) in args"
          :key="arg.n"
          :ref="el => setItemRef(el, i)"
          :style="{
            borderTop: '1px solid rgba(221,209,186,0.8)',
            borderBottom: i === args.length - 1 ? '1px solid rgba(221,209,186,0.8)' : 'none',
            position: 'relative',
            transition: 'opacity 0.5s ease',
            opacity: active === i ? 1 : 0.3,
          }"
        >
          <!-- Active left accent -->
          <div :style="{
            position: 'absolute', left: 0, top: 0, bottom: 0,
            width: '3px', borderRadius: '2px',
            background: 'var(--color-terracotta-500)',
            opacity: active === i ? 1 : 0,
            transition: 'opacity 0.35s ease',
          }" />

          <!-- Header row -->
          <div :style="{
            display: 'flex', alignItems: 'center',
            gap: '1.25rem', padding: '1.5rem 0 1.5rem 0.75rem',
          }">
            <!-- Icon -->
            <ChromaImage
              :src="arg.icon"
              :alt="arg.t"
              :threshold="40"
              :feather="20"
              class="arg-icon"
              :style="{
                width: '72px',
                height: '72px',
                objectFit: 'contain',
                flexShrink: 0,
                transition: 'opacity 0.3s ease',
              }"
            />

            <!-- Number -->
            <span :style="{
              fontFamily: 'var(--font-display)', fontStyle: 'italic',
              fontSize: '1.8rem', lineHeight: 1,
              color: active === i ? 'var(--color-terracotta-500)' : 'var(--color-brown-200)',
              transition: 'color 0.3s ease',
              width: '2.25rem', flexShrink: 0, textAlign: 'right',
            }">{{ arg.n }}</span>

            <!-- Title + sub -->
            <div :style="{ flex: 1, minWidth: 0 }">
              <h3 :style="{
                fontFamily: 'var(--font-display)',
                fontSize: 'clamp(1.15rem, 2vw, 1.4rem)', fontWeight: 400,
                letterSpacing: '-0.01em', color: 'var(--color-brown-900)',
                margin: 0, lineHeight: 1.2,
              }">{{ arg.t }}</h3>
              <p :style="{
                fontFamily: 'var(--font-body-alt)', fontStyle: 'italic',
                fontSize: '0.88rem',
                color: active === i ? 'var(--color-terracotta-500)' : 'var(--color-brown-400)',
                margin: '0.2rem 0 0', transition: 'color 0.3s ease',
              }">{{ arg.sub }}</p>
            </div>
          </div>

          <!-- Expandable body -->
          <div :style="{
            display: 'grid',
            gridTemplateRows: active === i ? '1fr' : '0fr',
            opacity: active === i ? 1 : 0,
            transition: 'grid-template-rows 0.5s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.4s ease',
          }">
            <div :style="{ overflow: 'hidden' }">
              <p class="arg-body" :style="{
                fontFamily: 'var(--font-body)', fontSize: '0.95rem',
                lineHeight: 1.65, color: 'var(--color-brown-400)',
                margin: '0 0 1.75rem',
                paddingLeft: 'calc(72px + 2.25rem + 1.25rem * 2 + 0.75rem)',
                maxWidth: '52ch',
              }">{{ arg.body }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
@media (max-width: 640px) {
  .arg-icon {
    width: 48px !important;
    height: 48px !important;
  }
  .arg-body {
    padding-left: 0.75rem !important;
  }
}
</style>
