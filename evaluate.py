
"""
    @Author: Junjie Jin
    @Date: 2022/05/17
    @Description: 三行情书 实现调用逻辑
"""

from main import hold_palm
from utils import get_love


if __name__ == '__main__':
    heart = hold_palm('love')  # 把你捧在手上，希望得到你的心 （加载模型）
    letter = heart(life='', live='')  # 你的心带着你的生命与生活，表达着对我的爱 life：生命（定性词）live：生活（上下文语境）（生成情书）
    get_love(letter)  # 生成心形词云，是爱的象征

