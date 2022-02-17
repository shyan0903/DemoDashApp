from dash import Dash, dcc, html, Input, Output
import altair as alt
import pandas as pd

data = pd.read_csv("crime.csv")

app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])    
server = app.server

app.layout = html.Div([
        html.Iframe(
            id='scatter',
            style={'border-width': '0', 'width': '100%', 'height': '400px'}),
        dcc.Slider(id='xslider', min=0, max=1, value=1),
        dcc.Dropdown(id='color', value='black', 
        options=['black', 'blue', 'red', 'green'])])

@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xslider', 'value'),
    Input('color', 'value'))
def plot_altair(xmax, color):
    chart = alt.Chart(data[data['racePctWhite'] < xmax]).mark_point(
        color=color
    ).encode(
        alt.X('racePctWhite', title='Percentage of White People'),
        alt.Y('NumImmig', title='Number of Immigrants')
    ).properties(
        title='Population Information of the U.S.A.'
    )
    return chart.to_html()       

if __name__ == '__main__':
    app.run_server(debug=True)
