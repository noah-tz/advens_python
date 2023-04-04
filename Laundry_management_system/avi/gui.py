import PySimpleGUI as sg


class CleanersGUI:
    def __init__(self):
        sg.theme("DarkAmber")
        self.__right_new_client_layout = [
            [sg.Input(font="any 12"), sg.Text(":םש", font="any 12")],
            [sg.Input(font="any 12"), sg.Text(":החפשמ", font="any 12")],
            [sg.Input(font="any 12"), sg.Text(":ריע", font="any 12")],
            [sg.Input(font="any 12"), sg.Text(":בוחר", font="any 12")],
            [sg.Input(font="any 12"), sg.Text(":רפסמ", font="any 12")],
        ]
        self.__left_new_client_layout = [
            [sg.Input(font="any 12"), sg.Text(":ליימ", font="any 12")],
            [sg.Input(font="any 12"), sg.Text(":ןופלט", font="any 12")],
            [sg.Input(font="any 12"), sg.Text(":1 דיינ", font="any 12")],
            [sg.Input(font="any 12"), sg.Text(":2 דיינ", font="any 12")],
            [
                sg.Radio("חולשל אל", "-RADIO-", font="any 12"),
                sg.Radio("ליימ", "-RADIO-", font="any 12"),
                sg.Radio("ןורסמ", "-RADIO-", font="any 12"),
                sg.Text(":ל חולשל", font="any 12"),
            ],
        ]
        self.__full_new_client_layout = [
            [
                sg.Column(self.__left_new_client_layout),
                sg.Column(self.__right_new_client_layout),
            ],
            [sg.Button("חולשל", font="any 12")],
        ]
        self.__right_new_order_layout = [
            [sg.Input(font="any 12"), sg.Text(":םש", font="any 12")],
            [sg.Input(font="any 12"), sg.Text(":החפשמ", font="any 12")],
        ]
        self.__left_new_order_layout = [
            [sg.Input(font="any 12"), sg.Text(":ןופלט", font="any 12")],
        ]
        self.__full_new_order_layout = [
            [
                sg.Column(self.__left_new_order_layout),
                sg.Column(self.__right_new_order_layout),
            ],
            [sg.Button("חולשל", font="any 12")],
        ]
        self.__full_settings_layout = [[sg.Text("settings")]]
        self.__full_tab_layout = [
            [
                sg.TabGroup(
                    [
                        [
                            sg.Tab(
                                "חוקל תפסוה",
                                self.__full_new_client_layout,
                                key="_mykey_",
                            ),
                            sg.Tab("שדח הנמזה", self.__full_new_order_layout),
                            sg.Tab("תורדגה", self.__full_settings_layout),
                        ]
                    ],
                    key="_group1_",
                    tab_location="righttop",
                )
            ]
        ]

    def build_window(self) -> object:
        """builds the main window with all the tabs
        Returns:
            object: sg.window element with all the elements
        """
        return sg.Window(
            "Cleaners program",
            finalize=True,
            element_padding=(20),
            resizable=True,
        ).Layout(self.__full_tab_layout)


instance_gui = CleanersGUI()
window = instance_gui.build_window()


while True:
    event, values = window.read()
    if event in [sg.WIN_CLOSED, "Cancel"]:  # if user closes window or clicks cancel
        break
    print(event)
    print(values)
