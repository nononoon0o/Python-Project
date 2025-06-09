import pandas as pd

# URL 지정
url = "https://en.wikipedia.org/wiki/Opinion_polling_for_the_2025_South_Korean_presidential_election"

# 모든 테이블 가져오기
tables = pd.read_html(url)

# 첫 번째 테이블 선택
poll_df = tables[0]

# 다중 인덱스 열 제거
if isinstance(poll_df.columns, pd.MultiIndex):
    poll_df.columns = poll_df.columns.get_level_values(0)

# 열 이름 변경
poll_df = poll_df.rename(columns={
    "Fieldwork date": "조사일",
    "Sample size": "표본 수",
    "Margin of error": "오차범위",
    "Polling firm": "조사기관",
    "DPK": "이재명",
    "PPP": "김문수",
    "RP": "이준석",
    "DLP": "권영국",
    "Others": "기타",
    "Und./no ans.": "무응답",
    "Lead": "격차"
})

# 정확히 일치하는 조사기관/매체 조합만 포함
valid_firms = [
    "Realmeter / EKN",
    "KSOI / CBS",
    "Hankook Research / KBS",
    "Hankook Researach / KBS"
]

# 조사기관 문자열에서 대괄호 제거 전 이름만 추출
poll_df["기관매체"] = poll_df["조사기관"].str.extract(r"^(.+?)\s*\[\d+\]?$")[0].str.strip()

# 필터링
filtered_df = poll_df[poll_df["기관매체"].isin(valid_firms)]

# 기타 컬럼에서 "—" 또는 "-" 를 0으로 처리
filtered_df["기타"] = filtered_df["기타"].replace(["—", "-", None], 0)
filtered_df["기타"] = pd.to_numeric(filtered_df["기타"], errors="coerce").fillna(0)

# 사용할 열만 선택 (격차 제거)
columns_to_keep = ["조사기관", "이재명", "김문수", "이준석", "권영국", "기타"]
filtered_df = filtered_df[columns_to_keep]
for col in ["권영국", "기타"]:
    filtered_df[col] = filtered_df[col].replace(["—", "-", None], 0)
    filtered_df[col] = pd.to_numeric(filtered_df[col], errors="coerce").fillna(0)
# CSV로 저장
filtered_df.to_csv("filtered_polls.csv", index=False, encoding="utf-8-sig")

# 결과 출력
print(filtered_df)
