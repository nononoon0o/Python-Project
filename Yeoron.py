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
from tkinter import ttk, simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import datetime
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한글 폰트 설정 (윈도우용)
font_path = "C:/Windows/Fonts/malgun.ttf"  # 말굽고딕 폰트 경로
fontprop = fm.FontProperties(fname=font_path).get_name()
plt.rcParams['font.family'] = fontprop

root = tk.Tk()
root.title("여론조사 시각화")

# 첫 번째 화면 크기
root.geometry("500x750")
root.configure(bg="#f0f4f8")

dates = [datetime.date(2025, 4, d) for d in [3, 10, 14, 21, 27]]
candidate_a = [48, 42, 38, 40, 55]
candidate_b = [32, 36, 44, 42, 30]
candidate_c = [20, 19, 18, 16, 15]

# 비교용 더미 데이터 (다른 기관 데이터라고 가정)
compare_data = {
    "갤럽": {
        "candidate_a": [48, 42, 38, 40, 55],
        "candidate_b": [32, 36, 44, 42, 30],
        "candidate_c": [20, 19, 18, 16, 15],
    },
    "한국리서치": {
        "candidate_a": [45, 44, 41, 39, 53],
        "candidate_b": [34, 35, 40, 41, 32],
        "candidate_c": [21, 21, 19, 20, 15],
    },
    "리얼미터": {
        "candidate_a": [46, 43, 39, 41, 54],
        "candidate_b": [33, 37, 42, 40, 31],
        "candidate_c": [21, 20, 19, 19, 15],
    },
    "KSOI": {
        "candidate_a": [47, 41, 37, 38, 52],
        "candidate_b": [31, 34, 43, 43, 33],
        "candidate_c": [22, 25, 20, 19, 15],
    }
}

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

agencies = ["갤럽", "한국리서치", "리얼미터", "KSOI"]
agency_var = tk.StringVar(value="갤럽")
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

period_label = tk.Label(form_area, text="조회 기간 선택:", font=("Malgun Gothic", 15, "bold"), fg="#2a9d8f", bg="#f0f4f8")
period_label.grid(row=4, column=0, sticky="w", pady=(8, 6))
period_cb = ttk.Combobox(form_area, values=["7일", "30일", "90일"], state="readonly", font=("Malgun Gothic", 13))
period_cb.set("30일")
period_cb.grid(row=5, column=0, sticky="we", pady=10)

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

    # 원래 선택된 기관 데이터
    agency = agency_var.get()
    data = compare_data[agency]

    ax.plot(dates, data["candidate_a"], label=f"{agency} 후보 A", color="#264653", linewidth=2.5)
    ax.plot(dates, data["candidate_b"], label=f"{agency} 후보 B", color="#e76f51", linewidth=2.5)
    ax.plot(dates, data["candidate_c"], label=f"{agency} 후보 C", color="#2a9d8f", linewidth=2.5)

    # 비교 모드 켜져 있고, 비교 기관이 다르고 유효하면 추가 시각화
    if compare_agency and compare_agency != agency and compare_agency in compare_data:
        comp = compare_data[compare_agency]
        ax.plot(dates, comp["candidate_a"], label=f"{compare_agency} 후보 A", color="#264653", linewidth=2.5, linestyle='dashed')
        ax.plot(dates, comp["candidate_b"], label=f"{compare_agency} 후보 B", color="#e76f51", linewidth=2.5, linestyle='dashed')
        ax.plot(dates, comp["candidate_c"], label=f"{compare_agency} 후보 C", color="#2a9d8f", linewidth=2.5, linestyle='dashed')

    ax.set_ylim(0, 60)
    ax.set_ylabel("지지율 (%)", fontsize=9, color="#264653")
    ax.set_xticks(dates)
    ax.set_xticklabels([d.strftime('%m/%d') for d in dates], fontsize=8, rotation=40, color="#264653")
    ax.legend(fontsize=9)
    ax.grid(axis='y', linestyle='--', alpha=0.6)
    fig.tight_layout()
    canvas.draw()

# 현재 비교 기관을 저장하는 변수
current_compare_agency = None

def generate_summary(agency, subject, period, compare_agency=None):
    base_summary = (
        f"{agency}의 여론조사 결과에 따르면, {subject} 선거에서\n"
        f"후보 A는 평균 {sum(compare_data[agency]['candidate_a'])//len(dates)}%, "
        f"후보 B는 평균 {sum(compare_data[agency]['candidate_b'])//len(dates)}%, "
        f"후보 C는 평균 {sum(compare_data[agency]['candidate_c'])//len(dates)}%의 지지율을 기록했습니다.\n"
        f"조회 기간은 {period}입니다."
    )
    if compare_agency and compare_agency != agency:
        base_summary += f"\n비교 대상은 {compare_agency} 기관의 데이터입니다."

    return base_summary

def on_next_click():
    global current_compare_agency
    current_compare_agency = None  # 초기화

    agency = agency_var.get()
    subject = subject_cb.get()
    period = period_cb.get()

    info_label.config(text=f"기관: {agency} / 선거 종류: {subject} / 기간: {period}")
    summary_label.config(text=generate_summary(agency, subject, period))
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
        summary_label.config(text=generate_summary(agency_var.get(), subject_cb.get(), period_cb.get(), current_compare_agency))
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
