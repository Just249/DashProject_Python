import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import altair as alt
#from vega_datasets import data
import pandas as pd
import dash_bootstrap_components as dbc


df = pd.read_csv('../data/Sleep_Efficiency.csv')

# Handling NA, Strategy = replaced by mean

df['Alcohol consumption'].fillna(round(df['Alcohol consumption'].mean()),inplace=True)
df['Caffeine consumption'].fillna(round(df['Caffeine consumption'].mean()),inplace=True)
df['Awakenings'].fillna(round(df['Awakenings'].mean()),inplace=True)
df['Exercise frequency'].fillna(round(df['Exercise frequency'].mean()),inplace=True)

# Bin ages into 11 groups, Create new df col binnedAge

age_bins = [0] + [5*i for i in range(3,13)] + [df.Age.max()]
age_bins_labels = ['0-15','15-20','21-25','26-30','31-35','36-40','41-45','46-50','51-55','56-60','60+']
df['binnedAge'] = pd.cut(df['Age'],bins=age_bins,labels=age_bins_labels)


################################

def awakening_bar():
    chart = alt.Chart(df).mark_bar().encode(
        x = 'count()',
        y = alt.Y('Awakenings:O'),
        color = alt.Color('Gender')
    )
    return chart.to_html()

################################

## Define Layout


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = dbc.Container([
    dbc.Tabs([
        
###########################################################################################################################        
##############################################General Information Tab #####################################################
###########################################################################################################################
        
        
        dbc.Tab(label='General Information Tab', children=[
            dbc.Row([
                dbc.Col([
                    html.H2('Sleep Efficiency Dash', style={'backgroundColor':'white'}),
                    html.Br(),
                    html.P("Dataset Source:", style={'marginBottom': 0}),
                    html.A("Sleep Efficiency Dataset by EQUILIBRIUMM",
                           href="https://www.kaggle.com/datasets/equilibriumm/sleep-efficiency",
                           style={'color': 'blue', 'text-decoration': 'underline', 'font-weight': 'bold'}),
                    html.Br(),
                    html.Br(),
                    html.Div(id='check-input-value1'),
                    html.P('Smoke Status', style={"font-weight": "bold"}),
                    dcc.Checklist(
                        id='smoke-status-input',
                        options=['Yes', 'No'],
                        value=['No'],
                        inline=True
                    ),
                    html.Br(),
                    html.P('Alcohol Consumption (Mg)', style={"font-weight": "bold"}),
                    dcc.RangeSlider(
                        id='alcohol-consumption-input',
                        min=0, max=5, step=1, value=[0, 2],
                        marks={i: str(i) for i in range(6)}
                    ),
                    html.Br(),
                    html.P('Caffeine Consumption (Oz)', style={"font-weight": "bold"}),
                    dcc.RangeSlider(
                        id='caffeine-consumption-input',
                        min=0, max=200, step=25, value=[0, 75],
                        marks={i: str(i) for i in range(0, 201, 25)}
                    ),
                    html.Br(),
                    html.P('Execise Frequency (Days/Week)', style={"font-weight": "bold"}),
                    dcc.RangeSlider(
                        id='exercise-frequency-input',
                        min=0, max=5, step=1, value=[0, 2],
                        marks={i: str(i) for i in range(6)}
                    ),
                    html.Br(),
                    html.P("Dataset Source:", style={'marginBottom': 0}),
                    html.A("Sleep Efficiency Dataset by EQUILIBRIUMM",
                           href="https://www.kaggle.com/datasets/equilibriumm/sleep-efficiency",
                           style={'color': 'blue', 'text-decoration': 'underline', 'font-weight': 'bold'}),
                    html.Br(),
                    html.Details([
                        html.Summary('Show Dataset Description', style={"font-weight": "bold"}),
                        html.Br(),
                        html.Div('''The dataset contains information about a group of test subjects and their sleep 
                      patterns. Each test subject is identified by a unique "Subject ID" and their age and gender are 
                      also recorded. The "Bedtime" and "Wakeup time" features indicate when each subject goes to bed and 
                      wakes up each day, and the "Sleep duration" feature records the total amount of time each subject 
                      slept in hours. The "Sleep efficiency" feature is a measure of the proportion of time spent in bed 
                      that is actually spent asleep. The "REM sleep percentage", "Deep sleep percentage", and "Light sleep 
                      percentage" features indicate the amount of time each subject spent in each stage of sleep. The 
                      "Awakenings" feature records the number of times each subject wakes up during the night. Additionally
                      , the dataset includes information about each subject's caffeine and alcohol consumption in the 24 
                      hours prior to bedtime, their smoking status, and their exercise frequency.''')
                    ]),
                ], style={'width': '15%', 'display': 'inline-block'}),
                
            ##################################### Right Column (Tab1) #########################################         
                dbc.Col([
                    # Right Top
                    dbc.Row([
                        # Right Top Left
                        dbc.Col([
                            '',
                            html.Br(),
                            html.Iframe(
                                id='age_sleepeff',
                                style={'height':'400px', 'width':'100%'}
                            )
                        ]), ## , style={'width': '100%', 'display': 'inline-block'}
                        # Right Top Right
                        dbc.Col([
                            '',
                            html.Br(),
                            html.Iframe(
                                id='age_sleepdur',
                                style={'height':'400px', 'width':'100%'}
                            )
                        ]) ## , style={'width': '40%', 'display': 'inline-block'}
                    ]),
                    # Right Bottom
                    dbc.Row([
                        dbc.Col([
                            '',
                            html.Iframe(
                                id='awakening',
                                srcDoc=awakening_bar(),
                                style={'width': '100%', 'height':'250px', 'display': 'inline-block'}
                            )
                        ])
                    ])
                ], width=9) ## , style={'width': '85%', 'float': 'right', 'display': 'inline-block'}
            ])
        ]),
        
        
        
###########################################################################################################################
########################################################## Filterable Tab #################################################
###########################################################################################################################
        
    
        dbc.Tab(label='Filterable Tab', children=[
            dbc.Row([
                dbc.Col([
                    html.H2('Sleep Efficiency Dash', style={'backgroundColor':'white'}),
                    html.Br(),
                    html.Br(),
                    html.Div(id='check-input-value2'),
                    html.P('Smoke Status', style={"font-weight": "bold"}),
                    dcc.Checklist(
                        id='smoke-status-input2',
                        options=['Yes', 'No'],
                        value=['No'],
                        inline=True
                    ),
                    html.Br(),
                    html.P('Alcohol Consumption (Mg)', style={"font-weight": "bold"}),
                    dcc.RangeSlider(
                        id='alcohol-consumption-inputt2',
                        min=0, max=5, step=1, value=[0, 2],
                        marks={i: str(i) for i in range(6)}
                    ),
                    html.Br(),
                    html.P('Caffeine Consumption (Oz)', style={"font-weight": "bold"}),
                    dcc.RangeSlider(
                        id='caffeine-consumption-inputt2',
                        min=0, max=200, step=25, value=[0, 75],
                        marks={i: str(i) for i in range(0, 201, 25)}
                    ),
                    html.Br(),
                    html.P('Execise Frequency (Days/Week)', style={"font-weight": "bold"}),
                    dcc.RangeSlider(
                        id='exercise-frequency-inputt2',
                        min=0, max=5, step=1, value=[0, 2],
                        marks={i: str(i) for i in range(6)}
                    ),
                    html.Br(),
                    html.P("Dataset Source:", style={'marginBottom': 0}),
                    html.A("Sleep Efficiency Dataset by EQUILIBRIUMM",
                           href="https://www.kaggle.com/datasets/equilibriumm/sleep-efficiency",
                           style={'color': 'blue', 'text-decoration': 'underline', 'font-weight': 'bold'}),
                    html.Br(),
                    html.Details([
                        html.Summary('Show Dataset Description', style={"font-weight": "bold"}),
                        html.Br(),
                        html.Div('''The dataset contains information about a group of test subjects and their sleep 
                      patterns. Each test subject is identified by a unique "Subject ID" and their age and gender are 
                      also recorded. The "Bedtime" and "Wakeup time" features indicate when each subject goes to bed and 
                      wakes up each day, and the "Sleep duration" feature records the total amount of time each subject 
                      slept in hours. The "Sleep efficiency" feature is a measure of the proportion of time spent in bed 
                      that is actually spent asleep. The "REM sleep percentage", "Deep sleep percentage", and "Light sleep 
                      percentage" features indicate the amount of time each subject spent in each stage of sleep. The 
                      "Awakenings" feature records the number of times each subject wakes up during the night. Additionally
                      , the dataset includes information about each subject's caffeine and alcohol consumption in the 24 
                      hours prior to bedtime, their smoking status, and their exercise frequency.''')
                    ]),
                ], style={'width': '25%', 'display': 'inline-block'}),
                
            ##################################### Right Column (Tab2) #########################################
                
                                dbc.Col([
                    # Right Top
                    dbc.Row([
                        dbc.Col([
                            html.Br(),
                            html.Iframe(
                                id='rs_count',
                                style={'height':'220px', 'width':'100%'}
                            )
                        ], width=12)
                    ], className='my-2'),

                    # Mid Section
                    dbc.Row([
                        dbc.Col([
                            html.Br(),
                            html.Iframe(
                                id='ds_count',
                                style={'height':'220px', 'width':'100%'}
                            )
                        ], width=12)
                    ]),

                    # Bottom Section
                    dbc.Row([
                        dbc.Col([
                            html.Iframe(
                                id='ls_count',
                                style={'height': '220px', 'width': '100%'}
                            )
                        ])
                    ])
                ], width=9)
                
            ])
        ])
    ])
])

