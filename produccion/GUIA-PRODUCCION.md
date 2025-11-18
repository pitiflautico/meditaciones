# 🎵 GUÍA DE PRODUCCIÓN COMPLETA - MEDITACIÓN 001

## 🎯 OBJETIVO
Producir el audio completo de la Meditación 001: "El Puente de Luz Hacia el Plano Astral"

---

## 📋 PASO 1: GENERAR AUDIO DE VOZ

### Opción A: Servicios TTS Online Gratuitos (Recomendado para comenzar)

**1. Google Cloud Text-to-Speech (Gratis hasta 1M caracteres/mes)**
- URL: https://cloud.google.com/text-to-speech
- Voces recomendadas en español:
  - `es-ES-Standard-A` (Femenina, España)
  - `es-US-Neural2-A` (Femenina, EEUU)
  - `es-ES-Wavenet-C` (Femenina, alta calidad)
- Configuración:
  - Speaking rate: 0.85
  - Pitch: -2.0
  - Audio encoding: MP3
  - Sample rate: 48000 Hz

**2. ElevenLabs (Calidad Premium - 10,000 caracteres gratis/mes)**
- URL: https://elevenlabs.io
- Modelo: Multilingual v2
- Voz: Buscar "meditación" o "calma"
- Configuración:
  - Stability: 75%
  - Clarity: 80%
  - Style exaggeration: 0%

**3. TTSMaker (Completamente gratis)**
- URL: https://ttsmaker.com
- Idioma: Español
- Voz: Seleccionar una voz femenina suave
- Velocidad: -20%

### Opción B: Grabación con Voz Humana Real
- Contratar narrador/a profesional en Fiverr, Upwork o similares
- Proporcionar el archivo `meditacion-001-voz.txt`
- Especificaciones: Voz cálida, hipnótica, femenina preferiblemente

### 📝 Archivo a usar:
- **Texto**: `/home/user/meditaciones/produccion/meditacion-001-voz.txt`

---

## 🎼 PASO 2: GENERAR MÚSICA Y FRECUENCIAS BINAURALES

### Opción A: Música Pre-hecha (Recomendado)

**Fuentes de Música Libre de Derechos:**

1. **YouTube Audio Library**
   - Buscar: "meditation ambient" "theta waves" "binaural beats"
   - Filtrar: No copyright

2. **Free Music Archive (FMA)**
   - URL: https://freemusicarchive.org
   - Buscar: meditation, ambient, drone, theta

3. **Pixabay Music**
   - URL: https://pixabay.com/music/
   - Buscar: meditation, calm, peaceful

**Características que debe tener la música:**
- Duración: 14-15 minutos
- BPM: 40-50
- Estilo: Ambient espacial, drones suaves
- Frecuencias binaurales: 4-7 Hz (Theta) si es posible
- Instrumentos: Cuencos tibetanos, sintetizadores suaves, pads

### Opción B: Crear Frecuencias Binaurales Propias

**Herramientas Online Gratuitas:**

1. **Gnaural** (Software descargable gratuito)
   - URL: https://gnaural.sourceforge.net
   - Crear preset: Theta 5 Hz
   - Duración: 14 minutos
   - Exportar como WAV

2. **MyNoise.net**
   - URL: https://mynoise.net/NoiseMachines/binauralBrainwaveGenerator.php
   - Configurar: Theta (4-7 Hz)
   - Grabar con software de captura de audio

### Opción C: Usar YouTube y Descargar

**Videos recomendados para descargar (verificar licencia):**
- "15 minute theta binaural beats meditation"
- "Ambient space music for meditation"
- "Tibetan singing bowls 15 minutes"

**Herramienta de descarga:**
- yt-dlp (línea de comandos)
- 4K Video Downloader
- SOLO usar videos con licencia Creative Commons

---

## 🎛️ PASO 3: MEZCLAR AUDIO (Voz + Música)

### Opción A: Audacity (Gratis, Multiplataforma)

**Instalación:**
```bash
# Linux
sudo apt install audacity

# Mac
brew install audacity

# Windows
Descargar de: https://www.audacityteam.org
```

**Proceso de Mezcla:**

1. **Importar Archivos**
   - Abrir Audacity
   - Archivo → Importar → Audio
   - Importar: voz.mp3 y musica.mp3

2. **Configurar Niveles**
   - Pista de voz: 0 dB (dejar como está)
   - Pista de música: -20 dB
   - Usar la herramienta de Amplificar/Normalizar

