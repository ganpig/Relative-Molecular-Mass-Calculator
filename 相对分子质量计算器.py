import easygui
 
表 = """H 1
He 4
Li 7
Be 9
B 11
C 12
N 14
O 16
F 19
Ne 20
Na 23
Mg 24
Al 27
Si 28
P 31
S 32
Cl 35.5
Ar 40
K 39
Ca 40
Sc 45
Ti 48
V 51
Cr 52
Mn 55
Fe 56
Co 59
Ni 59
Cu 64
Zn 65
Ga 70
Ge 73
As 75
Se 79
Br 80
Kr 84
Rb 85
Sr 88
Y 89
Zr 91
Nb 93
Mo 96
Tc 98
Ru 101
Rh 103
Pd 106
Ag 108
Cd 112
In 115
Sn 119
Sb 122
Te 128
I 127
Xe 131"""

相对原子质量表 = {元素: 相对原子质量 for 元素, 相对原子质量 in map(lambda 行: 行.split(), 表.splitlines())}


def 替换(化学式):
    for 元素 in sorted(相对原子质量表.keys(), key=len, reverse=True):
        化学式 = 化学式.replace(元素, '+'+相对原子质量表[元素]+'*')
    return 化学式.replace('(', '+(').replace(')', ')*').replace('*+', '+').replace('(+', '(').replace('*)', ')').strip('+').strip('*')


while 化学式 := easygui.enterbox('输入化学式', '相对分子质量计算器'):
    try:
        easygui.msgbox((算式 := 替换(化学式))+' = '+str(eval(算式)), 化学式+' 的相对分子质量')
    except:
        easygui.msgbox('请检查输入是否正确！（暂时仅支持 1~54 号元素）', '出错了！')
