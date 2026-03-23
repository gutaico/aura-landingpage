<script setup>
import { reactive } from 'vue'

const form = reactive({
  name: '',
  business: '',
  type: '',
  city: '',
  advertising: '',
  whatsapp: '',
})

const businessTypes = [
  'Clínica de estética facial/corporal',
  'Centro de depilación láser',
  'Clínica capilar / injerto capilar',
  'Clínica dental estética',
  'Centro de wellness / fitness',
  'Medicina estética (botox, rellenos)',
  'Cirugía plástica',
  'Otro',
]

function handleSubmit() {
  // TODO: connect to CRM / GHL
  alert('Formulario enviado. Te contactaremos pronto.')
}
</script>

<template>
  <section id="agenda" class="bg-brown-900 py-24 px-6">
    <div class="mx-auto max-w-2xl">
      <div class="text-center">
        <h2 class="font-heading text-3xl font-bold text-cream-50 sm:text-4xl">
          ¿Listo para llenar tu agenda<br>
          <span class="text-terracotta-400">de los pacientes correctos?</span>
        </h2>
        <p class="mx-auto mt-5 max-w-xl text-cream-300 leading-relaxed">
          El siguiente paso es una consultoría gratuita de 30 minutos donde analizamos
          tu situación actual y te mostramos cómo este sistema aplicaría a tu negocio.
          Sin compromiso.
        </p>
      </div>

      <form @submit.prevent="handleSubmit" class="mt-12 space-y-5">
        <div>
          <label class="block text-sm font-medium text-cream-300 mb-1.5">Nombre completo</label>
          <input v-model="form.name" type="text" required class="w-full rounded-xl border border-brown-700 bg-brown-800 px-4 py-3 text-cream-100 placeholder-brown-500 focus:border-terracotta-500 focus:outline-none focus:ring-1 focus:ring-terracotta-500" placeholder="Tu nombre" />
        </div>

        <div>
          <label class="block text-sm font-medium text-cream-300 mb-1.5">Nombre de tu negocio</label>
          <input v-model="form.business" type="text" required class="w-full rounded-xl border border-brown-700 bg-brown-800 px-4 py-3 text-cream-100 placeholder-brown-500 focus:border-terracotta-500 focus:outline-none focus:ring-1 focus:ring-terracotta-500" placeholder="Ej: Clínica Bella Vita" />
        </div>

        <div>
          <label class="block text-sm font-medium text-cream-300 mb-1.5">Tipo de negocio</label>
          <select v-model="form.type" required class="w-full rounded-xl border border-brown-700 bg-brown-800 px-4 py-3 text-cream-100 focus:border-terracotta-500 focus:outline-none focus:ring-1 focus:ring-terracotta-500">
            <option value="" disabled>Selecciona una opción</option>
            <option v-for="t in businessTypes" :key="t" :value="t">{{ t }}</option>
          </select>
        </div>

        <div>
          <label class="block text-sm font-medium text-cream-300 mb-1.5">Ciudad</label>
          <input v-model="form.city" type="text" required class="w-full rounded-xl border border-brown-700 bg-brown-800 px-4 py-3 text-cream-100 placeholder-brown-500 focus:border-terracotta-500 focus:outline-none focus:ring-1 focus:ring-terracotta-500" placeholder="Ej: Monterrey" />
        </div>

        <div>
          <label class="block text-sm font-medium text-cream-300 mb-1.5">¿Actualmente inviertes en publicidad digital?</label>
          <select v-model="form.advertising" required class="w-full rounded-xl border border-brown-700 bg-brown-800 px-4 py-3 text-cream-100 focus:border-terracotta-500 focus:outline-none focus:ring-1 focus:ring-terracotta-500">
            <option value="" disabled>Selecciona una opción</option>
            <option value="si">Sí</option>
            <option value="no">No</option>
            <option value="antes">Lo hice antes pero lo dejé</option>
          </select>
        </div>

        <div>
          <label class="block text-sm font-medium text-cream-300 mb-1.5">WhatsApp (para confirmar tu cita)</label>
          <input v-model="form.whatsapp" type="tel" required class="w-full rounded-xl border border-brown-700 bg-brown-800 px-4 py-3 text-cream-100 placeholder-brown-500 focus:border-terracotta-500 focus:outline-none focus:ring-1 focus:ring-terracotta-500" placeholder="Ej: 81 1234 5678" />
        </div>

        <button
          type="submit"
          class="w-full rounded-xl bg-terracotta-500 py-4 text-lg font-semibold text-white shadow-lg hover:bg-terracotta-600 transition-colors hover:shadow-xl"
        >
          Agendar mi consultoría gratuita
        </button>
      </form>

      <p class="mt-6 text-center text-xs text-cream-500 leading-relaxed">
        Esta consultoría es exclusiva para dueños y directores de negocios de bienestar y estética.
        No es una llamada de ventas — es un diagnóstico real con recomendaciones que puedes aplicar
        aunque no trabajes con nosotros.
      </p>
    </div>
  </section>
</template>
