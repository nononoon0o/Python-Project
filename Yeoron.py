# import tkinter as tk
# from tkinter import ttk
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import matplotlib.pyplot as plt
# import datetime

# root = tk.Tk()
# root.title("여론조사 시각화")
# root.geometry("650x800")
# root.configure(bg="#f9f9f9")  # 전체 배경색

# # 임시 데이터
# dates = [datetime.date(2025, 4, d) for d in [3, 10, 14, 21, 27]]
# candidate_a = [48, 42, 38, 40, 55]
# candidate_b = [32, 36, 44, 42, 30]
# candidate_c = [20, 19, 18, 16, 15]

# # 화면 전환 함수
# def show_frame(target):
#     for frame in all_frames:
#         frame.pack_forget()
#     target.pack(pady=20, fill="both", expand=True)

# # ------------------- [1단계] 기관 선택 -------------------
# frame1 = tk.Frame(root, bg="#f9f9f9")
# tk.Label(frame1, text="1단계: 여론조사 기관 선택", font=("맑은 고딕", 16, "bold"), bg="#f9f9f9", fg="#333").pack(pady=(20, 15))

# agencies = ["갤럽", "한국리서치", "리얼미터", "KSOI"]
# agency_var = tk.StringVar(value="갤럽")

# for agency in agencies:
#     ttk.Radiobutton(frame1, text=agency, variable=agency_var, value=agency).pack(anchor="w", padx=40, pady=5)

# ttk.Button(frame1, text="다음", command=lambda: show_frame(frame2)).pack(pady=30)

# # ------------------- [2단계] 선거 종류 및 기간 설정 -------------------
# frame2 = tk.Frame(root, bg="#f9f9f9")
# tk.Label(frame2, text="2단계: 선거 종류 및 조회 기간", font=("맑은 고딕", 16, "bold"), bg="#f9f9f9", fg="#333").pack(pady=(20, 15))

# subject_cb = ttk.Combobox(frame2, values=["대통령", "국회의원", "정당"], state="readonly", font=("맑은 고딕", 12))
# subject_cb.set("대통령")
# subject_cb.pack(pady=8, padx=40, fill="x")

# period_cb = ttk.Combobox(frame2, values=["7일", "30일", "90일"], state="readonly", font=("맑은 고딕", 12))
# period_cb.set("30일")
# period_cb.pack(pady=8, padx=40, fill="x")

# ttk.Button(frame2, text="다음", command=lambda: show_frame(frame3)).pack(pady=30)

# # ------------------- [3~5단계 통합] 그래프 + 상세정보 + 해설 -------------------
# frame3 = tk.Frame(root, bg="#f9f9f9")
# tk.Label(frame3, text="여론조사 시각화 결과", font=("맑은 고딕", 16, "bold"), bg="#f9f9f9", fg="#333").pack(pady=(20, 15))

# # 상세 정보 - 그래프 위쪽에 배치
# info_text = (
#     f"조사기관: {agency_var.get()}\n"
#     f"조사일시: 2025년 4월 3일 ~ 27일\n"
#     f"표본 수: 1,000명 이상\n"
#     f"오차범위: ±3.1%p\n"
# )
# info_label = tk.Label(frame3, text=info_text, justify="left", font=("맑은 고딕", 12), bg="#e1f0ff", fg="#024d8c",
#                       bd=2, relief="groove", padx=15, pady=10)
# info_label.pack(padx=40, pady=(0, 15), fill="x")

# # 그래프 영역
# fig, ax = plt.subplots(figsize=(6, 3.5), dpi=100)
# ax.plot(dates, candidate_a, label="후보 A", color="#1f77b4", linewidth=2)
# ax.plot(dates, candidate_b, label="후보 B", color="#d62728", linewidth=2)
# ax.plot(dates, candidate_c, label="후보 C", color="#ff7f0e", linewidth=2)
# ax.set_ylim(0, 60)
# ax.set_ylabel("지지율 (%)", fontsize=12)
# ax.set_xticks(dates)
# ax.set_xticklabels([d.strftime('%m/%d') for d in dates], fontsize=10)
# ax.legend(fontsize=10)
# ax.grid(axis='y', linestyle='--', alpha=0.7)

