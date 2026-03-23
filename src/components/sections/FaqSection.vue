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
    a: 'El sistema completo se instala en 21 días. Las primeras citas empiezan a llegar desde la primera semana de campañas activas. El mecanismo autocorrectivo mejora los resultados cada semana — los primeros 30 días son de calibración, y a partir de ahí la espiral se aprieta.',
  },
  {
    q: '¿Qué pasa si mis pacientes no usan redes sociales?',
    a: 'En México hay más de 93 millones de usuarios en Facebook y 53 millones en Instagram. Tu paciente sí está ahí — el tema es que hoy está viendo los anuncios de tu competencia. La pregunta no es si tu paciente usa redes, sino quién le está hablando primero.',
  },
]
</script>

<template>
  <section class="bg-cream-50 py-24 px-6">
    <div class="mx-auto max-w-3xl">
      <h2 class="text-center font-heading text-3xl font-bold text-brown-800 sm:text-4xl">
        Preguntas frecuentes
      </h2>

      <div class="mt-12 divide-y divide-cream-200">
        <div v-for="(faq, i) in faqs" :key="i">
          <button
            @click="toggle(i)"
            class="flex w-full items-center justify-between py-5 text-left"
          >
            <span class="font-medium text-brown-800 pr-4">{{ faq.q }}</span>
            <svg
              :class="['h-5 w-5 shrink-0 text-terracotta-500 transition-transform', openIndex === i ? 'rotate-180' : '']"
              fill="none" stroke="currentColor" viewBox="0 0 24 24"
            >
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
            </svg>
          </button>
          <div v-show="openIndex === i" class="pb-5 text-sm text-brown-500 leading-relaxed">
            {{ faq.a }}
          </div>
        </div>
      </div>

      <p class="mt-10 text-center text-brown-500">
        ¿Tienes otra pregunta?
        <a href="#agenda" class="font-medium text-terracotta-600 hover:text-terracotta-700 underline underline-offset-2">
          Resuélvela en tu consultoría gratuita &rarr;
        </a>
      </p>
    </div>
  </section>
</template>
