from subprocess import  run,PIPE

def download(url,args):
    if type(url)==str:
        url=[url]
    process=run((["python","-m","youtube_dl"]+url+args),stdout=PIPE,stderr=PIPE)
    return (process.stdout.decode(errors='ignore'),process.stderr.decode(errors='ignore'))


if __name__=="__main__":
    print(download('https://www.youtube.com/watch?v=zSOJk7ggJts',["-x","--audio-format","wav"]))

