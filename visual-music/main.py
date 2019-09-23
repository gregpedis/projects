import numpy as np
from PIL import Image
import wavio

def hilbert_curve(array):
    np.transpose(array)
    pass    


def main():
    pil_im = Image.open("flame.png")
    pil_image = np.asarray(pil_im)
    # h, w, bpp = np.shape(pil_image)

    ze_song = []

    for xs in pil_image:
        for y in xs:
            ze_song.append(y[1])

    wavio.write("flame.wav",np.array(ze_song), len(ze_song))

    rate = 22050  # samples per second
    T = 3         # sample duration (seconds)
    f = 440.0     # sound frequency (Hz)
    t = np.linspace(0, T, T*rate, endpoint=False)
    x = np.sin(2*np.pi * f * t)
    wavio.write("sine24.wav", x, rate, sampwidth=3)


if __name__ == "__main__":
    main()
