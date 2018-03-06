import tkinter as tk
import random as rnd
import math as mth


def meiksq(a, b, c):
    can.create_rectangle(a, b, a + 94, b + 94, fill=c, width=0)
    if c == '#fea':

        a += 12
        b += 12

        leaf(a, b, 'red', 67)
        leaf(a, b, 'red', 157)
        leaf(a, b, 'red', 247)
        leaf(a, b, 'red', 337)

        leaf(a, b, 'blue', 22)
        leaf(a, b, 'blue', 112)
        leaf(a, b, 'blue', 202)
        leaf(a, b, 'blue', 292)

        can.create_oval(a + 30, b + 30, a + 40, b + 40, fill='red', outline='red')


def leaf(a, b, c, d):

    a2 = a + 70
    b2 = b + 70

    d -= 40
    d2 = d + 180

    rad = (d / 180) * mth.pi
    rad2 = ((d + 80) / 180) * mth.pi

    chordstartx = mth.cos(rad) * 35
    chordstarty = mth.sin(rad) * 35

    chordendx = mth.cos(rad2) * 35
    chordendy = mth.sin(rad2) * 35

    can.create_arc(a - chordstartx, b + chordstarty, a2 - chordstartx, b2 + chordstarty, start=d, extent=80, fill=c, style=tk.CHORD, outline=c)
    can.create_arc(a + chordendx, b - chordendy, a2 + chordendx, b2 - chordendy, start=d2, extent=80, fill=c, style=tk.CHORD, outline=c)


def meikci(a, b, c, d):
    can.create_oval(a + 12, b + 12, a + 84, b + 84, fill=c, width=0)
    can.create_text(a + 50, b + 50, text=d, fill='#888', font=0, width=50)


class Blak:
    def __init__(self, x, y, tp, on, sym):
        self.x = x
        self.y = y
        self.tp = tp
        self.on = on
        self.sym = sym

    def rendr(self):
        if self.tp == 'sp':
            c = '#fea'
        elif self.tp == 'bg':
            c = '#ffe'
        elif self.tp == 'ed':
            c = '#fef'
        else:
            c = '#00a'
        meiksq(self.x, self.y, c)
        if self.on == 'R':
            meikci(self.x, self.y, '#eee', self.sym)
        if self.on == 'B':
            meikci(self.x, self.y, '#111', self.sym)


class Bead:
    def __init__(self, c, pos, sym):
        self.c = c
        self.pos = pos
        self.sym = sym

    def move(self, b):
        self.pos += b


class Sett:
    def __init__(self, a, trn, re):
        self.a = a
        self.trn = trn
        self.re = re


def setb():
    bstart = ''
    rstart = ''
    bhome = ''
    rhome = ''
    for n in bcoll:
        if n.pos == 0:
            bstart += n.sym
        if n.pos == 15:
            bhome += n.sym
    for n in rcoll:
        if n.pos == 0:
            rstart += n.sym
        if n.pos == 15:
            rhome += n.sym
    for n in range(16):
        p[pa[n]].on = ' '
        p[pb[n]].on = ' '
        for m in bcoll:
            if m.pos == n:
                p[pa[n]].on = 'B'
                p[pa[n]].sym = m.sym
        for m in rcoll:
            if m.pos == n:
                p[pb[n]].on = 'R'
                p[pb[n]].sym = m.sym
    p[0].sym = bstart
    p[5].sym = rstart
    p[20].sym = bhome
    p[23].sym = rhome


def mcvb(num, mcv, jface):

    mess.grid_forget()

    blocked = False
    coll = rcoll
    ocoll = bcoll
    rnumb.re = False

