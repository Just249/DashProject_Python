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

def age_sleepeff_line():
    chart = alt.Chart(df).mark_line().encode(
        x = 'binnedAge',
        y=alt.Y('mean(Sleep efficiency)',scale=alt.Scale(zero=False)),
        color = 'Gender'
    )
    return chart.to_html()

def age_sleepdur_bar():
    chart = alt.Chart(df).mark_bar().encode(
        x = alt.X('Gender',title=None),
        y = alt.Y('mean(Sleep duration)',scale=alt.Scale(zero=False),axis=alt.Axis(grid=False)),
        color = alt.Color('Gender',legend=alt.Legend(orient='top')),
        column='binnedAge'
    ).configure_view(
        stroke='transparent'
    )
    return chart.to_html()

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
             html.P('Input controls here...')],
            style={'width': '20%', 'display': 'inline-block'}),
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
                    srcDoc=age_sleepeff_line(),
                    style={'height':'500px','width':'400px'}
                )],style={'width': '38%', 'display': 'inline-block'}
            ),
            
            # Right Top Right
            html.Div([
                'Right Top Right Section',
                html.Iframe(
                    id = 'age_sleepdur',
                    srcDoc=age_sleepdur_bar(),
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
    

if __name__ == '__main__':
    app.run_server(debug=True)
    
    
    