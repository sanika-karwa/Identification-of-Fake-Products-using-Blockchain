import datetime
import json

import requests
from flask import render_template, redirect, request

from app import app

# The node with which our application interacts, there can be multiple
# such nodes as well.
CONNECTED_NODE_ADDRESS = "http://127.0.0.1:8000"

posts = []


def fetch_posts():
    """
    Function to fetch the chain from a blockchain node, parse the
    data and store it locally.
    """
    get_chain_address = "{}/chain".format(CONNECTED_NODE_ADDRESS)
    response = requests.get(get_chain_address)
    if response.status_code == 200:
        content = []
        chain = json.loads(response.content)
        for block in chain["chain"]:
            for tx in block["transactions"]:
                tx["index"] = block["index"]
                tx["hash"] = block["previous_hash"]
                content.append(tx)

        global posts
        posts = sorted(content, key=lambda k: k['timestamp'],
                       reverse=True)


@app.route('/')
def index():
    fetch_posts()
    return render_template('index.html',
                          # title='FAKE PRODUCT IDENTIFICATION! '
                           #      'IT\'S FAKE.IT\'S SAFE',
                           posts=posts,
                           node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string)


@app.route('/submit', methods=['POST'])
def submit_textarea():
    """
    Endpoint to create a new transaction via our application.
    """
    name = request.form["prodname"]
    pid = request.form["prodid"]
    mid = request.form["modelid"]
    v = request.form["vendor"]
    d = str(request.form["dateman"])

    post_object = {
        'prodname': name,
        'prodid': pid,
        'modelid':mid,
        'vendor':v,
        'dateman':d,
    }

    # Submit a transaction
    new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

    requests.post(new_tx_address,
                  json=post_object,
                  headers={'Content-type': 'application/json'})

    return redirect('/')


def timestamp_to_string(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%H:%M')

@app.route('/search/<hash>',methods=['GET','POST'])
def search(hash):
    found=0
    hash=str(hash)
    #query = request.form["search"]
    get_chain_address = "{}/chain".format(CONNECTED_NODE_ADDRESS)
    response = requests.get(get_chain_address)
    if response.status_code == 200:
        content = []
        chain = json.loads(response.content)
        for block in chain["chain"]:
            if hash== block["hash"]:
                found=1
                if found:
                    for tx in block["transactions"]:
                        posts={'Product Name':tx["prodname"],'Product ID':tx["prodid"],'Model ID':tx["modelid"],'Seller':tx["vendor"],'Date':tx["dateman"]}
                       # print('found', tx["prodname"],tx["prodid"],tx["modelid"],tx["vendor"],tx["dateman"],flush=True)
                        #post1=['Product Name','Product ID','Model ID','Seller','Vendor ','Date']
                        return render_template('found.html',node_address=CONNECTED_NODE_ADDRESS,readable_time=timestamp_to_string,posts=posts)
                        
                        

        if not found:
           # print('not found',flush=True)
           return render_template('notfound.html',node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string)
            
    return redirect('/')

#def mine(hash):
 #   return render_template('mine.html', node_address=CONNECTED_NODE_ADDRESS,
  #                         readable_time=timestamp_to_string,post1=post1)