#define quiz variables
quiza= 0
quizb= 0
quizc= 0
quizd= 0
quize= 0
quizf= 0
quizg= 0
#branch variables to assign to answer
b1=["Purple, the Colour of Shadows","Blue, the Colour of Tides","Green, the Colour of Gaia","Yellow, the Colour of Aether"]
b2=["Green, the Colour of Gaia","Yellow, the Colour of Aether","Orange, the Colour of the Smith","Red, the Colour of the Flame"]
b3=["Orange, the Colour of the Smith","Red, the Colour of the Flame","Purple, the Colour of Shadows","Blue, the Colour of Tides"]
b4=["Blue, the Colour of Tides","Green, the Colour of Gaia","Yellow, the Colour of Aether","Orange, the Colour of the Smith"]
b5=["Red, the Colour of the Flame","Purple, the Colour of Shadows","Blue, the Colour of Tides","Green, the Colour of Gaia"]
b6=["Yellow, the Colour of Aether","Orange, the Colour of the Smith","Red, the Colour of the Flame","Purple, the Colour of Shadows"]
a=["Error"]

print("\nGreetings, Traveller! Pull up a chair and rest for a while. Do you mind me asking some questions, just so I can figure out where you're from?")

def question(q):
    global quiza, quizb, quizc #define global variables
    answer = input(q)
    if answer.lower() == "a":
        quiza = quiza + 1
    elif answer.lower() == "b":
        quizb = quizb + 1
    elif answer.lower() == "c":
        quizc = quizc + 1
    else:
        print("Sorry, I don't understand that answer.")
        question(q)

#initial question block
question("\n1) Browsing a collection of worn books on a shelf, you look for some light reading to pass the time. Which book catches your eye? \na) A tale of wild beasts and mystery, of great heroes who journey out into the unknown to save their blighted homeland. \nb) A plucky group of adventurers band together to seek out knowledge and save their city from a great and fell evil. \nc) A young hero rises from the bottom to power and fame, fighting for the chance to right injustice and earn glory.\n")
question("\n2) You find yourself wandering through a great maze, one said to hold great treasures. What do you appreciate along your way? \na) The different flowers and plants you recognise beside the path, the small animals you see dart between cover ahead of you. \nb) The friends you have found and made, that help you find your way and share in your excitement. \nc) The opportunity to adapt and grow, to prove yourself and find riches and powerful artifacts that lay within.\n")
question("\n3) You find a peaceful place to contemplate and rest. What do you hear and see? \na) A calm beach, with rock pools full of sea life, the tide hugging the beach and whale song in the distance. \nb) A village square, with children playing on the grass across from you, the smell of fresh bread wafting on the breeze. \nc) A summers field on a warm, moonlit night, quiet and cool solitude to reflect on your inner thoughts.\n")
question("\n4) Your beliefs are as individual as you are and very personal. How would you feel the presence of your deity? \na) My deity is all around us, in the winds and the rivers, the life that flows through every living creature. \nb) My deity is found in churches and libraries, workshops and hospitals, wherever the light can shine through. \nc) My deity is approaches me in my darkest moments to push me and mentor me, watching as I prove myself and in my greatest victories, congratulate me and share in our glories. \n")


def question2(q2):
    global quizd, quize, quizf, quizg #define global variables
    answer = input(q2)
    if answer.lower() == "a":
        quizd = quizd + 1
    elif answer.lower() == "b":
        quize = quize + 1
    elif answer.lower() == "c":
        quizf = quizf + 1
    elif answer.lower() == "d":
        quizg = quizg + 1
    else:
        print("Sorry, I don't understand that answer.")
        question2(q2)

