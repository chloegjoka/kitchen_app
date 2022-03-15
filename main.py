from flask import Flask, render_template, request
from recipe_scrapers import scrape_me

app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])

def signup():
    if request.method == 'POST':
        try:
            url = request.form['url']
            scraper = scrape_me(url, wild_mode=True)
        except:
            return render_template("index.html", title="URL was invalid. Try again?")
        title = scraper.title()
        total_time = scraper.total_time()
        yields = scraper.yields()
        ingred = scraper.ingredients()
        instr = scraper.instructions()
        return render_template("index.html", title=title, total_time=total_time, yields=yields, ingred=ingred, instr=instr)
    elif request.method == 'GET':
        return render_template("index.html", title="empty")

if __name__ == "__main__":
    app.run()