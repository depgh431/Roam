from graphics import *
import winsound


class Hero:
    def __init__(self, helth, hel, n):
        self.helth = helth
        self.w = 0
        self.hel = hel
        self.n = n

    def dmg(self, c,n):
            import random
            if c>190 and c<290 and n>708 and n<752:
                d = 9
                self.w = 5
                r = ["mur1.gif", "mur2.gif", 'mur3.gif', 'mur4.gif', 'mur5.gif', 'mur6.gif', 'mur7.gif', 'mur8.gif', 'mur8.gif']
                l = [0, 1, 2, 3, 4, 5, 6, 7, 0]
                for x in l:
                    im = Image(Point(480, 416), r[x])
                    im.draw(win)
                    time.sleep(0.3)
            elif c > 430 and c < 530 and n > 708 and n < 752:
                d = 5
                self.w = 9
                r = ["ne1.gif", "ne2.gif", 'ne3.gif', 'ne4.gif', 'ne5.gif', 'ne6.gif', 'ne7.gif', 'ne8.gif', 'ne9.gif',
                     'ne10.gif',
                     'ne11.gif']
                l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 0]
                for x in l:
                    im = Image(Point(480, 416), r[x])
                    im.draw(win)
                    time.sleep(0.3)
            elif c>670 and c<770 and n>708 and n<752:
                d = 6
                k = 0
                tx=Text(Point(480, 671),"Gon charges up an attack , Spam Mouse click to make it faster")
                tx.draw(win)
                win.checkMouse()
                time.sleep(2)
                tx.setText("Now")
                start_time = time.time()
                seconds = 3.0
                while True:
                    current_time = time.time()
                    elapsed_time = current_time - start_time
                    if win.checkMouse() != None:
                        k = k + 1
                    if elapsed_time > seconds:
                        tx.undraw()
                        break
                r = ["mur1.gif", "mur2.gif", 'mur3.gif', 'mur4.gif', 'mur5.gif','mur9.gif','mur11.gif','mur10.gif','mur11.gif', 'mur6.gif', 'mur7.gif', 'mur8.gif']
                l = [0, 1, 2, 3, 4, 5, 6, 7, 8,9,10,11,0]
                for x in l:
                    im = Image(Point(480, 416), r[x])
                    im.draw(win)
                    time.sleep(0.3)
                if k<5 or k==None:
                    self.w=2
                elif k>=5 and k<8:
                    self.w=6
                elif k>=8 and k<13:
                    self.w=8
                elif k>=13 and k<15:
                    self.w=10
                elif k>=15 and k<20:
                    self.w=12
                elif k>=20:
                    self.w=15
            else:
                qw = Text(Point(480, 671), "Wrong Input")
                qw.draw(win)
                win.getMouse()
                qw.undraw()
                return 0
            op = (random.randint(1, 10))
            if op <= d:
                return self.w
            else:
                self.w = 0
    def helt(self):
        self.helth = self.helth - self.w
        if self.helth > 0:
            u = "Enemy's Health"+ " "+str(self.helth)
        else:
            u = "Foe Defeated"
        return u
    def hel2(self):
        self.dm = (random.randint(2, self.n))
        self.hel = self.hel - self.dm
        return self.hel