#define question block for the second part of the quiz 
if quiza > quizb and quiza > quizc:
    a=b1
    q2 =["\n5) You come across a mighty Stag, that in a deep voice proclaims himself King of the Woods. He has been caught in a bear trap by his hind leg. \na) I tell him I will help him, but only if he gives me the title of King. If he doesn't, helping him serves no purpose. \nb) I free him, but only so I can challenge him fairly for the title of King. When he is ready we will face each other in combat.\nc) I free him, tending to his wounds as he rests. When he wakes again I will ask him for his blessing, as I travel through his woods.\nd) I free him, then work with him, dismantling any other traps and finding and stopping those who have been placing them.\n",
         "\n6) In the ancient ruins of a forgotten city, you have followed rumours of a rare and mystical flower, that flowers once every hundred moons. You think it rests high atop a crooked tower. \na) I find a way to the top of the tower, taking the flower and keeping it for myself, owning its rare qualities.  \nb) I climb the tower, reaching the top on my own strength, and take any part of the flower that I might need. \nc) Carefully reaching the top, I will collect the pollen of the flower, hoping to find other places to grow and nurture it. \nd) I stabilize the tower, driving away any pests so that the flower can continue blooming and grant this world its beauty. \n",
         "\n7) As you cross a bridge, a big booming voice yells out that crossing the bridge requires a price. You see a Troll peeking out from beneath. \na) I inform the lurking troll that you are a tax collector from the troll king, and that if he does not give me half of everything he has, I will be forced to slay him.  \nb) I yell out in return, challenging the troll to hand to hand combat. If he wins, I will pay, but if I win, then all will cross for free. \nc) I bring him a feast of fruits, and try and convince him to move deeper into the forest, where food is plentiful and he won't come into conflict with any travellers.\nd) I ask him to leave, and if he does not, I will work with the local village to either force him out, or build another bridge. \n ",
         "\n8) You come across a tree that has Golden fruits, shining in the setting sun.\na) I will take as many fruit as I can, then chop the tree down, so that noone else may have them \nb) I sit beneath the tree, feasting on it's rich fruits. I will stay here as long as I want, and noone can stop me. \nc) I take some of the fallen fruit, then thank the tree, getting back on my way. \nd) I stop a while, gathering fruit so that the others I'm travelling with can share in its deliciousness. \n",
         "\n9) After helping an Elder King cure a blighted grove, he brings you to this ancient cavern, and tells you that you may take any axe that they have taken from trespassers in his land. \na) I take a long and nasty looking scythe-like axe, its blade kept ever sharp, even after years of dis-use. \nb) I take the largest axe I can find, its haft made from a long and ancient bone, chiselled with runes, the heft of it belaying its mighty power. \nc) I take an axe with a simple head, but the haft looks like it was naturally grown into shape and coaxed into being. It feels alive, and is blessed by the trees. \nd) I take an axe with an old, wooden haft, but with a head made of pure amber. It glimmers and almost glows in the light, and whoever made it was a highly devoted artisan. \n"]
    for i in q2:
        question2(i)
elif quizb > quiza and quizb > quizc:
     a=b2
     q2 =["\n5) A wildfire erupts, burning furiously, threatening to engulf a village. What will you do? \na) I will run out and warn the wildlife around, seeking some guardians of the forest to help thwart the blaze. \nb) I will help co-ordinate the response, making a chain of water carriers from the river to the blaze and making sure the young have evacuated. \nc) Flying into action, I divert the river further upstream so that it flows into the blaze and quenches it. The ground might be waterlogged for a while but this is the most effective plan of action.\nd) I watch in awe of the out of control blaze, but I will dive in and risk myself to rescue those in its path.\n",
         "\n6) A two-headed Giant blocks a cliffside pass, preventing wagons making their way to the city. \na) Shifting the plant growth atop the cliff, I cause rocks to tumble down, forcing the giant away. \nb) I work with the wagon owners, protecting them from the giant as the make their way past.\nc) Studying it from a distance, I enact a plan to quickly blind the giant, then push it off the cliff.\nd) Stepping up to the large twin heads, you exclaim proudly that you are the son of a dragon, and shoot plumes of flame out to scare it into leaving. \n",
         "\n7) In the middle of a quiet tavern, voices get heated and a fight breaks out. \na) In my drunken revelry, I join the fight, trading blows with all who come to brawl. \nb) I force my way to the middle, trying to break the scrap up before it starts. \nc) I will move to a table against the far wall, studying the different fighters to learn their moves and gain insight into their strength. \nd) Downing my drink, I jump into the fray, ducking and diving, sending people sprawling with sharp jabs. \n",
         "\n8) Finding yourself outside a manor on a stormy night, the lord of the house invites you to stay, but only in the stables behind the house. \na) Thanking him, I settle in with the horses, gathering with them for warmth. \nb) I thank him for his generosity, and find the cleanest part of the stables to rest in. \nc) I thank him, but spend the evening studying the lights in the house, then coaxing the lock I make my way into the wine cellar for the night. \nd) I yawn theatrically, and after he goes to bed, I find a window to force open and find the comfiest seat in his drawing room, falling asleep in front of the fire. \n",
         "\n9) A sword sits embedded in a ancient oak throne, and upon it is etched the inscription “Whomever is fit and noble shall hath this sword to hold aloft.” \na) I will channel the power of the sword into the throne without removing it, reviving the throne into a huge and lofty oak. \nb) Praying for the blessings of my deity, I will try to channel the purity of my soul to wrest it out, so I may use it for good. \nc) I will check the oak throne for runes or inscriptions, then attempt to carve out the wood around the blade so that I may take the sword. \nd) I set the throne alight, and spend hours watching it burn down to embers, than take the sword from the ashes, the blade still glowing with heat. \n"]
     for i in q2:
        question2(i)
