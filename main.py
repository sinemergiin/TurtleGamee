import turtle
import random
#turtle Game
screen = turtle.Screen()  #ekranı oluştrudum
screen.bgcolor("light blue") #ekranın arka planındaki rengini belirledim
screen.title("cath the Turtle") #Başlığını belirledim
FONT = ('Arial', 30, 'normal') #FONT olarak atadım font'u aşağıda yazdım 12. satırda font yerine
score = 0
game_over = False
#turtle list
turtle_list = []


#score turtle

#countdown turtle
countdown_turtle = turtle.Turtle()

score_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle() #turtleyi orada bulunan ok'u gizledim sakladım
    score_turtle.color("dark blue") #score yazısının rengini belirledim


    top_height = screen.window_height() /2 #ekranımın boyutunu belirledim ikiye böldüm score ortadan başladığı için
    y = top_height * 0.9 #yüzde 90 ile çarptım score:0 ortadaydı yukarı taşıdım
    score_turtle.penup() #çizgisini gizledim

    score_turtle.setpos(0, y)

    score_turtle.write(arg="score:0", move=False , align="center", font=FONT)

grid_size = 10  #kaplumbağaların ne kadar gidebileceğini ölçüyorum aşağıda 34-37. kodlar bununla ilgili

def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x , y):
        global score
        score += 1
        score_turtle.clear() #score arttıkça önce yazılanları silmek demek
        score_turtle.write("Score: {}".format(score),move=False, align="center", font=FONT)


    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2) #kaplumbağamın boyutunu belirledim
    t.color("dark green")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t) #her bir oluşturulan turtleyi bir dizide saklıyorum

x_coorinates = [-20,-10,0,10,20]
y_coordinates = [20,10,0,-20,-10]

def setup_turtles():
    for x in x_coorinates:
        for y in y_coordinates:
             make_turtle(x, y)

    #yukarıdaki for döngüsü aşağıdaki uzun kodun kısa hali ikiside aynı işlevi yapıyor

#make_turtle(-20,20)
#make_turtle(-10,20)
#make_turtle(0,20)
#make_turtle(10,20)
#make_turtle(20,20)
def hide_turtles():
    for t in turtle_list:
        t.hideturtle()  #turtle gizledim
#recursive function
def show_turtles_randomly(): #ratgele turtle gösterme
    if not game_over:
        hide_turtles() #turtle gizledim
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly ,500) #her 500 milisaniyede turtle çıkacak karşımıza


def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.setposition(0, y - 30)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)



turtle.tracer(0) #takip edici

setup_score_turtle()
setup_turtles()
hide_turtles()
show_turtles_randomly()
countdown(10)

turtle.tracer(1) #kaplumbağalarımı tek seferde ekrana getiriyor tek tek getirmek yerine


turtle.mainloop()


