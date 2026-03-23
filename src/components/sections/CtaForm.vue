<script setup>
import { reactive, ref } from 'vue'

const submitted = ref(false)

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
  submitted.value = true
}
</script>

<template>
  <section id="agenda" class="relative bg-brown-900 py-16 lg:py-32 px-5 lg:px-10 overflow-hidden grain">
    <div class="relative mx-auto max-w-5xl">
      <!-- Two-column: text + form -->
      <div class="grid lg:grid-cols-2 gap-12 lg:gap-20">
        <!-- Left: text + image -->
        <div class="reveal">
          <p class="font-secondary text-[0.68rem] font-medium uppercase tracking-[0.25em] text-terracotta-300/80 mb-5">
            Da el primer paso
          </p>
          <h2 class="font-heading text-[clamp(1.7rem,3vw,2.5rem)] font-bold text-cream-50 leading-[1.12]">
            ¿Listo para llenar tu agenda
            <span class="text-terracotta-400">de los pacientes correctos?</span>
          </h2>
          <p class="mt-6 text-cream-200/80 leading-[1.8] text-[0.95rem]">
            Consultoría gratuita de 30 minutos. Analizamos tu situación actual y te mostramos
            cómo este sistema aplicaría a tu negocio. Sin compromiso.
          </p>

          <!-- Image — open door -->
          <div class="mt-10 hidden lg:block">
            <img
              src="/img/cta-open-door.png"
              alt="Puerta de consulta abierta invitando a entrar"
              class="w-full max-w-sm object-contain"
            />
          </div>

          <p class="mt-6 font-secondary text-[0.7rem] text-cream-400/50 leading-relaxed">
            Esta consultoría es exclusiva para dueños y directores de negocios
            de bienestar y estética.
          </p>
        </div>

        <!-- Right: form -->
        <div>
          <!-- Success state -->
          <div v-if="submitted" class="flex items-center justify-center h-full reveal">
            <div class="text-center">
              <svg class="w-10 h-10 text-terracotta-400 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <h3 class="font-heading text-xl font-bold text-cream-50 mb-2">Recibimos tu solicitud</h3>
              <p class="text-cream-200/70 text-sm">Te contactamos en menos de 24 horas por WhatsApp.</p>
            </div>
          </div>

          <!-- Form -->
          <form v-else @submit.prevent="handleSubmit" class="space-y-5 reveal reveal-delay-1">
            <div>
              <label class="block font-secondary text-[0.68rem] font-medium text-cream-300/80 mb-2 uppercase tracking-wider">Nombre completo</label>
              <input
                v-model="form.name" type="text" required
                class="w-full border-b border-brown-700/60 bg-transparent px-0 py-3
                       text-[0.92rem] text-cream-100 placeholder-brown-400
                       focus:border-terracotta-500/60 focus:outline-none
                       transition-colors duration-300"
                placeholder="Tu nombre"
              />
            </div>
            <div>
              <label class="block font-secondary text-[0.68rem] font-medium text-cream-300/80 mb-2 uppercase tracking-wider">Nombre de tu negocio</label>
              <input
                v-model="form.business" type="text" required
                class="w-full border-b border-brown-700/60 bg-transparent px-0 py-3
                       text-[0.92rem] text-cream-100 placeholder-brown-400
                       focus:border-terracotta-500/60 focus:outline-none
                       transition-colors duration-300"
                placeholder="Ej: Clínica Bella Vita"
              />
            </div>
            <div>
              <label class="block font-secondary text-[0.68rem] font-medium text-cream-300/80 mb-2 uppercase tracking-wider">Tipo de negocio</label>
              <select
                v-model="form.type" required
                class="w-full border-b border-brown-700/60 bg-transparent px-0 py-3
                       text-[0.92rem] text-cream-100
                       focus:border-terracotta-500/60 focus:outline-none
                       transition-colors duration-300 appearance-none cursor-pointer"
              >
                <option value="" disabled class="bg-brown-900 text-brown-500">Selecciona una opción</option>
                <option v-for="t in businessTypes" :key="t" :value="t" class="bg-brown-900">{{ t }}</option>
              </select>
            </div>
            <div class="grid sm:grid-cols-2 gap-5 sm:gap-6">
              <div>
                <label class="block font-secondary text-[0.68rem] font-medium text-cream-300/80 mb-2 uppercase tracking-wider">Ciudad</label>
                <input
                  v-model="form.city" type="text" required
                  class="w-full border-b border-brown-700/60 bg-transparent px-0 py-3
                         text-[0.92rem] text-cream-100 placeholder-brown-400
                         focus:border-terracotta-500/60 focus:outline-none
                         transition-colors duration-300"
                  placeholder="Ej: Monterrey"
                />
              </div>
              <div>
                <label class="block font-secondary text-[0.68rem] font-medium text-cream-300/80 mb-2 uppercase tracking-wider">¿Inviertes en ads?</label>
                <select
                  v-model="form.advertising" required
                  class="w-full border-b border-brown-700/60 bg-transparent px-0 py-3
                         text-[0.92rem] text-cream-100
                         focus:border-terracotta-500/60 focus:outline-none
                         transition-colors duration-300 appearance-none cursor-pointer"
                >
                  <option value="" disabled class="bg-brown-900 text-brown-500">Selecciona</option>
                  <option value="si" class="bg-brown-900">Sí</option>
                  <option value="no" class="bg-brown-900">No</option>
                  <option value="antes" class="bg-brown-900">Antes sí</option>
                </select>
              </div>
            </div>
            <div>
              <label class="block font-secondary text-[0.68rem] font-medium text-cream-300/80 mb-2 uppercase tracking-wider">WhatsApp</label>
              <input
                v-model="form.whatsapp" type="tel" required
                class="w-full border-b border-brown-700/60 bg-transparent px-0 py-3
                       text-[0.92rem] text-cream-100 placeholder-brown-400
                       focus:border-terracotta-500/60 focus:outline-none
                       transition-colors duration-300"
                placeholder="81 1234 5678"
              />
            </div>

            <div class="pt-4">
              <button
                type="submit"
                class="group flex items-center gap-3 font-secondary text-[0.85rem] font-semibold text-terracotta-400
                       hover:text-terracotta-300 transition-colors duration-300
                       bg-transparent border-none cursor-pointer px-0"
              >
                Agendar mi consultoría gratuita
                <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3" />
                </svg>
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>
