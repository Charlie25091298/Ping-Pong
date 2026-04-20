import tkinter

screen = tkinter.Tk()
screen.geometry("800x600")
screen.title("Ping Pong")
canvas = tkinter.Canvas(screen,width=800,height=600,bg="black")
canvas.place(x=0,y=0)
canvas.create_line(400,0,400,800,fill="White")
canvas.create_oval(300,200,500,400,outline="White")
scoretext = canvas.create_text(300,50, text= f"0 : 0",fill="white",font=("ariel",20,"normal"))
class Ball():
    def __init__(self,x0,y0,x1,y1,colour):
        self.sprite = canvas.create_oval(x0,y0,x1,y1,fill=colour)
        self.y = 0.1
        self.x = 0.2
        self.s1 = 0
        self.s2 = 0
    def draw(self):
        canvas.move(self.sprite,self.x,self.y)
        pos = canvas.coords(self.sprite)
        if pos[2] > 800 :
            self.x = -0.2
            self.s1 += 1
            canvas.itemconfig(scoretext,text = f"{self.s1} : {self.s2}")
        if pos[0] < 0 :
            self.x = 0.2
            self.s2 += 1
            canvas.itemconfig(scoretext,text = f"{self.s1} : {self.s2}")
        if pos[1] < 0 :
            self.y = 0.2
        if pos[3] > 600 :
            self.y = -0.2
    def hit_paddle(self,p1,p2):
        p1 = canvas.coords(player1.sprite)
        p2 = canvas.coords(player2.sprite)
        pos = canvas.coords(self.sprite)
        if pos[3] > p1[1] and pos[1] < p1[3] and pos[0] > p1[0] and pos[0] < p1[2]  :
            self.x = 0.2
        if pos[3] > p2[1] and pos[1] < p2[3] and pos[2] > p2[0] and pos[2] < p1[2]:
            self.x = -0.2
    

        
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
        self.y = -0.5
    def movedown(self,event):
        self.y = 0.5
   

player1 = Player(5,5,20,100,"green")
player2 = Player(780,5,795,100,"purple")
ball = Ball(375,325,400,350,"yellow")

canvas.bind_all("w",player1.moveup)
canvas.bind_all("s",player1.movedown)
canvas.bind_all("<KeyPress-Down>",player2.movedown)
canvas.bind_all("<KeyPress-Up>",player2.moveup)


while True :
    player1.draw()
    player2.draw()
    ball.draw()
    ball.hit_paddle(player1,player2)
    screen.update_idletasks()
    screen.update()

screen.mainloop()