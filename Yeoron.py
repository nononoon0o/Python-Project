import pandas as pd
import tkinter as tk
from tkinter import ttk, simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

import matplotlib.font_manager as fm
import openai
from openai import OpenAI

# 한글 폰트 설정 (윈도우용)
font_path = "C:/Windows/Fonts/malgun.ttf"  # 말굽고딕 폰트 경로
fontprop = fm.FontProperties(fname=font_path).get_name()
plt.rcParams['font.family'] = fontprop

root = tk.Tk()
root.title("여론조사 시각화")

# 첫 번째 화면 크기
root.geometry("500x750")
root.configure(bg="#f0f4f8")

df = pd.read_csv("C:/Users/Lee/Desktop/학교/python/Python-Project/filtered_polls.csv")

def request_gpt_summary(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "당신은 데이터 분석가입니다."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content
def generate_prompt(agency, subject, data, compare_agency=None):
    prompt = f"{agency}의 여론조사 데이터를 바탕으로 {subject} 선거의 지지율 요약을 작성해주세요.\n\n"
    prompt += f"각 후보별 지지율은 다음과 같습니다:\n"

    for candidate, values in data.items():
        if values:
            avg = sum(values) / len(values)
            prompt += f"- {candidate}: {avg:.1f}% 평균 지지율\n"
        else:
            prompt += f"- {candidate}: 데이터 없음\n"

    if compare_agency and compare_agency != agency:
        prompt += f"\n비교 대상 기관: {compare_agency}도 함께 고려해주세요."

    prompt += """
다음과 같은 방식으로 설명해주세요:

1. 어떤 후보가 가장 우세한지, 왜 그렇게 판단되는지 언급합니다.
2. 주요 후보 간의 격차가 크거나 근소한 경우 이를 명확히 설명합니다.
3. 특정 후보가 상대적으로 약세이거나 하락세라면 이를 분석합니다.
4. 데이터에 익숙하지 않은 사용자가 보아도 직관적으로 이해할 수 있도록 쉬운 표현을 사용하세요.

설명은 자연스럽고 간결하게 3~5문장으로 작성해주세요.
"""
    return prompt
# 후보 이름 변환 (영문 키로 바꾸기)
candidate_map = {
    "이재명": "이재명",
    "김문수": "김문수",
    "이준석": "이준석"
}

# 기관별 지지율을 저장할 딕셔너리
compare_data = defaultdict(lambda: defaultdict(list))

# 조사기관명에서 핵심 기관명 추출 함수
def extract_agency(name):
    if "Realmeter" in name:
        return "리얼미터"
    elif "KSOI" in name:
        return "KSOI"
    elif "Hankook" in name or "한국리서치" in name:
        return "한국리서치"
    return "기타"

# 데이터 정리
for _, row in df.iterrows():
    agency = extract_agency(row["조사기관"])
    for kr_name, en_key in candidate_map.items():
        compare_data[agency][en_key].append(row[kr_name])

# 딕셔너리를 일반 dict로 변환
compare_data = dict(compare_data)
print(compare_data)
dates = [datetime.date(2025, 4, d) for d in [3, 10, 14, 21, 27]]
candidate_a = [48, 42, 38, 40, 55]
candidate_b = [32, 36, 44, 42, 30]
candidate_c = [20, 19, 18, 16, 15]

def show_frame(target):
    # 화면 크기 조절: 첫 번째 화면과 두 번째 화면 크기 다르게 설정
    if target == frame_selection:
        root.geometry("500x750")
    elif target == frame_result:
        root.geometry("600x900")  # 두 번째 화면 세로 좀 더 크게
    
    for frame in all_frames:
        frame.pack_forget()
    target.pack(pady=10, fill="both", expand=True)

def on_share_click():
    # 저장할 파일 경로를 다이얼로그로 선택
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG 파일", "*.png"), ("모든 파일", "*.*")],
        title="그래프 이미지 저장"
    )
    if file_path:
        try:
            fig.savefig(file_path)
            messagebox.showinfo("저장 완료", f"그래프가 '{file_path}'에 저장되었습니다.")
        except Exception as e:
            messagebox.showerror("저장 실패", f"저장 중 오류가 발생했습니다:\n{e}")
# 첫 화면
frame_selection = tk.Frame(root, bg="#f0f4f8")

title_label = tk.Label(frame_selection, text="여론조사 시각화 시작", font=("Malgun Gothic", 20, "bold"), fg="#264653", bg="#f0f4f8")
title_label.pack(pady=(30, 15))

