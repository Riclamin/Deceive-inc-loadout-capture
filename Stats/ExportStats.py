import os

def AceStats():
    w1 = "dmg = regular/charged: HS 60/75; HS&Vul 75/94; BS 30/38; BS&Vul 38/48"
    w2 = "dmg = regular/charged: HS 45/57; HS&Vul 57/72; BS 23/29; BS&Vul 29/37"
    w3 = "dmg = regular/charged: HS 45/57; HS&Vul 102/128; BS 45/57; BS&Vul 57/72"
    e1 = "Trace the last scoped target or shot enemy for 25s. Also shows a path to them. cd: 20s"
    e2 = "Make the last scoped target or shot enemy vulnerable for 25s increasing dmg by 30%. cd: 20s"
    e3 = "Place a zone that reveals everyone (incl npcs) that remains until cancelled by ace. cd: 5s"
    p1 = "A charged shot also slows the target by 40% for 20s"
    p2 = "A charged shot also neutralises the target for 20s"
    p3 = "A charged shot also exposes the target for 20s"
    return ','.join(['Ace',w1,w2,w3,e1,e2,e3,p1,p2,p3])+ '\n'

def CavaliereStats():
    w1 = "HS 15; BS 11"
    w2 = "HS 40; BS 20"
    w3 = "HS 14; BS 10"
    e1 = "Analyse nearby objects that enemies interacted with to trace them for 6/9/12 seconds."
    e2 = "Place a zone that traps all electronic devices. When an enemy interacts with one; trace them for 12 seconds."
    e3 = "Analyse eliminated players or knocked down npcs or holocrumbs. Trace the enemy responsible for 12 seconds."
    p1 = "A charged melee also makes you dash forward for xm."
    p2 = "A charged melee also grants you amped up"
    p3 = "A charged melee also slows your target for 40%."
    return ','.join(['Cavaliere',w1,w2,w3,e1,e2,e3,p1,p2,p3])+ '\n'

def ChavezStats():
    w1 = "HS 50; BS 25"
    w2 = "HS 45; BS 23"
    w3 = "HS 70; BS 35"
    e1 = "You are immune to damage for 7 seconds. min cd: 17.5s; max cd: 40s"
    e2 = "Place down a zone that grants the resistant buff to you and your allies for 15s. cd = 40s"
    e3 = "You are immune to damage for 3.5s. Reflect all dmg done to you afterwards. cd = 40s"
    p1 = "Chavez turns a portion of the damage he takes into grey health. He regenerates this health over time."
    p2 = "Chavez can overheal. All overhealth is temporary and drains after a few seconds."
    p3 = "Chavez turns a portion of the damage he takes into grey health. Dealing damage to rivals heals part of the grey health based on the damage dealth."
    return ','.join(['Chavez',w1,w2,w3,e1,e2,e3,p1,p2,p3])+ '\n'

def HansStats():
    w1 = "M1 (Shotgun): 45; M2 (ADS): HS 50; BS 25"
    w2 = "M1 (Shotgun): 30; M2 (ADS): HS 35; BS 20"
    w3 = "M1 (Shotgun): 45; M2 (ADS): HS 53; BS 30"
    e1 = "Hans shoots an orb that neutralizes and slows enemies by 40% for 4.5s. cd = 40s"
    e2 = "Hans instantly creates a zone around him. Rivals entering or eleaving the zone get neutralized and slowed by 40% for 7.5s. cd = 40s"
    e3 = "Hans shoots a spark that spreads to nearby targets until it can't find more targets or has spread too many times. The spark neutralizes and slows rivals by 40% for 4.5s. cd = 40s"
    p1 = "Hans projects a wave when he breaks his own cover. Enemies caught in the wave get their cover blown and are slowed by 40%."
    p2 = "Hans' Rivals project a wave when Hans breaks their cover. Enemies caught in the wave get their cover blown and are slowed by 40%."
    p3 = "Hans gets a portion of his expertise cd back when he hits rivals with his expertise."
    return ','.join(['Hans',w1,w2,w3,e1,e2,e3,p1,p2,p3])+ '\n'

