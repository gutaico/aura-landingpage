<script setup>
const items = [
  {
    num: '01',
    title: 'La meta la definimos juntos',
    body: 'Durante el onboarding cruzamos tu inversión, tu capacidad operativa y los benchmarks del sector. El número mínimo lo firmamos ambos.',
  },
  {
    num: '02',
    title: 'Compromiso bilateral',
    body: 'Nosotros ponemos el mecanismo, tú pones la respuesta a los leads y el presupuesto acordado. Si ambos cumplimos y no llegan los resultados, el dinero es tuyo.',
  },
  {
    num: '03',
    title: 'Ninguna agencia te ofrece esto',
    body: 'Podemos hacerlo porque confiamos en el mecanismo. Si no funciona, preferimos devolver el dinero y quedarnos con la reputación intacta.',
  },
]

const starPositions = [
  { top: '0', left: '50%', transform: 'translateX(-50%) translateY(-50%)' },
  { bottom: '0', left: '50%', transform: 'translateX(-50%) translateY(50%)' },
  { left: '0', top: '50%', transform: 'translateY(-50%) translateX(-50%)' },
  { right: '0', top: '50%', transform: 'translateY(-50%) translateX(50%)' },
]
</script>

<template>
  <section
    id="garantia"
    class="aura-section-pad"
    :style="{
      background: 'var(--color-cream-100)',
      padding: 'clamp(5rem, 8vw, 9rem) 2.5rem',
      borderTop: '1px solid rgba(221,209,186,0.8)',
    }"
  >
    <div :style="{ maxWidth: '1200px', margin: '0 auto' }">
      <div
        class="aura-hero-grid"
        :style="{
          display: 'grid',
          gridTemplateColumns: '1fr 1fr',
          gap: '5rem',
          alignItems: 'center',
        }"
      >
        <!-- Left: Badge -->
        <div class="reveal" :style="{ display: 'flex', justifyContent: 'center' }">
          <div :style="{
            position: 'relative',
            width: 'min(420px, 90vw)',
            aspectRatio: '1/1',
          }">
            <!-- Outer rotating ring with text on path -->
            <svg
              viewBox="0 0 400 400"
              :style="{
                position: 'absolute',
                inset: 0,
                width: '100%',
                height: '100%',
                animation: 'auraSpin 40s linear infinite',
              }"
            >
              <defs>
                <path
                  id="circlePath"
                  d="M 200,200 m -180,0 a 180,180 0 1,1 360,0 a 180,180 0 1,1 -360,0"
                />
              </defs>
              <text
                fill="var(--color-brown-700)"
                :style="{
                  fontFamily: 'var(--font-ui)',
                  fontSize: '18px',
                  letterSpacing: '0.5em',
                  fontWeight: 500,
                  textTransform: 'uppercase',
                }"
              >
                <textPath href="#circlePath">
                  &middot; GARANT&Iacute;A &middot; 30 D&Iacute;AS &middot; DEVOLUCI&Oacute;N TOTAL &middot; SIN LETRA CHICA &middot; GARANT&Iacute;A &middot; 30 D&Iacute;AS &middot; DEVOLUCI&Oacute;N TOTAL &middot;
                </textPath>
              </text>
            </svg>

            <!-- Dotted ring -->
            <svg
              viewBox="0 0 400 400"
              :style="{
                position: 'absolute',
                inset: '30px',
                width: 'calc(100% - 60px)',
                height: 'calc(100% - 60px)',
              }"
            >
              <circle
                cx="200"
                cy="200"
                r="180"
                fill="none"
                stroke="var(--color-terracotta-500)"
                stroke-width="1"
                stroke-dasharray="2 6"
                opacity="0.5"
              />
            </svg>

            <!-- Inner badge -->
            <div :style="{
              position: 'absolute',
              inset: '18%',
              borderRadius: '50%',
              background: 'radial-gradient(circle at 30% 30%, var(--color-terracotta-400), var(--color-terracotta-500) 60%, var(--color-terracotta-700))',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center',
              color: 'white',
              textAlign: 'center',
              boxShadow: 'inset 0 -10px 40px rgba(0,0,0,0.2), 0 30px 60px rgba(145,65,38,0.35)',
              transform: 'rotate(-6deg)',
            }">
              <!-- Inner border ring -->
              <div :style="{
                position: 'absolute',
                inset: '12px',
                borderRadius: '50%',
                border: '1px solid rgba(255,255,255,0.3)',
                pointerEvents: 'none',
              }"></div>

              <p :style="{
                fontFamily: 'var(--font-ui)',
                fontSize: '0.75rem',
                fontWeight: 500,
                letterSpacing: '0.4em',
                textTransform: 'uppercase',
                margin: '0 0 0.4rem',
                opacity: 0.9,
              }">
                Garantía
              </p>

              <span :style="{
                display: 'block',
                width: '42px',
                height: '1px',
                background: 'rgba(255,255,255,0.5)',
                marginBottom: '0.65rem',
              }"></span>

              <p :style="{
                fontFamily: 'var(--font-display)',
                fontWeight: 400,
                fontStyle: 'italic',
                fontSize: '5rem',
                lineHeight: 0.9,
                margin: 0,
                letterSpacing: '-0.03em',
                textShadow: '0 4px 16px rgba(0,0,0,0.25)',
              }">
                30
              </p>

              <p :style="{
                fontFamily: 'var(--font-display)',
                fontWeight: 500,
                fontSize: '1rem',
                textTransform: 'uppercase',
                letterSpacing: '0.4em',
                margin: '0.4rem 0 0.65rem',
                opacity: 0.95,
              }">
                días
              </p>

              <span :style="{
                display: 'block',
                width: '42px',
                height: '1px',
                background: 'rgba(255,255,255,0.5)',
                marginBottom: '0.65rem',
              }"></span>

              <p :style="{
                fontFamily: 'var(--font-ui-alt)',
                fontStyle: 'italic',
                fontSize: '0.78rem',
                margin: 0,
                opacity: 0.85,
                letterSpacing: '0.05em',
              }">
                o tu dinero de vuelta
              </p>
            </div>

            <!-- Decorative stars at cardinal points -->
            <span
              v-for="(pos, i) in starPositions"
              :key="i"
              :style="{
                position: 'absolute',
                ...pos,
                fontFamily: 'var(--font-ui)',
                fontSize: '0.85rem',
                color: 'var(--color-terracotta-500)',
                animation: `auraStar 3s ease-in-out ${i * 0.75}s infinite`,
                pointerEvents: 'none',
              }"
              aria-hidden="true"
            >&#10022;</span>
          </div>
        </div>

        <!-- Right: Copy -->
        <div>
          <div class="reveal">
            <p :style="{
              fontFamily: 'var(--font-ui)',
              fontSize: '0.7rem',
              fontWeight: 500,
              textTransform: 'uppercase',
              letterSpacing: '0.28em',
              color: 'var(--color-terracotta-500)',
              margin: '0 0 1.25rem',
            }">
              &sect; VIII &middot; Garantía
            </p>

            <h2 :style="{
              fontFamily: 'var(--font-display)',
              fontWeight: 400,
              fontSize: 'clamp(2rem, 4vw, 3rem)',
              lineHeight: 1.05,
              letterSpacing: '-0.022em',
              margin: '0 0 2rem',
              color: 'var(--color-brown-900)',
            }">
              Si no cumplimos, devolvemos todo.
              <span :style="{ fontStyle: 'italic', color: 'var(--color-terracotta-500)' }">Literalmente todo</span>.
            </h2>
          </div>

          <!-- Numbered items -->
          <div :style="{ display: 'flex', flexDirection: 'column', gap: '2.25rem' }">
            <div
              v-for="(item, i) in items"
              :key="i"
              class="reveal"
              :class="`reveal-delay-${i + 1}`"
              :style="{
                display: 'grid',
                gridTemplateColumns: 'auto 1fr',
                gap: '1.25rem',
                alignItems: 'start',
              }"
            >
              <span :style="{
                fontFamily: 'var(--font-display)',
                fontWeight: 400,
                fontStyle: 'italic',
                fontSize: '2rem',
                lineHeight: 1,
                color: 'var(--color-terracotta-300)',
                opacity: 0.5,
              }">
                {{ item.num }}
              </span>
              <div>
                <h3 :style="{
                  fontFamily: 'var(--font-display)',
                  fontWeight: 500,
                  fontSize: '1.1rem',
                  color: 'var(--color-brown-900)',
                  margin: '0 0 0.5rem',
                  letterSpacing: '-0.005em',
                }">
                  {{ item.title }}
                </h3>
                <p :style="{
                  fontFamily: 'var(--font-body)',
                  fontSize: '0.88rem',
                  lineHeight: 1.6,
                  color: 'var(--color-brown-400)',
                  margin: 0,
                }">
                  {{ item.body }}
                </p>
              </div>
            </div>
          </div>

          <!-- Closing italic quote -->
          <div class="reveal reveal-delay-4" :style="{ marginTop: '2.5rem' }">
            <p :style="{
              fontFamily: 'var(--font-body-alt)',
              fontStyle: 'italic',
              fontSize: '1.05rem',
              lineHeight: 1.55,
              color: 'var(--color-terracotta-500)',
              margin: 0,
              maxWidth: '42ch',
            }">
              "Tu peor escenario es que te devolvamos todo el dinero. Tu mejor escenario es una máquina que te trae clientes cada semana."
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
