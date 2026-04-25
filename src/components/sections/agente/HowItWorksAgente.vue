<script setup>
const steps = [
  {
    num: '01',
    time: 'Día 1',
    title: 'Entendemos tu clínica',
    body: 'Mapeamos servicios, precios, objeciones frecuentes, tono de voz y flujo de pacientes. El agente no habla como robot: habla como tu mejor recepcionista.',
    icon: 'users',
  },
  {
    num: '02',
    time: 'Día 2',
    title: 'Configuramos la inteligencia',
    body: 'Programamos respuestas, calificación de leads, lógica de agendamiento y seguimiento. Incluimos el know-how comercial de +40 clínicas.',
    icon: 'brain',
  },
  {
    num: '03',
    time: 'Día 2-3',
    title: 'Pruebas en vivo contigo',
    body: 'Lo probamos juntos. Ajustamos tono, tiempos y escenarios hasta que estés 100% conforme. Nada se lanza sin tu aprobación.',
    icon: 'eye',
  },
  {
    num: '04',
    time: 'Día 3',
    title: 'Encendemos el agente',
    body: 'Conectamos a WhatsApp, activamos campañas y el agente empieza a responder, calificar y agendar. Tú solo ves citas confirmadas.',
    icon: 'zap',
  },
]
</script>

<template>
  <section id="como-funciona" class="aura-section-pad" :style="{
    background: 'var(--color-cream-50)',
    padding: 'clamp(5rem, 9vw, 9rem) 2.5rem',
    borderTop: '1px solid rgba(221,209,186,0.8)',
    position: 'relative',
  }">
    <div :style="{ maxWidth: '1200px', margin: '0 auto' }">

      <!-- Section label -->
      <div class="reveal" :style="{
        display: 'flex',
        alignItems: 'center',
        gap: '1rem',
        justifyContent: 'center',
        marginBottom: '1.5rem',
      }">
        <span :style="{ width: '2rem', height: '1px', background: 'rgba(221,209,186,0.8)' }" />
        <span :style="{
          fontFamily: 'var(--font-ui)',
          fontSize: '0.68rem',
          fontWeight: 500,
          textTransform: 'uppercase',
          letterSpacing: '0.25em',
          color: 'var(--color-terracotta-500)',
        }">03 · Cómo funciona</span>
        <span :style="{ width: '2rem', height: '1px', background: 'rgba(221,209,186,0.8)' }" />
      </div>

      <!-- Headline -->
      <div class="reveal" :style="{ textAlign: 'center', marginBottom: '3.5rem' }">
        <h2 :style="{
          fontFamily: 'var(--font-display)',
          fontWeight: 400,
          fontSize: 'clamp(1.8rem, 3.8vw, 2.8rem)',
          lineHeight: 1.1,
          letterSpacing: '-0.022em',
          margin: '0 auto',
          color: 'var(--color-brown-900)',
          maxWidth: '28ch',
        }">
          De 0 a <span :style="{ fontStyle: 'italic', color: 'var(--color-terracotta-500)' }">olvidarte de los mensajes</span> en 3 días
        </h2>
      </div>

      <!-- Process flow — unified container -->
      <div class="how-flow reveal">
        <template v-for="(step, i) in steps" :key="step.num">
          <!-- Step -->
          <div class="how-step">
            <!-- Number + time chip -->
            <div :style="{
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'flex-start',
              marginBottom: '1.25rem',
            }">
              <span :style="{
                fontFamily: 'var(--font-display)',
                fontSize: '2.4rem',
                fontWeight: 400,
                lineHeight: 1,
                color: 'var(--color-cream-200)',
                letterSpacing: '-0.03em',
              }">{{ step.num }}</span>
              <span :style="{
                fontFamily: 'var(--font-ui)',
                fontSize: '0.6rem',
                fontWeight: 600,
                textTransform: 'uppercase',
                letterSpacing: '0.12em',
                color: 'var(--color-terracotta-500)',
                background: 'var(--color-terracotta-50)',
                padding: '0.25rem 0.55rem',
                borderRadius: '999px',
              }">{{ step.time }}</span>
            </div>

            <!-- Icon -->
            <div :style="{
              width: '40px',
              height: '40px',
              borderRadius: '10px',
              background: 'var(--color-terracotta-50)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              marginBottom: '1rem',
            }">
              <svg v-if="step.icon === 'users'" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--color-terracotta-500)" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">
                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>
              </svg>
              <svg v-else-if="step.icon === 'brain'" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--color-terracotta-500)" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 2a4 4 0 0 1 4 4 4 4 0 0 1-1.18 2.84A5 5 0 0 1 18 13a5 5 0 0 1-2.09 4.07A3.5 3.5 0 0 1 12 22a3.5 3.5 0 0 1-3.91-4.93A5 5 0 0 1 6 13a5 5 0 0 1 3.18-4.16A4 4 0 0 1 8 6a4 4 0 0 1 4-4z"/><path d="M12 2v20"/><path d="M8 6h1"/><path d="M15 6h1"/><path d="M6 13h2"/><path d="M16 13h2"/>
              </svg>
              <svg v-else-if="step.icon === 'eye'" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--color-terracotta-500)" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">
                <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>
              </svg>
              <svg v-else-if="step.icon === 'zap'" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--color-terracotta-500)" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">
                <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
              </svg>
            </div>

            <!-- Title -->
            <h3 :style="{
              fontFamily: 'var(--font-display)',
              fontSize: '1.1rem',
              fontWeight: 400,
              color: 'var(--color-brown-900)',
              margin: '0 0 0.5rem',
              letterSpacing: '-0.01em',
              lineHeight: 1.2,
            }">{{ step.title }}</h3>

            <!-- Body -->
            <p :style="{
              fontFamily: 'var(--font-body)',
              fontSize: '0.82rem',
              lineHeight: 1.55,
              color: 'var(--color-brown-400)',
              margin: 0,
            }">{{ step.body }}</p>
          </div>

          <!-- Arrow separator -->
          <div v-if="i < steps.length - 1" class="how-arrow">
            <span class="how-arrow-line" />
            <span class="how-arrow-icon">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--color-terracotta-400)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M9 6l6 6-6 6" />
              </svg>
            </span>
          </div>
        </template>
      </div>
    </div>
  </section>
</template>

<style scoped>
.how-flow {
  display: flex;
  background: white;
  border-radius: 16px;
  border: 1px solid rgba(221, 209, 186, 0.8);
  overflow: hidden;
}

.how-step {
  flex: 1;
  padding: 2rem 1.75rem;
  min-width: 0;
}

.how-arrow {
  width: 48px;
  flex-shrink: 0;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.how-arrow-line {
  position: absolute;
  top: 12%;
  bottom: 12%;
  left: 50%;
  width: 1px;
  background: var(--color-cream-200);
  transform: translateX(-50%);
}

.how-arrow-icon {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: var(--color-cream-50);
  border: 1px solid var(--color-cream-200);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  z-index: 1;
}

@media (max-width: 900px) {
  .how-flow {
    flex-direction: column;
  }

  .how-step {
    padding: 1.75rem;
  }

  .how-arrow {
    width: 100%;
    height: 48px;
  }

  .how-arrow-line {
    top: 50%;
    bottom: auto;
    left: 12%;
    right: 12%;
    width: auto;
    height: 1px;
    transform: translateY(-50%);
  }

  .how-arrow-icon svg {
    transform: rotate(90deg);
  }
}
</style>
