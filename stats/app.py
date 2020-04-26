from flask import Flask, jsonify, request, Response
from data import games
# import data as stats.data

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/data', methods=['GET'])
def show_stats():
    return games

if __name__ == "__main__":
    app.run()