winsound.PlaySound("brr.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
win = GraphWin("Roam", 960, 832)
ima = Image(Point(480, 416), "mur1.gif")
ima.draw(win)
io = Text(Point(480, 671),
          "Welcome to the Heaven's Arena , you and your friend Gon are on a journey to go through the floors and have managed to reach the 200s floor")
io.draw(win)
io.setSize(10)
ic = Text(Point(480, 751),
          'But here is where the trouble begins, with the fighters in the 200s and above knowing Nen , its becoming increasingly difficult for you to move on')
ic.draw(win)
ic.setSize(10)
win.getMouse()
io.undraw()
ic.undraw()
win.getMouse()
io = Text(Point(480, 671), "Will you be able to meet the challenge and reach the floor masters? Why don't we find out")
io.draw(win)
io.setSize(10)
ic = Text(Point(480, 751),
          "you face off with Hisoka during your first match, a magician who doesn't yield to the likes of you")
ic.draw(win)
ic.setSize(10)
win.getMouse()
io.undraw()
ic.undraw()
win.getMouse()
io = Text(Point(480, 671), "Hisoka steps forward but you shake as you look at him , his Nen overpowering you")
io.draw(win)
io.setSize(10)
ic = Text(Point(480, 751),
          "You have only a small moveset between the two of you that would work on him as well as having 25hp")
ic.draw(win)
ic.setSize(10)
win.getMouse()
io.undraw()
ic.undraw()
win.getMouse()
io = Text(Point(480, 671), "You have 3 moves in your arsenal")
io.draw(win)
io.setSize(10)
ic = Text(Point(480, 751),
          "Rod- Gon uses his fishing rod to try to hit the enemy, a very reliable move with low damage")
ic.draw(win)
ic.setSize(10)
win.getMouse()
io.undraw()
ic.undraw()
win.getMouse()
io = Text(Point(480, 671),
          "Phantom step - you use your Nen to shadow step and deliver a blow , a less reliable but higher damage move")
io.draw(win)
io.setSize(10)
ic = Text(Point(480, 751),
          "JaJanken- Gon charges up a powerful attack with your help , it has huge damage potential but depends on input")
ic.draw(win)
ic.setSize(10)
win.getMouse()
io.undraw()
ic.undraw()
win.getMouse()
r=["IM1.gif","IM2.gif","IM3.gif","IM4.gif",'IM5.gif',"IM6.gif"]
l=[0,1,2,3,4,3,2,1,0]
for x in range(2):
    for y in l:
        im = Image(Point(480, 416), r[y])
        im.draw(win)
        time.sleep(0.2)
ima.undraw()
ima.draw(win)
import random

a = 30
g = 25
n = 2
while a > 0:
        obj = Hero(a, g, n)
        io = Text(Point(480, 671), "Do an Attack")
        re1 = Rectangle(Point(190, 708), Point(290, 752))
        re2 = Rectangle(Point(430, 708), Point(530, 752))
        re3 = Rectangle(Point(670, 708), Point(770, 752))
        re2.setWidth(2)
        re1.setWidth(2)
        re3.setWidth(2)
        e = Text(Point(240, 730), "Pole")
        f = Text(Point(480, 730), "Phantom step")
        rt = Text(Point(720, 730), "JaJanken")
        rt.setSize(10)
        rt.draw(win)
        f.setSize(8)
        f.draw(win)
        e.draw(win)
        re3.draw(win)
        re1.draw(win)
        re2.draw(win)
        io.draw(win)
        j = win.getMouse()
        c = j.getX()
        kl = j.getY()
        g = obj.hel2()
        io.undraw()
        re1.undraw()
        re2.undraw()
        re3.undraw()
        e.undraw()
        f.undraw()
        rt.undraw()
        r=["h1.gif","h2.gif",'h3.gif',"h4.gif",'hi7.gif']
        l=[0,1,2,3,4,1,0]
        for x in l:
            im = Image(Point(480, 416), r[x])
            im.draw(win)
            time.sleep(0.2)
        re = Text(Point(480, 671), ("Hisoka attacks"))
        fe = Text(Point(480, 700), ("Damage taken {}".format(obj.dm)))
        ui = Text(Point(480, 729), ("Your Health {}".format(g)))
        re.draw(win)
        fe.draw(win)
        ui.draw(win)
        win.getMouse()
        re.undraw()
        fe.undraw()
        ui.undraw()
        if g <= 0:
            ew=Image(Point(480,416),"rip.gif")
            ew.draw(win)
            winsound.PlaySound("rip.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
            win.getMouse()
            exit()
            break
        ofw=obj.dmg(c,kl)
        if ofw==None:
            im= Text(Point(480, 758), ("Attack Missed , 0 Damage given"))
        else:
            im = Text(Point(480, 758), ("Damage Given {}".format(ofw)))
        im.draw(win)
        q = str(obj.helt())
        qi = Text(Point(480, 700), q)
        qi.draw(win)
        win.getMouse()
        im.undraw()
        qi.undraw()
        a = a - obj.w
        n = n + 1
        if a <= 0:
            print(
                "You have won, for now , he did say he went easy on you but let us see what awaits you on the Higher floors")
            win.getMouse()
            win.close()
            wi=GraphWin("Dn",744,741)
            winsound.PlaySound("dn.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
            im=Image(Point(744/2,741/2),"Dn.gif")
            im.draw(wi)
            wi.getMouse()
            wi.close()
            break
