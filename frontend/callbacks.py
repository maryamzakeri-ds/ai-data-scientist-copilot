from dash import Input, Output, State, html
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from api import ask_chat

def register_callbacks(app):
    @app.callback(
        Output('chat-history', 'data'),
        Output('chat-window', 'children'),
        Output('question', 'value'),
        Input('send', 'n_clicks'),
        State('question', 'value'),
        State('chat-history', 'data'),
        prevent_initial_call=True
    )

    def send_message(n_clicks, question, history):
        if not question:
            raise PreventUpdate

        history.append({
            'role': 'user',
            'content': question
        })

        response = ask_chat(question)
        history.append({
            'role': 'assistent',
            'content': response['answer']
        })

        messages = []
        for msg in history:
            if msg['role'] == 'user':
                messages.append(
                    html.Div(
                        dbc.Alert(msg['content'], color='primary'),
                        style={
                            'display': 'flex',
                            'justifyContent': 'flex-end'
                        }
                    ) 
                )
                    
            else:
                messages.append(
                    html.Div(
                        dbc.Alert(msg['content'], color='light'),
                        style={
                            'display': 'flex',
                            'justifyContent': 'flex-start'
                        }
                    ) 
                )

        return history, messages, ''
    