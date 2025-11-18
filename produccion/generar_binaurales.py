#!/usr/bin/env python3
"""
Generador de Frecuencias Binaurales para Meditación
Crea audio con ondas binaurales en frecuencias Theta (4-7 Hz)
"""

import math
import wave
import struct
import sys

def generar_onda_sinusoidal(frecuencia, duracion, sample_rate=48000, amplitud=0.3):
    """
    Genera una onda sinusoidal pura.

    Args:
        frecuencia: Frecuencia en Hz
        duracion: Duración en segundos
        sample_rate: Tasa de muestreo (Hz)
        amplitud: Amplitud de la onda (0.0 a 1.0)

    Returns:
        Lista de muestras de audio
    """
    num_samples = int(duracion * sample_rate)
    samples = []

    for i in range(num_samples):
        # Calcular el valor de la onda sinusoidal
        t = i / sample_rate
        valor = amplitud * math.sin(2 * math.pi * frecuencia * t)
        samples.append(valor)

    return samples

def generar_binaural(frecuencia_base, frecuencia_binaural, duracion,
                     output_file="binaural.wav", sample_rate=48000):
    """
    Genera un archivo WAV estéreo con frecuencias binaurales.

    Args:
        frecuencia_base: Frecuencia portadora en Hz (ej: 200 Hz)
        frecuencia_binaural: Diferencia binaural en Hz (ej: 5 Hz para Theta)
        duracion: Duración en segundos
        output_file: Nombre del archivo de salida
        sample_rate: Tasa de muestreo
    """

    print(f"🎵 Generando audio binaural...")
    print(f"   Frecuencia base: {frecuencia_base} Hz")
    print(f"   Frecuencia binaural: {frecuencia_binaural} Hz (Theta)")
    print(f"   Duración: {duracion} segundos ({duracion/60:.1f} minutos)")
    print(f"   Archivo: {output_file}")

    # Generar canal izquierdo (frecuencia base)
    canal_izquierdo = generar_onda_sinusoidal(
        frecuencia_base, duracion, sample_rate, amplitud=0.15
    )

    # Generar canal derecho (frecuencia base + diferencia binaural)
    canal_derecho = generar_onda_sinusoidal(
        frecuencia_base + frecuencia_binaural, duracion, sample_rate, amplitud=0.15
    )

    # Crear archivo WAV
    with wave.open(output_file, 'w') as wav_file:
        # Configurar parámetros del archivo WAV
        num_canales = 2  # Estéreo
        sample_width = 2  # 16 bits
        framerate = sample_rate
        num_frames = len(canal_izquierdo)

        wav_file.setparams((num_canales, sample_width, framerate,
                           num_frames, 'NONE', 'not compressed'))

        # Escribir los datos de audio
        for i in range(num_frames):
            # Convertir valores flotantes (-1 a 1) a enteros de 16 bits
            muestra_izq = int(canal_izquierdo[i] * 32767)
            muestra_der = int(canal_derecho[i] * 32767)

            # Empaquetar en formato de 16 bits little-endian
            data = struct.pack('<hh', muestra_izq, muestra_der)
            wav_file.writeframes(data)

    print(f"✅ Archivo generado exitosamente: {output_file}")
    print(f"   Tamaño: {num_frames * num_canales * sample_width / 1024 / 1024:.2f} MB")

def crear_mezcla_frecuencias(duracion, output_file="meditacion_base.wav"):
    """
    Crea una base musical con múltiples frecuencias armónicas.
    """

    print(f"🎼 Creando base musical con armónicos...")

    sample_rate = 48000
    num_samples = int(duracion * sample_rate)

    # Crear canales vacíos
    canal_izq = [0.0] * num_samples
    canal_der = [0.0] * num_samples

    # Frecuencias armónicas (basadas en la escala natural)
    # Usamos frecuencias que resuenan bien juntas
    frecuencias = [
        (136.10, 0.08),  # Om primordial (C#)
        (256.00, 0.06),  # Do (C)
        (384.00, 0.04),  # Sol (G)
        (512.00, 0.03),  # Do alto (C)
    ]

    for freq, amp in frecuencias:
        print(f"   Añadiendo armónico: {freq} Hz (amplitud {amp})")

        # Generar para canal izquierdo
        onda_izq = generar_onda_sinusoidal(freq, duracion, sample_rate, amp)
        # Generar para canal derecho (ligeramente diferente para crear espacialidad)
        onda_der = generar_onda_sinusoidal(freq + 0.5, duracion, sample_rate, amp)

        # Sumar a los canales
        for i in range(num_samples):
            canal_izq[i] += onda_izq[i]
            canal_der[i] += onda_der[i]

    # Normalizar para evitar clipping
    max_valor = max(max(abs(x) for x in canal_izq), max(abs(x) for x in canal_der))
    if max_valor > 0.9:
        factor_normalizacion = 0.9 / max_valor
        canal_izq = [x * factor_normalizacion for x in canal_izq]
        canal_der = [x * factor_normalizacion for x in canal_der]

    # Guardar archivo
    with wave.open(output_file, 'w') as wav_file:
        wav_file.setparams((2, 2, sample_rate, num_samples, 'NONE', 'not compressed'))

        for i in range(num_samples):
            muestra_izq = int(canal_izq[i] * 32767)
            muestra_der = int(canal_der[i] * 32767)
            data = struct.pack('<hh', muestra_izq, muestra_der)
            wav_file.writeframes(data)

    print(f"✅ Base musical generada: {output_file}")

def main():
    """
    Función principal del script.
    """

    print("=" * 60)
    print("🧘 GENERADOR DE FRECUENCIAS BINAURALES PARA MEDITACIÓN")
    print("=" * 60)
    print()

    # Parámetros para Meditación 001
    duracion = 14 * 60  # 14 minutos en segundos

    # Opción 1: Generar solo binaurales puros
    print("📋 OPCIÓN 1: Generar frecuencias binaurales Theta (5 Hz)")
    print()
    respuesta = input("¿Deseas generar binaurales puros? (s/n): ").lower()

    if respuesta == 's':
        generar_binaural(
            frecuencia_base=200,  # Frecuencia portadora
            frecuencia_binaural=5,  # 5 Hz = Theta medio
            duracion=duracion,
            output_file="meditacion-001-binaurales.wav"
        )
        print()

    # Opción 2: Generar base musical con armónicos
    print("📋 OPCIÓN 2: Generar base musical con armónicos sagrados")
    print()
    respuesta2 = input("¿Deseas generar base musical armónica? (s/n): ").lower()

    if respuesta2 == 's':
        crear_mezcla_frecuencias(
            duracion=duracion,
            output_file="meditacion-001-base-musical.wav"
        )
        print()

    print("=" * 60)
    print("✨ PROCESO COMPLETADO")
    print("=" * 60)
    print()
    print("📝 SIGUIENTES PASOS:")
    print("   1. Importa los archivos WAV generados en Audacity")
    print("   2. Añade la pista de voz")
    print("   3. Ajusta los niveles según la guía de producción")
    print("   4. Exporta la mezcla final")
    print()
    print("🎧 Recuerda escuchar con AURICULARES para percibir el efecto binaural")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Proceso cancelado por el usuario")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        sys.exit(1)
