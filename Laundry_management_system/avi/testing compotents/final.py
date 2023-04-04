from functools import partial
from typing import Callable, Any

from fuzzywuzzy import process, fuzz
import PySimpleGUI as sg


# SG: Helper functions:
def clear_combo_tooltip(*_, ui_handle: sg.Element, **__) -> None:
    if tt := ui_handle.TooltipObject:
        tt.hidetip()
        ui_handle.TooltipObject = None


def show_combo_tooltip(ui_handle: sg.Element, tooltip: str) -> None:
    ui_handle.set_tooltip(tooltip)
    tt = ui_handle.TooltipObject
    tt.y += 40
    tt.showtip()


def symbol_text_updated(
    event_data: dict[str, Any], all_values: list[str], ui_handle: sg.Element
) -> None:
    new_text = event_data[ui_handle.key]
    if new_text == "":
        ui_handle.update(values=all_values)
        return
    matches = process.extractBests(
        new_text, all_values, scorer=fuzz.ratio, score_cutoff=40
    )
    sym = [m[0] for m in matches]
    ui_handle.update(new_text, values=sym)

    # tk.call('ttk::combobox::Post', ui_handle.widget)  # This opens the list of options, but takes focus
    clear_combo_tooltip(ui_handle=ui_handle)
    show_combo_tooltip(ui_handle=ui_handle, tooltip="\n".join(sym))


# Prepare data:
all_symbols = [
    "AAPL",
    "AMZN",
    "MSFT",
    "TSLA",
    "GOOGL",
    "BRK.B",
    "UNH",
    "JNJ",
    "XOM",
    "JPM",
    "META",
    "PG",
    "NVDA",
    "KO",
]

# SG: Layout
sg.theme("DarkAmber")
layout = [
    [
        sg.Text("Symbol:"),
        sg.Combo(
            all_symbols,
            enable_events=True,
            key="-SYMBOL-",
        ),
    ]
]

# SG: Window
window = sg.Window("Symbol data:", layout, finalize=True)
window["-SYMBOL-"].bind("<Key-Down>", "KeyDown")

# SG: Event loop
callbacks: dict[str:Callable] = {
    "-SYMBOL-": partial(
        symbol_text_updated, all_values=all_symbols, ui_handle=window["-SYMBOL-"]
    ),
    "-SYMBOL-KeyDown": partial(clear_combo_tooltip, ui_handle=window["-SYMBOL-"]),
}
unhandled_event_callback = partial(
    lambda x: print(f"Unhandled event key: {event}. Values: {x}")
)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    callbacks.get(event, unhandled_event_callback)(values)


# SG: Cleanup
window.close()