# canvas = FigureCanvasTkAgg(fig, master=frame3)
# canvas.draw()
# canvas.get_tk_widget().pack(padx=40)

# # GPT 해설
# tk.Label(frame3, text="GPT 요약 및 해설", font=("맑은 고딕", 14, "bold"), bg="#f9f9f9", fg="#333").pack(pady=(20, 8))
# summary = (
#     "후보 A는 초반 지지율 하락 후 다시 상승세를 보이며\n"
#     "최종적으로 55%의 높은 지지율을 기록했습니다.\n"
#     "후보 B는 한때 지지율이 상승했으나, 막판에 감소했고\n"
#     "후보 C는 지속적으로 하락세를 보였습니다."
# )
# summary_label = tk.Label(frame3, text=summary, justify="left", font=("맑은 고딕", 11), bg="#f9f9f9", fg="#555", padx=20, pady=10)
# summary_label.pack(padx=40, fill="x")

# # 버튼 영역
# btn_frame = tk.Frame(frame3, bg="#f9f9f9")
# btn_frame.pack(pady=20)

# def show_popup(msg):
#     popup = tk.Toplevel(root)
#     popup.title("알림")
#     popup.geometry("300x130")
#     popup.configure(bg="#f0f8ff")
#     tk.Label(popup, text=msg, font=("맑은 고딕", 13), bg="#f0f8ff", fg="#333").pack(padx=20, pady=20)
#     ttk.Button(popup, text="닫기", command=popup.destroy).pack()

# btn_style = ttk.Style()
# btn_style.configure("TButton", font=("맑은 고딕", 11), padding=6)

# ttk.Button(btn_frame, text="비교모드", command=lambda: show_popup("비교모드 클릭")).grid(row=0, column=0, padx=12)
# ttk.Button(btn_frame, text="공유", command=lambda: show_popup("공유 클릭")).grid(row=0, column=1, padx=12)
# ttk.Button(btn_frame, text="북마크", command=lambda: show_popup("북마크 클릭")).grid(row=0, column=2, padx=12)

# # ------------------- 화면 리스트 -------------------
# all_frames = [frame1, frame2, frame3]
# show_frame(frame1)

# root.mainloop()
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import datetime

root = tk.Tk()
root.title("여론조사 시각화")
root.geometry("650x750")
root.configure(bg="#f9f9f9")

dates = [datetime.date(2025, 4, d) for d in [3, 10, 14, 21, 27]]
candidate_a = [48, 42, 38, 40, 55]
candidate_b = [32, 36, 44, 42, 30]
candidate_c = [20, 19, 18, 16, 15]

def show_frame(target):
    for frame in all_frames:
        frame.pack_forget()
    target.pack(pady=20, fill="both", expand=True)

frame_selection = tk.Frame(root, bg="#f9f9f9")

# 전체 제목
tk.Label(frame_selection, text="여론조사 기관, 선거 종류 및 조회 기간 선택",
         font=("맑은 고딕", 16, "bold"), bg="#f9f9f9", fg="#333").pack(pady=(20, 15))

# 기관 선택 소제목
tk.Label(frame_selection, text="기관 선택:", font=("맑은 고딕", 14, "bold"), bg="#f9f9f9", fg="#444").pack(anchor="w", padx=40, pady=(10, 0))

agencies = ["갤럽", "한국리서치", "리얼미터", "KSOI"]
agency_var = tk.StringVar(value="갤럽")
agency_frame = tk.Frame(frame_selection, bg="#f9f9f9")
agency_frame.pack(padx=40, pady=(5, 15), fill="x")
for agency in agencies:
    ttk.Radiobutton(agency_frame, text=agency, variable=agency_var, value=agency).pack(anchor="w", pady=3)

# 선거 종류 및 기간 선택 소제목
tk.Label(frame_selection, text="선거 종류 및 조회 기간:", font=("맑은 고딕", 14, "bold"), bg="#f9f9f9", fg="#444").pack(anchor="w", padx=40, pady=(10, 0))

