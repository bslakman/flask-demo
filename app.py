from stockticker import plot
from flask import Flask, render_template, request, redirect

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
        app.vars['list_of_metrics'] = []
        if request.form['open']:
            app.vars['list_of_metrics'].append('open')
        if request.form['close']:
            app.vars['list_of_metrics'].append('close')
        if request.form['high']:
            app.vars['list_of_metrics'].append('high')

        return redirect('/result')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        return render_template('stock_result.html')
    else:
        return redirect('/')

@app.route('/fig/') 
def fig(): 
    fig = plot(app.vars['ticker'], app.vars['list_of_metrics']) 
    img = BytesIO() 
    fig.savefig(img) 
    img.seek(0) 
    return send_file(img, mimetype='image/png') 

###################################################################################

if __name__ == '__main__':
  app.run(port=33507)