form_area = tk.Frame(frame_selection, bg="#f0f4f8")
form_area.pack(padx=10, pady=5)

agency_label = tk.Label(form_area, text="조사 기관 선택:", font=("Malgun Gothic", 15, "bold"), fg="#2a9d8f", bg="#f0f4f8")
agency_label.grid(row=0, column=0, sticky="w", pady=(8, 6))

agencies = ["한국리서치", "리얼미터", "KSOI"]
agency_var = tk.StringVar(value="한국리서치")
agency_options = tk.Frame(form_area, bg="#f0f4f8")
agency_options.grid(row=1, column=0, sticky="w", pady=(0, 15))
for agency in agencies:
    rb = ttk.Radiobutton(agency_options, text=agency, variable=agency_var, value=agency)
    rb.pack(side=tk.LEFT, padx=10)

subject_label = tk.Label(form_area, text="선거 종류 선택:", font=("Malgun Gothic", 15, "bold"), fg="#2a9d8f", bg="#f0f4f8")
subject_label.grid(row=2, column=0, sticky="w", pady=(8, 6))
subject_cb = ttk.Combobox(form_area, values=["대통령", "국회의원", "정당"], state="readonly", font=("Malgun Gothic", 13))
subject_cb.set("대통령")
subject_cb.grid(row=3, column=0, sticky="we", pady=10)

next_btn = tk.Button(frame_selection, text="다음으로 ▶", font=("Malgun Gothic", 15, "bold"),
                     bg="#2a9d8f", fg="white", activebackground="#264653", activeforeground="white",
                     relief="flat", padx=15, pady=8, cursor="hand2", command=lambda: on_next_click())
next_btn.pack(pady=35)

# 두 번째 화면
frame_result = tk.Frame(root, bg="#f0f4f8")

# 뒤로가기 버튼 왼쪽 위 고정 배치
back_btn = tk.Button(frame_result, text="◀ 뒤로가기", font=("Malgun Gothic", 11, "bold"),
                     bg="#e76f51", fg="white", relief="flat", padx=10, pady=5, cursor="hand2",
                     command=lambda: show_frame(frame_selection))
back_btn.place(x=15, y=15)

result_title = tk.Label(frame_result, text="여론조사 시각화 결과", font=("Malgun Gothic", 20, "bold"), fg="#264653", bg="#f0f4f8")
result_title.pack(pady=(50, 10))

info_label = tk.Label(frame_result, font=("Malgun Gothic", 13), fg="#555", bg="#f0f4f8")
info_label.pack(padx=30, pady=(0, 18))

fig, ax = plt.subplots(figsize=(6, 3.5), dpi=100)
fig.patch.set_facecolor('#f0f4f8')
canvas = FigureCanvasTkAgg(fig, master=frame_result)
canvas.draw()
canvas.get_tk_widget().pack(padx=30)

summary_title = tk.Label(frame_result, text="GPT 요약 및 해설", font=("Malgun Gothic", 16, "bold"), fg="#264653", bg="#f0f4f8")
summary_title.pack(pady=(25, 10))

summary_label = tk.Label(frame_result, text="", justify="left", font=("Malgun Gothic", 12), fg="black", bg="#f0f4f8",
                         wraplength=520, padx=15, pady=12, relief="groove", bd=1)
summary_label.pack(padx=30, fill="x")

btn_frame = tk.Frame(frame_result, bg="#f0f4f8")
btn_frame.pack(pady=25, fill='x', padx=30)

def show_popup(msg):
    popup = tk.Toplevel(root)
    popup.title("알림")
    popup.geometry("320x150")
    popup.configure(bg="#e9f1f7")
    tk.Label(popup, text=msg, font=("Malgun Gothic", 14), bg="#e9f1f7", fg="#333").pack(padx=20, pady=40)
    ttk.Button(popup, text="닫기", command=popup.destroy).pack()

ttk.Style().configure("TButton", font=("Malgun Gothic", 12), padding=6)

btn_style = {"bg": "#2a9d8f", "fg": "white", "activebackground": "#264653", "activeforeground": "white",
             "relief": "flat", "cursor": "hand2", "padx": 15, "pady": 8, "font": ("Malgun Gothic", 13, "bold")}

# 기존 버튼들 중 북마크 제거하고 공유, 비교모드만 남김
btn_compare = tk.Button(btn_frame, text="비교모드", command=lambda: open_compare_dialog(), **btn_style)
btn_compare.pack(side=tk.LEFT, expand=True, fill='x', padx=6)

btn_share = tk.Button(btn_frame, text="공유", command=on_share_click, **btn_style)
btn_share.pack(side=tk.LEFT, expand=True, fill='x', padx=6)

