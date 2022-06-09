

"""
    @Author: Junjie Jin
    @Date: 2022/5/17
    @Description: 实现工具方法
"""

from wordcloud import WordCloud
import PIL.Image as image
import numpy as np
import jieba
import turtle
import random
import cv2
import matplotlib.pyplot as plt


# 分词
def trans_CN(text):
    # 接收分词的字符串
    word_list = jieba.cut(text)
    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)
    return result


def getMask():
    mask = []
    with open('mask.txt', 'r') as f:
        lines = f.readlines()
    for line in lines:
        mask.append([1 - int(_) for _ in line.strip()])
    mask = np.array(mask, np.int8)
    # mask = np.stack([mask, mask, mask], axis = -1)
    # print(mask.shape)
    mask = cv2.resize(np.uint8(mask), (512, 512), cv2.INTER_NEAREST)
    im = np.zeros((512, 512))
    for i in range(512):
        for j in range(512):
            im[i][j] = 0 if mask[i][j] >= 0.5 else 255
    # plt.imshow(im)
    # plt.show()
    return im  # np.stack([im, im, im], axis=-1)

dics = []
voc_len = 0


def get_love(letter):

    text = letter + (" " + trans_CN(letter)) * 5 + (" " + " ".join(list(letter))) * 5
    mask = getMask()  # np.array(image.open("love.png"))  # 添加心形图片
    wordcloud = WordCloud(
        # 添加遮罩层
        mask=mask,
        background_color='white',
        # contour_width=5,
        # 生成中文字的字体,必须要加,不然看不到中文
        font_path="C:\Windows\Fonts\STXINGKA.TTF"
    ).generate(text)
    image_produce = wordcloud.to_image()
    image_produce.show()
#
# # 要读取的txt文本
# with open("love.txt", encoding="utf-8") as fp:
#     text = fp.read()
#     for i, line in enumerate(text):
#         dics.append(line.strip())
#         voc_len += 1
#     print(text)
#     # 将读取的中文文档进行分词
#     text = text + (" " + trans_CN(text)) * 5 + (" " + " ".join(list(text))) * 5
#     mask = getMask()  # np.array(image.open("love.png"))  # 添加心形图片
#     wordcloud = WordCloud(
#         # 添加遮罩层
#         mask=mask,
#         background_color='white',
#         # contour_width=5,
#         # 生成中文字的字体,必须要加,不然看不到中文
#         font_path="C:\Windows\Fonts\STXINGKA.TTF"
#     ).generate(text)
#     image_produce = wordcloud.to_image()
#     image_produce.show()



def fxn(x, y):
    print(x, y)


def love(x, y):  # 在(x,y)处画爱心
    s = np.random.choice(dics, 1)[0]
    lv = turtle.Turtle()
    lv.onclick(fxn)
    lv.hideturtle()
    lv.up()
    lv.goto(x, y)  # 定位到(x,y)

    def curvemove():  # 画圆弧
        for i in range(33):
            lv.right(6)
            lv.forward(1.5)

    lv.color('red', 'pink')
    lv.speed(10)
    lv.pensize(1)
    # 开始画爱心lalala
    lv.down()
    lv.begin_fill()
    lv.left(140)
    lv.forward(30)
    curvemove()
    lv.left(120)
    curvemove()
    lv.forward(30)
    lv.write(s, font=("Arial", 12, "normal"), align="center")
    lv.left(140)  # 画完复位
    lv.end_fill()


def tree(branchLen, t):
    if branchLen > 5:  # 剩余树枝太少要结束递归
        if branchLen < 20:  # 如果树枝剩余长度较短则变绿
            t.color("green")
            t.pensize(random.uniform((branchLen + 5) / 4 - 2, (branchLen + 6) / 4 + 5))
            t.down()
            t.forward(branchLen)
            love(t.xcor(), t.ycor())  # 传输现在turtle的坐标
            t.up()
            t.backward(branchLen)
            t.color("brown")
            return
        t.pensize(random.uniform((branchLen + 5) / 4 - 2, (branchLen + 6) / 4 + 5))
        t.down()
        t.forward(branchLen)
        # 以下递归
        ang = random.uniform(15, 45)
        t.right(ang)
        tree(branchLen - random.uniform(12, 16), t)  # 随机决定减小长度
        t.left(2 * ang)
        tree(branchLen - random.uniform(12, 16), t)  # 随机决定减小长度
        t.right(ang)
        t.up()
        t.backward(branchLen)


def draw():
    myWin = turtle.Screen()
    turtle.title('AI写诗')
    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(32)

    t.speed(1000)
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("brown")
    t.pensize(32)
    t.forward(60)
    tree(100, t)
    # love(t.xcor(), t.ycor())
    myWin.exitonclick()

# draw()
