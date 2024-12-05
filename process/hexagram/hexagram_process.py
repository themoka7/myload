import json
import os
import random
from pathlib import Path

current_dir = os.path.dirname(os.path.abspath(__file__))
def get_hexagram_random_data():
    # 64괘 목록 (각 괘에 대한 해석 포함)

    hexagrams = json.loads(Path(current_dir, 'json/hexagram.json').read_text(encoding='utf-8'))['hexagrams']


    selected_hexagram = random.choice(hexagrams)

    # 선택된 괘와 해석을 반환
    return {
        "hexagram": selected_hexagram["name"],
        "type_1": selected_hexagram["type"][0],
        "type_2": selected_hexagram["type"][1],
        "desc": selected_hexagram["desc"],
        "interpretation": selected_hexagram["interpretation"]
    }


def get_hexagram_data(hexagram):
    # 64괘 목록 (각 괘에 대한 해석 포함)

    print(hexagram)
    hexagrams = json.loads(Path(current_dir, 'json/hexagram.json').read_text(encoding='utf-8'))['hexagrams']

    selected_hexagram = next((h for h in hexagrams if h['name'] == hexagram), '')

    # 선택된 괘가 없으면 None 반환
    if not selected_hexagram:
        return None

    # 선택된 괘와 해석을 반환
    return {
        "hexagram": selected_hexagram["name"],
        "type_1": selected_hexagram["type"][0],
        "type_2": selected_hexagram["type"][1],
        "desc": selected_hexagram["desc"],
        "interpretation": selected_hexagram["interpretation"]
    }