all_frames = [frame_selection, frame_result]

def draw_plot(compare_agency=None):
    ax.clear()

    # 선택된 기관 데이터
    agency = agency_var.get()
    data = compare_data[agency]

    # 후보들
    candidates = ["이재명", "김문수", "이준석"]
    display_names = ["이재명", "김문수", "이준석"]
    colors = ["#264653", "#e76f51", "#2a9d8f"]

    # 각 후보의 최근(0번째) 지지율
    values = [data[name][0] if len(data[name]) > 0 else 0 for name in candidates]

    bar_width = 0.35
    x = range(len(candidates))
    ax.bar(x, values, width=bar_width, color=colors, label=agency)

    # 비교 기관 처리
    if compare_agency and compare_agency != agency and compare_agency in compare_data:
        comp_data = compare_data[compare_agency]
        comp_values = [comp_data[name][0] if len(comp_data[name]) > 0 else 0 for name in candidates]
        ax.bar([i + bar_width for i in x], comp_values, width=bar_width, color=["#7b9e89", "#d98e7e", "#7fd1b9"], label=compare_agency)
        ax.set_xticks([i + bar_width / 2 for i in x])
    else:
        ax.set_xticks(x)

    ax.set_xticklabels(display_names, fontsize=11)
    ax.set_ylim(0, 60)
    ax.set_ylabel("지지율 (%)", fontsize=11)
    ax.set_title(f"{agency} 여론조사 결과", fontsize=13)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax.legend(fontsize=9)
    fig.tight_layout()
    canvas.draw()


# 현재 비교 기관을 저장하는 변수
current_compare_agency = None

def generate_summary(agency, subject, compare_agency=None):
    data = compare_data.get(agency, {})

    # GPT용 프롬프트 생성
    prompt = generate_prompt(agency, subject, data, compare_agency)

    try:
        gpt_summary = request_gpt_summary(prompt)
    except Exception as e:
        gpt_summary = f"요약 생성 중 오류 발생: {e}"
        print(e)

    return gpt_summary

def on_next_click():
    global current_compare_agency
    current_compare_agency = None  # 초기화

    agency = agency_var.get()
    subject = subject_cb.get()

    info_label.config(text=f"기관: {agency} / 선거 종류: {subject}")
    summary_label.config(text=generate_summary(agency, subject))
    draw_plot()

    show_frame(frame_result)

def open_compare_dialog():
    global current_compare_agency

    compare_list = [a for a in agencies if a != agency_var.get()]
    if not compare_list:
        show_popup("비교할 기관이 없습니다.")
        return

    compare_win = tk.Toplevel(root)
    compare_win.title("비교 기관 선택")
    compare_win.geometry("320x260")  # 높이 늘림
    compare_win.configure(bg="#e9f1f7")

    title_label = tk.Label(compare_win, text="비교할 기관을 선택하세요:", font=("Malgun Gothic", 14, "bold"), bg="#e9f1f7", fg="#264653")
    title_label.pack(pady=(20, 10))

    selected_agency = tk.StringVar(value=compare_list[0])

    rb_frame = tk.Frame(compare_win, bg="#e9f1f7")
    rb_frame.pack(pady=(0, 20))

    for ag in compare_list:
        rb = tk.Radiobutton(rb_frame, text=ag, variable=selected_agency, value=ag,
                            font=("Malgun Gothic", 12), bg="#e9f1f7", fg="#264653", activebackground="#e9f1f7",
                            selectcolor="#a8dadc", cursor="hand2")
        rb.pack(anchor='w', padx=20, pady=5)

    def on_confirm():
        nonlocal selected_agency
        current_compare_agency = selected_agency.get()
        info_label.config(text=f"기관: {agency_var.get()} / 비교 기관: {current_compare_agency}")
        summary_label.config(text=generate_summary(agency_var.get(), subject_cb.get(), current_compare_agency))
        draw_plot(current_compare_agency)
        compare_win.destroy()

    confirm_btn = tk.Button(compare_win, text="확인", font=("Malgun Gothic", 13, "bold"),
                            bg="#2a9d8f", fg="white", activebackground="#264653", activeforeground="white",
                            relief="flat", padx=15, pady=8, cursor="hand2", command=on_confirm)
    confirm_btn.pack(pady=(0, 20), ipadx=10)

def save_graph():
    filename = f"poll_result_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    fig.savefig(filename)
    show_popup(f"그래프를 '{filename}' 이름으로 저장했습니다.")

show_frame(frame_selection)
root.mainloop()