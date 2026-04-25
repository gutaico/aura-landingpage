<script setup>
import { ref } from 'vue'

const openIndex = ref(0)

function toggle(i) {
  openIndex.value = openIndex.value === i ? null : i
}

const faqs = [
  {
    q: '¿Cuánto cuesta trabajar con Aura?',
    a: 'Hay una activación única + mensualidad fija que cubre operación, optimización semanal y acceso al Dashboard de resultados en tiempo real. Si tu inversión publicitaria crece, se agrega un porcentaje sobre el excedente. Los números exactos los ajustamos a tu volumen en el diagnóstico.',
  },
  {
    q: '¿Por qué solo trabajan con estética y wellness?',
    a: 'Porque dominar a un paciente toma años de iteración. Sabemos qué triggers activar, qué objeciones aparecen y cómo nutrir. Una agencia "para todos" es, en realidad, mediocre para todos.',
  },
  {
    q: '¿En cuánto tiempo veo resultados?',
    a: 'En 7 días tienes campañas al aire. Primeros leads en la primera semana. La optimización se afina semana a semana -- a los 30 días ya tenemos data sólida del recorrido completo.',
  },
  {
    q: '¿Qué pasa si no me funciona?',
    a: 'Garantía de 30 días. Si no llegamos al 70% de la meta de prospectos calificados acordada y tú cumpliste con tu parte, te devolvemos todo lo que pagaste.',
  },
  {
    q: '¿Yo tengo que hacer algo o ustedes se ocupan de todo?',
    a: 'Nos ocupamos del 95%: estrategia, creativos, lanzamiento, optimización, respuesta, agenda, recordatorios, retención. Lo único que tú haces es atender al paciente cuando llegue a la silla -- y aprobar creativos antes de publicarlos.',
  },
  {
    q: '¿Me amarran a un contrato largo?',
    a: 'No. No pedimos 6 meses de compromiso. Si no te funciona, te vas -- pero no te vas a ir porque te devolvemos el dinero si no cumplimos.',
  },
  {
    q: '¿Ya trabajan en mi ciudad / con mi competencia?',
    a: 'Trabajamos con exclusividad zonal. Una sola clínica de estética por zona de cobertura, una sola barbería por zona. Si alguien de tu competencia ya está con nosotros, no tomamos tu caso.',
  },
  {
    q: '¿Puedo ver el Dashboard antes de contratar?',
    a: 'Sí. En el diagnóstico te mostramos una cuenta demo en vivo — con data real anonimizada — para que veas exactamente qué vas a consultar tú cada día.',
  },
]
</script>

<template>
  <section
    id="faq"
    class="aura-section-pad"
    :style="{
      background: 'var(--color-cream-100)',
      padding: 'clamp(5rem, 8vw, 9rem) 2.5rem',
    }"
  >
    <div :style="{ maxWidth: '880px', margin: '0 auto' }">
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
            &sect; IX &middot; Preguntas honestas
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

      <div :style="{ display: 'flex', flexDirection: 'column' }">
        <div
          v-for="(faq, i) in faqs"
          :key="i"
          class="reveal"
          :style="{
            borderBottom: '1px solid rgba(221,209,186,0.8)',
            transition: 'all .3s',
          }"
        >
          <button
            @click="toggle(i)"
            class="faq-btn"
            :style="{
              width: '100%',
              textAlign: 'left',
              padding: '1.5rem 0',
              background: 'transparent',
              border: 'none',
              cursor: 'pointer',
              display: 'grid',
              gridTemplateColumns: 'auto 1fr auto',
              gap: '1.5rem',
              alignItems: 'center',
            }"
          >
            <span
              :style="{
                fontFamily: 'var(--font-ui-alt)',
                fontStyle: 'italic',
                fontSize: '0.85rem',
                color: 'var(--color-terracotta-500)',
                opacity: 0.7,
              }"
            >
              0{{ i + 1 }}
            </span>
            <span
              :style="{
                fontFamily: 'var(--font-display)',
                fontSize: 'clamp(1.05rem, 1.4vw, 1.2rem)',
                fontWeight: 400,
                color: 'var(--color-brown-900)',
                letterSpacing: '-0.005em',
              }"
            >
              {{ faq.q }}
            </span>
            <span
              :style="{
                width: '32px',
                height: '32px',
                borderRadius: '50%',
                border: '1px solid var(--color-cream-300)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: 'var(--color-terracotta-500)',
                flexShrink: 0,
                transform: openIndex === i ? 'rotate(45deg)' : 'rotate(0)',
                transition: 'transform .3s cubic-bezier(0.16,1,0.3,1)',
                fontSize: '1.1rem',
                lineHeight: 1,
                fontWeight: 300,
              }"
            >
              +
            </span>
          </button>

          <div
            :style="{
              maxHeight: openIndex === i ? '400px' : '0',
              overflow: 'hidden',
              transition: 'max-height .4s cubic-bezier(0.16,1,0.3,1)',
            }"
          >
            <p
              class="faq-answer"
              :style="{
                padding: '0 0 1.75rem 2.75rem',
                fontFamily: 'var(--font-body)',
                fontSize: '0.95rem',
                lineHeight: 1.65,
                color: 'var(--color-brown-400)',
                margin: 0,
                maxWidth: '66ch',
              }"
            >
              {{ faq.a }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
@media (max-width: 640px) {
  .faq-btn {
    gap: 0.75rem !important;
  }
  .faq-answer {
    padding-left: 0 !important;
  }
}
</style>
