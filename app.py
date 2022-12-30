from flask import Flask, render_template, request
from pytube import YouTube

app=Flask(__name__)

def getDwLinks(vid):
    video = YouTube(vid).streams
    return [[video.get_highest_resolution(), video.get_lowest_resolution()], [video.get_audio_only(subtype="mp4")]]


@app.get('/')
def homeView():
    return render_template('index.html')

@app.post('/')
def downloadView():
    videoLink = request.form.get('videoLink')
    links = getDwLinks(videoLink)
    return render_template('download.html', links=links)

if __name__ == '__main__':
    app.run()