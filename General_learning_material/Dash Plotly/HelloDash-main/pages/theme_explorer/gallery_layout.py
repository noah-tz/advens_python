import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output, State
import lib.nav
from lib.other_components import change_theme_alert

# ------ Make Subheading

DBC_DOCS = "https://dash-bootstrap-components.opensource.faculty.ai/docs/components/"


def make_subheading(label, link):
    slug = label.replace(" ", "")

    heading = html.H3(
        html.Span(
            [
                label,
                html.A(
                    html.I(className="bi bi-book h4 ms-2"),
                    href=f"{DBC_DOCS}{link}",
                    target="_blank",
                    id=f"tooltip_target_{slug}",
                ),
            ],
        ),
    )

    return html.Div(
        [
            heading,
            dbc.Tooltip(f"See {label} documentation", target=f"tooltip_target_{slug}"),
        ],
        className="mt-3",
    )


# ----- Intro

intro = change_theme_alert()

# ------------ Alerts

alerts1 = dbc.Col(
    [
        dbc.Alert("This is a primary alert", color="primary"),
        dbc.Alert("This is a secondary alert", color="secondary"),
        dbc.Alert("This is a success alert! Well done!", color="success"),
        dbc.Alert("This is a warning alert... be careful...", color="warning"),
    ],
    md=6,
    xs=12,
)

alerts2 = dbc.Col(
    [
        dbc.Alert("This is a danger alert. Scary!", color="danger"),
        dbc.Alert("This is an info alert. Good to know!", color="info"),
        dbc.Alert("This is a light alert", color="light"),
        dbc.Alert("This is a dark alert", color="dark"),
    ],
    md=6,
    xs=12,
)

alerts = html.Div(
    [make_subheading("dbc.Alert", "alert"), dbc.Row([alerts1, alerts2])],
    className="mb-4",
)

# -------------------


badge = html.Div(
    [
        dbc.Badge("Primary", color="primary", className="me-1"),
        dbc.Badge("Secondary", color="secondary", className="me-1"),
        dbc.Badge("Success", color="success", className="me-1"),
        dbc.Badge("Warning", color="warning", className="me-1"),
        dbc.Badge("Danger", color="danger", className="me-1"),
        dbc.Badge("Info", color="info", className="me-1"),
        dbc.Badge("Light", color="light", className="me-1 text-dark"),
        dbc.Badge("Dark", color="dark", className="text-light"),
    ],
    className="mb-2",
)

badge_pills = html.Div(
    [
        dbc.Badge("Primary", color="primary", className="me-1", pill=True),
        dbc.Badge("Secondary", color="secondary", className="me-1", pill=True),
        dbc.Badge("Success", color="success", className="me-1", pill=True),
        dbc.Badge("Warning", color="warning", className="me-1", pill=True),
        dbc.Badge("Danger", color="danger", className="me-1", pill=True),
        dbc.Badge("Info", color="info", className="me-1", pill=True),
        dbc.Badge("Light", color="light", className="me-1 text-dark", pill=True),
        dbc.Badge("Dark", color="dark", pill=True, className="text-light"),
    ],
)

badges = html.Div(
    [make_subheading("dbc.Badge", "badge"), badge, badge_pills],
    className="mb-4",
)

