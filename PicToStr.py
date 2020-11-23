from PIL import Image

#赋值字符画需要的字符集 字符集中的字符可以根据需求调换
pain_char = list(" $@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
#定义绘制图片的大小 宽*高 = 60*40
W = 60
H = 40

#将256个灰度值映射给70个字符
def RGB_char(r,g,b,hd=256):
    if hd == 0:
        return ''
    pain_char_len = len(pain_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)  # 根据灰度计算公式来计算灰度
    blok = 256.0/pain_char_len #把256个灰度分 对应分成和字符集中字符个数相等的块
    return pain_char[int(gray/blok)]

if __name__=='__main__':
    img = 'E:\VSCode\Python-Exercises\\4.jpg' #图片路径
    im = Image.open(img)
    im = im.resize((W,H),Image.NEAREST)
    #resize的参数 宽 ， 高 ，图象质量 
    # 其中Image.NEAREST ：低质量、
    # Image.BILINEAR：双线性、
    # Image.BICUBIC ：三次样条插值、
    # Image.ANTIALIAS：高质量
    pain = ""

    for i in range(H):
        for j in range(W):
            pain += RGB_char(*im.getpixel((j, i))) # 获得相应的字符
        pain += '\n'
    
    print(pain)