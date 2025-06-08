import tkinter as tk
from tkinter import filedialog
import fitz  # PyMuPDF
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")  

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def get_iterative_summary(text):
    prompt1 = (
        "너는 여론조사결과 해석 전문가야. 다음 문서를 한 줄로 요약하되, 너가 중요하다고 생각하는 결과나 의미, 또는 통찰을 반드시 포함해서 작성해줘:\n"
        + text[:10000]
    )
    response1 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt1}],
        max_tokens=300,
        temperature=0.7,
    )
    summary1 = response1.choices[0].message.content.strip()
    
    print("\n[1차 요약]:", summary1) 

    prompt2 = (
        f"아래 한 줄 요약을 읽고, 빠진 점이나 더 강조해야 할 점, 또는 더 깊이 있는 해석이 있으면 지적하고 보완해줘.\n"
        f"요약: {summary1}\n"
        f"원문 일부: {text[:5000]}"
    )
    response2 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt2}],
        max_tokens=300,
        temperature=0.7,
    )
    critique = response2.choices[0].message.content.strip()
    
    print("\n[빠진 점]:", critique) 

    # 3차 최종 해석(보완)
    prompt3 = (
        f"아래의 1차 요약과 2차 자기 검토를 참고해서, "
        f"가장 중요한 결과와 의미를 포함한 최종 한 줄 해석을 다시 작성해줘.\n"
        f"1차 요약: {summary1}\n"
        f"자기 검토: {critique}"
    )
    response3 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt3}],
        max_tokens=300,
        temperature=0.7,
    )
    final_summary = response3.choices[0].message.content.strip()

    print("\n[최종 답변]:", final_summary)
    return final_summary

def select_and_summarize_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if not file_path:
        return
    result_label.config(text="PDF에서 텍스트 추출 중...")
    window.update()
    try:
        text = extract_text_from_pdf(file_path)
        result_label.config(text="GPT가 해석을 생성 중입니다...")
        window.update()
        summary = get_iterative_summary(text)
        result_label.config(text=f"{summary}")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

window = tk.Tk()
window.title("PDF 자동 반복 해석 (GPT 연동)")
window.geometry("700x200")

desc_label = tk.Label(window, text="PDF 파일을 선택하면 한 줄 평이 생성됩니다.")
desc_label.pack(pady=(20, 5))

select_button = tk.Button(window, text="PDF 파일 선택 및 해석", command=select_and_summarize_pdf)
select_button.pack(pady=10)

result_label = tk.Label(window, text="", wraplength=650, justify="left", fg="blue")
result_label.pack(pady=10)

window.mainloop()