3. **Ajustar Música Durante Pausas**
   - Durante introducción (0-30s): Música -18 dB
   - Durante narración activa: Música -22 dB
   - Durante pausas largas (8s): Música -18 dB
   - Durante experiencia (min 7-10): Música -16 dB

4. **Aplicar Efectos a Voz**
   - Seleccionar pista de voz
   - Efecto → Ecualizador
     - Corte pasa-altos: 80 Hz
     - Realce: 3 kHz (+2 dB)
   - Efecto → Compresor
     - Ratio: 3:1
     - Threshold: -12 dB
   - Efecto → Reverb
     - Room size: 50%
     - Damping: 50%
     - Wet: 12%

5. **Fade In/Out**
   - Música: Fade in 3s al inicio, Fade out 5s al final

6. **Exportar**
   - Archivo → Exportar → Exportar como WAV
   - Calidad: 48000 Hz, 24 bit
   - Archivo → Exportar → Exportar como MP3
   - Calidad: 320 kbps

### Opción B: Usar Servicios Online

**1. AudioMass (Editor online gratuito)**
- URL: https://audiomass.co
- Importar ambas pistas
- Mezclar manualmente

**2. TwistedWave Online**
- URL: https://twistedwave.com/online
- Gratis para archivos <5min (necesitarías dividir)

---

## 📊 PASO 4: MASTERIZACIÓN FINAL

### En Audacity:

1. **Normalizar**
   - Efecto → Normalizar
   - Peak amplitude: -1.0 dB

2. **Compresor Multibanda** (si está disponible)
   - Suave, solo para cohesión

3. **Verificar Niveles**
   - Analizar → Medidor de nivel
   - LUFS objetivo: -17 dB

4. **Exportación Final**
   - **Master**: WAV 48 kHz / 24 bit
   - **Distribución**: MP3 320 kbps
   - **Móvil**: MP3 192 kbps (más ligero)

---

## 🗂️ ESTRUCTURA DE ARCHIVOS FINAL

```
/home/user/meditaciones/produccion/meditacion-001/
├── 01-voz-raw.mp3         (Voz generada con TTS)
├── 02-musica-base.mp3     (Música ambiente seleccionada)
├── 03-mix-draft.wav       (Primera mezcla de prueba)
├── 04-mix-final.wav       (Mezcla final masterizada)
├── meditacion-001.mp3     (Versión final para distribución)
└── meditacion-001.wav     (Versión master de alta calidad)
```

---

## ✅ CHECKLIST DE CALIDAD

Antes de considerar finalizado, verificar:

- [ ] La voz es clara y se entiende perfectamente
- [ ] Las pausas respetan los tiempos indicados
- [ ] La música no opaca la voz en ningún momento
- [ ] Las frecuencias binaurales son audibles (con auriculares)
- [ ] No hay clics, pops o distorsión
- [ ] El volumen es consistente en toda la grabación
- [ ] La duración total es 12-14 minutos
- [ ] El audio induce un estado de calma al escucharlo
- [ ] Las transiciones musicales son suaves
- [ ] El archivo final no excede -1 dB de peak

---

## 🚀 PROCESO AUTOMATIZADO (Para usuarios avanzados)

Si tienes ffmpeg instalado, puedes automatizar parte del proceso:

```bash
# Instalar ffmpeg
# Linux: sudo apt install ffmpeg
# Mac: brew install ffmpeg

# Mezclar voz y música
ffmpeg -i voz.mp3 -i musica.mp3 \
  -filter_complex "[1:a]volume=0.25[m];[0:a][m]amix=inputs=2:duration=first" \
  -c:a libmp3lame -b:a 320k \
  meditacion-001.mp3
```

---

## 📞 SOPORTE Y RECURSOS

**Tutoriales de Audacity:**
- YouTube: "Audacity tutorial español meditación"
- Documentación oficial: https://manual.audacityteam.org

**Comunidades:**
- Reddit: r/audioengineering, r/meditation
- Discord: Servidores de producción de audio

---

## 💡 CONSEJOS FINALES

1. **Escucha con auriculares de calidad** durante todo el proceso
2. **Prueba la meditación tú mismo** antes de publicar
3. **Pide feedback** a 2-3 personas
4. **Itera**: La primera versión rara vez es la final
5. **Guarda todas las versiones** por si necesitas volver atrás

---

**¿Listo para producir tu primera meditación guiada profesional?** 🎧✨

Comienza por el Paso 1: Generar el audio de voz. Una vez tengas ese archivo, continúa con los siguientes pasos en orden.
