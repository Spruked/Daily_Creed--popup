import json
import os
import time
import tkinter as tk
from datetime import date
import schedule

# ---------- SETTINGS ----------
POPUP_TIMES = ["07:00", "12:00", "18:00"]   # 3 times/day - edit anytime
CREEDS_JSON = "creeds.json"
STATE_FILE = "creed_state.json"
AUTO_CLOSE_SECONDS = 45                      # popup closes itself
# ----------------------------

def load_creeds():
    if not os.path.exists(CREEDS_JSON):
        raise FileNotFoundError(f"Missing {CREEDS_JSON}. Run extract_creeds.py first.")
    with open(CREEDS_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def load_state():
    # State holds: day_index (1..101) and last_date (YYYY-MM-DD)
    if not os.path.exists(STATE_FILE):
        return {"day_index": 1, "last_date": None}
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

def roll_day_if_needed(state):
    today = date.today().isoformat()
    if state.get("last_date") != today:
        # New day → advance day_index
        state["last_date"] = today
        if state["day_index"] < 101:
            state["day_index"] += 1
        else:
            state["day_index"] = 1
        save_state(state)

def show_popup(title, message):
    root = tk.Tk()
    root.title(title)
    root.geometry("720x420")
    root.attributes("-topmost", True)

    # Simple readable layout
    root.configure(bg="#0b0b0b")
    frame = tk.Frame(root, bg="#0b0b0b", padx=24, pady=24)
    frame.pack(expand=True, fill="both")

    heading = tk.Label(
        frame,
        text=title,
        fg="#ffffff",
        bg="#0b0b0b",
        font=("Segoe UI", 18, "bold")
    )
    heading.pack(anchor="w")

    body = tk.Label(
        frame,
        text=message,
        fg="#e8e8e8",
        bg="#0b0b0b",
        font=("Segoe UI", 13),
        justify="left",
        wraplength=660
    )
    body.pack(anchor="w", pady=(14, 18), fill="both", expand=True)

    btn = tk.Button(frame, text="Stand.", command=root.destroy)
    btn.pack(anchor="e")

    # Auto-close
    root.after(AUTO_CLOSE_SECONDS * 1000, root.destroy)
    root.mainloop()

def popup_job():
    creeds = load_creeds()
    state = load_state()
    roll_day_if_needed(state)

    idx = str(state["day_index"])
    creed_text = creeds.get(idx, f"(Missing creed {idx} in {CREEDS_JSON})")

    title = f"Creed {idx} of 101"
    show_popup(title, creed_text)

def main():
    print("Starting...")
    popup_job()
    print("Popup job finished.")
if __name__ == "__main__":
    main()

