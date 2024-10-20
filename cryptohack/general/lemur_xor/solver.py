from PIL import Image

lemur = Image.open("lemur.png")
flag = Image.open("flag.png")

# print(flag)
pixels_lemur = lemur.load()
# print(pixels_lemur)
pixels_flag = flag.load()

# print(lemur.size[])
for i in range(lemur.size[0]):
	for j in range(lemur.size[1]):
		l = pixels_lemur[i,j]
		f = pixels_flag[i,j]

		r = l[0] ^ f[0]
		g = l[1] ^ f[1]
		b = l[2] ^ f[2]

		pixels_flag[i,j] = (r, g, b)
		pixels_lemur[i,j] = (r, g, b)

flag.save("lemur_xor_flag.png")
flag.save("lemur_asli.png")
