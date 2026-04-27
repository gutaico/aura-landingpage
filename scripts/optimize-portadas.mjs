import sharp from 'sharp'
import { readdirSync, mkdirSync } from 'fs'
import { join, parse } from 'path'

const SRC = 'public/img/portadas_reels'
const OUT = 'public/img/portadas_reels/optimized'

mkdirSync(OUT, { recursive: true })

const files = readdirSync(SRC).filter(f => /\.(jpg|jpeg|png)$/i.test(f))

for (const file of files) {
  const { name } = parse(file)
  await sharp(join(SRC, file))
    .resize({ width: 600, withoutEnlargement: true })
    .webp({ quality: 80 })
    .toFile(join(OUT, `${name}.webp`))
  console.log(`✓ ${file} → ${name}.webp`)
}

console.log(`\nDone — ${files.length} images optimized`)
