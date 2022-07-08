import requests as req,json

from flask import Flask , jsonify ,request, send_file , render_template

  
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    
    return "Wkwkwkw", 404
    
@app.route("/flipcakedapes/<id>")
def cakedapes(id):
  
  url = f"https://nervous.mypinata.cloud/ipfs/QmUL1dHBJpbSMi8qXgRNMqRYLJMP2FmMFTFp1vu3vbeBuN/{id}"
  
  js = req.get(url).json()
  
  js["name"] = f"Flip Caked Apes #{id}"
  
  js["image"] = f"https://nftstorage.link/ipfs/bafybeiexnomle7nzrdjgejs4gllgb6tl32nkixmhvofhagzzdx2pp6pr7a/{id}.png"
  
  js["description"] = "Flip Caked Apes are 2222 unique and randomly generated NFTs living in Polygon Blockchain."
  
  return jsonify(js)

@app.route("/flipbokizombie/<id>")
def bokizombie(id):
  
  url = f"https://nervous.mypinata.cloud/ipfs/QmSSHVtFZcadkgpzEA9KSRUEXP1o9c9zUX9xJUw76ey91X/{id}"
  
  js = req.get(url).json()
  
  js["name"] = f"Flip Boki Zombie #{id}"

  js["collection"] = "Flip Boki Zombie"
  
  js["image"] = f"https://bafybeiecxmtho5k23ognvjclahx7kivaftbaf4ujogsw3euysdvzt54u3q.ipfs.nftstorage.link/{id}.png"
  
  return jsonify(js)

@app.route("/yeahtiger/<id>")
def yeahtiger(id):
  
  url = f"https://bafybeia737e3bpzusnxxn36alotv2fwviezjm44e5rx4fnuvmpfgcfh3ha.ipfs.nftstorage.link/{id}.json"
  
  js = req.get(url).json()

  js["description"] = js["description"].replace('Solana','Polygon')

  js.pop('symbol')
  js.pop('seller_fee_basis_points')
  js.pop('external_url')
  js.pop('properties')
  
  return jsonify(js)

@app.route("/hellopantha/<id>")
def hellopantha(id):
  
  url = f"https://bafybeid7mz2iel2gr2g56dpkng2djx7fy2j5t4sbkpdzvc4gmgnli6k2mq.ipfs.nftstorage.link/{id}.json"
  
  js = req.get(url).json()

  js.pop('symbol')
  js.pop('seller_fee_basis_points')
  js.pop('properties')
  
  return jsonify(js)

@app.route("/justape/<id>")
def justape(id):
  
  url = f"https://bafybeiakbrndp6sdfxghx3xrixplhrw5jpkga2ua527gtn46dripqnsqo4.ipfs.nftstorage.link/{id}.json"
  
  js = req.get(url).json()

  js.pop('symbol')
  js.pop('seller_fee_basis_points')
  js.pop('properties')
  
  return jsonify(js)

@app.route("/reindeer/<id>")
def reindeer(id):
  
  url = f"https://testlaunchmynft.mypinata.cloud/ipfs/QmVejm66qwcoQnwSETJGNvc7FaByd5ZLR7tbbJCJhzcnCg/{int(id)-1}.json"
  
  js = req.get(url).json()

  js.pop('symbol')
  js.pop('seller_fee_basis_points')
  js.pop('properties')
  
  return jsonify(js)

@app.route("/warlocks/<id>")
def warlocks(id):
  
  url = f"https://testlaunchmynft.mypinata.cloud/ipfs/QmXz2XMvAwwL8aRuQqifrpW6FB6XHBXKYKJw57qEd7KxzD/{int(id)-1}.json"
  
  js = req.get(url).json()

  js.pop('symbol')
  js.pop('seller_fee_basis_points')
  js.pop('properties')
  js["description"] = js["description"].replace('solana','polygon')
  
  return jsonify(js)

@app.route("/trippiest/<id>")
def trippiest(id):
  
  url = f"https://nervous.mypinata.cloud/ipfs/QmdrrF9RUBRitrwWV2apRZ9RVcrFQ7amcEBRSPrCG1RM2f/{id}"
  
  js = req.get(url).json()
  
  js["description"] = "The Trippiest Ape Tribe Flip Trippin On The Polygon Blockchain."

  js["image"] = f"https://bafybeihlql46abes4k2myshgtd7v4yfyxg5v42bfcul7gu2vgkrxqwp3ay.ipfs.nftstorage.link/{id}.png"

  js["name"] = f"Trippiest Ape Tribe #{id}"
  
  return jsonify(js)

@app.route("/moonturtlez/<id>")
def moonturtle(id):
  
  url = f"https://moonturtlez.xyz/api/metadata/{id}"
  
  js = req.get(url).json()
  
  js["description"] = "Moonturtlez is a community driven collection of 8,888 randomly generated NFTs on the Polygon blockchain."
  
  return jsonify(js)

@app.route("/moonpepe/<id>")
def moonpepe(id):
  
  url = f"https://ipfs.io/ipfs/QmbhbALyqYkiP5JevHPcYEV8Q9feU1iLJhTsadPoYjKYcM/{id}.json"
  
  js = req.get(url).json()
  
  js["description"] = "MoonPepes is an animated glitch collection on the Polygon blockchain, Pepe inspired and with traits from all your favorite collections. No roadmap, just memes."
  
  return jsonify(js)