# Ref: https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Dash%20Components/Checklist/checkbox.py

@app.callback(
    Output('age_sleepeff','srcDoc'),
    Output('age_sleepdur','srcDoc'),
    Output('awakening','srcDoc'),
    Output('rs_count','srcDoc'),
    Output('ds_count','srcDoc'),
    Output('ls_count','srcDoc'),
    Input('smoke-status-input','value'),
    Input('alcohol-consumption-input','value'),
    Input('caffeine-consumption-input','value'),
    Input('exercise-frequency-input','value'),
    Input('smoke-status-input2','value'),
    Input('alcohol-consumption-inputt2','value'),
    Input('caffeine-consumption-inputt2','value'),
    Input('exercise-frequency-inputt2','value')
    )


def update_output(smoke_status,alcohol_consumption,caffeine_consumption,exercise_frequency,smoke_status2,alcohol_consumption2,caffeine_consumption2,exercise_frequency2):
    df_local = df[df['Smoking status'].isin(smoke_status)].copy()
    df_local = df_local[df_local['Alcohol consumption'].between(alcohol_consumption[0],alcohol_consumption[1])]
    df_local = df_local[df_local['Caffeine consumption'].between(caffeine_consumption[0],caffeine_consumption[1])]
    df_local = df_local[df_local['Exercise frequency'].between(exercise_frequency[0],exercise_frequency[1])]
    df_local2 = df[df['Smoking status'].isin(smoke_status2)].copy()
    df_local2 = df_local2[df_local2['Alcohol consumption'].between(alcohol_consumption2[0],alcohol_consumption2[1])]
    df_local2 = df_local2[df_local2['Caffeine consumption'].between(caffeine_consumption2[0],caffeine_consumption2[1])]
    df_local2 = df_local2[df_local2['Exercise frequency'].between(exercise_frequency2[0],exercise_frequency2[1])]
    
    domain = ['Male', 'Female']
    range_ = ['#3493bf', '#c74448']
    
    
