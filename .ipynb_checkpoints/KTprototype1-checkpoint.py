import dash
import dash_html_components as html
import dash_core_components as dcc
import altair as alt
import pandas as pd
from vega_datasets import data
from dash.dependencies import Input, Output

##########################
df = pd.read_csv('Sleep_Efficiency.csv')

## Wrangle Data 
# Handling na, strategy = replaced by mean
df['Alcohol consumption'].fillna(df['Alcohol consumption'].mean(),inplace=True)
df['Caffeine consumption'].fillna(df['Caffeine consumption'].mean(),inplace=True)
df['Awakenings'].fillna(round(df['Awakenings'].mean()),inplace=True)
df['Exercise frequency'].fillna(round(df['Exercise frequency'].mean()),inplace=True)

# df['Awakenings'].value_counts()
# df.isnull().sum()

# Bin ages into 11 groups, Create new df col binnedAge
age_bins = [0] + [5*i for i in range(3,13)] + [df.Age.max()]
age_bins_labels = ['0-15','15-20','21-25','26-30','31-35','36-40','41-45','46-50','51-55','56-60','60+']
df['binnedAge'] = pd.cut(df['Age'],bins=age_bins,labels=age_bins_labels)

################################
## Define Charts


def awakening_bar():
    chart = alt.Chart(df).mark_bar().encode(
        x = 'count()',
        y = alt.Y('Awakenings:O'),
        color = alt.Color('Gender')
    )
    return chart.to_html()

################################
## Define Layouts
# Tentative, appropriate css to be set
app=dash.Dash(__name__,external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = html.Div([
    # Left Div : Input Controls
    html.Div([html.P('Sleep Efficiency Dash'),
             html.Br(),
             html.Div(id='check-input-value'),
             html.P('Smoke Status'),
             dcc.Checklist(
                 id='smoke-status-input',
                 options=['Yes','No'],
                 value=['Yes','No']),             
             html.P('Alcohol Consumption'),
             dcc.RangeSlider(
                 id='alcohol-consumption-input',
                 min=0,max=5,step=1,value=[0,5],
                 marks={i:str(i) for i in range(0,6)}),
             html.P('Caffeine Consumption'),
             dcc.RangeSlider(
                 id='caffeine-consumption-input',
                 min=0,max=200,step=25,value=[0,200],
                 marks={25*i:str(25*i) for i in range(0,9)}),
             html.P('Execise Frequency'),
             dcc.RangeSlider(
                 id='exercise-frequency-input',
                 min=0,max=5,step=1,value=[0,5],
                 marks={i:str(i) for i in range(0,6)})
             ],
            style={'width': '15%', 'display': 'inline-block'}),
    # Right Main Div 
    html.Div([
        # Right Top
        html.Div([
            # Right Top Left
            html.Div([
                'Right Top Left Section',
                html.Br(),
                html.Iframe(
                    id = 'age_sleepeff',
#                    srcDoc=age_sleepeff_line(),
                    style={'height':'500px','width':'400px'}
                )],style={'width': '38%', 'display': 'inline-block'}
            ),
            
            # Right Top Right
            html.Div([
                'Right Top Right Section',
                html.Iframe(
                    id = 'age_sleepdur',
#                    srcDoc=age_sleepdur_bar(),
                    style={'height':'500px','width':'800px'} #,'float':'right', 'display': 'inline-block'}
                )], style={'width': '58%','display': 'inline-block'}
            )]         
        ),
        # Right Bottom
        html.Div([
            'graph bottom',
            html.Iframe(
                id = 'awakening',
                srcDoc=awakening_bar(),
                style={'width': '100%','height':'400px', 'display': 'inline-block'}
            )
        ])],
        style={'width': '78%', 'float':'right','display': 'inline-block'}
    )]
)
# Ref: https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Dash%20Components/Checklist/checkbox.py

@app.callback(
    Output('age_sleepeff','srcDoc'),
    Output('age_sleepdur','srcDoc'),
    Output('awakening','srcDoc'),
#    Output('check-input-value','children'),
    Input('smoke-status-input','value'))
def update_output(smoke_status):
#    return smoke_status
    df_local = df[df['Smoking status'].isin(smoke_status)].copy()
    age_sleepeff_line = alt.Chart(df_local).mark_line().encode(
        x = 'binnedAge',
        y=alt.Y('mean(Sleep efficiency)',scale=alt.Scale(zero=False)),
        color = 'Gender'
    )
    age_sleepdur_bar = alt.Chart(df_local).mark_bar().encode(
        x = alt.X('Gender',title=None),
        y = alt.Y('mean(Sleep duration)',scale=alt.Scale(zero=False),axis=alt.Axis(grid=False)),
        color = alt.Color('Gender',legend=alt.Legend(orient='top')),
        column='binnedAge'
    ).configure_view(
        stroke='transparent'
    )
    awakening_bar = alt.Chart(df_local).mark_bar().encode(
        x = 'count()',
        y = alt.Y('Awakenings:O'),
        color = alt.Color('Gender')
    )
    
    return age_sleepeff_line.to_html(), age_sleepdur_bar.to_html(), awakening_bar.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)
    
    
    