# Check for rolling zero
    if mcv != 0:
        # Set coll to current player's pieces and ocoll to opponent's
        if rnumb.trn == '#111':
            coll = bcoll
            ocoll = rcoll

        # bid is the space the piece would land on
        bid = coll[num].pos + mcv

        # Check for special space
        for n in spnumb:
            if bid == n:
                rnumb.re = True

        # Check for space is occupied by a friendly piece
        for n in coll:
            if n.pos == bid:
                if not bid == 15:
                    tvar.set('Blocked')
                    mess.grid(row=0, column=3, columnspan=3)
                    blocked = True

        # Check for space is occupied by enemy piece
        for n in ocoll:
            if 4 < bid < 13 and bid == n.pos:
                if n.pos == 8:
                    tvar.set('Blocked')
                    mess.grid(row=0, column=3, columnspan=3)
                    blocked = True
                else:
                    n.pos = 0

        # Check if the space is off the board
        if bid > 15:
            tvar.set('Overshoot')
            mess.grid(row=0, column=3, columnspan=3)
            blocked = True

        # Check if piece is already in goal
        if coll[num].pos == 15:
            tvar.set('Already Scored')
            mess.grid(row=0, column=3, columnspan=3)

    # If all checks out
    if not blocked:
        coll[num].move(mcv)

        # Checks if all pieces have scored
        win = True
        for n in coll:
            if not n.pos == 15:
                win = False
        if win:
            tvar.set('WINNER')
            mess.grid(row=0, column=3, columnspan=3)
        setb()
        massrend()
        doroll(jface)


def massrend():
    can.delete('all')
    for w in p:
        w.rendr()

    can.create_rectangle(0, 0, 830, 342, width=12)

    can.create_line(xm + 503, 0, xm + 503, 112, width=6)
    can.create_line(xm + 503, 230, xm + 503, 342, width=6)
    can.create_line(xm + 97, 227, xm + 709, 227, width=6)
    can.create_line(xm + 97, 115, xm + 709, 115, width=6)


def doroll(kface):
    if not rnumb.re:
        if rnumb.trn == '#eee':
            rnumb.trn = '#111'
        else:
            rnumb.trn = '#eee'
    displ = ''
    nf = 0
    for n in range(4):
        if rnd.randint(0, 1) == 1:
            nf += 1
            displ += '\u26ab'
        else:
            displ += '\u26aa'
    rnumb.a = nf

    kface[0].configure(bg=rnumb.trn, text=displ)
    for zxz in range(1, 9):
        kface[zxz].configure(bg=rnumb.trn)


def passon(mcv):

    mess.grid_forget()

    coll = rcoll
    ocoll = bcoll

    if rnumb.trn == '#111':
        coll = bcoll
        ocoll = rcoll

    novalid = True
    for n in coll:
        valid = True
        bid = n.pos + mcv

        for m in coll:
            if bid == m.pos:
                valid = False

        if bid > 15:
            valid = False

        if bid == 8:
            for m in ocoll:
                if m.pos == 8:
                    valid = False

        if valid:
            novalid = False

    if novalid:
        mess.grid_forget()
        rnumb.re = False
        doroll(iface)
    else:
        tvar.set('One Or More Valid Moves')
        mess.grid(row=0, column=3, columnspan=3)


def reset(jface):
    mess.grid_forget()
    for n in rcoll:
        n.pos = 0
    for n in bcoll:
        n.pos = 0

    setb()
    massrend()
    doroll(jface)


def showboard():
    startscreen.grid_forget()
    game.grid(row=0, column=0)

root = tk.Tk()
game = tk.Frame(root, bg='black', bd=0)

startscreen = tk.Frame(root, bg='black')
titlecard = tk.Label(startscreen, bg='#000', fg='#fff', text='The Royal Game of Ur', width=30, height=6)
startb = tk.Button(startscreen, text='Single Player', command=showboard)

titlecard.grid(row=0)
startb.grid(row=1)
startscreen.grid()

can = tk.Canvas(game, width=830, height=342, bd=0, highlightthickness=0, bg='#fc0')

tvar = tk.StringVar()
tvar.set('Default')

mess = tk.Label(game, textvariable=tvar, bg='#000', fg='#fff')


rnumb = Sett(0, '#111', False)

bead1 = Bead('B', 0, '\u10ac')
bead2 = Bead('B', 0, '\u10ab')
bead3 = Bead('B', 0, '\u10b2')
bead4 = Bead('B', 0, '\u10a1')
bead5 = Bead('B', 0, '\u10bf')
bead6 = Bead('B', 0, '\u10c5')

read1 = Bead('R', 0, '\u10ac')
read2 = Bead('R', 0, '\u10ab')
read3 = Bead('R', 0, '\u10b2')
read4 = Bead('R', 0, '\u10a1')
read5 = Bead('R', 0, '\u10bf')
read6 = Bead('R', 0, '\u10c5')

