import os
import json

# 주어진 데이터
selected_tarot = [
    {'type': 1, 'idx': '2', 'direction': 'Reverse'},
    {'type': 2, 'idx': '22', 'direction': 'Forward'}
]

# 함수를 정의하여 데이터를 처리하고, idx에 맞는 JSON 파일을 불러옴
def get_tarot_data(selected_tarot):
    new_tarot_data = []  # 새로운 데이터를 저장할 리스트
    for card in selected_tarot:
        card_type = card['type']
        idx = card['idx']
        direction = card['direction']

        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir,'json', f'{idx}.json')

        # 파일이 존재하는지 확인
        if os.path.exists(file_path):
            # JSON 파일을 열고 데이터 로드

            with open(file_path, 'r', encoding='utf-8') as file:
                json_data = json.load(file)


                # 선택된 interpretations에서 type과 direction을 모두 비교
                matching_interpretations = [
                    interpretation for interpretation in json_data.get("interpretations", [])
                    if interpretation["direction"] == direction and interpretation["type"] == card_type
                ]

                # card_definition과 selected_tarot 값을 포함해 새로운 JSON 생성
                new_data = {
                    "card_definition": json_data["card_definition"],
                    "selected_interpretations": matching_interpretations,
                    "selected_tarot": {
                        "type": card_type,
                        "idx": idx,
                        "direction": direction
                    }
                }

                # 새로운 데이터를 저장
                new_tarot_data.append(new_data)
        else:
            print(f"File {idx}.json not found in json directory.")

    return new_tarot_data  # 새로운 데이터를 반환

# 함수 호출 및 결과 저장
updated_tarot_data = get_tarot_data(selected_tarot)

# 결과 출력
'''for card in updated_tarot_data:
    print(json.dumps(card, indent=4, ensure_ascii=False))'''