@app.route("/japanape/<id>")
def japanape(id):
  
  url = f"https://nervous.mypinata.cloud/ipfs/QmTuNrKE6n6BYnasmPR9NsMbAkuTDpRne2nFcPXk5fWKde/{int(id)-1}"
  
  js = req.get(url).json()

  js['image'] = f'https://nftstorage.link/ipfs/bafybeicztatu7luqklcggvhas2h2tg3epgoyaij46qtactkinzbpn2mj74/{int(id)-1}.png'
  js['name'] = f"Not Japanese Born Ape #{id}"
  return jsonify(js)

@app.route("/lunaticape/<id>")
def lunaticape(id):
  
  url = f"https://bafybeia3d64k2wchcm5lsvvjhoifnq4telp6mge6yp3rml32rqpfdgaiiy.ipfs.nftstorage.link/{id}.json"
  
  js = req.get(url).json()

  js.pop('seller_fee_basis_points')
  js.pop('fee_recipient')

  return jsonify(js)

@app.route("/wzrds/<id>")
def wzrds(id):
  
  url = f"https://wzrds.xyz/metadata/{id}"
  
  js = req.get(url).json()

  return jsonify(js)

@app.route("/fcheebs/<id>")
def fcheebs(id):
  
  url = f"https://nervous.mypinata.cloud/ipfs/QmcnydfBmiaQxFB7CkUB8DHS2jX6WYEyqG3SjRnCdvGjJV/{id}.json"
    
  js = req.get(url).json()

  js['image'] = f"https://bafybeih3mzql5kp6qwbgwbhvvf3ocwln2n4e7vposket4te7mlcmgkg36m.ipfs.nftstorage.link/{id}.png"
  
  js['name'] = f"Flip Cheebs #{id}"
  
  js['description'] = "Flip Cheebs is a collection of 10,000 Friends looking to build a world we can vibe in."

  return jsonify(js)

@app.route("/bunnybats/<id>")
def bunnybats(id):
  
  url = f"https://nftstorage.link/ipfs/bafybeifjf3jpjqc2krfehhmkh2bf47jokmradluvonccjnvqnsxapofdke/{id}.json"
    
  js = req.get(url).json()

  return jsonify(js)



@app.route("/mechaboki/<id>")
def mechaboki(id):
  
  url = f"https://nervous.mypinata.cloud/ipfs/QmcKogBDzNpzQAF3VnaxWXBx6hJP2Cc7mieUD9Q4m1gWgg/{id}.json"
    
  js = req.get(url).json()

  return jsonify(js)

@app.route("/boki/<id>")
def boki(id):
  
  url = f"https://boki.mypinata.cloud/ipfs/QmNTzpH5qLmUV8fDqaWKESFcV4CEKvUstAi7EtrAakF2Tx/{id}"
    
  js = req.get(url).json()

  return jsonify(js)

@app.route("/mutantgoat/<id>")
def mutantgoat(id):
  
  url = f"https://bafybeiem2hc6stktvfsmikvcffimx6oe5siiotecad4rt46b53fl734oim.ipfs.nftstorage.link/{id}.json"
      
  js = req.get(url).json()

  js['name'] = f"Mutant Goat #{id}"

  return jsonify(js)

@app.route("/brokeape/<id>")
def brokeape(id):
  
  url = f"https://bafybeid44c2fcedwxiwsypul2o3ne35h2zncbxhryvqnz6ggw2qbi2vd3u.ipfs.nftstorage.link/{id}.json"
      
  js = req.get(url).json()

  js['name'] = f"Broke Ape #{id}"

  return jsonify(js)

@app.route("/flipbros/<id>")
def flipbros(id):
  
  url = f"https://nervous.mypinata.cloud/ipfs/QmTGB7nUqK6i7gMcULaJHbwDjZyqohgZ2TujRwBMusbw3T/{id}.json"
      
  js = req.get(url).json()

  js['name'] = f"Flip Small Bro #{id}"

  js['image'] = f"https://bafybeifimvcfjmny5f4scnnp4hhbx7gxa7eddml3pmlnphrsahbs6mvrzy.ipfs.nftstorage.link/{id}.png"

  js['description'] = "8888 Flip Small Bros that are here to remind you you're never alone in this journey !"

  return jsonify(js)

@app.route("/flippluto/<id>")
def flippluto(id):
  
  url = f"https://bafybeif6o7frey32hivrcact22cazwshls76uklzvzprvbo2u3pkgxpdbe.ipfs.nftstorage.link/{id}.json"
      
  js = req.get(url).json()

  return jsonify(js)

@app.route("/friendlyfox/<id>")
def friendlyfox(id):
  
  url = f"https://bafybeiaoan7ganz52aqidn5llmxyrji7woff4lwewhmtorzvhw6uepsbx4.ipfs.nftstorage.link/{int(id)-1}.json"
      
  js = req.get(url).json()

  js.pop('properties')
  js.pop('collection')
  js.pop('seller_fee_basis_points')

  del js['attributes'][-1]

  return jsonify(js)


  # https://testlaunchmynft.mypinata.cloud/ipfs/QmU4ED8jgnZt4CBKZm3GjMr7uy4qjFCoPufLMjB3URAGy2/3332.json


@app.route("/")
def hello_world():
  
  return 'Hello world'


  