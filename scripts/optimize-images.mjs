import sharp from 'sharp';
import { readdir, stat, unlink } from 'fs/promises';
import { join, extname, basename, dirname } from 'path';

const ROOT = process.cwd();
const DIRS = ['public', 'src/assets'];
const EXTENSIONS = new Set(['.png', '.jpg', '.jpeg']);
const WEBP_QUALITY = 80;
const MAX_WIDTH = 1920;

async function getImages(dir) {
  const entries = await readdir(dir, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const full = join(dir, entry.name);
    if (entry.isDirectory()) {
      files.push(...await getImages(full));
    } else if (EXTENSIONS.has(extname(entry.name).toLowerCase())) {
      files.push(full);
    }
  }
  return files;
}

async function optimizeImage(filePath) {
  const info = await stat(filePath);
  const originalSize = info.size;
  const ext = extname(filePath).toLowerCase();
  const webpPath = filePath.replace(/\.(png|jpe?g)$/i, '.webp');

  let pipeline = sharp(filePath);
  const metadata = await pipeline.metadata();

  // Resize if wider than MAX_WIDTH, keeping aspect ratio
  if (metadata.width > MAX_WIDTH) {
    pipeline = pipeline.resize(MAX_WIDTH, null, { withoutEnlargement: true });
  }

  // Convert to WebP
  await pipeline
    .webp({ quality: WEBP_QUALITY, effort: 6 })
    .toFile(webpPath);

  const newInfo = await stat(webpPath);
  const saved = ((1 - newInfo.size / originalSize) * 100).toFixed(1);

  console.log(
    `${filePath.replace(ROOT, '')}` +
    `  ${(originalSize / 1024).toFixed(0)}KB -> ${(newInfo.size / 1024).toFixed(0)}KB` +
    `  (-${saved}%)`
  );

  // Remove original PNG/JPG
  await unlink(filePath);

  return { original: originalSize, optimized: newInfo.size };
}

async function main() {
  let totalOriginal = 0;
  let totalOptimized = 0;
  let count = 0;

  for (const dir of DIRS) {
    const fullDir = join(ROOT, dir);
    try {
      const images = await getImages(fullDir);
      for (const img of images) {
        const result = await optimizeImage(img);
        totalOriginal += result.original;
        totalOptimized += result.optimized;
        count++;
      }
    } catch (e) {
      // Directory might not exist
    }
  }

  console.log(`\n--- Summary ---`);
  console.log(`${count} images optimized`);
  console.log(`Total: ${(totalOriginal / 1024 / 1024).toFixed(1)}MB -> ${(totalOptimized / 1024 / 1024).toFixed(1)}MB`);
  console.log(`Saved: ${((1 - totalOptimized / totalOriginal) * 100).toFixed(1)}%`);
}

main().catch(console.error);