def LarcinStats():
    w1 = "HS 13; BS 10; Throw HS 20; Throw BS 10"
    w2 = "HS 15; BS 10; Throw HS 17; Throw BS 9"
    w3 = "HS 20; BS 15; Throw HS 60; Throw BS 30"
    e1 = "You become invisible and immune for 5s. min cd = 22s; max cd = 60s."
    e2 = "You create a zone for 10s where you and your allies become invisible. cd = 60s."
    e3 = "You become invisible and immune and gain amped up for 8s but also leave a trail. min cd=17.5s; max cd = 60s"
    p1 = "When you melee an enemy spy you will steal their most valuable tier asset. Will steal the package if the enemy has it. Can steal intel if they don't have items."
    p2 = "Whenever Larcin blows the cover of an enemy they will drop their higest value item (excep the package)."
    p3 = "When in cover, Larcin's melee attacks steal items from rivals; melee attacks don't deal damage; gains heat from melee attacks on npcs; melee attacks don't break cover. Larcin will prioritise stealing the package and will steal intel if the rival doesn't have items.   "
    return ','.join(['Larcin',w1,w2,w3,e1,e2,e3,p1,p2,p3])+ '\n'

def MadameXiuStats():
    w1 = "HS 12; BS 9"
    w2 = "HS 15; BS 10"
    w3 = "HS 8; BS 6"
    e1 = "Teleport into another npc. You leave a clone wearing your current disguise behind. Teleporting into another player will place you next to them with their disguise broken. cd = 60s."
    e2 = "Mark an npc for 20s. Activate the expertise again to teleport into this npc. You leave a clone wearing your current disguise behind. Teleporting into another player will place you next to them with their disguise broken. min cd = 12s; max cd = 60s."
    e3 = "You can teleport 3 times in short succession into another npc. You leave a clone wearing your current disguise behind. Teleporting into another player will place you next to them with their disguise broken. cd = 60s."
    p1 = "You know when a player within xm loses their cover. A mark will be visible for a short while at the location where this happened."
    p2 = "You can see players under x% hp within xm through walls."
    p3 = "Every time a terminal is hacked; the phase changes or the extraction vehicle is moved; you see a snapshot of all enemies alive."
    return ','.join(['Madame Xiu',w1,w2,w3,e1,e2,e3,p1,p2,p3])+ '\n'

def OctoStats():
    w1 = "HS 20 dmg; BS 10 dmg; ADS (costs 1 intel) 20dmg"
    w2 = "HS 7 dmg; BS 5 dmg; ADS spend 1/2/3/4/5 intel to deal 10/x/x/x/70 dmg"
    w3 = "HS x dmg; BS 6 dmg; ADS spend 3 intel to deal 34 dmg or 60 HS dmg"
    e1 = "Hack all intel in a cone in front of you and reactive all intel that has already been hacked. cd = y"
    e2 = "All electronic devices arouind you become syphon beacons. Drain intel from enemies within these beacons. When another player acquires intel within range of a beacon you get it as well. cd = y"
    e3 = "Drain intel from all enemy players in sight. An enemy without cover is also neutralised and exposed. cd = y"
    p1 = "Whenever you spend intel there is a chance for octo to gain it back. This chance becomes bigger the fewer intell you have compared to your max intel."
    p2 = "For every 10 intel obtained octo's max intel increases by 2."
    p3 = "Whenever octo obtains intel octo also reduces the cooldown of his expertise by 1s. There is a chance that the cooldown is instead fully reset."
    return ','.join(['Octo',w1,w2,w3,e1,e2,e3,p1,p2,p3])+ '\n'

def RedStats():
    w1 = "HS 11; BS 8"
    w2 = "HS 30; BS 20"
    w3 = "HS 40; BS 40"
    e1 = "Red charms rivals for 8s in a cone in front of her and red regains her cover. Charmed rivals that break their own cover become heartbroken. cd = 45s."
    e2 = "You and your allies heal 20 hp and regain cover. cd = 60s."
    e3 = "Place down a love bomb. Shooting the bomb denotates it; causing enemies within range to be slowed slowed for 40 % and become vulnerable for 30% for 8s. The bomb also automatically explodes aif out of cover rivals are in range. Red and her allies can interact with the bomb to regain cover."
    p1 = "Whenever you regain cover; you regain another cver of the same security tier. Also gain resistance for a short while."
    p2 = "Whenever an agent is killed nearby; you gain amped up and increased cover recovery speed until you regain your cover."
    p3 = "Trace rivals in a large radius arround red whenever they are being scolded by npcs or gain heat."
    return ','.join(['Red',w1,w2,w3,e1,e2,e3,p1,p2,p3])+ '\n'

