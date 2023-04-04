import PySimpleGUI as sg

sg.theme("DarkAmber")

add_item_layout = [
    [
        sg.Text("Plate number", font="any 12"),
        sg.Input(
            "a",  # FOR TESTING default value
            font="any 12",
            key="-NEW_CAR_REGISTRATION_INPUT-",
        ),
    ],
    [
        sg.Text("Car color", font="any 12"),
        sg.Input(
            "a",  # FOR TESTING default value
            font="any 12",
            key="-COLOR_INPUT-",
        ),
    ],
    [
        sg.Text("Company name", font="any 12"),
        sg.Input(
            "a",  # FOR TESTING default value
            font="any 12",
            key="-COMPANY_NAME_INPUT-",
        ),
    ],
    [
        sg.Text("Car size", font="any 12"),
        sg.Combo(
            ["Bike", "Car", "Bus"],
            default_value="Bike",  # FOR TESTING
            font="any 12",
            key="-VEHICLE_TYPE-",
            readonly=True,
        ),
        sg.Text("Entry point", font="any 12"),
        sg.Combo(
            ["A", "B", "C"],
            default_value="A",  # FOR TESTING,
            font="any 12",
            key="-ENTRY_POINT-",
            readonly=True,
        ),
        sg.Button("Enter", font="any 12", key="-NEW_VEHICLE_SUBMIT-"),
    ],
]


window = sg.Window(
    "Excel send to email in PDF form",
    add_item_layout,
    finalize=True,
    element_padding=(20),
)

while True:
    event, values = window.read()
    if event in [sg.WIN_CLOSED, "Cancel"]:  # if user closes window or clicks cancel
        break
    print(event)
    if event == "-NEW_VEHICLE_SUBMIT-":
        print("values: ", values, "\nevents:", event)


window.close()