# ------- buttons
buttons1 = dbc.Col(
    [
        make_subheading("dbc.Button", "button"),
        html.Div(
            [
                dbc.Button("Primary", color="primary", className="me-1 mt-1"),
                dbc.Button("Secondary", color="secondary", className="me-1 mt-1"),
                dbc.Button("Success", color="success", className="me-1 mt-1"),
                dbc.Button("Warning", color="warning", className="me-1 mt-1"),
                dbc.Button("Danger", color="danger", className="me-1 mt-1"),
                dbc.Button("Info", color="info", className="me-1 mt-1"),
            ],
            className="mb-2",
        ),
        html.Div(
            [
                dbc.Button(
                    "Primary",
                    outline=True,
                    color="primary",
                    className="me-1 mt-1",
                ),
                dbc.Button(
                    "Secondary",
                    outline=True,
                    color="secondary",
                    className="me-1 mt-1",
                ),
                dbc.Button(
                    "Success",
                    outline=True,
                    color="success",
                    className="me-1 mt-1",
                ),
                dbc.Button(
                    "Warning",
                    outline=True,
                    color="warning",
                    className="me-1 mt-1",
                ),
                dbc.Button(
                    "Danger",
                    outline=True,
                    color="danger",
                    className="me-1 mt-1",
                ),
                dbc.Button("Info", outline=True, color="info", className="me-1 mt-1"),
            ],
            className="mb-2",
        ),
        html.Div(
            [
                dbc.Button("Regular", color="primary", className="me-1 mt-1"),
                dbc.Button(
                    "Active",
                    color="primary",
                    active=True,
                    className="me-1 mt-1",
                ),
                dbc.Button(
                    "Disabled",
                    color="primary",
                    disabled=True,
                    className="me-1 mt-1",
                ),
            ],
            className="mb-2",
        ),
        html.Div(
            [
                dbc.Button("Large button", size="lg", className="me-1 mt-1"),
                dbc.Button("Regular button", className="me-1 mt-1"),
                dbc.Button("Small button", size="sm", className="me-1 mt-1"),
            ],
            className="mb-2",
        ),
    ],
    lg=6,
    xs=12,
)

buttons2 = dbc.Col(
    [
        make_subheading("ButtonGroup", "buttongroups"),
        html.Div(
            dbc.ButtonGroup(
                [
                    dbc.Button("Success", color="success"),
                    dbc.Button("Warning", color="warning"),
                    dbc.Button("Danger", color="danger"),
                ]
            ),
            className="mb-2",
        ),
        html.Div(
            dbc.ButtonGroup(
                [
                    dbc.Button("First"),
                    dbc.Button("Second"),
                    dbc.DropdownMenu(
                        [
                            dbc.DropdownMenuItem("Item 1"),
                            dbc.DropdownMenuItem("Item 2"),
                        ],
                        label="Dropdown",
                        group=True,
                    ),
                ],
                vertical=True,
            ),
            className="mb-2",
        ),
    ],
    lg=6,
    xs=12,
)

buttons = dbc.Row([buttons1, buttons2], className="mb-4")

# ----- cards

cards = html.Div(
    [
        make_subheading("dbc.Card", "card"),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader("Header"),
                            dbc.CardBody(
                                [
                                    html.H5(
                                        "This card has a title",
                                        className="card-title",
                                    ),
                                    html.P("And some text", className="card-text"),
                                ]
                            ),
                        ]
                    )
                ),
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H5(
                                        "This card has a title",
                                        className="card-title",
                                    ),
                                    html.P(
                                        "and some text, but no header",
                                        className="card-text",
                                    ),
                                ]
                            )
                        ],
                        outline=True,
                        color="primary",
                    )
                ),
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H5(
                                        "This card has a title",
                                        className="card-title",
                                    ),
                                    html.P(
                                        "and some text, and a footer!",
                                        className="card-text",
                                    ),
                                ]
                            ),
                            dbc.CardFooter("Footer"),
                        ],
                        outline=True,
                        color="dark",
                    )
                ),
            ]
        ),
    ],
    className="mb-4",
)

# ------ collapse

collapse = html.Div(
    [
        make_subheading("dbc.Collapse", "collapse"),
        html.Div(
            [
                dbc.Button(
                    "Open collapse",
                    id="dbc-gallery-x-collapse-button",
                    className="mb-2",
                ),
                dbc.Collapse(
                    dbc.Card(dbc.CardBody("This content is hidden in the collapse")),
                    id="dbc-gallery-x-collapse",
                ),
            ]
        ),
    ],
    className="mb-4",
)


