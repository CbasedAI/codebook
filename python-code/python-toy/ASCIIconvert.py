from PIL import Image
import argparse

#命令行输入参数处理
parser = argparse.ArgumentParser()

# 添加参数
parser.add_argument("file")     #输入文件
parser.add_argument("-o", "--output")   #输出文件
parser.add_argument("--width", type=int, default=80) #输出字符画宽
parser.add_argument("--height", type=int, default=80) #输出字符画高

#获取参数
args = parser.parse_args()

IMG = args.file
OUTPUT = args.output
WIDTH = args.width
HEIGHT = args.height

# 字符画中所出现的字符集
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return " "
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == "__main__":

    rgb_im = Image.open(IMG)
    im = rgb_im.convert("RGBA")
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += "\n"

    print("转换成功")

    if OUTPUT:
        with open(OUTPUT,"w") as f:
            f.write(txt)
    else:
        with open("output.txt","w") as f:
            f.write(txt)