bcoll = [bead1, bead2, bead3, bead4, bead5, bead6]
rcoll = [read1, read2, read3, read4, read5, read6]

xm = 12
ym = 12

s0a = Blak(xm + 400, ym, 'bg', 'None', '')
s1a = Blak(xm + 300, ym, '', 'None', '')
s2a = Blak(xm + 200, ym, '', 'None', '')
s3a = Blak(xm + 100, ym, '', 'None', '')
s4a = Blak(xm, ym, 'sp', 'None', '')

s0b = Blak(xm + 400, ym + 224, 'bg', 'None', '')
s1b = Blak(xm + 300, ym + 224, '', 'None', '')
s2b = Blak(xm + 200, ym + 224, '', 'None', '')
s3b = Blak(xm + 100, ym + 224, '', 'None', '')
s4b = Blak(xm, ym + 224, 'sp', 'None', '')

s5 = Blak(xm, ym + 112, '', 'None', '')
s6 = Blak(xm + 100, ym + 112, '', 'None', '')
s7 = Blak(xm + 202, ym + 112, '', 'None', '')
s8 = Blak(xm + 304, ym + 112, 'sp', 'None', '')
s9 = Blak(xm + 406, ym + 112, '', 'None', '')
s10 = Blak(xm + 508, ym + 112, '', 'None', '')
s11 = Blak(xm + 610, ym + 112, '', 'None', '')
s12 = Blak(xm + 712, ym + 112, '', 'None', '')

s13a = Blak(xm + 712, ym, '', 'None', '')
s14a = Blak(xm + 612, ym, 'sp', 'None', '')
s15a = Blak(xm + 512, ym, 'ed', 'None', '')

s13b = Blak(xm + 712, ym + 224, '', 'None', '')
s14b = Blak(xm + 612, ym + 224, 'sp', 'None', '')
s15b = Blak(xm + 512, ym + 224, 'ed', 'None', '')


p = [s0a, s1a, s2a, s3a, s4a, s0b, s1b, s2b, s3b, s4b, s5, s6, s7, s8, s9,
     s10, s11, s12, s13a, s14a, s15a, s13b, s14b, s15b]

pa = [0, 1, 2, 3, 4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pb = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 22, 23]
spnumb = [4, 8, 14]

lab = tk.Label(game, text='', bg=rnumb.trn, fg='#888', font=1)
mcv1 = tk.Button(game, text='\u10ac', relief=tk.FLAT, font=1, bg=rnumb.trn, fg='#888', command=lambda: mcvb(0, rnumb.a, iface))
mcv2 = tk.Button(game, text='\u10ab', relief=tk.FLAT, font=1, bg=rnumb.trn, fg='#888', command=lambda: mcvb(1, rnumb.a, iface))
mcv3 = tk.Button(game, text='\u10b2', relief=tk.FLAT, font=1, bg=rnumb.trn, fg='#888', command=lambda: mcvb(2, rnumb.a, iface))
mcv4 = tk.Button(game, text='\u10a1', relief=tk.FLAT, font=1, bg=rnumb.trn, fg='#888', command=lambda: mcvb(3, rnumb.a, iface))
mcv5 = tk.Button(game, text='\u10bf', relief=tk.FLAT, font=1, bg=rnumb.trn, fg='#888', command=lambda: mcvb(4, rnumb.a, iface))
mcv6 = tk.Button(game, text='\u10c5', relief=tk.FLAT, font=1, bg=rnumb.trn, fg='#888', command=lambda: mcvb(5, rnumb.a, iface))
pazz = tk.Button(game, text='pass', font=5, relief=tk.FLAT, bg=rnumb.trn, fg='#888', command=lambda: passon(rnumb.a))
rset = tk.Button(game, text='reset', font=5, relief=tk.FLAT, bg=rnumb.trn, fg='#888', command=lambda: reset(iface))
iface = [lab, mcv1, mcv2, mcv3, mcv4, mcv5, mcv6, pazz, rset]

can.grid(column=0, row=0, columnspan=9)
for z in range(9):
    iface[z].grid(row=1, column=z, sticky='ewns', padx=1)


setb()
massrend()
doroll(iface)

root.mainloop()
