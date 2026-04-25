<script setup>
import { ref } from 'vue'

const openIndex = ref(null)

function toggle(i) {
  openIndex.value = openIndex.value === i ? null : i
}

const faqs = [
  {
    q: '¿Qué pasa si el agente dice algo incorrecto sobre un tratamiento?',
    a: 'Tú defines qué puede y qué no puede decir. Se entrena con la información que tú nos das. Y si algo se sale de su conocimiento, te llega una notificación al celular y tú decides con un toque.',
  },
  {
    q: '¿Mis pacientes van a sentir que hablan con un robot?',
    a: 'No es un chatbot genérico. El agente tiene el tono de tu negocio, conoce tus tratamientos, envía fotos de tus resultados y sabe cuándo pasarte la conversación. La mayoría de pacientes piensa que es tu recepcionista.',
  },
  {
    q: '¿Cuánto cuesta empezar?',
    a: 'Depende del volumen de conversaciones de tu clínica. Agenda una llamada de 15 minutos y te damos un número exacto con base en tu operación. Sin compromiso.',
  },
  {
    q: '¿Qué pasa si no me funciona?',
    a: 'Garantía de 30 días. Si no llegamos al 70% de la meta de citas que definimos juntos, te devolvemos todo lo que pagaste. Sin letras chicas.',
  },
  {
    q: '¿Se conecta con mi agenda actual?',
    a: 'Sí. Integramos con Google Calendar, Agenda Pro y los sistemas de agendamiento más comunes en el sector.',
  },
  {
    q: '¿Qué tanto tengo que meterle yo?',
    a: 'El setup son 3 días con tu participación (60-90 minutos totales repartidos). Después, abres la app una vez al día para revisar.',
  },
  {
    q: '¿Entiende audios, fotos, PDFs?',
    a: 'Sí. Procesa notas de voz (muy común en WhatsApp), fotos que le mandan los pacientes, PDFs y documentos. Transcribe, analiza y responde con contexto.',
  },
]
</script>

<template>
  <section
    class="aura-section-pad"
    :style="{
      background: 'var(--color-cream-50)',
      padding: 'clamp(5rem, 8vw, 9rem) 2.5rem',
      borderTop: '1px solid rgba(221,209,186,0.8)',
    }"
  >
    <div :style="{ maxWidth: '880px', margin: '0 auto' }">
      <!-- Header -->
      <div class="reveal">
        <div :style="{ textAlign: 'center', marginBottom: '3.5rem' }">
          <p
            :style="{
              fontFamily: 'var(--font-ui)',
              fontSize: '0.7rem',
              fontWeight: 500,
              textTransform: 'uppercase',
              letterSpacing: '0.28em',
              color: 'var(--color-terracotta-500)',
              margin: '0 0 1.25rem',
            }"
          >
            Preguntas frecuentes
          </p>
          <h2
            :style="{
              fontFamily: 'var(--font-display)',
              fontWeight: 400,
              fontSize: 'clamp(2rem, 4vw, 3rem)',
              lineHeight: 1.05,
              letterSpacing: '-0.022em',
              margin: 0,
              color: 'var(--color-brown-900)',
            }"
          >
            Lo que
            <span :style="{ fontStyle: 'italic', color: 'var(--color-terracotta-500)' }">todos</span>
            preguntan.
          </h2>
        </div>
      </div>

      <!-- FAQ cards -->
      <div :style="{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }">
        <div
          v-for="(faq, i) in faqs"
          :key="i"
          class="reveal"
          :style="{
            borderRadius: '12px',
            border: '1px solid rgba(221,209,186,0.8)',
            background: openIndex === i ? 'white' : 'transparent',
            transition: 'all .3s cubic-bezier(0.16,1,0.3,1)',
            overflow: 'hidden',
          }"
        >
          <button
            @click="toggle(i)"
            :style="{
              width: '100%',
              textAlign: 'left',
              padding: '1.25rem 1.5rem',
              background: 'transparent',
              border: 'none',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '1rem',
            }"
          >
            <!-- Number -->
            <span
              :style="{
                fontFamily: 'var(--font-ui-alt)',
                fontStyle: 'italic',
                fontSize: '0.82rem',
                color: 'var(--color-terracotta-500)',
                opacity: 0.6,
                flexShrink: 0,
              }"
            >0{{ i + 1 }}</span>

            <!-- Question text -->
            <span
              :style="{
                flex: 1,
                fontFamily: 'var(--font-display)',
                fontSize: 'clamp(1rem, 1.3vw, 1.12rem)',
                fontWeight: 400,
                color: 'var(--color-brown-900)',
                letterSpacing: '-0.005em',
                lineHeight: 1.35,
              }"
            >{{ faq.q }}</span>

            <!-- Chevron circle -->
            <span
              :style="{
                width: '28px',
                height: '28px',
                borderRadius: '50%',
                border: '1px solid var(--color-cream-300)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                flexShrink: 0,
                transform: openIndex === i ? 'rotate(180deg)' : 'rotate(0)',
                transition: 'transform .3s cubic-bezier(0.16,1,0.3,1)',
              }"
            >
              <svg
                width="12"
                height="12"
                fill="none"
                stroke="var(--color-terracotta-500)"
                stroke-width="2"
                viewBox="0 0 24 24"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <polyline points="6 9 12 15 18 9" />
              </svg>
            </span>
          </button>

          <!-- Answer -->
          <div
            :style="{
              maxHeight: openIndex === i ? '400px' : '0',
              overflow: 'hidden',
              transition: 'max-height .4s cubic-bezier(0.16,1,0.3,1)',
            }"
          >
            <p
              class="faq-a-answer"
              :style="{
                padding: '0 1.5rem 1.5rem 3.5rem',
                fontFamily: 'var(--font-body)',
                fontSize: '0.92rem',
                lineHeight: 1.65,
                color: 'var(--color-brown-400)',
                margin: 0,
                maxWidth: '62ch',
              }"
            >{{ faq.a }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
@media (max-width: 640px) {
  .faq-a-answer {
    padding-left: 1.5rem !important;
  }
}
</style>
