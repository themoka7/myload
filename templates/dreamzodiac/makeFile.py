import os
import shutil
from bs4 import BeautifulSoup

# HTML 파일 경로
file_path = "dreamzodiac_index.html"  # HTML 파일 경로
sample_file_path = "animal/sample.html"  # 샘플 HTML 파일 경로

# HTML 파일 열기
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

# BeautifulSoup으로 HTML 파싱
soup = BeautifulSoup(content, "html.parser")
dream_subject_divs = soup.find_all("div", class_="dream-subject")  # 모든 `dream-subject`를 찾음

if dream_subject_divs:
    for div in dream_subject_divs:  # 각 `dream-subject` 처리
        links = div.find_all("a")
        dream_links = [{"text": link.text.strip(), "href": link.get("href")} for link in links]

        for link in dream_links:
            href = link["href"]

            # `animal` 또는 `plant` 경로 처리
            if "/dreamzodiac/animal/" in href:
                file_to_check = href.replace("/dreamzodiac/animal/", "animal/") + ".html"
            elif "/dreamzodiac/plant/" in href:
                file_to_check = href.replace("/dreamzodiac/plant/", "plant/") + ".html"
            elif "/dreamzodiac/food/" in href:
                file_to_check = href.replace("/dreamzodiac/food/", "food/") + ".html"
            elif "/dreamzodiac/factor/" in href:
                file_to_check = href.replace("/dreamzodiac/factor/", "factor/") + ".html"
            elif "/dreamzodiac/place/" in href:
                file_to_check = href.replace("/dreamzodiac/place/", "place/") + ".html"
            else:
                print(f"Skipping unsupported href: {href}")
                continue

            replacement_text = link["text"]

            if os.path.exists(file_to_check):
                print(f"File exists: {file_to_check}")
            else:
                print(f"File does not exist: {file_to_check}. Creating file...")
                # 파일이 없을 경우 sample.html 복사
                os.makedirs(os.path.dirname(file_to_check), exist_ok=True)
                shutil.copy(sample_file_path, file_to_check)
                print(f"Created file: {file_to_check}")

                # 파일 내용 수정: "동물"을 replacement_text로 대체
                with open(file_to_check, "r", encoding="utf-8") as f:
                    file_content = f.read()

                updated_content = file_content.replace("동물", replacement_text)

                # 수정된 내용을 새 파일에 다시 저장
                with open(file_to_check, "w", encoding="utf-8") as f:
                    f.write(updated_content)
                print(f"Updated file: {file_to_check} with replacement: {replacement_text}")
else:
    print("No <div class='dream-subject'> found.")
