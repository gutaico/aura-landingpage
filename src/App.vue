<script setup>
import { useReveal } from './composables/useReveal'
import NavHeader from './components/NavHeader.vue'
import HeroSection from './components/sections/HeroSection.vue'
import PainBar from './components/sections/PainBar.vue'
import UnderstandPatient from './components/sections/UnderstandPatient.vue'
import HowItWorks from './components/sections/HowItWorks.vue'
import FullSystem from './components/sections/FullSystem.vue'
import GuaranteeSection from './components/sections/GuaranteeSection.vue'
import Results from './components/sections/Results.vue'
import WhyAura from './components/sections/WhyAura.vue'
import CtaForm from './components/sections/CtaForm.vue'
import FaqSection from './components/sections/FaqSection.vue'
import FooterSection from './components/FooterSection.vue'

useReveal()
</script>

<template>
  <NavHeader />
  <main>
    <HeroSection />
    <PainBar />
    <UnderstandPatient />
    <HowItWorks />
    <FullSystem />
    <GuaranteeSection />
    <Results />
    <WhyAura />
    <CtaForm />
    <FaqSection />
  </main>
  <FooterSection />
</template>