############################################## General Information Tab #####################################################
    
    
    # Sleep efficiency
    
    age_sleepeff_point = alt.Chart(df_local, title = alt.TitleParams(text = ["Sleep efficiency % by Age Group"], fontSize=20, anchor = "middle")).mark_point().encode(
    x = alt.X('binnedAge', title = "Age Groups", axis=alt.Axis(labelFontSize=12, titleFontSize=14)),
    y = alt.Y('mean(Sleep efficiency)',title = "Mean Sleep Efficiency (%)", scale=alt.Scale(zero=False), 
              axis=alt.Axis(labelFontSize=12, titleFontSize=14)),
    color = alt.Color('Gender', scale=alt.Scale(domain=domain, range=range_), legend=alt.Legend(orient='bottom-right')),
    tooltip=['binnedAge', 'mean(Sleep efficiency)', 'binnedAge']
    ).properties(height=260, width=350)

    age_sleepeff_line2 = age_sleepeff_point + age_sleepeff_point.mark_line()
        
    # Sleep duration
    
    age_sleepdur_bar = alt.Chart(df_local, title = alt.TitleParams(text = ["Mean Sleep Duration by Age Group"], fontSize=20,
    anchor = "middle")).mark_bar().encode(
    x = alt.X('Gender',title=None, axis=alt.Axis(grid=False, ticks=False,labels=False)),
    y = alt.Y('mean(Sleep duration)', title = "Mean Sleep Duration (hours)",scale=alt.Scale(zero=False),
              axis=alt.Axis(grid=False, labelFontSize=12, titleFontSize=14)),
    color = alt.Color('Gender',legend=alt.Legend(orient='bottom'),scale=alt.Scale(domain=domain, range=range_)),
    column='binnedAge',
    tooltip=['mean(Sleep duration)', 'Gender', 'binnedAge']
    ).properties(height=220, width=13).configure_view(stroke='transparent')
    
    # Awakening
    
    awakening_bar = alt.Chart(df_local, title = alt.TitleParams(text = ["Count of Awakenings"], fontSize=20,
    anchor = "middle")).mark_bar().encode(
    x = alt.X('count()', title = None, axis=alt.Axis(labelFontSize=12, titleFontSize=14)),
    y = alt.Y('Awakenings:O', title = "Number of Awakenings", axis=alt.Axis(labelFontSize=12, titleFontSize=14)),
    color = alt.Color('Gender',legend=alt.Legend(orient='bottom-right'),scale=alt.Scale(domain=domain, range=range_)),
    tooltip=['Awakenings', 'count()']
    ).properties(height=150, width=870)
    
    
    
