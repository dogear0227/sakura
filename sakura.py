import tkinter as tk

index=0

def btn_next():
    global index
    root['bg']='lightblue'
    index=(index+1) % len(photos)
    canvas.delete('p1')
    canvas.create_image(320,213,image=photos[index],tag='p1')
    text_label["text"]=names[index]

root=tk.Tk()
root.geometry('700x560')
root['bg']='lightgreen'

canvas=tk.Canvas(root,width=640,height=426,bd=0,highlightthickness=0,relief='ridge')
canvas.pack(pady=20)
photos=[
        tk.PhotoImage(file='sakura1.png'),
        tk.PhotoImage(file='sakura2.png'),
        tk.PhotoImage(file='sakura3.png'),
        tk.PhotoImage(file='sakura4.png'),
        tk.PhotoImage(file='sakura5.png'),
]
names=[
        "千鳥ヶ淵(千代田区)",
        "井の頭恩賜公園(武蔵野市)",
        "中目黒目黒川(目黒区)",
        "六本木ヒルズ(港区)",
        "新宿御苑(新宿区)"
        
        ]
canvas.create_image(320,213,image=photos[index],tag='p1')
btn=tk.Button(text='次へ',command=btn_next)
btn.pack(ipadx=10,ipady=5)
text_label = tk.Label(root, text="東京の桜の名所", font=("Helvetica", 16), bg="lightblue")
text_label.pack()
root.mainloop()
