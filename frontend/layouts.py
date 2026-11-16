from dash import html, dcc
import dash_bootstrap_components as dbc

sidebar = dbc.Card(
    dbc.CardBody(
        [
            html.H5('Dataset', className='mb-3'),
            dcc.Upload(
                id='upload',
                children=dbc.Button('Choose CSV', color='primary', className='w-100'),
                multiple=False
            ),
            html.Br(),
            html.Label('Select dataset'),
            dcc.Dropdown(
                id='dataset-dropdown',
                placeholder='Choose a dataset...'
            )
        ]
    ),
    style={
        'borderRadius': '15px'
    }
)

chat_area = dbc.Card(
    dbc.CardBody(
        [
            html.H4('AI Data Scientist Copilot', className='mb-4'),
            html.Div(
                id='chat-window',
                children=[
                    dbc.Alert('Hello! Upload a dataset and ask me anything.', color='light')
                ],
                style={
                    'height': '500px',
                    'overflowY': 'auto',
                    'padding': '10px'
                }
            ),
            html.Br(),
            dcc.Store(
                id='chat-history',
                data=[]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Textarea(
                            id='question',
                            placeholder='Ask a question about your dataset...',
                            style={
                                'width': '100%',
                                'height': '70px',
                                'borderRadius': '10px',
                                'padding': '10px'
                            }
                        ),
                        width=10
                    ),
                    dbc.Col(
                        dbc.Button('Send', id='send', color='success', style={'height': '70px', 'width': '100%'}),
                        width=2
                    )
                ]
            )
        ]
    ),
    style={'borderRadius': '15px'}
)

layout = dbc.Container(
    dbc.Row(
        [
            dbc.Col(sidebar, width=3),
            dbc.Col(chat_area, width=9)
        ],
        style={
            'height': '100vh',
            'paddingTop': '30px'
        }
    ),
    fluid=True,
    style={
        'backgroundColor': '#f8f9fa',
        'height': '100vh'
    }
)

# layout = dbc.Container(
#     [
#         dbc.Row(
#             [
#                 dbc.Col(
#                     html.Div(
#                         "SIDEBAR",
#                         style={
#                             "backgroundColor": "lightblue",
#                             "height": "500px"
#                         }
#                     ),
#                     width=3
#                 ),

#                 dbc.Col(
#                     html.Div(
#                         "CHAT",
#                         style={
#                             "backgroundColor": "lightgray",
#                             "height": "500px"
#                         }
#                     ),
#                     width=9
#                 )
#             ]
#         )
#     ],
#     fluid=True
# )