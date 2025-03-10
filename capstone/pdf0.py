import requests
import os
from fpdf import FPDF

# 폰트 파일 다운로드 함수
def download_font(font_url, save_path):
    response = requests.get(font_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"폰트 다운로드 완료: {save_path}")
    else:
        print("폰트 다운로드 실패")

# 다운로드할 폰트 URL (NanumGothic)
font_url = "https://github.com/google/fonts/raw/main/apache/nanumgothic/NanumGothic.ttf"
font_path = "C:/Users/Grace/Fonts/NanumGothic.ttf"  # 폰트를 저장할 경로

# 폰트가 이미 존재하는지 확인 후 다운로드
if not os.path.exists(font_path):
    os.makedirs(os.path.dirname(font_path), exist_ok=True)  # 폰트 저장 폴더가 없으면 생성
    download_font(font_url, font_path)

# PDF 생성
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# 폰트 추가 (한글 지원)
if os.path.exists(font_path):
    pdf.add_font('NanumGothic', '', font_path, uni=True)
else:
    print("폰트 파일을 찾을 수 없습니다.")
    exit()

# 폰트 설정
pdf.set_font("NanumGothic", size=16)

# 제목 추가
pdf.cell(200, 10, "AI 기반 여행 사진 & 엽서 시스템", ln=True, align='C')
pdf.ln(10)

# 내용 추가
pdf.set_font("NanumGothic", size=12)
content = """
1. 날씨 데이터 기반 여행 최적 경로 추천
- 날씨를 기준으로 여행 일정을 최적화하여 추천.

2. 사진 구도 추천
- 먼저 찍을 장소를 찍고, 인물 없이 사진을 찍은 후, 사람을 넣었을 때 비율이 좋도록 AI가 추천.
- 역사적 장소의 'Before/After' 제공 및 랜드마크 설명.
- 찍은 사진을 엽서화하여 감성 필터와 함께 실물로 제공하는 기능.

3. 엽서화와 문구 대신 도장 스타일로 변경
- 여행 사진을 엽서화할 때 문구 대신 도장을 활용한 디자인.
- 여행의 감성을 강조하는 독특한 방식.

4. 사진 구도에서 어울리는 자세 추천
- 사람 없이 찍은 장소 사진을 바탕으로, 배경과 잘 어울리는 사람의 포즈와 배치 추천.
- 포즈 추천 시, 사람의 자세 추정을 통해 비율이 좋아 보이는 포즈를 추천.

5. 배경 물체 검출을 활용한 구도 추천
- 배경의 물체를 검출하여 그에 맞는 사람의 배치 및 포즈 추천.
- 물체와 사람의 비율을 최적화하여 자연스러운 구도 만들기.

6. 랜드마크와 역사적 'Before/After' 제공
- 랜드마크 사진을 찍었을 때, 1900년대의 모습과 비교하는 'Before/After' 역사적 변화를 보여주는 기능.
- 각 랜드마크에 대한 역사적 설명을 추가하여 교육적인 요소도 제공.

7. 엽서 디자인 및 실물 배송
- 엽서화된 사진을 감성적으로 꾸며주는 AI 시스템.
- 사용자에게 실물 엽서를 제공할 수 있는 실물 배송 기능 추가.

이 시스템은 여행 중 찍은 사진을 실시간으로 분석하여 **최적의 사진 구도와 포즈**를 추천하고, **역사적 정보** 및 **엽서 디자인**까지 제공하는 혁신적인 시스템입니다.
"""

pdf.multi_cell(0, 10, content)

# PDF 저장
output_dir = "C:/Users/grace/Documents/"
output_filename = "AI_Travel_Photo_Postcard_System_Updated.pdf"

file_path = os.path.join(output_dir, output_filename)

# PDF 출력
pdf.output(file_path)

file_path