elif quizc > quiza and quizc > quizb:
    a=b3
    q2 =["\n5) A sudden storm threatens to overturn your ship, and the squall forces it towards the jagged rocks. \na) Knowing little about sailing but a lot about fulcrums, I fashion a lever that will force the sail into a position that will guide our ship away. \nb) Cursing the names of several dead sea gods, I shout sailors into position, ready to steer it away from harm. \nc) I climb into the crow's nest, and seeing the dangers from there, I call orders down, guiding those below me to safety. \nd) With a keen eye I watch the flows and currents, and struggle with the rudder to beat the ship back onto course.\n",
         "\n6) You strike a deal with an overconfident Fae known locally as the Blindling. For a barrelful of gold coin, you must battle him in a test of wits, and find his true name three days hence, or your sight will be forfeit. \na) I browse through local tomes of Fae history, and finding legends of a blind fae, I inscribe its true name in the meeting place as preparation. \nb) I seek out other Fae, and swap songs and tales with them for three days, before strolling confidently to the meeting place. \nc) I follow him everywhere, lurking in the darkness, and listen to his celebrations that he makes three days too soon. I know his name now, and I will be waiting. \nd) Confiding with local animals and plants, I hear their tales of woe at the hands of this trickster. When it is time to meet, I body slam him, holding him against the earth and whispering his name into his ear.\n",
         "\n7) After drinking for several days straight, you wake up in a strange laboratory, lying on a steel table. \na) I find certain chemicals, mixing them together to make a cure for my hangover. Having fixed that, I will look for a book to read while I wait for the owner of the premise to return. \nb) Patting myself down, making sure all of my organs were where I left them, I rescue a flask from my sock and take a swig, then find a window to sneak out of. \nc) Cursing myself for being so sloppy, I check out my surroundings so that when my abductor finally returns, I will have the upper hand. \nd) Waking up with a raging headache, confused where I am, I clear the shelves out searching for alcohol and finding none, I kick the door down and leave. \n",
         "\n8) A famous old Mage invites you into his tower for an evening of drinking. You sit inside a room full of ancient books and fizzling jars. \na) I drink with him, but keep myself sober, curious of the unknown knowledge that is gathered and resides in this room. \nb) I drink heartily into the night, challenging the mage to tales of bravery and riddles. \nc) I drink reservedly, carefully weighing the costs of the artifacts in the room against the price of the Mage's ire. \nd) I drink his sweet-smelling liquor, sitting as still as possible as to not destroy my surroundings through clumsiness. \n",
         "\n9) A master smith has promised you a master weapon, crafted and waiting for you upon your return. What do you hope is waiting? \na) A fine and delicate rifle, with a precision hammer and a long and accurate barrel. \nb) A light and balanced dagger, etched with golden flames and faerie wings. \nc) A dull looking but extremely sharp curved blade, that slices through the air with no sound. \nd) A large and heavy warhammer, weighted to deal a brutal blow against any in it's way. \n"]
    for i in q2:
        question2(i)
