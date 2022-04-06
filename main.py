import pandas as pd
from flask import *
from flipkart import kart_item
from amazon import azon
app = Flask(__name__)


@app.route("/" ,methods=["GET","POST"])
def index():
    df1 = ""
    df2 = ""
    if request.method == "POST":
        search = request.form["search_item"]
        df1 = kart_item(search)
        df2 = azon(search)
    return render_template("index.html",tables1=[df1.to_html(classes="data", justify="center")],tables2=[df2.to_html(classes="data",  justify="center")], titles1=df1.columns.values, titles2=df2.columns.values)

if __name__ == "__main__":
    app.run(debug=True)


