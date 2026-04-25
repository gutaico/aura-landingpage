<script setup>
import ChromaImage from '../ChromaImage.vue'

const emit = defineEmits(['goAgente'])

const features = [
  { t: 'Responde en 30 segundos', b: 'WhatsApp, Instagram, Facebook. 24/7. Nunca duerme, nunca pide vacaciones.' },
  { t: 'Califica y agenda', b: 'Filtra al curioso, identifica al paciente real, agenda directo en tu calendario.' },
  { t: 'Reactiva conversaciones perdidas', b: 'Si dejó de responder hace 3 días, lo busca. Si dijo "lo pienso", lo nutre.' },
  { t: 'Recuerda cada paciente', b: 'Historial, gustos, próximo retoque, fecha de cumpleaños. Atención de boutique a escala.' },
]

</script>

<template>
  <section
    id="agente-ia"
    class="aura-section-pad"
    :style="{
      background: 'var(--color-cream-50)',
      padding: 'clamp(5rem, 9vw, 9rem) 2.5rem',
      borderTop: '1px solid rgba(221,209,186,0.8)',
      position: 'relative',
    }"
  >
    <div :style="{ maxWidth: '1200px', margin: '0 auto' }">
      <div
        class="aura-hero-grid"
        :style="{
          display: 'grid',
          gridTemplateColumns: '1fr 1fr',
          gap: '4.5rem',
          alignItems: 'start',
        }"
      >
        <!-- ═══ Left — copy + features ═══ -->
        <div class="reveal">
          <!-- Eyebrow -->
          <p :style="{
            fontFamily: 'var(--font-ui)',
            fontSize: '0.7rem',
            fontWeight: 500,
            textTransform: 'uppercase',
            letterSpacing: '0.28em',
            color: 'var(--color-terracotta-500)',
            margin: '0 0 1.25rem',
          }">
            &sect; IV bis &middot; El motor del sistema
          </p>

          <!-- Headline -->
          <h2 :style="{
            fontFamily: 'var(--font-display)',
            fontWeight: 400,
            fontSize: 'clamp(2rem, 4vw, 3rem)',
            lineHeight: 1.05,
            letterSpacing: '-0.022em',
            margin: '0 0 1.25rem',
            color: 'var(--color-brown-900)',
          }">
            Lo que hace que<br />
            <span :style="{ fontStyle: 'italic', color: 'var(--color-terracotta-500)' }">todo lo dem&aacute;s</span><br />
            funcione.
          </h2>

          <!-- Lead paragraph -->
          <p :style="{
            fontFamily: 'var(--font-body-alt)',
            fontStyle: 'italic',
            fontSize: 'clamp(1.05rem, 1.4vw, 1.2rem)',
            lineHeight: 1.55,
            color: 'var(--color-brown-400)',
            margin: '0 0 2.5rem',
            maxWidth: '48ch',
          }">
            Detr&aacute;s de cada campa&ntilde;a hay un agente de IA propio,
            entrenado con la voz de tu marca, que convierte prospectos en
            pacientes — sin intervenci&oacute;n humana.
          </p>

          <!-- Features list -->
          <div :style="{ display: 'flex', flexDirection: 'column' }">
            <div
              v-for="(f, i) in features"
              :key="i"
              :style="{
                display: 'grid',
                gridTemplateColumns: 'auto 1fr',
                gap: '1.25rem',
                padding: '1.1rem 0',
                borderTop: '1px solid rgba(221,209,186,0.8)',
                borderBottom: i === features.length - 1 ? '1px solid rgba(221,209,186,0.8)' : 'none',
              }"
            >
              <!-- Number circle -->
              <span :style="{
                width: '28px',
                height: '28px',
                borderRadius: '50%',
                background: 'var(--color-terracotta-500)',
                color: 'white',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontFamily: 'var(--font-ui)',
                fontSize: '0.72rem',
                fontWeight: 600,
                flexShrink: 0,
              }">{{ i + 1 }}</span>

              <!-- Feature text -->
              <div>
                <p :style="{
                  fontFamily: 'var(--font-display)',
                  fontSize: '1.1rem',
                  fontWeight: 500,
                  color: 'var(--color-brown-900)',
                  margin: '0 0 0.25rem',
                  letterSpacing: '-0.005em',
                }">{{ f.t }}</p>
                <p :style="{
                  fontFamily: 'var(--font-body)',
                  fontSize: '0.9rem',
                  lineHeight: 1.55,
                  color: 'var(--color-brown-400)',
                  margin: 0,
                }">{{ f.b }}</p>
              </div>
            </div>
          </div>

          <!-- Link -->
          <div :style="{ marginTop: '2rem' }">
            <a
              href="#"
              @click.prevent="emit('goAgente')"
              :style="{
                display: 'inline-flex',
                alignItems: 'center',
                gap: '0.6rem',
                padding: '0.9rem 1.8rem',
                fontFamily: 'var(--font-ui)',
                fontSize: '0.82rem',
                fontWeight: 600,
                letterSpacing: '0.05em',
                textTransform: 'uppercase',
                color: 'var(--color-cream-50)',
                background: 'var(--color-terracotta-500)',
                borderRadius: '999px',
                textDecoration: 'none',
                cursor: 'pointer',
                transition: 'all .3s cubic-bezier(0.16,1,0.3,1)',
                boxShadow: '0 6px 24px rgba(145,65,38,0.25)',
              }"
            >Ver m&aacute;s sobre el agente <span :style="{ fontSize: '1rem' }">&rarr;</span></a>
          </div>
        </div>

        <!-- ═══ Right — conversation screenshot ═══ -->
        <div class="showcase-img" :style="{
          position: 'sticky',
          top: '12vh',
          alignSelf: 'start',
          maxWidth: '600px',
          margin: '0 auto',
        }">
          <ChromaImage
            src="/conversacion.webp"
            alt="Conversación real del agente Aura en WhatsApp — desde la primera pregunta hasta la cita agendada"
            :threshold="40"
            :feather="20"
            :style="{
              width: '100%',
              height: 'auto',
              display: 'block',
            }"
          />
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
@media (max-width: 980px) {
  .showcase-img {
    position: static !important;
  }
}
</style>