@callback(
    Output("dbc-gallery-x-collapse", "is_open"),
    [Input("dbc-gallery-x-collapse-button", "n_clicks")],
    [State("dbc-gallery-x-collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


# ----- fade

fade = html.Div(
    [
        make_subheading("dbc.Fade", "fade"),
        html.Div(
            [
                dbc.Button(
                    "Toggle fade",
                    id="dbc-gallery-x-fade-button",
                    style={"marginBottom": "1rem"},
                ),
                dbc.Fade(
                    dbc.Card(
                        dbc.CardBody(
                            html.P(
                                "This content fades in and out",
                                className="card-text",
                            )
                        )
                    ),
                    id="dbc-gallery-x-fade",
                    is_in=True,
                ),
            ]
        ),
    ],
)


@callback(
    Output("dbc-gallery-x-fade", "is_in"),
    [Input("dbc-gallery-x-fade-button", "n_clicks")],
    [State("dbc-gallery-x-fade", "is_in")],
)
def toggle_fade(n, is_in):
    if n:
        return not is_in
    return is_in


# ------ form

form = html.Div(
    [
        make_subheading("dbc.Form", "form"),
        dbc.Form(
            [
                html.Div(
                    [
                        dbc.Label("Username"),
                        dbc.Input(
                            placeholder="Enter your username",
                            type="text",
                        ),
                        dbc.FormText(
                            [
                                "Can't remember your username? ",
                                html.A(
                                    "Click here.",
                                    href="#",
                                    className="text-muted",
                                    style={"textDecoration": "underline"},
                                ),
                            ]
                        ),
                    ]
                ),
                html.Div(
                    [
                        dbc.Label("Username"),
                        dbc.Input(
                            placeholder="Enter your password",
                            type="password",
                        ),
                        dbc.FormText(
                            [
                                "Can't remember your password? ",
                                html.A(
                                    "Click here.",
                                    href="#",
                                    className="text-muted",
                                    style={"textDecoration": "underline"},
                                ),
                            ]
                        ),
                    ]
                ),
            ]
        ),
    ],
    className="mb-4",
)

# ------ input

input_ = html.Div(
    [
        make_subheading("dbc.Input", "input"),
        html.Div(
            [
                dbc.Label("Valid text input"),
                dbc.Input(type="text", valid=True),
                dbc.FormFeedback("That's a valid input!", type="valid"),
            ]
        ),
        html.Div(
            [
                dbc.Label("Invalid text input"),
                dbc.Input(type="text", invalid=True),
                dbc.FormFeedback("That's an invalid input...", type="invalid"),
            ]
        ),
    ]
)

checklist_items = html.Div(
    [
        make_subheading("dbc.Checklist", "input"),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Checklist(
                        id="gallery_checklist1",
                        options=[
                            {
                                "label": "Option {}".format(i),
                                "value": i,
                            }
                            for i in range(3)
                        ],
                        value=[1, 2],
                    )
                ),
                dbc.Col(
                    dbc.Checklist(
                        id="gallery_checklist2",
                        options=[
                            {
                                "label": "Option {}".format(i),
                                "value": i,
                            }
                            for i in range(3)
                        ],
                        value=[1, 2],
                        switch=True,
                    )
                ),
            ]
        ),
        html.H5("Inline checklist", className="mt-3"),
        dbc.Checklist(
            id="gallery_checklist3",
            options=[{"label": f"Option {i + 1}", "value": i} for i in range(5)],
            value=[0, 4],
            inline=True,
        ),
    ],
    className="mb-4",
)

radio_items = html.Div(
    [
        make_subheading("dbc.RadioItems", "input"),
        dbc.RadioItems(
            id="gallery_radio1",
            options=[{"label": f"Option {i + 1}", "value": i} for i in range(3)],
            value=0,
        ),
        html.H5("Inline radioitems", className="mt-3"),
        dbc.RadioItems(
            id="gallery_radio2",
            options=[{"label": f"Option {i + 1}", "value": i} for i in range(5)],
            value=0,
            inline=True,
        ),
    ]
)

input_group = html.Div(
    [
        make_subheading("InputGroup and addons", "input_group"),
        dbc.InputGroup(
            [
                dbc.Button("To the left!", color="danger"),
                dbc.Input(type="text"),
            ],
            className="my-3",
        ),
        dbc.InputGroup(
            [
                dbc.Input(type="text"),
                dbc.Button("To the right!", color="success"),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("@"),
                dbc.Input(type="text", placeholder="Enter username"),
            ],
            className="mb-3",
        ),
    ],
    className="mb-4",
)


