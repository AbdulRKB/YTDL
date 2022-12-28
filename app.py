from flask import Flask, render_template, url_for, request, redirect
from pytube import YouTube

app = Flask(__name__)

def ytLink(videoLink):
	yt = YouTube(videoLink)
	video_stream = yt.streams.filter(resolution='720p').first()
	return video_stream.url


@app.get('/')
def index():
	return render_template("index.html")

@app.post('/')
def index_post():
	videoURL = request.form.get('videoLink')
	downloadLink = ytLink(videoURL)
	return redirect(downloadLink)

if __name__ == '__main__':
	app.run()
