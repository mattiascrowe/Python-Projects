quiza= 0
quizb= 0
quizc= 0
quizd= 0
quize= 0
quizf= 0
quizg= 0
b1=["Your colour is Purple, the Colour of Shadows!","Your colour is Blue, the Colour of Tides!","Your colour is Green, the Colour of Gaia!","Your colour is Yellow, the Colour of Aether!","You may choose between Purple, the Colour of Shadows, and Blue, the Colour of Tides!","You may choose between Purple, the Colour of Shadows, and Green, the Colour of Gaia!","You may choose between Purple, the Colour of Shadows, and Yellow, the Colour of Aether!","You may choose between Blue, the Colour of Tides, and Green, the Colour of Gaia!","You may choose between Blue, the Colour of Tides, and Yellow, the Colour of Aether!","You may choose between Green, the Colour of Gaia, and Yellow, the Colour of Aether!"]
b2=["a","b","c","d","You may choose between ab","You may choose between ac","You may choose between ad","You may choose between bc","You may choose between bd","You may choose between cd"]
b3=["a","b","c","d","You may choose between ab","You may choose between ac","You may choose between ad","You may choose between bc","You may choose between bd","You may choose between cd"]
b4=["a","b","c","d","You may choose between ab","You may choose between ac","You may choose between ad","You may choose between bc","You may choose between bd","You may choose between cd"]
b5=["a","b","c","d","You may choose between ab","You may choose between ac","You may choose between ad","You may choose between bc","You may choose between bd","You may choose between cd"]
b6=["a","b","c","d","You may choose between ab","You may choose between ac","You may choose between ad","You may choose between bc","You may choose between bd","You may choose between cd"]
a=["Error"]

print("Greetings, Traveller! Pull up a chair and rest for a while. Do you mind me asking some questions, just so I can figure out where you're from?")

def question(q):
    global quiza, quizb, quizc #define global variables
    answer = input(q)
    if answer == "a":
        quiza = quiza + 1
    elif answer == "b":
        quizb = quizb + 1
    elif answer == "c":
        quizc = quizc + 1
    else:
        print("Sorry, I don't understand that answer.")
        question(q)


question("1) Browsing a collection of worn books on a shelf, you look for some light reading to pass the time. Which book catches your eye? \na) A tale of wild beasts and mystery, of great heroes who journey out into the unknown to save their blighted homeland. \nb) A plucky group of adventurers band together to seek out knowledge and save their city from a great and fell evil. \nc) A young hero rises from the bottom to power and fame, fighting for the chance to right injustice and earn glory.\n")
question("2) You find yourself wandering through a great maze, one said to hold great treasures. What do you appreciate along your way? \na) The different flowers and plants you recognise beside the path, the small animals you see dart between cover ahead of you. \nb) The friends you have found and made, that help you find your way and share in your excitement. \nc) The opportunity to adapt and grow, to prove yourself and find riches and powerful artifacts that lay within.\n")
question("3) You find a peaceful place to contemplate and rest. What do you hear and see? \na) A calm beach, with rock pools full of sea life, the tide hugging the beach and whale song in the distance. \nb) A village square, with children playing on the grass across from you, the smell of fresh bread wafting on the breeze. \nc) A summers field on a warm, moonlit night, quiet and cool solitude to reflect on your inner thoughts.\n")
question("4) Your beliefs are as individual as you are and very personal. How would you feel the presence of your deity? \na) My deity is all around us, in the winds and the rivers, the life that flows through every living creature. \nb) My deity is found in churches and libraries, workshops and hospitals, wherever the light can shine through. \nc) My deity is approaches me in my darkest moments to push me and mentor me, watching as I prove myself and in my greatest victories, congratulate me and share in our glories. \n")


def question2(q2):
    global quizd, quize, quizf, quizg #define global variables
    answer = input(q2)
    if answer == "a":
        quizd = quizd + 1
    elif answer == "b":
        quize = quize + 1
    elif answer == "c":
        quizf = quizf + 1
    elif answer == "d":
        quizg = quizg + 1
    else:
        print("Sorry, I don't understand that answer.")
        question2(q2)

