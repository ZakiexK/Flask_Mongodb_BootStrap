from flask import Flask , jsonify, request, redirect
from flask.helpers import url_for
from flask_pymongo import PyMongo
from flask_cors import CORS , cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/FavInfo'
app.config['CORS_Headers'] = 'Content-Type'

mongo = PyMongo(app)

@app.route('/', methods = ['GET'])
def retrieveAllData():
    currentCollection = mongo.db.FavInfo
    holder = list()
    for i in currentCollection.find():
        holder.append({"game" : i['favGame'], "genre" : i["favGenre"], "name" : i['name']})
    return(jsonify(holder))

@app.route('/<name>', methods = ['GET'])
@cross_origin()
def retrieveFromName(name):
    currentCollection = mongo.db.FavInfo 
    data = currentCollection.find_one({"name" : name})
    return(jsonify({'name' : data['name'] , 'genre' : data['favGenre'], 'game' : data['favGame']}))

@app.route('/postData', methods = ['POST'])
def postData():
    currentCollection = mongo.db.FavInfo
    name = request.json['name']
    genre = request.json['favGenre']
    game = request.json['favGame']
    currentCollection.insert_one({'name' : name, 'favGenre' : genre, 'favGame': game})
    return(jsonify({'name' : name, 'genre' : genre, 'game': game}))

@app.route('/deleteData/<name>', methods = ["DELETE"])
def deleteData(name):
    currentCollection = mongo.db.FavInfo
    currentCollection.delete_one({"name" : name})
    return (redirect(url_for('retrieveAllData')))

@app.route('/update/<name>', methods = ['PUT'])
def updateDate(name):
    currentCollection = mongo.db.FavInfo
    Updatedname = request.json['name']
    currentCollection.update_one({'name' : name}, {"$set" ,{'name' : Updatedname}})
    return redirect(url_for('retrieveAllData'))




if __name__ == "__main__":
    app.run(debug=True)