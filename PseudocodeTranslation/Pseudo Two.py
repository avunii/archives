# Alvin Maranx II (maranxlee)
# Fork of PureInJava
# Pseudocode Translation (Part Two)

# PRE-REQUISETES

import array as arr
import sys

space = " "
period = "."
q_mark = "?"
lab = ">"
comma = ","
brack_one = "("
brack_two = ")"
lab_two = lab + space

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

# PRE-MATH

num1 = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
num2 = [80, 81, 82, 83, 84, 85, 86, 87, 88, 89]
num3 = [70, 71, 72, 73, 74, 75, 76, 77, 78, 79]
num4 = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
num5 = [50, 51, 52, 53, 54, 55, 56, 58, 58, 59]
num6 = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
num7 = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
num8 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
num9 = [11, 12, 13, 14, 15, 16, 17, 18, 19]

# TAGS

tag1 = "Alvin Maranx. II (maranxlee)"   
tag2 = "Fork of PureInJava"
tag3 = "Pseudocode Translation (Part Two)"

# PRINTING TAG

print(space)
print(tag1)
print(tag2)
print(tag3)
print(space)

# PRINTING TAG (2)

print(tsk7ad)
print(space)



# TASK 7 (ADVANCED)
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
mth_one = "You entered your Math Marks which were:"
eng_one = "You entered your English Marks which were:"
ksw_one = "You entered your Kiswahili Marks which were:"
bio_one = "You entered your Biology Marks which were:"
che_one = "You entered your Chemistry Marks which were:"
phy_one = "You entered your Physics Marks which were:"
bus_one = "You entered your Business Marks which were:"
ict_one = "You entered your Computer Science Marks which were:"
geo_one = "You entered your Geography Marks which were:"
hist_one = "You entered your History Marks which were:"
art_one = "You entered your Art Marks which were:"
mus_one = "You entered your Music Marks which were:"
rw = "Your raw marks were:"
yrav = "and, your average is:"
andy = "and you"
passd = "passed"
faild = "failed"
inccrt = "Incorrect Score! Please enter a vaild score."
nrm_av = 12
wtha = "with a(n):"
a_star = "A*"
a = "A"
b = "B"
c = "C"
d = "D"
e = "E"
f = "F"
g = "G"
u = "U"
a_star_pss = andy + comma + space + passd + comma + space +  wtha + space + a_star
a_pss = andy + comma + space + passd + comma + space +  wtha + space + a
b_pss = andy + comma + space + passd + comma + space +  wtha + space + b
c_pss = andy + comma + space + passd + comma + space +  wtha + space + c
d_fail = andy + comma + space + faild + comma + space +  wtha + space + d
e_fail = andy + comma + space + faild + comma + space +  wtha + space + e
f_fail = andy + comma + space + faild + comma + space +  wtha + space + f
g_fail = andy + comma + space + faild + comma + space +  wtha + space + g
u_fail = andy + comma + space + faild + comma + space +  wtha + space + u

print(trs)
stna = input(lab_two)
stna = str(stna)

print(mth)
math = input(lab_two)
math = int(math)

if math > 100:
        print(inccrt)
        sys.exit()


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

av_full = av_one / nrm_av

av_full = int(av_full)

flav_one = yrav

print(space)
print(greeting_full)
print(space)
print(mth_one)
print(space)
print (lab_two, math)
print(space)
print(eng_one)
print(space)
print (lab_two, engl)
print(ict_one)
print(space)
print (lab_two, comp)
print(space)
print(ksw_one)
print(space)
print (lab_two, kswa)
print(space)
print(bio_one)
print(space)
print (lab_two, biol)
print(space)
print(che_one)
print(space)
print (lab_two, chem)
print(space)
print(phy_one)
print(space)
print (lab_two, phys)
print(space)
print(bus_one)
print(space)
print (lab_two, buss)
print(space)
print(geo_one)
print(space)
print (lab_two, geog)
print(space)
print(hist_one)
print (lab_two, histo)
print(space)
print(art_one)
print(space)
print (lab_two, artt)
print(space)
print(mus_one)
print(space)
print (lab_two, musi)
print(space)


if av_full > 100:
        print(inccrt)


elif av_full in num1:
        print(rw, av_one, yrav, av_full, comma, a_star_pss)
        
elif av_full in num2:
        print(rw, av_one, yrav, av_full, comma, a_pss)

elif av_full in num1:
        print(rw, av_one, yrav, av_full, comma, b_pss)
        
elif av_full in num3:
        print(rw, av_one, yrav, av_full, comma, c_pss)
        
elif av_full in num4:
        print(rw, av_one, yrav, av_full, comma, d_fail)
                
elif av_full in num5:
        print(rw, av_one, yrav, av_full, comma, e_fail)
        
elif av_full in num6:
        
        print(rw, av_one, yrav, av_full, comma, f_fail)
        
elif av_full in num7:
        print(rw, av_one, yrav, av_full, comma, g_fail)
        
elif av_full in num8:
        print(rw, av_one, yrav, av_full, comma, u_fail)
        
elif av_full in num9:
        print(rw, av_one, yrav, av_full, comma, u_fail)

elif av_full <= 10:
        print(rw, av_one, yrav, av_full, comma, u_fail)
        
