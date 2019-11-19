from subprocess import run,PIPE

process=run(["youtube-dl"],stdout=PIPE)
print(process.stdout)
