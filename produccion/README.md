# 🎬 Sistema de Producción de Audio - Meditación 001

Este directorio contiene todo lo necesario para producir el audio completo de la **Meditación 001: El Puente de Luz Hacia el Plano Astral**.

## 📁 Archivos Incluidos

- **`GUIA-PRODUCCION.md`** - Guía paso a paso completa
- **`meditacion-001-voz.txt`** - Guion preparado para TTS con pausas
- **`generar_binaurales.py`** - Script Python para generar frecuencias binaurales

## 🚀 Inicio Rápido

### Paso 1: Generar Frecuencias Binaurales (OPCIONAL pero recomendado)

```bash
cd /home/user/meditaciones/produccion
python3 generar_binaurales.py
```

Este script generará:
- `meditacion-001-binaurales.wav` - Frecuencias binaurales Theta (5 Hz)
- `meditacion-001-base-musical.wav` - Base musical con armónicos sagrados (Om, Do, Sol)

**Duración:** 14 minutos
**Formato:** WAV 48 kHz estéreo
**Peso:** ~240 MB por archivo

### Paso 2: Generar Voz con TTS

Opciones:

**A) Google Cloud TTS (Recomendado)**
1. Ir a: https://cloud.google.com/text-to-speech
2. Copiar el texto de `meditacion-001-voz.txt`
3. Configurar:
   - Voz: `es-ES-Wavenet-C` (Femenina)
   - Velocidad: 0.85
   - Tono: -2.0
4. Generar y descargar como `meditacion-001-voz.mp3`

**B) ElevenLabs (Calidad Premium)**
1. Ir a: https://elevenlabs.io
2. Crear cuenta (10,000 caracteres gratis/mes)
3. Usar voz en español con estilo "meditación"
4. Generar audio

**C) TTSMaker (Gratis sin límite)**
1. Ir a: https://ttsmaker.com
2. Pegar texto
3. Seleccionar voz española femenina suave
4. Velocidad: -20%
5. Descargar

### Paso 3: Mezclar en Audacity

```bash
# Instalar Audacity si no lo tienes
# Linux:
sudo apt install audacity

# Mac:
brew install audacity

# Windows: descargar de https://www.audacityteam.org
```

**Proceso:**
1. Abrir Audacity
2. Importar:
   - `meditacion-001-voz.mp3` (generado en Paso 2)
   - `meditacion-001-base-musical.wav` (generado en Paso 1)
   - O cualquier música ambiente que encuentres
3. Ajustar niveles:
   - Voz: 0 dB
   - Música: -20 dB
4. Aplicar efectos a voz (ver `GUIA-PRODUCCION.md`)
5. Exportar como `meditacion-001-FINAL.mp3` (320 kbps)

## 📊 Especificaciones Técnicas

| Parámetro | Valor |
|-----------|-------|
| **Duración** | 12-14 minutos |
| **Sample Rate** | 48 kHz |
| **Bit Depth** | 24 bit (master), 16 bit (distribución) |
| **LUFS** | -17 dB |
| **True Peak** | -1.0 dB máximo |
| **Formato Master** | WAV |
| **Formato Distribución** | MP3 320 kbps |

## 🎯 Estructura de Archivos Recomendada

Organiza tus archivos así:

```
produccion/meditacion-001/
├── 01-binaurales-generados/
│   ├── meditacion-001-binaurales.wav
│   └── meditacion-001-base-musical.wav
├── 02-voz/
│   └── meditacion-001-voz.mp3
├── 03-mezclas/
│   ├── mix-v1.wav
│   ├── mix-v2.wav
│   └── mix-final.wav
└── 04-master/
    ├── meditacion-001.wav (master)
    └── meditacion-001.mp3 (distribución)
```

## ✅ Checklist de Calidad

Antes de publicar, verificar:

- [ ] Voz clara y sin distorsión
- [ ] Pausas respetadas (usar marcas [PAUSA: Xs])
- [ ] Música no opaca la voz
- [ ] Frecuencias binaurales audibles (con auriculares)
- [ ] Sin clics ni pops
- [ ] Volumen consistente
- [ ] Duración: 12-14 minutos
- [ ] Induce estado de calma
- [ ] Peak no excede -1.0 dB

## 🛠️ Herramientas Recomendadas

### Gratuitas
- **Audacity** - Editor de audio multiplataforma
- **Python 3** - Para generar binaurales (incluido)
- **Google Cloud TTS** - Generación de voz
- **TTSMaker** - TTS gratuito sin límite

### Premium (Opcional)
- **ElevenLabs** - Voz AI de alta calidad
- **Logic Pro X / Ableton Live** - DAWs profesionales
- **iZotope RX** - Limpieza y masterización
- **Omnisphere** - Sintetizadores ambient

## 📚 Recursos Adicionales

- **Guía completa**: Ver `GUIA-PRODUCCION.md`
- **Tutorial Audacity**: https://manual.audacityteam.org/
- **Mezcla para meditación**: https://www.youtube.com/results?search_query=mixing+guided+meditation

## 💡 Tips Profesionales

1. **Usa auriculares de calidad** durante todo el proceso
2. **Haz pausas** - tus oídos se cansan
3. **Prueba la meditación** antes de publicar
4. **Pide feedback** a 2-3 personas
5. **Guarda TODAS las versiones** - nunca sabes cuándo volverás atrás

## 🐛 Solución de Problemas

### "El script de Python no funciona"
```bash
# Verificar Python instalado
python3 --version

# Si falta, instalar:
# Linux: sudo apt install python3
# Mac: brew install python3
```

### "No puedo importar WAV en Audacity"
- Verifica que el archivo no esté corrupto
- Asegúrate de que sea estéreo 48 kHz
- Prueba convertir con: `ffmpeg -i input.wav output.wav`

### "La voz suena robótica"
- Reduce la velocidad en el TTS
- Usa servicios premium como ElevenLabs
- Considera contratar narrador humano

## 🎓 ¿Primera vez produciendo audio?

No te preocupes! La curva de aprendizaje es suave. Sigue la `GUIA-PRODUCCION.md` paso a paso y en 1-2 horas tendrás tu primer audio profesional.

---

**¿Necesitas ayuda?** Consulta la guía completa o busca tutoriales en YouTube sobre "mezclar meditación guiada en Audacity".

**¡Buena suerte con tu producción! 🎧✨**
