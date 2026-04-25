<script setup>
import { ref } from 'vue'

const active = ref(0)

const pillars = [
  {
    k: 'Atraer',
    t: 'Anuncios que sí detienen el scroll',
    body: 'Hooks probados en tu sector. Creatividad producida por nuestro equipo — no templates. Testeo A/B constante sobre el dolor real del paciente, no sobre el "tratamiento".',
    points: [
      'Hooks con 0.8s de atención',
      'Producción profesional incluida',
      'A/B testing semanal',
      'Ángulos basados en data, no en intuición',
    ],
  },
  {
    k: 'Persuadir',
    t: 'Conversaciones que cierran',
    body: 'El agente responde en 30 segundos, 24/7. Califica, agenda, confirma. Si el paciente duda, nutre con contenido. Si no contesta, reactiva.',
    points: [
      'WhatsApp + Instagram + Facebook',
      'Script entrenado por sector',
      'Agenda directo en tu calendario',
      'Reactivación automática de fríos',
    ],
  },
  {
    k: 'Convertir',
    t: 'Agentes de IA que cierran, sin trucos',
    body: 'Una vez en el canal, nuestros agentes autónomos llevan al prospecto desde el saludo hasta la venta. Sin guiones robóticos, sin redirigir a humanos. Recuperan conversaciones perdidas y reconfirman cada cita.',
    points: [
      'Agente IA autónomo del saludo a la venta',
      'Recuperación activa de conversaciones perdidas',
      'Reconfirmación 24h y 2h antes — cero no-shows',
      'Tono y voz entrenados con tu marca',
    ],
  },
  {
    k: 'Retener',
    t: 'El agente que nunca olvida un paciente',
    body: 'El mismo agente IA que vendió, ahora retiene. Cumpleaños, aniversario del primer tratamiento, fechas clave, retoques pendientes. El paciente vuelve solo, sin que nadie levante el teléfono.',
    points: [
      'Agente IA con memoria de cada paciente',
      'Mensajes en cumpleaños, aniversarios y retoques',
      'Campañas de fechas especiales automatizadas',
      'Plan de embajadoras + referidos gestionado por IA',
    ],
  },
]
</script>

