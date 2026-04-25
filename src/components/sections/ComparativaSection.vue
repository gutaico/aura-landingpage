<script setup>
const rows = [
  { d: 'KPI principal',     a: 'Leads / impresiones',           b: 'Pacientes que pagaron' },
  { d: 'Especialización',   a: 'Cualquier industria',           b: 'Solo estética, wellness y salud' },
  { d: 'Creatividad',       a: 'Templates de Canva',            b: 'Producción propia con equipo dedicado' },
  { d: 'Respuesta al lead', a: 'Tú la haces (o no)',            b: 'Agente IA en <30s · 24/7' },
  { d: 'Panel de datos',    a: 'Informe PDF mensual',           b: 'Dashboard en tiempo real — tú tienes el control' },
  { d: 'CRM',               a: 'Pagas aparte',                  b: 'Incluido, integrado al agente' },
  { d: 'Retención',         a: 'No entra en el alcance',        b: 'Cumpleaños, aniversarios, retoques' },
  { d: 'Garantía',          a: 'Contrato con letras chicas',    b: '30 días o devolvemos todo' },
  { d: 'Tiempo al aire',    a: '30 a 60 días de "setup"',       b: '7 días. Punto.' },
]
</script>

<template>
  <section
    id="comparativa"
    class="aura-section-pad"
    :style="{
      background: 'var(--color-cream-50)',
      padding: 'clamp(5rem, 9vw, 9rem) 2.5rem',
      borderTop: '1px solid rgba(221,209,186,0.8)',
      position: 'relative',
      overflow: 'hidden',
    }"
  >
    <div :style="{ maxWidth: '1200px', margin: '0 auto' }">
      <!-- Section header -->
      <div class="reveal" :style="{ textAlign: 'center', marginBottom: '4rem' }">
        <p :style="{
          fontFamily: 'var(--font-ui)',
          fontSize: '0.7rem',
          fontWeight: 500,
          textTransform: 'uppercase',
          letterSpacing: '0.28em',
          color: 'var(--color-terracotta-500)',
          margin: '0 0 1.25rem',
        }">
          &sect; V &middot; Comparativa
        </p>
        <h2 :style="{
          fontFamily: 'var(--font-display)',
          fontWeight: 400,
          fontSize: 'clamp(2rem, 4vw, 3rem)',
          lineHeight: 1.05,
          letterSpacing: '-0.022em',
          margin: '0 auto',
          color: 'var(--color-brown-900)',
          maxWidth: '24ch',
        }">
          No es lo mismo<br />
          <span :style="{ fontStyle: 'italic', color: 'var(--color-terracotta-500)' }">tener agencia</span>
          que tener<br />sistema.
        </h2>
      </div>

      <!-- Comparison table -->
      <div class="reveal" :style="{ position: 'relative', maxWidth: '960px', margin: '0 auto' }">

        <!-- Scroll wrapper for mobile -->
        <div class="aura-compare-scroll">
        <!-- Table container -->
        <div class="aura-compare-wrap" :style="{
          borderRadius: '20px',
          border: '1px solid rgba(221,209,186,0.8)',
          overflow: 'hidden',
          boxShadow: '0 16px 48px rgba(74,52,40,0.08)',
          background: 'white',
        }">
          <!-- Header row -->
          <div
            class="aura-compare"
            :style="{
              display: 'grid',
              gridTemplateColumns: '1.1fr 1fr 1.2fr',
            }"
          >
            <!-- Empty first column header -->
            <div :style="{
              padding: '1.35rem 1.5rem',
              background: 'white',
              borderBottom: '1px solid rgba(221,209,186,0.6)',
            }" />

            <!-- "Las otras" column header -->
            <div :style="{
              padding: '1.35rem 1.5rem',
              background: 'var(--color-cream-100)',
              borderBottom: '1px solid rgba(221,209,186,0.6)',
            }">
              <p :style="{
                fontFamily: 'var(--font-ui-alt)',
                fontStyle: 'italic',
                fontSize: '0.7rem',
                color: 'var(--color-brown-300)',
                margin: '0 0 0.15rem',
              }">Las otras</p>
              <p :style="{
                fontFamily: 'var(--font-display)',
                fontSize: '1.05rem',
                fontWeight: 400,
                color: 'var(--color-brown-500)',
                margin: 0,
                letterSpacing: '-0.01em',
              }">Agencia tradicional</p>
            </div>

            <!-- "Nosotros" column header -->
            <div :style="{
              padding: '1.35rem 1.5rem',
              background: 'var(--color-brown-900)',
              borderBottom: '1px solid rgba(212,154,120,0.2)',
            }">
              <p :style="{
                fontFamily: 'var(--font-ui-alt)',
                fontStyle: 'italic',
                fontSize: '0.7rem',
                color: 'var(--color-terracotta-300)',
                margin: '0 0 0.15rem',
              }">Nosotros</p>
              <p :style="{
                fontFamily: 'var(--font-display)',
                fontSize: '1.05rem',
                fontWeight: 400,
                color: 'var(--color-cream-50)',
                margin: 0,
                letterSpacing: '-0.01em',
                display: 'flex',
                alignItems: 'center',
                gap: '0.45rem',
              }">
                Aura
                <span :style="{
                  fontSize: '0.65rem',
                  color: 'var(--color-terracotta-300)',
                  animation: 'auraStar 3s ease-in-out infinite',
                }">&starf;</span>
              </p>
            </div>
          </div>

          <!-- Data rows -->
          <div
            v-for="(row, i) in rows"
            :key="i"
            class="aura-compare compare-row"
            :style="{
              display: 'grid',
              gridTemplateColumns: '1.1fr 1fr 1.2fr',
            }"
          >
            <!-- Attribute name -->
            <div class="compare-attr" :style="{
              padding: '1rem 1.5rem',
              display: 'flex',
              alignItems: 'center',
              gap: '0.65rem',
              borderBottom: i < rows.length - 1 ? '1px solid rgba(221,209,186,0.5)' : 'none',
            }">
              <span class="compare-num" :style="{
                fontFamily: 'var(--font-ui-alt)',
                fontStyle: 'italic',
                fontSize: '0.72rem',
                color: 'var(--color-brown-300)',
                opacity: 0.5,
                width: '1.5rem',
                textAlign: 'right',
                flexShrink: 0,
              }">0{{ i + 1 }}</span>
              <span :style="{
                fontFamily: 'var(--font-ui)',
                fontSize: '0.82rem',
                fontWeight: 500,
                color: 'var(--color-brown-700)',
              }">{{ row.d }}</span>
            </div>

            <!-- Traditional agency value -->
            <div :style="{
              padding: '1rem 1.5rem',
              background: i % 2 === 0 ? 'var(--color-cream-100)' : 'rgba(234,225,208,0.35)',
              display: 'flex',
              alignItems: 'center',
              gap: '0.55rem',
              borderBottom: i < rows.length - 1 ? '1px solid rgba(221,209,186,0.35)' : 'none',
            }">
              <svg width="13" height="13" fill="none" stroke="var(--color-brown-300)" stroke-width="1.75" viewBox="0 0 24 24" :style="{ flexShrink: 0, opacity: 0.4 }">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
              </svg>
              <span :style="{
                fontFamily: 'var(--font-body)',
                fontSize: '0.82rem',
                color: 'var(--color-brown-300)',
                fontStyle: 'italic',
                textDecoration: 'line-through',
                lineHeight: 1.4,
              }">{{ row.a }}</span>
            </div>

            <!-- Aura value -->
            <div :style="{
              padding: '1rem 1.5rem',
              background: 'var(--color-brown-900)',
              display: 'flex',
              alignItems: 'center',
              gap: '0.55rem',
              borderBottom: i < rows.length - 1 ? '1px solid rgba(212,154,120,0.12)' : 'none',
            }">
              <svg width="13" height="13" fill="none" stroke="var(--color-terracotta-300)" stroke-width="1.75" viewBox="0 0 24 24" :style="{ flexShrink: 0 }">
                <path stroke-linecap="round" stroke-linejoin="round" d="M5 12l5 5L20 7" />
              </svg>
              <span :style="{
                fontFamily: 'var(--font-body)',
                fontSize: '0.82rem',
                color: 'var(--color-cream-50)',
                fontWeight: 500,
                lineHeight: 1.4,
              }">{{ row.b }}</span>
            </div>
          </div>
        </div>
        </div><!-- /aura-compare-scroll -->
      </div>
    </div>
  </section>
</template>

