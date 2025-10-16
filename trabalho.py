import librosa
import numpy as np
import os

!wget https://raw.githubusercontent.com/RogerFialho/sinais-e-sistemas-trabalho/main/marcha_imperial.wav

audio = "marcha_imperial.wav"

y, sr = librosa.load(audio)
n = len(y)
print("Amostras:", n)
print("Frequência de amostragem:", sr)
print(f"Duração: {n / sr:.1f} segundos")

energia = np.sum(y**2)
print(f"Energia: {energia:.2f}")

potencia = energia / n
print(f"Potencia: {potencia:.5f}")
