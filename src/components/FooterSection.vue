<script setup>
const linkColumns = [
  {
    title: 'Producto',
    items: ['Agente IA', 'Agencia', 'Precios', 'Garantia'],
  },
  {
    title: 'Recursos',
    items: ['Blog', 'Casos de exito', 'Playbook', 'FAQ'],
  },
  {
    title: 'Contacto',
    items: ['WhatsApp', 'Email', 'Guadalajara, México', 'Lun-Sab'],
  },
]

const legalLinks = ['Terminos', 'Privacidad', 'Cookies']

const grainBg = "url(\"data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E\")"

function handleLinkEnter(e) {
  e.target.style.color = 'var(--color-cream-50)'
}
function handleLinkLeave(e) {
  e.target.style.color = 'rgb(234, 225, 208, 0.75)'
}
</script>

<template>
  <footer
    :style="{
      background: 'var(--color-brown-900)',
      color: 'var(--color-cream-50)',
      position: 'relative',
      overflow: 'hidden',
      padding: '5rem clamp(1.25rem, 4vw, 2.5rem) 2.5rem',
    }"
  >
    <!-- Grain overlay -->
    <div
      aria-hidden="true"
      :style="{
        position: 'absolute',
        inset: 0,
        backgroundImage: grainBg,
        backgroundSize: '180px',
        opacity: 0.03,
        pointerEvents: 'none',
      }"
    ></div>

    <div :style="{ maxWidth: '1200px', margin: '0 auto', position: 'relative' }">
      <!-- Main grid -->
      <div
        class="aura-footer-grid"
        :style="{
          display: 'grid',
          gridTemplateColumns: '1.3fr 1fr 1fr 1fr',
          gap: '3rem',
          paddingBottom: '3rem',
          borderBottom: '1px solid rgba(102,48,30,0.5)',
        }"
      >
        <!-- Brand column -->
        <div>
          <img
            src="/logo-light.webp"
            alt="Aura"
            :style="{ height: '24px', marginBottom: '1.25rem' }"
          />
          <p
            :style="{
              fontFamily: 'var(--font-body-alt)',
              fontStyle: 'italic',
              fontSize: '1rem',
              lineHeight: 1.6,
              color: 'rgb(234, 225, 208, 0.7)',
              margin: 0,
              maxWidth: '32ch',
            }"
          >
            Publicidad que se mide en pacientes. Para clinicas de estetica, wellness y salud personal.
          </p>
        </div>

        <!-- Link columns -->
        <div v-for="col in linkColumns" :key="col.title">
          <p
            :style="{
              fontFamily: 'var(--font-ui)',
              fontSize: '0.68rem',
              fontWeight: 500,
              textTransform: 'uppercase',
              letterSpacing: '0.2em',
              color: 'var(--color-terracotta-300)',
              margin: '0 0 1.1rem',
            }"
          >
            {{ col.title }}
          </p>
          <ul
            :style="{
              listStyle: 'none',
              margin: 0,
              padding: 0,
              display: 'flex',
              flexDirection: 'column',
              gap: '0.75rem',
            }"
          >
            <li v-for="item in col.items" :key="item">
              <a
                href="#"
                :style="{
                  fontFamily: 'var(--font-ui)',
                  fontSize: '0.85rem',
                  color: 'rgb(234, 225, 208, 0.75)',
                  textDecoration: 'none',
                  transition: 'color .3s',
                }"
                @mouseenter="handleLinkEnter"
                @mouseleave="handleLinkLeave"
              >
                {{ item }}
              </a>
            </li>
          </ul>
        </div>
      </div>

      <!-- Bottom bar -->
      <div
        :style="{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          paddingTop: '2rem',
          gap: '2rem',
          flexWrap: 'wrap',
        }"
      >
        <p
          :style="{
            fontFamily: 'var(--font-ui-alt)',
            fontStyle: 'italic',
            fontSize: '0.8rem',
            color: 'rgb(206, 190, 162, 0.5)',
            margin: 0,
          }"
        >
          &copy; 2026 Aura Marketing &middot; Una vertical de Gutai Co. Advertising
        </p>
        <div :style="{ display: 'flex', gap: '1.5rem' }">
          <a
            v-for="link in legalLinks"
            :key="link"
            href="#"
            :style="{
              fontFamily: 'var(--font-ui)',
              fontSize: '0.72rem',
              color: 'rgb(206, 190, 162, 0.55)',
              textDecoration: 'none',
              textTransform: 'uppercase',
              letterSpacing: '0.12em',
            }"
          >
            {{ link }}
          </a>
        </div>
      </div>
    </div>
  </footer>
</template>
