#https://www.chartjs.org/docs/latest/getting-started/

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        mya=request.form.get('chartN')
        return render_template('index.html', chartN=mya)

    return render_template('index.html', chartN='')


if __name__ =="__main__":
    app.run()