subject_cb = ttk.Combobox(frame_selection, values=["대통령", "국회의원", "정당"], state="readonly", font=("맑은 고딕", 12))
subject_cb.set("대통령")
subject_cb.pack(pady=8, padx=40, fill="x")

period_cb = ttk.Combobox(frame_selection, values=["7일", "30일", "90일"], state="readonly", font=("맑은 고딕", 12))
period_cb.set("30일")
period_cb.pack(pady=8, padx=40, fill="x")

ttk.Button(frame_selection, text="다음", command=lambda: on_next_click()).pack(pady=30)

frame3 = tk.Frame(root, bg="#f9f9f9")
tk.Label(frame3, text="여론조사 시각화 결과", font=("맑은 고딕", 16, "bold"), bg="#f9f9f9", fg="#333").pack(pady=(20, 15))

info_label = tk.Label(frame3, font=("맑은 고딕", 12), bg="#f9f9f9", fg="#666")
info_label.pack(padx=40, pady=(0, 15))

fig, ax = plt.subplots(figsize=(6, 3.5), dpi=100)

def draw_plot():
    ax.clear()
    ax.plot(dates, candidate_a, label="후보 A", color="#1f77b4", linewidth=2)
    ax.plot(dates, candidate_b, label="후보 B", color="#d62728", linewidth=2)
    ax.plot(dates, candidate_c, label="후보 C", color="#ff7f0e", linewidth=2)
    ax.set_ylim(0, 60)
    ax.set_ylabel("지지율 (%)", fontsize=12)
    ax.set_xticks(dates)
    ax.set_xticklabels([d.strftime('%m/%d') for d in dates], fontsize=10)
    ax.legend(fontsize=10)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

canvas = FigureCanvasTkAgg(fig, master=frame3)
canvas.draw()
canvas.get_tk_widget().pack(padx=40)

tk.Label(frame3, text="GPT 요약 및 해설", font=("맑은 고딕", 14, "bold"), bg="#f9f9f9", fg="#333").pack(pady=(20, 8))
summary = (
    "후보 A는 초반 지지율 하락 후 다시 상승세를 보이며\n"
    "최종적으로 55%의 높은 지지율을 기록했습니다.\n"
    "후보 B는 한때 지지율이 상승했으나, 막판에 감소했고\n"
    "후보 C는 지속적으로 하락세를 보였습니다."
)
summary_label = tk.Label(frame3, text=summary, justify="left", font=("맑은 고딕", 11), bg="#f9f9f9", fg="#555",
                         padx=20, pady=10)
summary_label.pack(padx=40, fill="x")

btn_frame = tk.Frame(frame3, bg="#f9f9f9")
btn_frame.pack(pady=20, fill='x', padx=40)

def show_popup(msg):
    popup = tk.Toplevel(root)
    popup.title("알림")
    popup.geometry("300x130")
    popup.configure(bg="#f0f8ff")
    tk.Label(popup, text=msg, font=("맑은 고딕", 13), bg="#f0f8ff", fg="#333").pack(padx=20, pady=20)
    ttk.Button(popup, text="닫기", command=popup.destroy).pack()

btn_style = ttk.Style()
btn_style.configure("TButton", font=("맑은 고딕", 11), padding=6)

ttk.Button(btn_frame, text="비교모드", command=lambda: show_popup("비교모드 클릭"))\
    .pack(side=tk.LEFT, expand=True, fill='x', padx=5)
ttk.Button(btn_frame, text="공유", command=lambda: show_popup("공유 클릭"))\
    .pack(side=tk.LEFT, expand=True, fill='x', padx=5)
ttk.Button(btn_frame, text="북마크", command=lambda: show_popup("북마크 클릭"))\
    .pack(side=tk.LEFT, expand=True, fill='x', padx=5)

all_frames = [frame_selection, frame3]

def update_info_and_plot():
    info_label.config(text=f"조사기관: {agency_var.get()}  |  기간: {period_cb.get()}")
    draw_plot()
    canvas.draw()

def on_next_click():
    update_info_and_plot()
    show_frame(frame3)

show_frame(frame_selection)

root.mainloop()
