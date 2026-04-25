<script setup>
const rows = [
  { d: 'Respuesta al lead', a: '2-24 hrs (si responden)', b: '<30 segundos, 24/7' },
  { d: 'Seguimiento', a: 'Manual (si alguien se acuerda)', b: 'Automático: 2h, 24h, 7d' },
  { d: 'Reagendamiento', a: 'Tú lo haces', b: 'El agente lo resuelve solo' },
  { d: 'Retención', a: 'No incluida', b: 'Recuerda retoques, cumpleaños, aniversarios' },
  { d: 'Personalización', a: 'Mensajes genéricos', b: 'Sabe nombre, historial, preferencias' },
  { d: 'Know-how comercial', a: 'Manual de usuario PDF', b: 'Estrategia Aura: objeciones, upsell, timing' },
  { d: 'Configuración', a: '30-60 días', b: '3 días hábiles' },
  { d: 'Garantía', a: 'Contrato anual forzoso', b: '30 días o devolvemos todo' },
]
</script>

<template>
  <section class="aura-section-pad" :style="{
    background: 'var(--color-cream-50)',
    padding: 'clamp(5rem, 9vw, 9rem) 2.5rem',
    position: 'relative',
    overflow: 'hidden',
  }">
    <div :style="{ maxWidth: '1200px', margin: '0 auto' }">

      <!-- Section number label -->
      <div class="reveal" :style="{
        display: 'flex',
        alignItems: 'center',
        gap: '1rem',
        justifyContent: 'center',
        marginBottom: '1.5rem',
      }">
        <span :style="{
          width: '2rem',
          height: '1px',
          background: 'rgba(221,209,186,0.8)',
        }" />
        <span :style="{
          fontFamily: 'var(--font-ui)',
          fontSize: '0.68rem',
          fontWeight: 500,
          textTransform: 'uppercase',
          letterSpacing: '0.25em',
          color: 'var(--color-terracotta-500)',
        }">02 · El problema real</span>
        <span :style="{
          width: '2rem',
          height: '1px',
          background: 'rgba(221,209,186,0.8)',
        }" />
      </div>

      <!-- Headline -->
      <div class="reveal" :style="{ textAlign: 'center', marginBottom: '2.5rem' }">
        <h2 :style="{
          fontFamily: 'var(--font-display)',
          fontWeight: 400,
          fontSize: 'clamp(1.8rem, 3.8vw, 2.8rem)',
          lineHeight: 1.1,
          letterSpacing: '-0.022em',
          margin: '0 auto',
          color: 'var(--color-brown-900)',
          maxWidth: '30ch',
        }">
          Un agente sin <span :style="{ fontStyle: 'italic', color: 'var(--color-terracotta-500)' }">proceso comercial</span><br />es solo un gasto más.
        </h2>
      </div>

      <!-- ═══ Editorial narrative — single flowing block ═══ -->
      <div class="reveal comp-narrative" :style="{
        maxWidth: '640px',
        margin: '0 auto 4.5rem',
        position: 'relative',
        paddingLeft: '2rem',
      }">
        <!-- Vertical accent line -->
        <div aria-hidden="true" :style="{
          position: 'absolute',
          left: 0,
          top: '0.25rem',
          bottom: '0.25rem',
          width: '3px',
          borderRadius: '2px',
          background: 'linear-gradient(180deg, var(--color-terracotta-500) 0%, rgba(221,209,186,0.3) 100%)',
        }" />

        <p :style="{
          fontFamily: 'var(--font-body)',
          fontSize: 'clamp(1.02rem, 1.3vw, 1.12rem)',
          lineHeight: 1.7,
          color: 'var(--color-brown-600)',
          margin: '0 0 1.5rem',
        }">
          La mayoría de proveedores te dan acceso a una plataforma. Tú escribes los mensajes, armas los flujos, decides cuándo dar seguimiento y qué decir ante cada objeción. <span :style="{ fontFamily: 'var(--font-body-alt)', fontStyle: 'italic', color: 'var(--color-brown-400)' }">En la práctica, si no tienes un proceso comercial probado, el agente replica tus mismos errores&mdash;más rápido.</span>
        </p>

        <p :style="{
          fontFamily: 'var(--font-body)',
          fontSize: 'clamp(1.02rem, 1.3vw, 1.12rem)',
          lineHeight: 1.7,
          color: 'var(--color-brown-900)',
          margin: '0 0 1.5rem',
          fontWeight: 500,
        }">
          Nosotros no entregamos herramientas. Configuramos, entrenamos y operamos tu agente con la estrategia comercial que ya ha generado <span :style="{ color: 'var(--color-terracotta-500)', fontWeight: 600 }">+2,000 citas</span> para clínicas.
        </p>

        <p :style="{
          fontFamily: 'var(--font-body-alt)',
          fontStyle: 'italic',
          fontSize: '0.95rem',
          lineHeight: 1.6,
          color: 'var(--color-brown-400)',
          margin: 0,
        }">
          Sabe responder objeciones, hacer upsell, y cuándo insistir sin ser invasivo. Eso no viene en un manual de usuario.
        </p>
      </div>

      <!-- Comparison table -->
      <div class="reveal" :style="{ position: 'relative', maxWidth: '960px', margin: '0 auto' }">
        <div :style="{
          borderRadius: '20px',
          border: '1px solid rgba(221,209,186,0.8)',
          overflow: 'hidden',
          boxShadow: '0 16px 48px rgba(74,52,40,0.08)',
          background: 'white',
        }">

          <!-- Header row -->
          <div class="aura-compare-agente" :style="{
            display: 'grid',
            gridTemplateColumns: '1.1fr 1fr 1.2fr',
          }">
            <!-- Empty first column header -->
            <div :style="{
              padding: '1.35rem 1.5rem',
              background: 'white',
              borderBottom: '1px solid rgba(221,209,186,0.6)',
            }" />

            <!-- Others column header -->
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
              }">Los otros</p>
              <p :style="{
                fontFamily: 'var(--font-display)',
                fontSize: '1.05rem',
                fontWeight: 400,
                color: 'var(--color-brown-500)',
                margin: 0,
                letterSpacing: '-0.01em',
              }">Otros agentes</p>
            </div>

            <!-- Aura column header -->
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
                Agente Aura
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
            class="aura-compare-agente"
            :style="{
              display: 'grid',
              gridTemplateColumns: '1.1fr 1fr 1.2fr',
            }"
          >
            <!-- Feature name -->
            <div :style="{
              padding: '1rem 1.5rem',
              display: 'flex',
              alignItems: 'center',
              gap: '0.65rem',
              borderBottom: i < rows.length - 1 ? '1px solid rgba(221,209,186,0.5)' : 'none',
            }">
              <span :style="{
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

            <!-- Others value -->
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
      </div>

      <!-- Bottom quote -->
      <div class="reveal" :style="{
        textAlign: 'center',
        marginTop: '3.5rem',
        maxWidth: '52ch',
        marginLeft: 'auto',
        marginRight: 'auto',
      }">
        <p :style="{
          fontFamily: 'var(--font-body-alt)',
          fontStyle: 'italic',
          fontSize: 'clamp(1rem, 1.3vw, 1.15rem)',
          lineHeight: 1.55,
          color: 'var(--color-brown-400)',
          margin: 0,
        }">
          &ldquo;No buscábamos otro chatbot. Buscábamos a alguien que supiera vender por nosotros.&rdquo;
        </p>
      </div>
    </div>
  </section>
</template>

<style scoped>
@media (max-width: 720px) {
  .aura-compare-agente {
    grid-template-columns: 1fr !important;
  }
  .aura-compare-agente > div {
    padding: 0.85rem 1.25rem !important;
  }
}
@media (max-width: 640px) {
  .comp-narrative {
    padding-left: 1.25rem !important;
  }
}
</style>
