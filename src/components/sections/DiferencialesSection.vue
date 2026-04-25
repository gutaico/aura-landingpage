<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import ChromaImage from '../ChromaImage.vue'

const items = [
  { n: '01', t: 'Garantía de 30 días', sub: 'Si no cumplimos, devolvemos.', body: 'Acordamos un mínimo de prospectos calificados en la primera semana. Si en 30 días no llegamos — y cumpliste tu parte — devolvemos todo.', icon: '/img/iconos/garantia.webp' },
  { n: '02', t: 'Dashboard de resultados', sub: 'Todo en tiempo real. Tú tienes el control.', body: 'Plataforma propia donde ves cada anuncio, conversación, cita y venta conectados. Sin esperar reportes — consultas lo que quieras, cuando quieras.', icon: '/img/iconos/dashboard.webp' },
  { n: '03', t: 'CRM incluido', sub: 'Sin cuota extra.', body: 'Base de datos con historial, notas, segmentos y pipeline. Integrado al agente y a las campañas. Sin pagar Hubspot ni cosas raras.', icon: '/img/iconos/crm.webp' },
  { n: '04', t: 'Campaña en 7 días', sub: 'Al aire en una semana.', body: 'Día 1 onboarding. Día 3 creativos aprobados. Día 7 anuncios corriendo. Sin meses de "setup" que otras agencias usan de excusa.', icon: '/img/iconos/anuncios.webp' },
  { n: '05', t: 'Nutrición y retención', sub: 'Nadie más lo incluye.', body: 'Cumpleaños, aniversarios de cliente, recordatorios de retoque, fechas especiales. El paciente regresa solo, sin que lo persigas.', icon: '/img/iconos/conversaciones.webp' },
  { n: '06', t: 'Atraer, persuadir, convertir', sub: 'Una sola agencia, un solo KPI.', body: 'No te mandamos leads — te mandamos pacientes que pagaron. Medimos del primer impression al último ticket cobrado.', icon: '/img/iconos/datos.webp' },
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
    id="diferenciales"
    class="aura-section-pad"
    :style="{
      background: 'var(--color-cream-50)',
      padding: 'clamp(5rem, 8vw, 9rem) 2.5rem',
      borderTop: '1px solid rgba(221,209,186,0.8)',
    }"
  >
    <div :style="{ maxWidth: '820px', margin: '0 auto' }">
      <!-- Header -->
      <div class="reveal" :style="{
        textAlign: 'center',
        marginBottom: '4rem',
      }">
        <p :style="{
          fontFamily: 'var(--font-ui)',
          fontSize: '0.7rem',
          fontWeight: 500,
          textTransform: 'uppercase',
          letterSpacing: '0.28em',
          color: 'var(--color-terracotta-500)',
          margin: '0 0 1.25rem',
        }">
          &sect; III &middot; Lo que nos hace diferentes
        </p>
        <h2 :style="{
          fontFamily: 'var(--font-display)',
          fontWeight: 400,
          fontSize: 'clamp(2rem, 4vw, 3rem)',
          lineHeight: 1.05,
          letterSpacing: '-0.022em',
          margin: '0 0 1.25rem',
          color: 'var(--color-brown-900)',
        }">
          Por qu&eacute; vas a
          <span :style="{ fontStyle: 'italic', color: 'var(--color-terracotta-500)' }">amar</span>
          trabajar con Aura.
        </h2>
        <p :style="{
          fontFamily: 'var(--font-body-alt)',
          fontStyle: 'italic',
          fontSize: '1.05rem',
          color: 'var(--color-brown-400)',
          margin: 0,
          maxWidth: '50ch',
          marginInline: 'auto',
        }">
          Preg&uacute;ntale a las otras agencias por estas seis. Cuando no las tengan, regresa.
        </p>
      </div>

      <!-- Scroll-driven accordion -->
      <div>
        <div
          v-for="(it, i) in items"
          :key="it.n"
          :ref="el => setItemRef(el, i)"
          :style="{
            borderTop: '1px solid rgba(221,209,186,0.8)',
            borderBottom: i === items.length - 1 ? '1px solid rgba(221,209,186,0.8)' : 'none',
            position: 'relative',
            transition: 'opacity 0.5s ease',
            opacity: active === i ? 1 : 0.3,
          }"
        >
          <!-- Active left accent -->
          <div :style="{
            position: 'absolute',
            left: 0,
            top: 0,
            bottom: 0,
            width: '3px',
            borderRadius: '2px',
            background: 'var(--color-terracotta-500)',
            opacity: active === i ? 1 : 0,
            transition: 'opacity 0.35s ease',
          }" />

          <!-- Header row -->
          <div :style="{
            display: 'flex',
            alignItems: 'center',
            gap: '1.25rem',
            padding: '1.5rem 0 1.5rem 0.75rem',
          }">
            <!-- Icon -->
            <ChromaImage
              :src="it.icon"
              :alt="it.t"
              :threshold="40"
              :feather="20"
              class="dif-icon"
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
              fontFamily: 'var(--font-display)',
              fontStyle: 'italic',
              fontSize: '1.8rem',
              lineHeight: 1,
              color: active === i ? 'var(--color-terracotta-500)' : 'var(--color-brown-200)',
              transition: 'color 0.3s ease',
              width: '2.25rem',
              flexShrink: 0,
              textAlign: 'right',
            }">{{ it.n }}</span>

            <!-- Title + sub -->
            <div :style="{ flex: 1, minWidth: 0 }">
              <h3 :style="{
                fontFamily: 'var(--font-display)',
                fontSize: 'clamp(1.15rem, 2vw, 1.4rem)',
                fontWeight: 400,
                letterSpacing: '-0.01em',
                color: 'var(--color-brown-900)',
                margin: 0,
                lineHeight: 1.2,
              }">{{ it.t }}</h3>
              <p :style="{
                fontFamily: 'var(--font-body-alt)',
                fontStyle: 'italic',
                fontSize: '0.88rem',
                color: active === i ? 'var(--color-terracotta-500)' : 'var(--color-brown-400)',
                margin: '0.2rem 0 0',
                transition: 'color 0.3s ease',
              }">{{ it.sub }}</p>
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
              <p class="dif-body" :style="{
                fontFamily: 'var(--font-body)',
                fontSize: '0.95rem',
                lineHeight: 1.65,
                color: 'var(--color-brown-400)',
                margin: '0 0 1.75rem',
                paddingLeft: 'calc(72px + 2.25rem + 1.25rem * 2 + 0.75rem)',
                maxWidth: '52ch',
              }">{{ it.body }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
@media (max-width: 640px) {
  .dif-icon {
    width: 48px !important;
    height: 48px !important;
  }
  .dif-body {
    padding-left: 0.75rem !important;
  }
}
</style>
