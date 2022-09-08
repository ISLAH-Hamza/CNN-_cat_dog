from turtle import delay, down
from unittest import skip
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time


def download_image(download_path, url, file_name):
	try:
		image_content = requests.get(url).content
		image_file = io.BytesIO(image_content)
		image = Image.open(image_file)
		file_path = download_path + file_name

		with open(file_path, "wb") as f:
			new_image = image.resize((250, 250))
			new_image.save(f, "JPEG")
		print("Success")

	except Exception as e:
		print('FAILED -', e)


PATH="C:\\Program Files (x86)\\chromDrive\\chromedriver.exe"
urls =["https://www.google.com/search?q=elephant+images&sxsrf=ALiCzsaW7TSYiWtX7WoQxiPjOmFuf1eYlg:1661932279415&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjlwZ6ZzPD5AhXI0YUKHUi6B1IQ_AUoAXoECAEQAw&biw=1777&bih=841&dpr=0.9"]
wd = webdriver.Chrome(PATH)
wd.get(urls[0])
links=wd.find_elements(By.CLASS_NAME, "ZZ7G7b")
j=0
for link in links:
	source=link.get_attribute('href')
	urls.append(source)

for l in urls:
	j=j+1
	wd.get(l)
	while True :
		pos=wd.execute_script("return document.body.scrollHeight;")
		wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(1)
		posnew=wd.execute_script("return document.body.scrollHeight;")
		if(pos == posnew):
			break

	thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")

	for i,thm in enumerate(thumbnails):
		source=thm.get_attribute('src')
		download_image('elephants/',source,'image ' + str(j) + 'j' + str(i+1)+'.jpg')


wd.quit()