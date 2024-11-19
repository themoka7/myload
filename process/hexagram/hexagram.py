import json
import os
import random
from pathlib import Path

current_dir = os.path.dirname(os.path.abspath(__file__))
def get_hexagram_all_data():
    # 64괘 목록 (각 괘에 대한 해석 포함)

    hexagrams = json.loads(Path(current_dir, 'json/hexagram.json').read_text(encoding='utf-8'))['hexagrams']

    print(hexagrams)
    # 필요한 값만 추출
    filtered_data = [
        {
            "name": hexagram["name"],
            "type": hexagram["type"],
            "desc": hexagram["desc"]
        }
        for hexagram in hexagrams
    ]

    # 선택된 괘와 해석을 반환
    return filtered_data
