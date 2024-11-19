import json
import os
import random
from pathlib import Path

current_dir = os.path.dirname(os.path.abspath(__file__))
def get_hexagram_data():
    # 64괘 목록 (각 괘에 대한 해석 포함)

    hexagrams = json.loads(Path(current_dir, 'json/hexagram.json').read_text(encoding='utf-8'))['hexagrams']

    print(hexagrams)
    selected_hexagram = random.choice(hexagrams)

    # 선택된 괘와 해석을 반환
    return {
        "hexagram": selected_hexagram["name"],
        "type_1": selected_hexagram["type"][0],
        "type_2": selected_hexagram["type"][1],
        "desc": selected_hexagram["desc"],
        "interpretation": selected_hexagram["interpretation"]
    }


print(get_hexagram_data())