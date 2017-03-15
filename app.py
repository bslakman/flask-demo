from stockticker import plot
from flask import Flask, render_template, request, redirect
from io import BytesIO
from bokeh.embed import components

app = Flask(__name__)

app.vars = {}

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('stock_info.html')
    else:
        app.vars['ticker'] = request.form['ticker_symbol']
        return redirect('/result')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        graph = plot(app.vars['ticker'])
        script, div = components(graph)
        return render_template('stock_result.html', script=script, div=div)
    else:
        return redirect('/')
###################################################################################

if __name__ == '__main__':
  app.run(port=33507)
