# Streamlit on Heroku

This project is intended to help you tie together some important concepts and
technologies from the 12-day course, including Git, Streamlit, JSON, Pandas,
Requests, Heroku, and Bokeh for visualization.

The repository contains a basic template for a Streamlit configuration that will
work on Heroku.

A [finished example](https://streamlit-12day-example.herokuapp.com/) that demonstrates some basic functionality.

SUMMARY OF STEPS: 
1. Design app.py using streamlit - [Streamlit Documentation](https://docs.streamlit.io/en/stable/) is very helpful
2. Need a key for API access for [Alpha Vantage](https://www.alphavantage.co/documentation/#)
3. Need access to [Heroku](www.heroku.com)
4. Fork repo to your Github account. 
5. Clone to local machine using git
6. Write the code - app.py - and set requirements as needed.
7. Create a heroku app - use command <heroku create <appname>>. You may need to login first.
8. For API key, you will need to use config vars so you do not have the key publicly available. Use command <heroku config:set API_Key=<your key>>. 
   In your app, you will need to import os and get the key using command <key = os.environ.get('API_Key')>
9. Commit changes and push to github and to Heroku - use command <git push heroku master>. 
10. If all goes well, you can see your app at < https://appname.herokuapp.com/>

TDI ORIGINAL INSTRUCTIONS:

## Step 1: Setup and deploy
- Git clone the existing template repository.
- `Procfile`, `requirements.txt`, and `setup.py` contain some default settings. If you want, you can change the email address in `setup.py` to your own, but it won't affect anything in the app.

- Create Heroku application with `heroku create <app_name>` or leave blank to
  auto-generate a name.

- Deploy to Heroku: `git push heroku master`
- You should be able to see your site at `https://<app_name>.herokuapp.com`
- A useful reference is the Heroku [quickstart guide](https://devcenter.heroku.com/articles/getting-started-with-python-o).

## Step 2: Get data from API and put it in pandas
- Use the `requests` library to grab some data from a public API. This will
  often be in JSON format, in which case `simplejson` will be useful.
- Build in some interactivity by having the user submit a form which determines which data is requested.
- Create a `pandas` dataframe with the data.

## Step 3: Plot pandas data
- Create an interactive plot from the dataframe. Some recommended libraries: Altair, Bokeh, and Plotly.
- Altair provides a simple interface for creating linked and layered plots. They can even be exported and embedded in static HTML (and remain fully interactive!) See the [documentation](https://altair-viz.github.io/)
  and be sure to check out the example gallery.
- Bokeh can be used in a wide range of applications, from simple charts to extensive dashboards with sophisticated backends. It's the most fully-featured library of these three, but you won't be using it for anything complicated in the Milestone Project. Here you can find the Bokeh [documentation](http://bokeh.pydata.org/en/latest/docs/user_guide/embed.html)
  and some [examples](https://github.com/bokeh/bokeh/tree/master/examples/embed).
- Plotly provides a range of APIs in their library. Plotly express, for instance, can be used to create commonly used plots. The Graph Objects API affords more customization, but is more complicated to use. Here is the [documentation](https://plotly.com/python/plotly-express/#gallery) for Plotly Express.

NOTES: 

Bokeh 2.2.0 needs to be used although the latest release was 2.3.4 at the time of this project. This is due to a known error where the latest version will not display the graph. 
