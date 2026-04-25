<script setup>
import { ref, watch, onMounted } from 'vue'

const props = defineProps({
  src: { type: String, required: true },
  alt: { type: String, default: '' },
  threshold: { type: Number, default: 40 },
  feather: { type: Number, default: 20 },
})

const processedSrc = ref(null)
const loading = ref(true)

function removeWhiteBg(imgSrc) {
  return new Promise((resolve) => {
    const img = new Image()
    img.crossOrigin = 'anonymous'
    img.onload = () => {
      const canvas = document.createElement('canvas')
      canvas.width = img.naturalWidth
      canvas.height = img.naturalHeight
      const ctx = canvas.getContext('2d')
      ctx.drawImage(img, 0, 0)

      const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height)
      const data = imageData.data
      const t = 255 - props.threshold
      const f = props.feather

      for (let i = 0; i < data.length; i += 4) {
        const r = data[i]
        const g = data[i + 1]
        const b = data[i + 2]

        if (r >= t && g >= t && b >= t) {
          data[i + 3] = 0
        } else if (f > 0) {
          const dist = Math.min(255 - r, 255 - g, 255 - b)
          if (dist < props.threshold + f) {
            const alpha = Math.min(255, Math.round((dist - (255 - t)) * (255 / f)))
            if (alpha < data[i + 3]) {
              data[i + 3] = Math.max(0, alpha)
            }
          }
        }
      }

      ctx.putImageData(imageData, 0, 0)
      resolve(canvas.toDataURL('image/png'))
    }
    img.onerror = () => resolve(imgSrc)
    img.src = imgSrc
  })
}

async function process() {
  loading.value = true
  processedSrc.value = await removeWhiteBg(props.src)
  loading.value = false
}

onMounted(process)
watch(() => props.src, process)
</script>

<template>
  <img
    v-if="processedSrc"
    :src="processedSrc"
    :alt="alt"
    v-bind="$attrs"
  />
</template>