########################################################## Filterable Tab #################################################
    
    
    
    # REM sleep %
    
    rs_bar = alt.Chart(df_local2, title = alt.TitleParams(text = ["Count of records", ""], fontSize=20,
    anchor = "middle")).mark_bar().encode(
    x = alt.X('count()', axis=alt.Axis(labelFontSize=12, titleFontSize=14), title=None),
    y = alt.Y('binned_REM:O', title = "REM Sleep %", axis=alt.Axis(labelFontSize=12, titleFontSize=14)),
    color = alt.Color('Gender',legend=alt.Legend(orient='top-right'),scale=alt.Scale(domain=domain, range=range_)),
    tooltip=['Gender', 'binned_REM:O', 'count()']
    ).transform_bin('binned_REM',field='REM sleep percentage').properties(height=100, width=850)
    
    # Deep sleep %
    
    ds_bar = alt.Chart(df_local2).mark_bar().encode(
    x = alt.X('count()', axis=alt.Axis(labelFontSize=12, titleFontSize=14), title=None),
    y = alt.Y('binned_DS:O', title = "Deep Sleep %", axis=alt.Axis(labelFontSize=12, titleFontSize=14)),
    color = alt.Color('Gender',legend=None,scale=alt.Scale(domain=domain, range=range_)),
    tooltip=['Gender', 'binned_DS:O', 'count()']   
    ).properties(height=100, width=870).transform_bin('binned_DS',field='Deep sleep percentage')
    
    # Light sleep %
    
    ls_bar = alt.Chart(df_local2).mark_bar().encode(
    x = alt.X('count()', axis=alt.Axis(labelFontSize=12, titleFontSize=14), title=None), 
    y = alt.Y('binned_LS:O', title = "Light Sleep %", axis=alt.Axis(labelFontSize=12, titleFontSize=14)),
    color = alt.Color('Gender',legend=None,scale=alt.Scale(domain=domain, range=range_)),
    tooltip=['Gender', 'binned_DS:O', 'count()']   
    ).properties(height=100, width=870).transform_bin('binned_LS',field='Light sleep percentage')
    
    
    return age_sleepeff_line2.to_html(), age_sleepdur_bar.to_html(), awakening_bar.to_html(), rs_bar.to_html(), ds_bar.to_html(), ls_bar.to_html()

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)  