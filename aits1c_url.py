from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key='96663fde97714acd8f34a66758c011e5')
model = app.models.get('aisdts')
model.get_version('d078178ce3974dcba38872655026bf2a')

# Concept: GOOD, CLEANING, BURN, EOL, CONTAINMENT, SOLDER, WORN OUT
# img1 = ClImage(url="https://samples.clarifai.com/metro-north.jpg")
# img1 = ClImage(url="https://raw.githubusercontent.com/aimwts/ai_pogo/master/Image/fail_worn_out.jpg")



img1 = ClImage(url="https://raw.githubusercontent.com/aimwts/ai_pogo/master/Image/a_0k_0u_31g_42mo.jpg")
response1 = model.predict([img1])
img2 = ClImage(url="https://raw.githubusercontent.com/aimwts/ai_pogo/master/Image/a_30k_10.2u_27.6g_59.1mo.jpg")
response2 = model.predict([img2])
img3 = ClImage(url="https://raw.githubusercontent.com/aimwts/ai_pogo/master/Image/fail_burn_pin1.jpg")
response2 = model.predict([img3])
img4 = ClImage(url="https://raw.githubusercontent.com/aimwts/ai_pogo/master/Image/fail_eol3_150k.jpg")
response2 = model.predict([img4])
img5 = ClImage(url="https://raw.githubusercontent.com/aimwts/ai_pogo/master/Image/fail_contamination1.jpg")
response2 = model.predict([img5])
img6 = ClImage(url="https://raw.githubusercontent.com/aimwts/ai_pogo/master/Image/fail_solder_residue1.jpg")
response2 = model.predict([img6])
img7 = ClImage(url="https://raw.githubusercontent.com/aimwts/ai_pogo/master/Image/fail_worn_out.jpg")
response2 = model.predict([img7])

#response = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')

response1 = model.predict([img1])
response2 = model.predict([img2])
response3 = model.predict([img3])
response4 = model.predict([img4])
response5 = model.predict([img5])
response6 = model.predict([img6])
response7 = model.predict([img7])

#response = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')

concepts1 = response1['outputs'][0]['data']['concepts']
concepts2 = response2['outputs'][0]['data']['concepts']
concepts3 = response3['outputs'][0]['data']['concepts']
concepts4 = response4['outputs'][0]['data']['concepts']
concepts5 = response5['outputs'][0]['data']['concepts']
concepts6 = response6['outputs'][0]['data']['concepts']
concepts7 = response7['outputs'][0]['data']['concepts']

for concept in concepts1:
    print(concept['name'], concept['value'])
	
print ("GOOD --------------------------------------------------")	

for concept in concepts2:
    print(concept['name'], concept['value'])		
	
print ("CLEANING --------------------------------------------------")

for concept in concepts3:
    print(concept['name'], concept['value'])

print (" BURN --------------------------------------------------")

for concept in concepts4:
    print(concept['name'], concept['value'])

print (" EOL --------------------------------------------------")

for concept in concepts5:
    print(concept['name'], concept['value'])

print ("CONTAINMENT --------------------------------------------------")

for concept in concepts6:
    print(concept['name'], concept['value'])

print ("SOLDER --------------------------------------------------")

for concept in concepts7:
    print(concept['name'], concept['value'])

print ("WORN OUT --------------------------------------------------")