elif quiza == quizb:
    a=b4
    q2 =["\n5) In the middle of a stricken village, the main well's water source seems to be poisoned. What would be the best way to solve this?  \na) I climb down into the well myself, fighting my way upstream until I can find the cause. \nb) I travel outside the village, looking for taint in the surrounding wildlife that can guide me towards the problem. \nc) I work with the villagers, caring for the sick and making preparations for a new water source to be found. \nd) I consult the village elders, taking samples of the water to identify how best to cleanse it. \n",
         "\n6) A travelling circus rolls into town with a large and foreign animal in tow. It looks starved, and one of its gargantuan limbs seems to be limping. \na) I bust my way into where the beast is being kept, breaking its chains and riding it to freedom. \nb) I try to communicate with it, to see if I can solve its problems. I will try to buy it's release from captivity. \nc) I offer my assistance to it's owners, buying it plenty of feed and nursing it back to strength, working to heal it's limb. \nd) I take a while studying it, making notes of its anatomy and its weak limb. Before the circus leaves town I will construct a device that will strengthen it's leg and alleviate it's pain. \n",
         "\n7) You come across an angry mob holding torches, who have cornered a lone wolf inside a barn. \na) I will push past them, and go in myself, to drive it away or defeat it. \nb) I urge them to part, to let it dart of into the night and never return. \nc) I will join them, helping them form a plan to capture the beast. \nd) Having previous experience in such matters, I will help to construct a trap, so that no-one will have to face it. \n",
         "\n8) On board this ship you have been travelling on, a voice cries out as they pull in the Nets. A Mermaid has found herself tangled in it. \na) I dive in, knife between my teeth, and grabbing the net, I cut her free. \nb) I plead with the captain, asking him to set her free, lest we incur the wrath of her people. \nc) I step forward, and helping them bring the net aboard, I will vouch for her safety as long as she's aboard this ship. \nd) My interest gets the better of me, and I make sure to be there to help communicate with her and learn from her. \n",
         "\n9) You find a Grim Gargoyle, thought to be the last of its kind. It is large, and dangerous. \na) I will fight it for the surge of adrenaline, and in vanquishing it I will take its tusks as a trophy. \nb) I will work with the inhabitants around these lands, avoiding conflict if possible and if not, I will help them drive it out. \nc) Helping the locals, I will form a party of soldiers to end it, and end any harm it may cause in the future. \nd) Skilled in fighting large beasts, I will spend days seeking its weaknesses, then end it in one foul swoop, taking its head in order to collect any bounty upon it. \n"]
    for i in q2:
        question2(i)
elif quiza== quizc:
    a=b5
    q2 =["\n5) You find yourselves lost, deep under the earth. Your group has run out of rations and light. How do you get out? \na) Calling forward a long and flickering flame, I walk pointedly so that I can make my choices in direction instinctively. \nb) My eyes adjusted to the shadow, I will scout ahead, finding likely paths to take and coming back to the group to tell them. \nc) Feeling claustrophobic, I bluster forward, listening out for sounds of life that could guide us to safety. \nd) Listening to the stones around me, I can feel in my bones where the walls run deep and where they grow hollow, and I will use this to guide us to safety. \n",
         "\n6) You find yourself at an old friend's wake. She lies there, deceased on the table. What kind of stories of her bravery will you tell? \na) She was the bravest, fairest lass that e'er walked the earth, she charmed the gods themselves and broke the hearts of many a Lord. She once took a Milk tooth from a Untertroll willingly, and the beast wept hot tears when she left, skipping into the dawn. \nb) She was strong, and committed. One time we had a package to deliver, but there were patrols on every route. She ended up climbing a sheer cliff face, the package strapped to her back, and delivered the package, promptly, right before passing out from exhaustion. \nc) She was fierce, and ruthless, and when a stampeding herd of Crowndeer was crashing towards a village, she stood out there, right in front of the biggest one, grabbed it by the antlers and wrestled it to the ground. The rest of the herd stopped dead out of sheer fright. \nd) She was a kind and faithful friend. When a Gryphawk hatchling fell out of its nest and down the side of the mountain, breaking its wing and too weak to call out, she came to it and fed it daily. Although it grew bigger than her in a matter of weeks, she still tended to it, fastening a splint to it's broken wing. Even after it could fly and hunt, they shared a bond that would see them as friends whenever they met again. \n",
         "\n7) You are on the run, after stealing a Tidegull egg from a rare Aviarian store. Why did you take it? \na) Because it would make a grand tale, to take it back to Tidegulls roost and watch it hatch. \nb) Because it's worth a lot of money, and calls for a sizeable ransom, even if I don't intend to return it. \nc) Because It's not natural, Eggs being snatched from nests, the chick inside deserves to know true freedom. \nd) Because the Tidegull lives in a briny habitat, flush with sea air and fish to catch. It would be better for the Gull inside to learn and grow somewhere that suits it's nature. \n",
         "\n8) A carnivorous thistleholly has been lashing out a locals and overtaking forest paths with voracious growth. \na) I'll venture out and burn it back, so that the villagers will be grateful, and I'll have an exciting time facing it. \nb) I'll sort it out, for a price. They say if you're good at something, never do it for free. \nc) I'll fight it back, not just for the villagers, but for the forest creatures that have been suffering from its overgrowth. \nd) I'll attempt to commune with it, to find out what has been twisting its nature so viciously, in hopes of restoring a peaceful order.  \n",
         "\n9) A revenant stands before you, a shambling, animated corpse that tells you that you are descended from Kings. \na) I laugh, because I never believed the tales my grandmother told me, but it's a fortunate yarn that's spun from the truth. \nb) I regard it with suspicion, because whatever joy that power brought my ancestors left us generations ago. This corpse just brings shackles disguised as a crown. \nc) I beat my chest with agreement. Of course, I am, for from whom but the mightiest can my strength come from? \nd) I shake my head. I have no need for a title, for I am tied to my own fate, bound to walk my own path. \n"]
    for i in q2:
         question2(i)
