<script setup>
const days = [
  { d: 'Día 1–2', t: 'Kickoff + Diagnóstico', body: 'Llamada de 90 min. Definimos ICP, mensajes clave. Auditamos tu cuenta, funnel y competencia en tu zona.' },
  { d: 'Día 2–3', t: 'Estrategia', body: 'Entregamos el plan: ángulos creativos, budget, targets, KPIs semanales.' },
  { d: 'Día 4', t: 'Creativos*', body: 'Seleccionamos los creativos para lanzar tus campañas. Tú apruebas todo antes de publicar.' },
  { d: 'Día 5', t: 'Setup técnico', body: 'Dashboard de resultados conectado, CRM poblado, agente entrenado con tu voz y servicios.' },
  { d: 'Día 6', t: 'QA + Aprobación', body: 'Prueba end-to-end: anuncio → lead → chat → agenda. Tú das el visto bueno.' },
  { d: 'Día 7', t: 'Al aire', body: 'Campañas activas. Primer lead en las próximas 24 horas.' },
]
</script>

<template>
  <section
    id="onboarding"
    class="aura-section-pad"
    :style="{
      background: 'var(--color-cream-100)',
      padding: 'clamp(5rem, 8vw, 9rem) 2.5rem',
    }"
  >
    <div :style="{ maxWidth: '1200px', margin: '0 auto' }">
      <!-- Header -->
      <div class="reveal">
        <div :style="{ textAlign: 'center', marginBottom: '4rem' }">
          <p :style="{
            fontFamily: 'var(--font-ui)',
            fontSize: '0.7rem',
            fontWeight: 500,
            textTransform: 'uppercase',
            letterSpacing: '0.28em',
            color: 'var(--color-terracotta-500)',
            margin: '0 0 1.25rem',
          }">
            &sect; VI &middot; Onboarding
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
            Siete días.
            <span :style="{ fontStyle: 'italic', color: 'var(--color-terracotta-500)' }">Al aire</span>.
          </h2>
          <p :style="{
            fontFamily: 'var(--font-body-alt)',
            fontStyle: 'italic',
            fontSize: '1.05rem',
            color: 'var(--color-brown-400)',
            margin: 0,
            maxWidth: '54ch',
            marginInline: 'auto',
          }">
            No es magia. Es expertise aplicada a tu negocio. Rapidez no significa menos calidad &mdash; significa que ya lo hemos hecho m&aacute;s de 40 veces.
          </p>
        </div>
      </div>

      <!-- Timeline grid -->
      <div
        class="aura-onboard"
        :style="{
          display: 'grid',
          gridTemplateColumns: 'repeat(6, 1fr)',
          gap: '0',
          position: 'relative',
        }"
      >
        <!-- Timeline line -->
        <div
          aria-hidden="true"
          class="aura-onboard-line"
          :style="{
            position: 'absolute',
            top: 'calc(2rem + 14px)',
            left: '7%',
            right: '7%',
            height: '2px',
            background: 'var(--color-cream-300)',
            zIndex: 0,
          }"
        ></div>

        <!-- Day cards -->
        <div
          v-for="(day, i) in days"
          :key="i"
          class="reveal"
          :class="`reveal-delay-${i + 1}`"
          :style="{
            padding: '2rem 0.75rem',
            textAlign: 'center',
            position: 'relative',
            zIndex: 1,
          }"
        >
          <!-- Numbered circle -->
          <div :style="{
            width: '30px',
            height: '30px',
            borderRadius: '50%',
            background: 'var(--color-terracotta-500)',
            color: 'white',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontFamily: 'var(--font-ui)',
            fontSize: '0.78rem',
            fontWeight: 600,
            margin: '0 auto 1.25rem',
            border: '4px solid var(--color-cream-100)',
          }">
            {{ i + 1 }}
          </div>

          <!-- Day label -->
          <p :style="{
            fontFamily: 'var(--font-ui-alt)',
            fontStyle: 'italic',
            fontSize: '0.78rem',
            color: 'var(--color-terracotta-500)',
            margin: '0 0 0.35rem',
          }">
            {{ day.d }}
          </p>

          <!-- Day title -->
          <h3 :style="{
            fontFamily: 'var(--font-display)',
            fontWeight: 500,
            fontSize: '1.05rem',
            color: 'var(--color-brown-900)',
            margin: '0 0 0.75rem',
            letterSpacing: '-0.005em',
          }">
            {{ day.t }}
          </h3>

          <!-- Day body -->
          <p class="onboard-body" :style="{
            fontFamily: 'var(--font-body)',
            fontSize: '0.82rem',
            lineHeight: 1.5,
            color: 'var(--color-brown-400)',
            margin: 0,
            maxWidth: '18ch',
            marginInline: 'auto',
          }">
            {{ day.body }}
          </p>
        </div>
      </div>

      <!-- Footnote -->
      <div class="reveal" :style="{
        marginTop: '2rem',
        textAlign: 'center',
      }">
        <p :style="{
          fontFamily: 'var(--font-body-alt)',
          fontStyle: 'italic',
          fontSize: '0.82rem',
          color: 'var(--color-brown-400)',
          margin: 0,
        }">
          *Tambi&eacute;n podemos producir los creativos por ti &mdash; eso suma una semana extra al lanzamiento.
        </p>
      </div>
    </div>
  </section>
</template>

<style scoped>
@media (max-width: 500px) {
  .onboard-body {
    max-width: 100% !important;
    text-align: left !important;
  }
}
</style>
