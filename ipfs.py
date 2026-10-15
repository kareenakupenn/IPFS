import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
  pinata_url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
  headers = {
      "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI4ODc4YjEwNS0yYTU1LTRlNjgtOGJjNC02MWRlZGM4Mzc4OTIiLCJlbWFpbCI6ImthcmVlbmFrQGVuZ2luZWVyaW5nLnVwZW5uLmVkdSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwaW5fcG9saWN5Ijp7InJlZ2lvbnMiOlt7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6IkZSQTEifSx7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6Ik5ZQzEifV0sInZlcnNpb24iOjF9LCJtZmFfZW5hYmxlZCI6ZmFsc2UsInN0YXR1cyI6IkFDVElWRSJ9LCJhdXRoZW50aWNhdGlvblR5cGUiOiJzY29wZWRLZXkiLCJzY29wZWRLZXlLZXkiOiIzMGJmZWNkMzNlNWM4OTBiMzMxZSIsInNjb3BlZEtleVNlY3JldCI6ImM0YmI0OTk1OTU2YzIwNDFlNzgzMzg5YjNmZjMyNmRjYzQwNWZlZjhkYmUwZDhiYzJiOTA0OGFkNmEzOWI2MGUiLCJleHAiOjE4MjM1NjgwMjZ9.vjRiZDeHi-kVnpsmr-SJk9yI99o4F0EneQCGR2VH7tc",
      "Content-Type": "application/json"
  }
  payload = {
      "pinataContent": data
  }
    
  response = requests.post(pinata_url, json=payload, headers=headers)
  res_data = response.json()
    
  cid = res_data.get("IpfsHash")
	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
  gateway_url = f"https://gateway.pinata.cloud/ipfs/{cid}"
  response = requests.get(gateway_url)
  data = response.json()

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
