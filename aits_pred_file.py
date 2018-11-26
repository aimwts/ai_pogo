import sys
import os

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key='96663fde97714acd8f34a66758c011e5')
model = app.models.get('aisdts')
model.get_version('d078178ce3974dcba38872655026bf2a')

user_input = input("Enter the path of your file: ")

assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
img1= ClImage(file_obj=open(user_input,'rb'))
print("Ok, found your file!")
#stuff you do with the file goes here

#f.close()

# Concept: GOOD, CLEANING, BURN, EOL, CONTAINMENT, SOLDER, WORN OUT

# file location: C:/afile/a_0k_0u_31g_42mo.jpg
# file location: C:/afile/a_40k_11.1u_27.5g_75.3mo.jpg
# img1 = ClImage(url="https://samples.clarifai.com/metro-north.jpg")
# img1 = ClImage(file_obj=open('C:/dhu_st/2018_projects/AIOT/clarifai-python/pogo_image/pogo_image/a_0k_0u_31g_42mo.jpg', 'rb'))

# img1 = ClImage(file_obj=open('C:/dhu_st/2018_projects/AIOT/clarifai-python/pogo_image/pogo_image/a_0k_0u_31g_42mo.jpg', 'rb'))
response1 = model.predict([img1])


#response = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')

#response = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')

concepts1 = response1['outputs'][0]['data']['concepts']


print ("Predict Result:  --------------------------------------------------")	
for concept in concepts1:
    print(concept['name'], concept['value'])
	
