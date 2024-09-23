import urllib3

url = "https://images.ecestaticos.com/5Zh8JtzJcA2pFfLpWd5sTSeGFMg=/137x6:2103x1481/557x418/filters:fill(white):format(jpg)/f.elconfidencial.com%2Foriginal%2Fed2%2Fe26%2F4ea%2Fed2e264ea1827650f92d2b6f27b8617d.jpg"

http = urllib3.PoolManager()
image_data = http.request("GET", url).data
file_name = "simpsons.jpg"

with open(file_name, 'wb') as file:
	file.write(image_data)