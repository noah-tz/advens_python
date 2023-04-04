from dash import Dash, dcc, Output, Input, html
import dash_bootstrap_components as dbc

from ticket import Ticket

list_tickets = [
    Ticket("a", "b"),
    Ticket("c", "d"),
    Ticket("e", "f"),
    Ticket("g", "h"),
    Ticket("i", "j"),
]
item_types = ["shirt", "pants", "suit", "underwear"]

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])


def ticket_card(ticket):
    return html.Div(
        [
            html.Div(
                [
                    html.P(f"item_type: {ticket.item_type}", style={"padding": "10px"}),
                    html.P(f"name: {ticket.name}", style={"padding": "10px"}),
                ],
                style={
                    "display": "flex",
                    "justify-content": "center",
                    "align-items": "center",
                    "padding": "10px",
                },
            ),
            html.P(
                f"item entered at: {ticket.time_entered}",
                style={"padding": "10px"},
            ),
            html.P(f"priority: {ticket.priority}", style={"padding": "10px"}),
        ],
        style={
            "display": "flex",
            "flex-direction": "column",
            "justify-content": "center",
            "align-items": "left",
            "width": "350px",
            "height": "150px",
            "border": "1px white solid",
            "border-radius": "5px",
            "margin": "5px",
        },
    )


def ticket_list(title, ticket_list):
    return html.Div(
        [
            html.H1(title),
            html.Div([ticket_card(ticket) for ticket in ticket_list]),
        ]
    )


main_tab = html.Div(
    [
        ticket_list("waiting list", list_tickets),
        ticket_list("ready for pickup", list_tickets),
    ],
    style={
        "display": "flex",
        "justify-content": "center",
        "align-items": "space-between",
    },
)

new_item_layout = html.Div([dcc.Input(placeholder="name"), dcc.Dropdown(item_types)])
input_exit_tab = html.Div(dcc.Dropdown(item_types))
first_text = dcc.Markdown("first_text")
second_text = dcc.Markdown("second_text")
second_element = dcc.Tabs(
    [
        dcc.Tab(input_exit_tab, label="new/remove item"),
        dcc.Tab(main_tab, label="main"),
        dcc.Tab(second_text, label="third tab"),
    ]
)

app.layout = dbc.Container([second_element])

if __name__ == "__main__":
    app.run_server(port=8053)
