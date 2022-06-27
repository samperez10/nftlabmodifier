import requests as req,inspect,json
import re,time, os

from PIL import Image, ImageOps
from io import BytesIO

from flask import Flask , jsonify ,request, send_file

  
app = Flask(__name__)
    
@app.route("/metadata/<id>")
def metadata(id):
  
  url = f"https://nervous.mypinata.cloud/ipfs/QmUL1dHBJpbSMi8qXgRNMqRYLJMP2FmMFTFp1vu3vbeBuN/{id}"
  
  js = req.get(url).json()
  
  js["name"] = f"Caked Apes Flip #{id}"
  
  js["image"] = f"https://nftstorage.link/ipfs/bafybeiexnomle7nzrdjgejs4gllgb6tl32nkixmhvofhagzzdx2pp6pr7a/{id}.png"
  
  js["description"] = "Caked Apes Flip are 2222 unique and randomly generated NFTs living in Polygon Blockchain."
  
  return jsonify(js)
  
if __name__ == '__main__':
  
  app.run(host='0.0.0.0', port=5000)
  
  