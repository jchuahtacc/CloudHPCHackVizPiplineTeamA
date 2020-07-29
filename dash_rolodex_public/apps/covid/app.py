import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
# included states and us areas along with fips code
statetofips= {
   "Alabama"                :  "01",
   "Alaska"                 :  "02",
   "Arizona"                :  "04",
   "Arkansas"               :  "05",
   "California"             :  "06",
   "Colorado"               :  "08",
   "Connecticut"            :  "09",
   "Delaware"               :  "10",
   "District of Columbia"   :  "11",
   "Florida"                :  "12",
   "Georgia"                 :  "13",
   "Hawaii"                 :  "15",
   "Idaho"                  :  "16",
   "Illinois"               :  "17",
   "Indiana"                :  "18",
   "Iowa"                   :  "19",
   "Kansas"                 :  "20",
   "Kentucky"               :  "21",
   "Louisiana"              :  "22",
   "Maine"                  :  "23",
   "Maryland"               :  "24",
   "Massachusetts"          :  "25",
   "Michigan"               :  "26",
   "Minnesota"              :  "27",
   "Mississippi"            :  "28",
   "Missouri"               :  "29",
   "Montana"                :  "30",
   "Nebraska"               :  "31",
   "Nevada"                 :  "32",
   "New Hampshire"          :  "33",
   "New Jersey"             :  "34",
   "New Mexico"             :  "35",
   "New York"               :  "36",
   "North Carolina"         :  "37",
   "North Dakota"           :  "38",
   "Ohio"                   :  "39",
   "Oklahoma"               :  "40",
   "Oregon"                 :  "41",
   "Pennsylvania"           :  "42",
   "Rhode Island"           :  "44",
   "South Carolina"         :  "45",
   "South Dakota"           :  "46",
   "Tennessee"              :  "47",
   "Texas"                  :  "48",
   "Utah"                   :  "49",
   "Vermont"                :  "50",
   "Virginia"               :  "51",
   "Washington"             :  "53",
   "West Virginia"          :  "54",
   "Wisconsin"              :  "55",
   "Wyoming"                :  "56",
    "Puerto Rico"           :   "72",
    "Virgin Islands"        :   "78",
    "American Samoa"		:   "60",
    "Guam"  	            :   "66",
    "Northern Mariana Islands"	:	"69"

}
#fips code
fipstocode= { '66' : "GU", '60' : "AS", '78' : "VI", '69': "MP", '72': "PR", '01': 'AL', '02': 'AK', '04': 'AZ', '05': 'AR', '06': 'CA', '08': 'CO', '09': 'CT', '10': 'DE', '11': 'DC', '12': 'FL', '13': 'GA', '15': 'HI', '16': 'ID', '17': 'IL', '18': 'IN', '19': 'IA', '20': 'KS', '21': 'KY', '22': 'LA', '23': 'ME', '24': 'MD', '25': 'MA', '26': 'MI', '27': 'MN', '28': 'MS', '29': 'MO', '30': 'MT', '31': 'NE', '32': 'NV', '33': 'NH', '34': 'NJ', '35': 'NM', '36': 'NY', '37': 'NC', '38': 'ND', '39': 'OH', '40': 'OK', '41': 'OR', '42': 'PA', '44': 'RI', '45': 'SC', '46': 'SD', '47': 'TN', '48': 'TX', '49': 'UT', '50': 'VT', '51': 'VA', '53': 'WA', '54': 'WV', '55': 'WI', '56': 'WY' }


# -----------------------------------------
# Import and clean data (importing csv into pandas)
df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")


df.reset_index(inplace=True)
df['code'] = df.apply(lambda row: fipstocode[statetofips[row['state']]], axis=1)
# df = df[df["date"] == "2020-07-27"]

dates = pd.DataFrame(data = df['date'].unique())
dates.columns = ['dates']

slider = dcc.Slider(
    id='my-slider',
    min=0,
    max=len(dates),
)
# ---Pearc20
# App layout
app.layout = html.Div([

    html.H1("Pearc20", style={'text-align': 'center'}),


    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={}),
    slider
])


# ------------------------------------------------------------------------------
#
@app.callback(
    dash.dependencies.Output('my_bee_map', 'figure'),
    [dash.dependencies.Input('my-slider', 'value')])
# Connect the Plotly graphs with Dash Components
def update_graph(value):
#If value is none select the first date
    if value == None:
        value = 0

# find the date string by index
    date = dates['dates'].iloc[value]

# Filter the data for that date
    filtered = df[df["date"] == date]

# Generate a new map using the filtered data
    fig = px.choropleth(
        data_frame=filtered,
        locationmode='USA-states',
        locations='code',
        scope="usa",
        color='cases',
        range_color=(0, 200000),

        color_continuous_scale=px.colors.sequential.YlOrRd,
        template='plotly_dark'
    )

    return fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
