<script setup>
import { ref } from 'vue'

const openIndex = ref(null)

function toggle(i) {
  openIndex.value = openIndex.value === i ? null : i
}

const faqs = [
  {
    q: '¿La consultoría tiene algún costo?',
    a: 'No. Son 30 minutos donde analizamos tu situación actual y te damos un diagnóstico real con recomendaciones. Si después de eso decides que quieres trabajar juntos, te hacemos una propuesta. Si no, te quedas con el diagnóstico sin costo.',
  },
  {
    q: '¿Cuánto cuesta el servicio si decido trabajar con ustedes?',
    a: 'Depende de tu negocio y tus objetivos. Tenemos un setup inicial (cobro único para montar todo el sistema) y un retainer mensual que incluye la operación continua. En la consultoría te damos números exactos para tu caso.',
  },
  {
    q: '¿Trabajan con cualquier tipo de negocio?',
    a: 'Nos especializamos exclusivamente en belleza y bienestar: clínicas de estética, centros de depilación láser, clínicas capilares, wellness, dental estético, medicina estética y cirugía plástica. No somos una agencia genérica — eso es lo que nos hace diferentes.',
  },
  {
    q: 'Ya trabajé con una agencia y me fue mal. ¿Por qué sería diferente?',
    a: 'Porque no prometemos leads — prometemos un mecanismo que cada semana entiende mejor qué funciona para tu negocio específico. Además, tú ves los datos en tiempo real. Sin reportes mensuales que oculten. Si algo no funciona, lo ves tú al mismo tiempo que nosotros.',
  },
  {
    q: '¿Cuánto tiempo tarda en verse resultados?',
    a: 'El sistema completo se instala en 7 días hábiles. Las primeras citas empiezan a llegar desde la primera semana de campañas activas. El mecanismo autocorrectivo mejora los resultados cada semana — los primeros 30 días son de calibración, y a partir de ahí la espiral se aprieta.',
  },
  {
    q: '¿Qué pasa si mis pacientes no usan redes sociales?',
    a: 'En México hay más de 93 millones de usuarios en Facebook y 53 millones en Instagram. Tu paciente sí está ahí — el tema es que hoy está viendo los anuncios de tu competencia. La pregunta no es si tu paciente usa redes, sino quién le está hablando primero.',
  },
]
</script>

<template>
  <section class="relative bg-cream-50 py-16 lg:py-32 px-5 lg:px-8">
    <div class="mx-auto max-w-3xl">
      <!-- Header -->
      <div class="text-center reveal">
        <p class="font-secondary text-[0.7rem] font-semibold uppercase tracking-[0.25em] text-terracotta-500 mb-4">
          Preguntas frecuentes
        </p>
        <h2 class="font-heading text-[clamp(1.8rem,3.5vw,2.4rem)] font-bold text-brown-800 leading-[1.15]">
          Resolvemos tus dudas
        </h2>
      </div>

      <!-- Accordion -->
      <div class="mt-12 reveal">
        <div
          v-for="(faq, i) in faqs"
          :key="i"
          class="border-b border-cream-200/80"
        >
          <button
            @click="toggle(i)"
            class="flex w-full items-center justify-between py-6 text-left bg-transparent border-none cursor-pointer group"
          >
            <span class="font-medium text-[0.92rem] text-brown-700 pr-8 group-hover:text-terracotta-600 transition-colors duration-300">
              {{ faq.q }}
            </span>
            <span class="flex h-7 w-7 shrink-0 items-center justify-center rounded-full border border-cream-300 text-brown-400
                         group-hover:border-terracotta-400 group-hover:text-terracotta-500 transition-all duration-300">
              <svg
                :class="['h-3.5 w-3.5 transition-transform duration-300', openIndex === i ? 'rotate-180' : '']"
                fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2"
              >
                <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
              </svg>
            </span>
          </button>

          <Transition
            enter-active-class="transition-all duration-300 ease-out overflow-hidden"
            enter-from-class="max-h-0 opacity-0"
            enter-to-class="max-h-40 opacity-100"
            leave-active-class="transition-all duration-200 ease-in overflow-hidden"
            leave-from-class="max-h-40 opacity-100"
            leave-to-class="max-h-0 opacity-0"
          >
            <div v-show="openIndex === i">
              <p class="pb-6 text-[0.88rem] text-brown-400 leading-relaxed pr-12">
                {{ faq.a }}
              </p>
            </div>
          </Transition>
        </div>
      </div>

      <!-- Post-FAQ CTA -->
      <p class="reveal mt-12 text-center text-brown-400 text-[0.9rem]">
        ¿Tienes otra pregunta?
        <a href="#agenda" class="font-medium text-terracotta-600 hover:text-terracotta-700 transition-colors duration-300
                                 underline underline-offset-4 decoration-terracotta-300/50 hover:decoration-terracotta-500">
          Resuélvela en tu consultoría gratuita &rarr;
        </a>
      </p>
    </div>
  </section>
</template>
