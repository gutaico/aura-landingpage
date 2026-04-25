<script setup>
import { ref, computed } from 'vue'

const questions = [
  { q: '¿Respondes cada mensaje de WhatsApp en menos de 5 minutos, 24/7?', impact: 'cold' },
  { q: '¿Sabes el costo exacto de cada paciente que pagó, por canal?', impact: 'blind' },
  { q: '¿Tienes un sistema que le recuerda al paciente su siguiente cita?', impact: 'retain' },
  { q: '¿Tus anuncios usan el mismo ángulo creativo hace más de 3 meses?', impact: 'fatigue' },
  { q: '¿Sabes qué diferencia a tu clínica del competidor a 2 km?', impact: 'positioning' },
]

const answers = ref(Array(questions.length).fill(null))

const score = computed(() => answers.value.filter(a => a === true).length)
const answered = computed(() => answers.value.filter(a => a !== null).length)
const showResult = computed(() => answered.value === questions.length)

const diagnosis = computed(() => {
  if (score.value <= 1) {
    return {
      t: 'Tu clínica está sangrando',
      s: 'Estás dejando entre el 60% y el 80% de tu potencial de ventas en la mesa. Cada día que pasa, un competidor se lleva a tu próximo paciente.',
      tone: 'urgent',
    }
  }
  if (score.value <= 3) {
    return {
      t: 'Buenas piezas, sin orquesta',
      s: 'Tienes partes del sistema, pero sin integrar. Un embudo con fugas sigue siendo un embudo que pierde ventas.',
      tone: 'warn',
    }
  }
  return {
    t: 'Cerca, pero hay fugas',
    s: 'Tienes lo básico. Lo que te falta es precisión — ese 20% que separa a una clínica que crece de una que se estanca.',
    tone: 'ok',
  }
})

function setAnswer(index, value) {
  const copy = [...answers.value]
  copy[index] = value
  answers.value = copy
}
</script>

