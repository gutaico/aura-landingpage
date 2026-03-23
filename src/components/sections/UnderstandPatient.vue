<template>
  <section class="bg-cream-50 py-24 px-6">
    <div class="mx-auto max-w-6xl">
      <div class="text-center">
        <h2 class="font-heading text-3xl font-bold text-brown-800 sm:text-4xl">
          No somos una agencia genérica.<br>
          <span class="text-terracotta-600">Entendemos por qué tu paciente compra.</span>
        </h2>
        <p class="mx-auto mt-5 max-w-2xl text-brown-500 leading-relaxed">
          Cada anuncio, cada mensaje, cada toque de seguimiento que hacemos está diseñado
          desde la psicología de compra de tu paciente. Sabemos qué los mueve, qué los frena
          y qué los hace decir "sí".
        </p>
      </div>

      <div class="mt-16 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
        <div v-for="item in transformations" :key="item.before" class="rounded-2xl border border-cream-200 bg-white p-6">
          <div class="flex items-center gap-3 mb-4">
            <span class="text-sm font-medium text-brown-400">{{ item.before }}</span>
            <svg class="h-4 w-4 text-terracotta-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
            </svg>
            <span class="text-sm font-bold text-terracotta-600">{{ item.after }}</span>
          </div>
          <p class="text-sm leading-relaxed text-brown-500">{{ item.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const transformations = [
  {
    before: 'Inseguridad',
    after: 'Confianza',
    description: 'Tu paciente no busca un tratamiento. Busca sentirse bien consigo mismo. Nosotros hablamos a esa emoción.',
  },
  {
    before: 'Miedo',
    after: 'Curiosidad',
    description: 'Le da miedo el procedimiento, el dolor, el resultado. Nuestro contenido desmitifica el proceso real y convierte el miedo en ganas de agendar.',
  },
  {
    before: 'Desconfianza',
    after: 'Autoridad',
    description: 'Ya vio 10 anuncios iguales. Posicionamos a tu especialista como la figura de confianza: en cámara, con resultados reales.',
  },
  {
    before: '"Algún día"',
    after: 'Ahora',
    description: 'Sabe que lo quiere pero lo pospone. Convertimos la intención en acción con urgencia suave y facilitadores reales.',
  },
]
</script>