#print 
if quiza > quizb and quiza > quizc:
    a=b1
    print("A")
    q2 =["1) You come across a mighty Stag, that in a deep voice proclaims himself King of the Woods. He has been caught in a bear trap by his hind leg. \na) I tell him I will help him, but only if he gives me the title of King. If he doesn’t, helping him serves no purpose. \nb) I free him, but only so I can challenge him fairly for the title of King. When he is ready we will face each other in combat.\nc) I free him, tending to his wounds as he rests. When he wakes again I will ask him for his blessing, as I travel through his woods.\nd) I free him, then work with him, dismantling any other traps and finding and stopping those who have been placing them.\n",
         "2) In the ancient ruins of a forgotten city, you have followed rumours of a rare and mystical flower, that flowers once every hundred moons. You think it rests high atop a crooked tower. \na) I find a way to the top of the tower, taking the flower and keeping it for myself, owning its rare qualities.  \nb) I climb the tower, reaching the top on my own strength, and take any part of the flower that I might need. \nc) Carefully reaching the top, I will collect the pollen of the flower, hoping to find other places to grow and nurture it. \nd) I stabilize the tower, driving away any pests so that the flower can continue blooming and grant this world its beauty. \n",
         "3) As you cross a bridge, a big booming voice yells out that crossing the bridge requires a price. You see a Troll peeking out from beneath. \na) I inform the lurking troll that you are a tax collector from the troll king, and that if he does not give me half of everything he has, I will be forced to slay him.  \nb) I yell out in return, challenging the troll to hand to hand combat. If he wins, I will pay, but if I win, then all will cross for free. \nc) I bring him a feast of fruits, and try and convince him to move deeper into the forest, where food is plentiful and he won’t come into conflict with any travellers.\nd) I ask him to leave, and if he does not, I will work with the local village to either force him out, or build another bridge. \n ",
         "4) You come across a tree that has Golden fruits, shining in the setting sun.\na) I will take as many fruit as I can, then chop the tree down, so that noone else may have them \nb) I sit beneath the tree, feasting on it’s rich fruits. I will stay here as long as I want, and noone can stop me. \nc) I take some of the fallen fruit, then thank the tree, getting back on my way. \nd) I stop a while, gathering fruit so that the others I’m travelling with can share in its deliciousness. \n",
         "5) After helping an Elder King cure a blighted grove, he brings you to this ancient cavern, and tells you that you may take any axe that they have taken from trespassers in his land. \na) I take a long and nasty looking scythe-like axe, its blade kept ever sharp, even after years of dis-use. \nb) I take the largest axe I can find, its haft made from a long and ancient bone, chiselled with runes, the heft of it belaying its mighty power. \nc) I take an axe with a simple head, but the haft looks like it was naturally grown into shape and coaxed into being. It feels alive, and is blessed by the trees. \nd) I take an axe with an old, wooden haft, but with a head made of pure amber. It glimmers and almost glows in the light, and whoever made it was a highly devoted artisan. \n"]
    for i in q2:
        question2(i)
elif quizb > quiza and quizb > quizc:
     a=b2
     q2 =["1? \na)\nb) \nc)",
         "2? \na)\nb) \nc)",
         "3? \na)\nb) \nc)",
         "4? \na)\nb) \nc)",
         "5? \na)\nb) \nc)"]
     for i in q2:
        question2(i)
elif quizc > quiza and quizc > quizb:
    a=b3
    q2 =["1? \na)\nb) \nc)",
         "2? \na)\nb) \nc)",
         "3? \na)\nb) \nc)",
         "4? \na)\nb) \nc)",
         "5? \na)\nb) \nc)"]
    for i in q2:
        question2(i)
elif quiza == quizb:
    a=b4
    q2 =["1? \na)\nb) \nc)",
         "2? \na)\nb) \nc)",
         "3? \na)\nb) \nc)",
         "4? \na)\nb) \nc)",
         "5? \na)\nb) \nc)"]
    for i in q2:
        question2(i)
elif quiza== quizc:
    a=b5
    q2 =["1? \na)\nb) \nc)",
         "2? \na)\nb) \nc)",
         "3? \na)\nb) \nc)",
         "4? \na)\nb) \nc)",
         "5? \na)\nb) \nc)"]
    for i in q2:
         question2(i)
elif quizb == quizc:
    a=b6
    q2 =["1? \na)\nb) \nc)",
         "2? \na)\nb) \nc)",
         "3? \na)\nb) \nc)",
         "4? \na)\nb) \nc)",
         "5? \na)\nb) \nc)"]
    for i in q2:
        question2(i)
else:
    print("ERRORR!!")




if quizd > quize and quizd>quizf and quizd>quizg:
     print(a[0])
elif quize > quizd and quize>quizf and quize>quizg:
    print(a[1])
elif quizf > quize and quizf>quizd and quizf>quizg:
    print(a[2])
elif quizg > quize and quizg>quizf and quizg>quizd:
    print(a[3])
elif quizd == quize:
    print(a[4])
elif quizd == quizf:
    print(a[5])
elif quizd == quizg:
    print(a[6])
elif quize == quizf:
    print(a[7])
elif quize == quizg:
    print(a[8])
elif quizf == quizg:
    print(a[9])
else:
    print("GRIEVIOUS ERROR")


