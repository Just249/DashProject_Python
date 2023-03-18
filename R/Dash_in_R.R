library(dash)
library(dashHtmlComponents)

app = Dash$new(external_stylesheets = "https://codepen.io/chriddyp/pen/bWLwgP.css")

app$layout(
  htmlDiv(
    htmlH1('I am alive!!',
           style=list('color' = 'cyan', 'background-color' = '#000000')
    )
  )
)

app$run_server(debug = T)
