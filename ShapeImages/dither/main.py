from PIL import Image

img_path = "/mnt/c/Users/trafa/Desktop/lena.jpg"

res_path1 = "/mnt/c/Users/trafa/Desktop/dither1.jpg"
res_path2 = "/mnt/c/Users/trafa/Desktop/dither2.jpg"
res_path3 = "/mnt/c/Users/trafa/Desktop/dither3.jpg"

weights1 = [7,3,5,1]
weights2 = [4,4,4,4]
weights3 = [0,0,0,16]
total = 16


def propagate_error(row, col, error, pixel_data, weights):
    max_x = len(pixel_data)
    max_y = len(pixel_data[0])
    if row+1 < max_x:
        pixel_data[row+1][col] += weights[0] * error / total
    if col+1 < max_y:
        pixel_data[row][col+1] += weights[2] * error / total
        if row-1 > 0:
            pixel_data[row-1][col+1] += weights[1] * error / total
        if row+1 < max_x:
            pixel_data[row+1][col+1] += weights[3] * error / total

def apply_grayscale(im):
    max_x, max_y = im.size
    pixel_data = [[0 for _ in range(max_x)] for _ in range(max_y)]
    for i in range(max_x):
        for j in range(max_y):
            (r,g,b, *args) = im.getpixel((i,j))
            gray = (r+g+b)//3
            pixel_data[j][i] = gray
    return pixel_data

def apply_dither(grayscale_data, im, weights):
    for j in range(len(grayscale_data)):
        for i in range((len(grayscale_data[0]))):
            old = grayscale_data[j][i]
            new = 255 if old > 127 else 0
            error = old - new
            propagate_error(j, i, error, grayscale_data, weights)
            im.putpixel((i,j), (new,new,new))


def main(res_path, weights):
    with Image.open(img_path) as im:
        grayscale_data = apply_grayscale(im)
        apply_dither(grayscale_data, im, weights)
        im.save(res_path)


if __name__ == "__main__":
    main(res_path1, weights1)
    main(res_path2, weights2)
    main(res_path3, weights3)

