import tkinter

screen = tkinter.Tk()
screen.geometry("800x600")
screen.title("Ping Pong")
canvas = tkinter.Canvas(screen,width=800,height=600,bg="black")
canvas.place(x=0,y=0)
canvas.create_line(400,0,400,800,fill="White")
canvas.create_oval(300,200,500,400,outline="White")
class Player():
    def __init__(self,x0,y0,x1,y1,colour):
        self.sprite = canvas.create_rectangle(x0,y0,x1,y1,fill=colour)
        self.y = 0
    def draw(self):
        canvas.move(self.sprite,0,self.y)
        pos = canvas.coords(self.sprite)
        if pos[1] < 0 :
            self.y = 0
        if pos[3] > 600 :
            self.y = 0
    def moveup(self,event):
        self.y = -2
    def movedown(self,event):
        self.y = 2
   

player1 = Player(5,5,20,100,"green")
player2 = Player(780,5,795,100,"purple")

canvas.bind_all("w",player1.moveup)
canvas.bind_all("s",player1.movedown)
canvas.bind_all("<KeyPress-Down>",player2.movedown)
canvas.bind_all("<KeyPress-Up>",player2.moveup)

while True :
    player1.draw()
    player2.draw()
    screen.update_idletasks()
    screen.update()

screen.mainloop()