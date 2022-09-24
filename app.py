from flask import Flask, render_template, request, redirect, url_for
import requests
app = Flask(__name__)


headers = {
'Host': 'srv5.y2mate.is',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Language': 'en-GB,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Origin': 'https://y2mate.is',
'X-Requested-With': 'XMLHttpRequest',
'Referer': 'https://y2mate.is/',
'Connection': 'keep-alive',
'Sec-Fetch-Dest': 'empty',
'Cache-Control': 'no-cache',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-site',
'Pragma': 'no-cache'
}

def getDownloadLink(link):
	j = []
	res = requests.get(f'http://srv5.y2mate.is/listFormats?url={link}', headers=headers)
	data = res.json()
	for x in data['formats']['video']:
		if 'googlevideo.com' in x['url']:
			j.append(x['url'].split('&title')[0])
	return j[1] if len(j) > 0 else link

@app.get("/")
def index():
	return render_template("index.html")

@app.post("/")
def index_post():
	videoLink = request.form.get("videoId")
	vidDwnLink = getDownloadLink(videoLink)
	return redirect(vidDwnLink)

if __name__ == '__main__':
	app.run()