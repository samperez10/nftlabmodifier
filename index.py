import requests as req,json

from flask import Flask , jsonify ,request, send_file , render_template

  
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    
    return "Wkwkwkw", 404
    
@app.route("/notcakedapes/<id>")
def cakedapes(id):
  
  url = f"https://nervous.mypinata.cloud/ipfs/QmUL1dHBJpbSMi8qXgRNMqRYLJMP2FmMFTFp1vu3vbeBuN/{id}"
  
  js = req.get(url).json()
  
  js["name"] = f"Caked Apes Flip #{id}"
  
  js["image"] = f"https://nftstorage.link/ipfs/bafybeiexnomle7nzrdjgejs4gllgb6tl32nkixmhvofhagzzdx2pp6pr7a/{id}.png"
  
  js["description"] = "Caked Apes Flip are 2222 unique and randomly generated NFTs living in Polygon Blockchain."
  
  return jsonify(js)

@app.route("/flipbokizombie/<id>")
def bokizombie(id):
  
  url = f"https://nervous.mypinata.cloud/ipfs/QmSSHVtFZcadkgpzEA9KSRUEXP1o9c9zUX9xJUw76ey91X/{id}"
  
  js = req.get(url).json()
  
  js["name"] = f"Flip Boki Zombie #{id}"

  js["collection"] = "Flip Boki Zombie"
  
  js["image"] = f"https://nftstorage.link/ipfs/bafybeiecxmtho5k23ognvjclahx7kivaftbaf4ujogsw3euysdvzt54u3q/{id}.png"
  
  return jsonify(js)

@app.route("/yeahtiger/<id>")
def yeahtiger(id):
  
  url = f"https://bafybeia737e3bpzusnxxn36alotv2fwviezjm44e5rx4fnuvmpfgcfh3ha.ipfs.nftstorage.link/{id}.json"
  
  js = req.get(url).json()
  
  js["name"] = f"Yeah Tigers NFT #{id}"

  js["description"].replace('Solana','Polygon')

  js.pop('symbol')
  js.pop('seller_fee_basis_points')
  js.pop('external_url')
  js.pop('properties')
  
  return jsonify(js)

@app.route("/")
def hello_world():
  
  return 'Hello world'


  