from flask import Flask, request, make_response, render_template, jsonify
from linkedlist import Linkedlist

app = Flask(__name__)

# create a data bucket
dataBucket = [None] * 10
link = []
for i in range(0,10):
    link.insert(i,'link'+str(i))


@app.route('/',methods=['GET','POST'])
def addbook():
    if request.method == "GET":
        return render_template('index.html')

    elif request.method == "POST":

        key = request.form.get('key','book')
        author = request.form.get('author',None)
        description = request.form.get('desc',None)
        price = request.form.get('price',0)

        # get the hash value
        hash_value = hashFunction(key)

        # once you get the hash value you can store the value in the data bucket

        checkspace = dataBucket[hash_value]

        if checkspace is None:
            link[hash_value] =  Linkedlist()
            dataBucket[hash_value] = link[hash_value]

            link[hash_value].insertData(author,description,price)


        else:
            exist_link = checkspace
            # find the last node (no need to travers, just call the insertData() method)
            temp = checkspace.head
            while temp is not None:
                temp = temp.next

            exist_link.insertData(author,description,price)



    return 'done'

def hashFunction(key):

    # the key is a string
    hashValue = 0
    for i in key:

        hashValue = hashValue + ord(i)

    hashValue = hashValue % 10
    return hashValue


# search result
@app.route('/search',methods=['GET','POST'])
def search():

    if request.method == 'GET':

        return render_template('search.html')

    elif request.method == 'POST':

        # get the search data
        search_query = request.form.get('search')

        hash_value = hashFunction(search_query)

        # find the data
        checkdata = dataBucket[hash_value]
        if checkdata is None:
            return jsonify({'msg':'no'})

        else:
            json_resp = []

            temp = checkdata
            json_resp.append(temp.findData())

            return jsonify({'msg':json_resp})




if __name__ == "__main__":
    app.run(debug=True)
