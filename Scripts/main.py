from subprocess import  run,PIPE

def download(url,args):
    if type(url)==str:
        url=[url]
    process=run((["python","-m","youtube_dl"]+url+args),stdout=PIPE,stderr=PIPE)
    return (process.stdout.format(),process.stderr.format())


if __name__=="__main__":
    print(download('https://www.youtube.com/watch?v=VpwAq7hiij0',["-x","--audio-format","wav"]))

