<script setup>
import { ref, watch, nextTick, onMounted, onUnmounted } from 'vue'
import { useReveal } from './composables/useReveal'
import NavHeader from './components/NavHeader.vue'
import FooterSection from './components/FooterSection.vue'

// Agencia sections
import HeroSection from './components/sections/HeroSection.vue'
import PainStrip from './components/sections/PainStrip.vue'
import DiagnosticoSection from './components/sections/DiagnosticoSection.vue'
import SectorExpertise from './components/sections/SectorExpertise.vue'
import DiferencialesSection from './components/sections/DiferencialesSection.vue'
import AgenteShowcase from './components/sections/AgenteShowcase.vue'
import ComparativaSection from './components/sections/ComparativaSection.vue'
import OnboardingSection from './components/sections/OnboardingSection.vue'
import PortfolioSection from './components/sections/PortfolioSection.vue'
import GarantiaSection from './components/sections/GarantiaSection.vue'
import FaqSection from './components/sections/FaqSection.vue'
import CtaFinal from './components/sections/CtaFinal.vue'

// Agente sections
import HeroAgente from './components/sections/agente/HeroAgente.vue'
import PainBarAgente from './components/sections/agente/PainBarAgente.vue'
import LeadJourneyAgente from './components/sections/agente/LeadJourneyAgente.vue'
import ComparativaAgente from './components/sections/agente/ComparativaAgente.vue'
import HowItWorksAgente from './components/sections/agente/HowItWorksAgente.vue'
import ArgumentsSection from './components/sections/agente/ArgumentsSection.vue'
import ROICalculator from './components/sections/agente/ROICalculator.vue'
import FaqAgente from './components/sections/agente/FaqAgente.vue'
import CtaAgente from './components/sections/agente/CtaAgente.vue'

/* ── Hash-based routing ── */
function pageFromHash() {
  const hash = window.location.hash.replace('#/', '').split('/')[0]
  return hash === 'agente' ? 'agente' : 'agencia'
}

const currentPage = ref(pageFromHash())
const { reinit } = useReveal()

watch(currentPage, async (val) => {
  const target = val === 'agente' ? '#/agente' : '#/agencia'
  if (window.location.hash !== target) {
    history.pushState(null, '', target)
  }
  await nextTick()
  reinit()
})

function onHashChange() {
  const page = pageFromHash()
  if (page !== currentPage.value) {
    currentPage.value = page
    window.scrollTo({ top: 0 })
  }
}

onMounted(() => {
  window.addEventListener('hashchange', onHashChange)

  // If someone navigates to /agente or /agencia as a path, redirect to hash route
  const path = window.location.pathname.replace(/^\/+|\/+$/g, '')
  if (path === 'agente' || path === 'agencia') {
    history.replaceState(null, '', '/#/' + path)
    currentPage.value = path
  } else if (!window.location.hash) {
    history.replaceState(null, '', '#/agencia')
  }
})
onUnmounted(() => window.removeEventListener('hashchange', onHashChange))

function onSwitchPage(page) {
  currentPage.value = page
}

async function goToAgente() {
  currentPage.value = 'agente'
  await nextTick()
  window.scrollTo({ top: 0, behavior: 'smooth' })
}
</script>

<template>
  <NavHeader :activeTab="currentPage" @switchPage="onSwitchPage" />

  <!-- AGENCIA -->
  <main v-if="currentPage === 'agencia'">
    <HeroSection />
    <PainStrip />
    <DiagnosticoSection />
    <SectorExpertise />
    <DiferencialesSection />
    <AgenteShowcase @goAgente="goToAgente" />
    <ComparativaSection />
    <OnboardingSection />
    <PortfolioSection />
    <GarantiaSection />
    <FaqSection />
    <CtaFinal />
  </main>

  <!-- AGENTE -->
  <main v-else>
    <HeroAgente />
    <PainBarAgente />
    <LeadJourneyAgente />
    <HowItWorksAgente />
    <ArgumentsSection />
    <ROICalculator />
    <ComparativaAgente />
    <FaqAgente />
    <CtaAgente />
  </main>

  <FooterSection />
</template>