<template>
  <section
    id="metodologia"
    class="grain grain-05"
    :style="{
      background: 'var(--color-brown-900)',
      color: 'var(--color-cream-50)',
      padding: 'clamp(5rem, 9vw, 10rem) 2.5rem',
      position: 'relative',
      overflow: 'hidden',
    }"
  >
    <!-- Decorative radial gradient -->
    <div :style="{
      position: 'absolute',
      top: '-20%',
      left: '-10%',
      width: '50%',
      height: '70%',
      background: 'radial-gradient(ellipse at center, rgba(145,65,38,0.25), transparent 60%)',
      pointerEvents: 'none',
    }"></div>

    <div :style="{ maxWidth: '1200px', margin: '0 auto', position: 'relative' }">
      <!-- Header -->
      <div class="reveal">
        <div
          class="aura-hero-grid"
          :style="{
            display: 'grid',
            gridTemplateColumns: '1fr 1.3fr',
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
              color: 'var(--color-terracotta-300)',
              margin: '0 0 1.25rem',
            }">
              &sect; IV &middot; Metodolog&iacute;a
            </p>
            <h2 :style="{
              fontFamily: 'var(--font-display)',
              fontWeight: 400,
              fontSize: 'clamp(2rem, 4vw, 3rem)',
              lineHeight: 1.05,
              letterSpacing: '-0.022em',
              margin: 0,
              color: 'var(--color-cream-50)',
            }">
              Cuatro pilares,<br />
              <span :style="{ fontStyle: 'italic', color: 'var(--color-terracotta-300)' }">un solo KPI</span>:<br />
              pacientes que pagaron.
            </h2>
          </div>
          <p :style="{
            fontFamily: 'var(--font-body-alt)',
            fontStyle: 'italic',
            fontSize: 'clamp(1.05rem, 1.4vw, 1.2rem)',
            lineHeight: 1.55,
            color: 'rgba(234,225,208,0.8)',
            margin: 0,
            maxWidth: '52ch',
          }">
            La mayor&iacute;a de las agencias te venden solo &ldquo;atraer&rdquo;. Nosotros
            vendemos el ciclo completo &mdash; porque un lead sin sistema es dinero tirado.
          </p>
        </div>
      </div>

      <!-- Tab switcher -->
      <div :style="{
        display: 'flex',
        gap: '0',
        borderBottom: '1px solid rgba(212,154,120,0.25)',
        marginBottom: '3rem',
        overflowX: 'auto',
      }">
        <button
          v-for="(p, i) in pillars"
          :key="p.k"
          @click="active = i"
          :style="{
            padding: '1.25rem 2rem',
            background: 'transparent',
            border: 'none',
            borderBottom: '2px solid',
            borderColor: active === i ? 'var(--color-terracotta-300)' : 'transparent',
            color: active === i ? 'var(--color-cream-50)' : 'rgba(234,225,208,0.5)',
            fontFamily: 'var(--font-display)',
            fontWeight: 400,
            fontSize: 'clamp(1.1rem, 1.6vw, 1.4rem)',
            cursor: 'pointer',
            transition: 'all .3s',
            display: 'flex',
            alignItems: 'baseline',
            gap: '0.6rem',
            whiteSpace: 'nowrap',
            marginBottom: '-1px',
          }"
        >
          <span :style="{
            fontFamily: 'var(--font-ui-alt)',
            fontStyle: 'italic',
            fontSize: '0.85rem',
            opacity: 0.7,
          }">0{{ i + 1 }}</span>
          <span :style="{ fontStyle: active === i ? 'italic' : 'normal' }">{{ p.k }}</span>
        </button>
      </div>

      <!-- Content — split into text + bullet points -->
      <div
        class="aura-hero-grid"
        :style="{
          display: 'grid',
          gridTemplateColumns: '1.3fr 1fr',
          gap: '4rem',
          minHeight: '280px',
        }"
      >
        <!-- Left: title + body -->
        <div :key="active" :style="{ animation: 'auraFadeSlide 500ms cubic-bezier(0.16,1,0.3,1)' }">
          <h3 :style="{
            fontFamily: 'var(--font-display)',
            fontWeight: 400,
            fontSize: 'clamp(1.8rem, 3vw, 2.4rem)',
            lineHeight: 1.1,
            letterSpacing: '-0.018em',
            margin: '0 0 1.25rem',
            color: 'var(--color-cream-50)',
          }">
            {{ pillars[active].t }}.
          </h3>
          <p :style="{
            fontFamily: 'var(--font-body)',
            fontSize: '1.05rem',
            lineHeight: 1.65,
            color: 'rgba(234,225,208,0.85)',
            margin: 0,
            maxWidth: '48ch',
          }">{{ pillars[active].body }}</p>
        </div>

        <!-- Right: bullet points -->
        <div :key="'pts-' + active" :style="{ animation: 'auraFadeSlide 500ms 100ms cubic-bezier(0.16,1,0.3,1) both' }">
          <ul :style="{
            listStyle: 'none',
            padding: 0,
            margin: 0,
            display: 'flex',
            flexDirection: 'column',
            gap: '0.9rem',
          }">
            <li
              v-for="point in pillars[active].points"
              :key="point"
              :style="{
                display: 'flex',
                alignItems: 'flex-start',
                gap: '0.75rem',
                fontFamily: 'var(--font-body)',
                fontSize: '0.95rem',
                color: 'rgba(234,225,208,0.78)',
                lineHeight: 1.5,
                paddingBottom: '0.9rem',
                borderBottom: '1px solid rgba(212,154,120,0.15)',
              }"
            >
              <svg
                width="16"
                height="16"
                fill="none"
                stroke="var(--color-terracotta-300)"
                stroke-width="1.75"
                viewBox="0 0 24 24"
                :style="{ flexShrink: 0, marginTop: '0.2rem' }"
              >
                <path stroke-linecap="round" stroke-linejoin="round" d="M5 12l5 5L20 7" />
              </svg>
              {{ point }}
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>
</template>
