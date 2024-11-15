import os
import shutil

# HTML 파일 경로
file_path = "dreamzodiac_index.html"  # HTML 파일 경로
sample_file_path = "animal/sample.html"  # 샘플 HTML 파일 경로

# HTML 파일 열기
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

# BeautifulSoup으로 HTML 파싱
from bs4 import BeautifulSoup

soup = BeautifulSoup(content, "html.parser")
dream_subject_div = soup.find("div", class_="dream-subject")

if dream_subject_div:
    links = dream_subject_div.find_all("a")
    dream_links = [{"text": link.text.strip(), "href": link.get("href")} for link in links]

    for link in dream_links:
        href = link["href"]
        file_to_check = href.replace("/dreamzodiac/animal/", "animal/") + ".html"  # 경로 변환
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
