import requests as req

s = req.get('https://www.nftscan.com/nftscan/nftSearch?searchValue=0x32f8EE2B5707138e1bdd04D3631A04EB104dc141&pageIndex=58&pageSize=40')
{
   "name":"Japanese Born Ape Society #2118",
   "image":"ipfs://QmepLasmAFkqg3HBSfeBAQCmyQZR76qm4nyxUa11VRjYF1",
   "attributes":[
      {
         "trait_type":"Background",
         "value":"Purple"
      },
      {
         "trait_type":"Accessories",
         "value":"None"
      },
      {
         "trait_type":"Fur",
         "value":"Phoenix Red"
      },
      {
         "trait_type":"Clothes",
         "value":"Black Hoodie"
      },
      {
         "trait_type":"Eyes",
         "value":"Japanese"
      },
      {
         "trait_type":"Hat",
         "value":"Female Hair"
      },
      {
         "trait_type":"Mouth",
         "value":"White Beard"
      },
      {
         "trait_type":"Earring",
         "value":"None"
      }
   ]
}
print(len(s.json()['data']['nftList']))