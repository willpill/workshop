# Yinwei Zhang
# China Rats Plus One
# SoftDev
# <randomDevos/Python Dictionaries/Function that picks a random key from a dictionary, then pick a random element from the list corresponding to the key.>
# 2024-9-14
# Time Spent : 1 Hour
import random

dict1 = {
    4: [
        'DUA', 'TAWAB', 'EVA', 'JACK', 'VICTOR', 'EVAN', 'JASON', 'COLYI', 'IVAN', 'TANZEEM',
        'TAHMIM', 'STANLEY', 'LEON', 'NAOMI', 'NIA', 'ANASTASIA', 'JADY', 'BRIAN', 'JACOB',
        'ALEX', 'CHONGTIAN', 'DANNY', 'MARCO', 'ABIDUR', 'ANKITA', 'ANDY', 'ETHAN', 'AMANDA',
        'AIDAN', 'LINDA', 'QIANJUN', 'JIAYING', 'KISHI'
    ],
    5: [
        'ADITYA', 'MARGIE', 'RACHEL', 'ALEXANDER', 'ZIYAD', 'DANNY', 'ENDRIT', 'CADEN',
        'VEDANT', 'SUHANA', 'KYLE', 'KEVIN', 'RAYMOND', 'CHRISTOPHER', 'JONATHAN', 'SASHA',
        'NAFIYU', 'TIM', 'WILL', 'DANIEL', 'BENJAMIN', 'CLAIRE', 'CHLOE', 'STELLA', 'TRACY',
        'JESSICA', 'JACKIE', 'WEN YUAN', 'YINWEI', 'TIFFANY', 'JAYDEN DANIEL', 'PRINCEDEN'
    ]
}


def randomDevos(dict1):
    keys = list(dict1.keys())
    key = random.randint(0, len(keys) - 1)  # Select index randomly from the keys list
    index = keys[key]
    devoList = dict1[index]
    index = random.randint(0, len(devoList) - 1)  # Randomly select index from the names list
    return devoList[index]


for i in range(20):
    print(randomDevos(dict1))