elif quizb == quizc:
    a=b6
    q2 =["\n5) You're walking through a market when you see a stall owner being shaken down for cash by two large thugs. What do you do? \na) Alert the guard, and having saved the stall owner, accept his thanks and leave. \nb) Alert the guard, and while the commotion is going on, rifle through the stall for any antique books. \nc) In a display of brashness and ferocity scare the thugs off, and having saved the Stall owner, accept his thanks in coin. \nd) While the thugs are shaking him down, cut the thugs purses off their belts, then alert the guard. \n",
         "\n6) Tales tell of some great beast breaking into the old chapel at night, ransacking the place before leaving nothing but tracks. \na) Gather together a group to hold watch, in hopes that you can catch whatever is doing this. \nb) Read up extensively on what could be doing this, then follow the tracks after dawn back to it's den. \nc) Fetch a chair and sit outside the door the whole night, ready to face whatever has been breaking in. \nd) Before the monster comes, I search the church for anything valuable, taking it then hiding in the shadows, ready to watch whatever has been breaking in, and then follow it home. \n",
         "\n7) Five men walk into the quayside tavern, telling tales of monsters capsizing fishing boats and lost colleagues. \na) Make sure they're not hurt, then assemble a search team in the morning. \nb) Listen carefully to their story, searching your memories for what kind of beast could have done this. \nc) Listen carefully to their tales, committing them to mind to be retold at a later date, buying them all a round of ale and drinking deep into the night with them. \nd) Watch them carefully and slip out after them, following them in case they've abandoned their fellow sailors and they return to the wreck. \n",
         "\n8) A large black raven settles on your windowsill, and calls your name. As you think you might have dreamed it, it calls your name again and flutters away. \na) I get up and close the window. Such dark portents should be avoided at all costs. \nb) I fetch a spyglass and look for it. Perhaps it has a message tied to its leg, meant for my eyes alone. \nc) I go to the window and sing an old song from my village, in hopes that the lyrical waxing will coax this curious creature back. \nd) Understanding it's message, I grab my cloak and leave through a back door, making sure to steer clear of prying eyes. \n",
         "\n9) A vast and ghastly creature of darkness chases you, and corners you in a dark alleyway. \na) Chanting words of spiritual protection, I fend it off, with a wall of radiant light. \nb) I tap the runes in the stonework I carefully drew into it two nights back. The creature has taken the bait, and now to spring the trap. \nc) Away from the eyes of the law and innocent bystanders, I crack my knuckles, flames burning in my eyes. \nd) I look for another way out, a balcony higher up than its reach or a sewer I can dive into to escape it. \n"]
    for i in q2:
        question2(i)
else:
    print("\nERRORR!!")




if quizd > quize and quizd>quizf and quizd>quizg:   #answers A
     print("\nYour colour is "+a[0]+"!")
elif quize > quizd and quize>quizf and quize>quizg: #answers B
    print("\nYour colour is "+a[1]+"!")
elif quizf > quize and quizf>quizd and quizf>quizg: #answers C
    print("\nYour colour is "+a[2]+"!")
elif quizg > quize and quizg>quizf and quizg>quizd: #answers D
    print("\nYour colour is "+a[3]+"!")
elif quizd == quize:                                #answers AB    
    print("\nYou may choose between "+a[0]+", and "+a[1]+"!")
elif quizd == quizf:                                #answers AC
    print("\nYou may choose between "+a[0]+", and "+a[2]+"!")
elif quizd == quizg:                                #answers AD
    print("\nYou may choose between "+a[0]+", and "+a[3]+"!")
elif quize == quizf:                                #answers BC
    print("\nYou may choose between "+a[1]+", and "+a[2]+"!")
elif quize == quizg:                                #answers BD
    print("\nYou may choose between "+a[1]+", and "+a[3]+"!")
elif quizf == quizg:                                #answers CD
    print("\nYou may choose between "+a[2]+", and "+a[3]+"!")
else:
    print("\nGRIEVIOUS ERROR")