def SasoriStats():
    w1 = "HS 32; BS 13; sword 40"
    w2 = "HS 16 per kunai (max 80); BS 8 per kunai (max 40); sword 30 (charged 60)"
    w3 = "HS 10; BS 7; dmg is increased by +/-6 for each debuff on the rival;  sword 15"
    e1 = "Apply poison to your weapon for xs. Poisoned spies cannot heal or use electronic devices. cd = ys"
    e2 = "Throw a vial to a location that leaves a poison cloud. Poisoned spies cannot heal or use electronic devices. cd = ys"
    e3 = "Drop a poisonous bomb that poisons and damages all enemy players nearby for 5dmg. Poisoned spies cannot heal or use electronic devices. cd = ys"
    p1 = "Poisoned enemies are also traced."
    p2 = "Your sword deals bonus damage to poisoned targets."
    p3 = "Poison lasts longer. Sasori recovers some expertise cd for every dmg dealt to a poisoned rival."
    return ','.join(['Sasori',w1,w2,w3,e1,e2,e3,p1,p2,p3])+ '\n'

def SquireStats():
    w1 = "HS 23; BS 17"
    w2 = "HS 12; BS 9"
    w3 = "HS 40; BS 20"
    e1 = "Mark all lootable objects in an area around you for 10s. cd = 20s."
    e2 = "You gain amped up for 6s as well as increased reload speed. min cd = 20s. max cd = 60s."
    e3 = "Create a zone around you for 15s. If an enemy spy is within your zone it'll change colour to red. cd = 20s."
    p1 = "Whenever Squire loses cover he becomes amped up. This ability will not trigger by fall damage. This ability will not trigger again until he regains his cover."
    p2 = "Whenever Squire loses cover by an enemy; they will be traced for ys."
    p3 = "Whenever squire loses cover he will keep the cover shield slightly longer. The cover shield also grants him damage reduction."
    return ','.join(['Squire',w1,w2,w3,e1,e2,e3,p1,p2,p3])+ '\n'

def YumiStats():
    w1 = "HS 51; BS 30"
    w2 = "Before Split: 48; After split: 45"
    w3 = "HS 102; BS 51"
    e1 = "Equip an emp pellet. This pellet will create a field that neutralizes and slows enemies by 40% for 12s at the point of impact. cd begins immediately after being shot. cd = 40s."
    e2 = "Equip a healing pellet. This pellet will create a healing field that heals Yu-mi and all allies for 10 seconds at 10hp/s. Healing is interrupted when taking damage. cd begins immediately after being shot. cd = 40s."
    e3 = "Equip 3 mini emp pellets. This pellet will create a mini field that neutralizes and slows enemies by 40% for 8s at the point of impact. Can be cancelled early and refunds 13s cd for each pellet not fired. cd = 40s."
    p1 = "Cooldown of gadgets is reduced by 65%."
    p2 = "Whenever Yu-Mi destroys a gadget; a portion of her expertise is refunded."
    p3 = "Whenever Yu-Mi destroys a gadget, a mini emp will detonate at that location."
    return ','.join(['Yu-Mi',w1,w2,w3,e1,e2,e3,p1,p2,p3]) + '\n'


localDirectory = os.getcwd()

Header = "Agent,w1,w2,w3,e1,e2,e3,p1,p2,p3\n"
Backup = "BACKUP_IN_CASE_OF_ERROR,x,x,x,x,x,x,x,x,x"
Lines = [Header,
         AceStats(),
         CavaliereStats(),
         ChavezStats(),
         HansStats(),
         LarcinStats(),
         MadameXiuStats(),
         OctoStats(),
         RedStats(),
         SasoriStats(),
         SquireStats(),
         YumiStats(),
         Backup]


with open(f'{localDirectory}\AgentLoadoutStats.csv', "w") as file:
    file.writelines(Lines)