# ----- list_group

list_group = html.Div(
    [
        make_subheading("dbc.ListGroup", "list_group"),
        dbc.ListGroup(
            [
                dbc.ListGroupItem("Item 1", color="primary", action=True),
                dbc.ListGroupItem("Item 2"),
                dbc.ListGroupItem("Item 3"),
                dbc.ListGroupItem(
                    [
                        html.H5("Item 4 heading"),
                        html.P("Item 4 text"),
                    ]
                ),
            ]
        ),
    ],
    className="mb-4",
)

# ----- modal


COOKIE = "https://todaysmama.com/.image/t_share/MTU5OTEwMzkyMDIyMTE1NzAz/cookie-monster.png"  # noqa
modal = html.Div(
    [
        make_subheading("dbc.Modal", "modal"),
        html.P(
            [
                dbc.Button("Show the cookie monster", id="dbc-gallery-x-button"),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Cookies!"),
                        dbc.ModalBody(html.Img(src=COOKIE, style={"width": "100%"})),
                    ],
                    id="dbc-gallery-x-modal",
                    is_open=False,
                ),
            ]
        ),
    ],
    className="mb-4",
)


@callback(
    Output("dbc-gallery-x-modal", "is_open"),
    [Input("dbc-gallery-x-button", "n_clicks")],
    [State("dbc-gallery-x-modal", "is_open")],
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open


# ------ navbar

DBC_HOME = "https://dash-bootstrap-components.opensource.faculty.ai/"
DBC_GITHUB = "https://github.com/facultyai/dash-bootstrap-components"

navbar_children = [
    dbc.NavItem(dbc.NavLink("GitHub", href=DBC_GITHUB, target="_blank")),
    dbc.DropdownMenu(
        nav=True,
        in_navbar=True,
        label="Menu",
        children=[
            dbc.DropdownMenuItem("Entry 1", href="https://google.com"),
            dbc.DropdownMenuItem("Entry 2", href="/test"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("A heading", header=True),
            dbc.DropdownMenuItem(
                "Entry 3",
                href="/external-relative",
                external_link=True,
            ),
            dbc.DropdownMenuItem("Entry 4 - does nothing"),
        ],
    ),
]

navbar = html.Div(
    [
        make_subheading("dbc.Navbar", "navbar"),
        dbc.NavbarSimple(
            children=navbar_children,
            brand="Navbar",
            brand_href=DBC_HOME,
            color="primary",
            dark=True,
            className="mb-3",
        ),
        dbc.NavbarSimple(
            children=navbar_children,
            brand="Navbar",
            brand_href=DBC_HOME,
            color="light",
            className="mb-3",
        ),
        dbc.NavbarSimple(
            children=navbar_children,
            brand="Navbar",
            brand_href=DBC_HOME,
            color="dark",
            dark=True,
        ),
    ],
    className="mb-4",
)

# ----- popover

popover = html.Div(
    [
        make_subheading("dbc.Popover", "popover"),
        dbc.Button(
            "Click to toggle popover", id="dbc-gallery-x-popover-target", color="danger"
        ),
        dbc.Popover(
            [
                dbc.PopoverHeader("Popover header"),
                dbc.PopoverBody("Popover body"),
            ],
            id="dbc-gallery-x-popover",
            is_open=False,
            target="popover-target",
        ),
    ],
    className="mb-4",
)


@callback(
    Output("dbc-gallery-x-popover", "is_open"),
    [Input("dbc-gallery-x-popover-target", "n_clicks")],
    [State("dbc-gallery-x-popover", "is_open")],
)
def toggle_popover(n, is_open):
    if n:
        return not is_open
    return is_open


# ------ progress

progress = html.Div(
    [
        make_subheading("dbc.Progress", "progress"),
        dbc.Progress("25%", value=25),
        dbc.Progress(value=50, striped=True, className="my-2"),
        dbc.Progress(value=75, color="success"),
    ],
    className="mb-4",
)

# ----- spinner

spinner = html.Div(
    [
        make_subheading("dbc.Spinner", "spinner"),
        html.Div(
            [
                dbc.Spinner(color=col)
                for col in [
                    "primary",
                    "secondary",
                    "success",
                    "warning",
                    "danger",
                ]
            ],
            className="mb-2",
        ),
        html.Div(
            [
                dbc.Spinner(color=col, type="grow")
                for col in [
                    "primary",
                    "secondary",
                    "success",
                    "warning",
                    "danger",
                ]
            ],
            className="mb-2",
        ),
    ],
    className="mb-4",
)

# ------ table

table = html.Div(
    [
        make_subheading("dbc.Table", "table"),
        dbc.Table(
            [
                html.Thead(
                    html.Tr(
                        [
                            html.Th("#"),
                            html.Th("First name"),
                            html.Th("Last name"),
                        ]
                    )
                ),
                html.Tbody(
                    [
                        html.Tr(
                            [
                                html.Th("1", scope="row"),
                                html.Td("Tom"),
                                html.Td("Cruise"),
                            ]
                        ),
                        html.Tr(
                            [
                                html.Th("2", scope="row"),
                                html.Td("Jodie"),
                                html.Td("Foster"),
                            ]
                        ),
                        html.Tr(
                            [
                                html.Th("3", scope="row"),
                                html.Td("Chadwick"),
                                html.Td("Boseman"),
                            ]
                        ),
                    ]
                ),
            ],
            responsive=True,
            striped=True,
            hover=True,
        ),
    ],
    className="mb-4",
)

# ------ tabs

tabs = html.Div(
    [
        make_subheading("dbc.Tabs", "tabs"),
        dbc.Tabs(
            [
                dbc.Tab(html.P("This is tab 1", className="py-3"), label="Tab 1"),
                dbc.Tab(
                    dbc.Card(
                        [
                            html.P(
                                "This tab has a card!",
                                className="card-text",
                            ),
                            dbc.Button("Click here", color="success"),
                        ],
                        body=True,
                    ),
                    label="Tab 2",
                    style={"padding": "10px"},
                ),
            ]
        ),
    ],
    className="mb-4",
)

#  This component causes the browser to crash if you switch pages too soon.
# probably because of the duration 4000

# ----- toast
#
# toast = html.Div(
#     [
#         make_subheading("dbc.Toast", "toast"),
#         dbc.Button(
#             "Open toast", id="dbc-gallery-x-auto-toast-toggle", color="primary", className="mb-3",
#         ),
#         dbc.Toast(
#             html.P("This is the content of the toast", className="mb-0"),
#             id="dbc-gallery-x-auto-toast",
#             header="This is the header",
#             icon="primary",
#             duration=4000,
#         ),
#     ],
#     className="mb-2",
# )


@callback(
    Output("dbc-gallery-x-auto-toast", "is_open"),
    [Input("dbc-gallery-x-auto-toast-toggle", "n_clicks")],
)
def open_toast(_):
    return True


# ------ tooltip

tooltip = html.Div(
    [
        make_subheading("dbc.Tooltip", "tooltip"),
        html.P(
            [
                "I wonder what ",
                html.Span("floccinaucinihilipilification", id="gallery-tooltip-target"),
                " means?",
            ]
        ),
        dbc.Tooltip(
            "Noun: rare, " "the action or habit of estimating something as worthless.",
            target="gallery-tooltip-target",
        ),
    ],
    className="mb-4",
)


layout = html.Div(
    [
        intro,
        lib.nav.make_header("Dash Bootstrap Components Gallery", spacing=""),
        alerts,
        badges,
        buttons,
        cards,
        collapse,
        fade,
        dbc.Row(
            [
                dbc.Col([form, input_group], xs=12, md=6),
                dbc.Col([input_], xs=12, md=6),
            ]
        ),
        dbc.Row(
            [
                dbc.Col([checklist_items], xs=12, md=6),
                dbc.Col([radio_items], xs=12, md=6),
            ]
        ),
        list_group,
        modal,
        navbar,
        popover,
        progress,
        spinner,
        table,
        tabs,
        #  toast,  Keep this deleted - causes the browser to crash
        tooltip,
    ],
    className="dbc",
)