<template>
  <section
    id="diagnostico"
    class="aura-section-pad"
    :style="{
      background: 'var(--color-cream-50)',
      padding: 'clamp(5rem, 8vw, 8rem) 2.5rem',
      borderTop: '1px solid rgba(221,209,186,0.8)',
    }"
  >
    <div :style="{ maxWidth: '900px', margin: '0 auto' }">
      <!-- Header -->
      <div class="reveal">
        <div :style="{ textAlign: 'center', marginBottom: '3.5rem' }">
          <p :style="{
            fontFamily: 'var(--font-ui)',
            fontSize: '0.7rem',
            fontWeight: 500,
            textTransform: 'uppercase',
            letterSpacing: '0.28em',
            color: 'var(--color-terracotta-500)',
            margin: '0 0 1.25rem',
          }">
            § I · Diagnóstico — 90 segundos
          </p>
          <h2 :style="{
            fontFamily: 'var(--font-display)',
            fontWeight: 400,
            fontSize: 'clamp(2rem, 4vw, 3.2rem)',
            lineHeight: 1.05,
            letterSpacing: '-0.022em',
            margin: '0 0 1.25rem',
            color: 'var(--color-brown-900)',
            maxWidth: '22ch',
            marginInline: 'auto',
          }">
            Antes de que leas nada más,
            <span :style="{ fontStyle: 'italic', color: 'var(--color-terracotta-500)' }">responde esto</span>.
          </h2>
          <p :style="{
            fontFamily: 'var(--font-body-alt)',
            fontStyle: 'italic',
            fontSize: '1.05rem',
            color: 'var(--color-brown-400)',
            margin: '0 auto',
            maxWidth: '54ch',
          }">
            Si respondes "no" más de dos veces, sigue leyendo. Si respondes "sí" a todo,
            cierra la pestaña — no nos necesitas.
          </p>
        </div>
      </div>

      <!-- Questions -->
      <div :style="{ display: 'flex', flexDirection: 'column', gap: '0.65rem' }">
        <div
          v-for="(q, i) in questions"
          :key="i"
          class="reveal"
          :class="'reveal-delay-' + Math.min(i + 1, 3)"
        >
          <div class="diag-card" :style="{
            background: 'white',
            border: '1px solid',
            borderColor: answers[i] === false ? 'var(--color-terracotta-500)' : 'rgba(221,209,186,0.8)',
            borderRadius: '12px',
            padding: '1.25rem 1.5rem',
            display: 'grid',
            gridTemplateColumns: 'auto 1fr auto auto',
            gap: '1rem',
            alignItems: 'center',
            transition: 'all .3s',
          }">
            <!-- Question number -->
            <span :style="{
              fontFamily: 'var(--font-ui-alt)',
              fontStyle: 'italic',
              fontSize: '0.9rem',
              color: 'var(--color-brown-300)',
              width: '2ch',
            }">0{{ i + 1 }}</span>

            <!-- Question text -->
            <p :style="{
              fontFamily: 'var(--font-body)',
              fontSize: '0.95rem',
              color: 'var(--color-brown-900)',
              margin: 0,
              lineHeight: 1.5,
            }">{{ q.q }}</p>

            <!-- Sí button -->
            <button
              @click="setAnswer(i, true)"
              :style="{
                padding: '0.5rem 1.1rem',
                borderRadius: '999px',
                border: '1px solid',
                borderColor: answers[i] === true ? 'var(--color-terracotta-500)' : 'var(--color-cream-300)',
                background: answers[i] === true ? 'var(--color-terracotta-500)' : 'transparent',
                color: answers[i] === true ? 'white' : 'var(--color-brown-400)',
                fontFamily: 'var(--font-ui)',
                fontSize: '0.72rem',
                fontWeight: 600,
                letterSpacing: '0.08em',
                textTransform: 'uppercase',
                cursor: 'pointer',
                transition: 'all .2s',
              }"
            >Sí</button>

            <!-- No button -->
            <button
              @click="setAnswer(i, false)"
              :style="{
                padding: '0.5rem 1.1rem',
                borderRadius: '999px',
                border: '1px solid',
                borderColor: answers[i] === false ? 'var(--color-terracotta-500)' : 'var(--color-cream-300)',
                background: answers[i] === false ? 'var(--color-terracotta-500)' : 'transparent',
                color: answers[i] === false ? 'white' : 'var(--color-brown-400)',
                fontFamily: 'var(--font-ui)',
                fontSize: '0.72rem',
                fontWeight: 600,
                letterSpacing: '0.08em',
                textTransform: 'uppercase',
                cursor: 'pointer',
                transition: 'all .2s',
              }"
            >No</button>
          </div>
        </div>
      </div>

      <!-- Result panel -->
      <div :style="{
        marginTop: '2.5rem',
        overflow: 'hidden',
        maxHeight: showResult ? '500px' : '0',
        opacity: showResult ? 1 : 0,
        transition: 'all .6s cubic-bezier(0.16,1,0.3,1)',
      }">
        <div :style="{
          background: 'var(--color-brown-900)',
          color: 'var(--color-cream-50)',
          padding: '2.5rem',
          borderRadius: '16px',
          position: 'relative',
          overflow: 'hidden',
        }">
          <!-- Grain overlay -->
          <div :style="{
            position: 'absolute',
            inset: 0,
            opacity: 0.05,
            pointerEvents: 'none',
            backgroundImage: 'url(/img/grain.png)',
            backgroundRepeat: 'repeat',
          }"></div>

          <p :style="{
            fontFamily: 'var(--font-ui)',
            fontSize: '0.68rem',
            fontWeight: 500,
            textTransform: 'uppercase',
            letterSpacing: '0.25em',
            color: 'var(--color-terracotta-300)',
            margin: '0 0 1rem',
            position: 'relative',
          }">
            Diagnóstico · {{ score }}/{{ questions.length }}
          </p>
          <h3 :style="{
            fontFamily: 'var(--font-display)',
            fontWeight: 400,
            fontSize: 'clamp(1.6rem, 3vw, 2.2rem)',
            lineHeight: 1.1,
            letterSpacing: '-0.018em',
            margin: '0 0 1rem',
            color: 'var(--color-cream-50)',
            position: 'relative',
          }">
            {{ diagnosis.t }}.
          </h3>
          <p :style="{
            fontFamily: 'var(--font-body)',
            fontSize: '1.02rem',
            lineHeight: 1.65,
            color: 'rgba(234,225,208,0.85)',
            margin: '0 0 1.5rem',
            maxWidth: '52ch',
            position: 'relative',
          }">
            {{ diagnosis.s }}
          </p>
          <a
            href="#cta"
            :style="{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '0.5rem',
              fontFamily: 'var(--font-ui)',
              fontSize: '0.8rem',
              fontWeight: 600,
              letterSpacing: '0.06em',
              color: 'var(--color-terracotta-300)',
              textDecoration: 'none',
              borderBottom: '1px solid',
              paddingBottom: '2px',
              position: 'relative',
            }"
          >Agendar diagnóstico con un experto →</a>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
@media (max-width: 600px) {
  .diag-card {
    grid-template-columns: 1fr auto auto !important;
    gap: 0.65rem !important;
  }
  .diag-card > span:first-child {
    display: none;
  }
}
</style>
