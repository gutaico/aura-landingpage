<script setup>
import NavHeader from './components/NavHeader.vue'
import HeroSection from './components/sections/HeroSection.vue'
import PainBar from './components/sections/PainBar.vue'
import UnderstandPatient from './components/sections/UnderstandPatient.vue'
import HowItWorks from './components/sections/HowItWorks.vue'
import FullSystem from './components/sections/FullSystem.vue'
import Results from './components/sections/Results.vue'
import WhyAura from './components/sections/WhyAura.vue'
import CtaForm from './components/sections/CtaForm.vue'
import FaqSection from './components/sections/FaqSection.vue'
import FooterSection from './components/FooterSection.vue'
</script>

<template>
  <NavHeader />
  <main>
    <HeroSection />
    <PainBar />
    <UnderstandPatient />
    <HowItWorks />
    <FullSystem />
    <Results />
    <WhyAura />
    <CtaForm />
    <FaqSection />
  </main>
  <FooterSection />
</template>
