from flask import Flask, render_template,request
from web import Web

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    # 'user_query' matches the 'name' attribute in your HTML input
    query = request.form.get('user_query')
    web = Web()

    return render_template('search.html', query=query, web=web.search_from_arrays(query))

if __name__ == "__main__":
    app.run()