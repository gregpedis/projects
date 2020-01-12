import os
import io
import numpy as np
import hilbert as hb
from PIL import Image
from matplotlib import cm
from scipy.io import wavfile as wf

base_dir = os.getcwd()
input_dir = f'{base_dir}\\data\\input'
output_dir = f'{base_dir}\\data\\output'

image_example = f"{input_dir}\\flame.png"
sound_example = f"{input_dir}\\example.wav"

def main():   
    # pil_im = Image.open(image_example)
    # pil_image = np.asarray(pil_im)
    # h, w, bpp = np.shape(pil_image)

    fs,data =  wf.read(sound_example)
    normal_line = hb.normalize_line_size(data)
    result_image = hb.hilb_space(normal_line)

    im = Image.fromarray(np.uint8(cm.gist_earth(result_image)*255))
    im.save('something','JPEG')

if __name__ == "__main__":
    main()
