import pytube, youtube_dl, sys
from rich.console import Console


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
    }],
    'postprocessor_args': [
        '-ar', '16000'
    ],
    'prefer_ffmpeg': True,
    'keepvideo': True
}


console = Console()

url = str(input('URL: '))

if 'youtu' not in url:
	console.print('[red][-] Invalid URL!')
	sys.exit()
if '/' not in url:
	console.print('[red][-] Invalid URL!')
	sys.exit()

def viD(url):
	try:
		video = pytube.YouTube(url).streams.get_highest_resolution()
		console.print(f"[green][+] [white]Downloading: '{video.title}'")
		video.download()
	except:
		console.print('[red][-] [white]Please Check Your Internet Connection!')

def auD(url):
	try:
		print('Downloading Audio')
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download([url])
	except:
		console.print('[red][-] [white]Please Check Your Internet Connection!')


console.print('''[yellow]
[1] Download Video
[2] Download Audio
[red][3] Exit Program''')


def getOP():
	global option
	try:
		option = int(input('Option: '))
		if option > 3 or option < 0:
			print('[-] Please Enter Valid Option.')
			getOP()
	except:
		print('[-] Please Enter Valid Option.')
		getOP()
	return option


option = getOP()

if option == 1:
	viD(url)
elif option == 2:
	auD(url)
else:
	console.print('[-] Good Bye!', style="bold red")
	sys.exit()

#CyberTitus.github.io