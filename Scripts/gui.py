from tkinter import *
from tkinter import messagebox
from Scripts.main import download
import json
class Main(object):
    def __init__(self):
        self.NewWindow()
    def NewWindow(self):
        self.Root=Tk()
        self.Root.title("py-youtubemp3")
        self.Init()
        self.Setupbar()
        self.SetupMain()
        self.Loop()
    def Init(self):
        self.Urls=[]
        self.NotifyVal=BooleanVar(value=True)
    def Setupbar(self):
        self.Topbar=Menu(self.Root,tearoff=0)
        self.Root.config(menu=self.Topbar)

        self.FiletypeMenu=Menu(self.Root,tearoff=0)
        self.Topbar.add_cascade(label="檔案類型",menu=self.FiletypeMenu)
        filetypes=[
            "wav","aac","vorbis","mp3","m4a","opus"
        ]
        self.FiletypeVar=StringVar(value=filetypes[0])
        for filetype in filetypes:
            self.FiletypeMenu.add_radiobutton(label=("."+filetype),variable=self.FiletypeVar,value=filetype)
        
        self.QualityMenu=Menu(self.Root,tearoff=0)
        self.Topbar.add_cascade(label="檔案品質",menu=self.QualityMenu)
        qualities=list(range(0,10))
        self.QualityVar=IntVar(value=qualities[0])
        qualitytag=lambda x: str(x) if x!=0 else str(x)+" (最優)"
        for quality in qualities:
            self.QualityMenu.add_radiobutton(label=qualitytag(quality),variable=self.QualityVar,value=quality)
        
        self.QueueMenu=Menu(self.Root,tearoff=0)
        self.Topbar.add_cascade(label="序列選項",menu=self.QueueMenu)
        self.QueueMenu.add_command(label="查看序列",command=lambda :messagebox.showinfo("py-youtubemp3",json.dumps(self.Urls) if self.Urls!=[] else messagebox.showinfo("py-youtubemp3","序列為空")))
        self.QueueMenu.add_command(label="清空序列",command=lambda :self.Urls.clear())
        self.QueueMenu.add_command(label="清除末項",command=lambda :self.Urls.pop() if self.Urls!=[] else None)


        self.OtherMenu=Menu(self.Root,tearoff=0)
        self.Topbar.add_cascade(label="其他選項",menu=self.OtherMenu)
        self.PlaylistVar=BooleanVar(value=True)
        self.OtherMenu.add_checkbutton(label="下載整個播放清單",variable=self.PlaylistVar,onvalue=True,offvalue=False)
        self.SearchVar=BooleanVar(value=False)
        self.OtherMenu.add_checkbutton(label="以歌名搜尋",variable=self.SearchVar,onvalue=True,offvalue=False)
    def SetupMain(self):
        self.UrlLabel=Label(self.Root,text="輸入網址：")
        self.UrlLabel.grid(row=0,column=0)
        self.UrlVar=StringVar()
        self.UrlEntry=Entry(self.Root,textvariable=self.UrlVar)
        self.UrlEntry.grid(row=0,column=1)
        self.QuequButton=Button(self.Root,text="加入序列",command=self.AddQueue)
        self.QuequButton.grid(row=0,column=2)
        self.StartButton=Button(self.Root,text="開始",command=self.Start,fg="green")
        self.StartButton.grid(row=0,column=3)
    def Loop(self):
        self.Root.mainloop()
    def Start(self):
        if self.UrlVar.get()=="":
            if self.Urls==[]:
                return None
        else:
            self.Urls.append(self.UrlVar.get()) if self.SearchVar.get() else self.Urls.append("ytsearch:"+self.UrlVar.get())
        args=[
            "-x",
            "--audio-format",self.FiletypeVar.get(),
            "--audio-quality",str(self.QualityVar.get()), 
        ]
        args.append("--yes-playlist") if self.PlaylistVar.get() else args.append("--no-playlist")
        if self.SearchVar.get():
            self.UrlVar.set("ytsearch:"+self.UrlVar.get())
        messagebox.showinfo("py-youtubemp3","下載檔案中")
        self.Root.withdraw()
        stdout,stderr=download(url=self.Urls,args=args)
        if len(stderr) !=0:
            messagebox.showerror("py-youtubemp3",stderr)
        else:
            messagebox.showinfo("py-youtubemp3","下載完成")
        self.Root.deiconify()
        self.UrlVar.set("")
        self.Urls=[]
    def AddQueue(self):
        if len(self.UrlVar.get())==0:
            return None
        self.Urls.append("ytsearch:"+self.UrlVar.get()) if self.SearchVar.get() else self.Urls.append(self.UrlVar.get())
        if self.NotifyVal.get():
            messagebox.showinfo("py-youtubemp3","已將{}加入下載序列\n點擊開始已開始下載".format(self.UrlVar.get()))
            self.NotifyVal.set(False)
        self.UrlVar.set("")
        

if __name__=="__main__":
    Main()