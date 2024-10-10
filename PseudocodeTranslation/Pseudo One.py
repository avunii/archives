# Alvin Maranx II (maranxlee)
# Fork of PureInJava
# Pseudocode Translation (Part One)

# PRE-REQUISETES

space = " "
period = "."
q_mark = "?"
lab = ">"
comma = ","
brack_one = "("
brack_two = ")"

tsk1 = "TASK 1"
tsk2 = "TASK 2"
tsk3 = "TASK 3"
tsk4 = "TASK 4"
tsk5 = "TASK 5"
tsk6 = "TASK 6"
tsk7 = "TASK 7"
dw = "Dumbed Down Edition"
adde = "Advanced Edition"

tsk7db = tsk7 + space + brack_one + dw + brack_two
tsk7ad = tsk7 + space + brack_one + adde + brack_two

# TAGS

tag1 = "Alvin Maranx. II (maranxlee)"
tag2 = "Fork of PureInJava"
tag3 = "Pseudocode Translation (Part One)"

# PRINTING TAG

print(space)
print(tag1)
print(tag2)
print(tag3)
print(space)

# TASK 1

print(tsk1)
print(space)

ans = "Your Answer is:"

a = input("Please enter your first number: ")
a = int(a)
b = input("Please enter your second number: ")
b = int(b)

c = a + b

print(ans, c, period)

print(space)

# TASK 2

print(tsk2)
print(space)

name_i = "What is your name?"
name_iv = "What is your name, "

print(name_i)

name_ii = input("Enter your name: ")
name_ii = str(name_ii)

name_iii = name_iv + name_ii + q_mark

print(name_iii)

print(space)

# TASK 3

print(tsk3)
print(space)


fr_nm = "What is your first name?"
fr_nm_ii = "Enter your first name: "
sc_nm = "What is your second name?"
sc_nm_ii = "Enter your second name: "
tr_nm = "What is your third name?"
tr_nm_ii = "Enter your third name: "
yrns = "Your names are: "

print(fr_nm)

nm_one = input(fr_nm_ii)
nm_one = str(nm_one)

print(sc_nm)

nm_two = input(sc_nm_ii)
nm_two = str(nm_two)

print(tr_nm)

nm_three = input(tr_nm_ii)
nm_three = str(nm_three)

yrns_full = yrns + nm_one + space + nm_two + space + nm_three + period

print(yrns_full)

print(space)

# TASK 4

print(tsk4)
print(space)

passd = "Pass"
faild = "Fail"
lab_two = lab + space

print("Enter Student's Marks")

marks = input(lab_two)

marks = int(marks)

if marks > 50:
    print(passd)
else:
    print(faild)

print(space)

# TASK 5

print(tsk5)
print(space)

error = "Error: Division by zero"
ans_three = "Your answer is:"
tr_one = "Enter your first number: "
tr_two = "Enter your second number: "

x = input(tr_one)
x = int(x)
y = input(tr_two)
y = int(y)

if y == 10:
    print(error)
else:
    quotient = x/y

print(ans_three, quotient)

print(space)

# TASK 6

print(tsk6)
print(space)

wht = "Enter Athlete's athlete"
wht_two = "Enter Athlete's position"
ps1 = "10,000 Reward"
ps2 = "5,000 Reward"
ps3 = "2,500 Reward"
yr = "You are"
ad = "and your reward is:"
sry = "Sorry, you are not legible for our awards"

print(wht)
athlete = input(lab_two)
athlete = str(athlete)
print(wht_two)
pos = input(lab_two)
pos = str(pos)

ps1_re =  yr + space + athlete + space + ad + space + ps1
ps2_re =  yr + space + athlete + space + ad + space + ps2
ps3_re =  yr + space + athlete + space + ad + space + ps3
sry_re =  sry + period

if pos == "Position 1":
    print(ps1_re)
    if pos == "Position 2":
        print(ps2_re)
    if pos == "Position 3":
        print(ps3_re)
else:
    print(sry_re)

print(space)

# TASK 7

print(tsk7db)
print(space)

trs = "Please Enter Student's Name"
mth = "Enter Math Marks"
eng = "Enter English Marks"
ksw = "Enter Kiswahili Marks"
bio = "Enter Biology Marks"
che = "Enter Chemistry Marks"
phy = "Enter Physics Marks"
bus = "Enter Business Marks"
ict = "Enter Computer Science Marks"
geo = "Enter Geography Marks"
hist = "Enter History Marks"
art = "Enter Art Marks"
mus = "Enter Music Marks"
greeting = "Hi"
yraw = "Your raw marks are:"
frm = "For more information run the second file"

print(trs)
stna = input(lab_two)
stna = str(stna)

print(mth)
math = input(lab_two)
math = int(math)

print(eng)
engl = input(lab_two)
engl = int(engl)

print(ict)
comp = input(lab_two)
comp = int(comp)

print(ksw)
kswa = input(lab_two)
kswa = int(kswa)

print(bio)
biol = input(lab_two)
biol = int(biol)

print(che)
chem = input(lab_two)
chem = int(chem)

print(phy)
phys = input(lab_two)
phys = int(phys)

print(bus)
buss = input(lab_two)
buss = int(buss)

print(geo)
geog = input(lab_two)
geog = int(geog)

print(hist)
histo = input(lab_two)
histo = int(histo)

print(art)
artt = input(lab_two)
artt = int(artt)

print(mus)
musi = input(lab_two)
musi = int(musi)

greeting_full = greeting + comma + space + stna


av_one = math + engl + comp + kswa + biol + chem + phys + buss + geog + histo + artt + musi

full_info = greeting + comma + space + stna + comma + yraw

full_info_ii = period + space + frm + period

print(full_info, av_one, full_info_ii)



















