import { onMounted, onUnmounted } from 'vue'

let observer = null

function initObserver() {
  if (observer) observer.disconnect()

  observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible')
          observer.unobserve(entry.target)
        }
      })
    },
    { threshold: 0.12, rootMargin: '0px 0px -8% 0px' }
  )

  document.querySelectorAll('.reveal:not(.visible)').forEach((el) => observer.observe(el))
}

export function useReveal() {
  onMounted(() => initObserver())
  onUnmounted(() => {
    if (observer) observer.disconnect()
  })

  return {
    reinit() {
      // Reset all reveal elements and re-observe
      document.querySelectorAll('.reveal').forEach((el) => el.classList.remove('visible'))
      setTimeout(() => initObserver(), 50)
    }
  }
}
