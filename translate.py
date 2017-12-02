from googletrans import Translator
translator = Translator()


story = \
"""
Mijn dagpatroon.
Ik ben op mijn werk.
Het is avond.
Ik ga naar huis.
Ik pak mijn sleutels.
Ik doe mijn kamer op slot.
Ik ga naar de lift.
Ik druk op de knop.
Ik ga naar beneden.
Ik ga naar mijn fiets.
Ik ga op mijn fiets zitten.
Ik fiets naar huis.
Ik kom thuis.
Ik doe de deur open.
Ik ga naar binnen.
Ik doe mijn jas uit.
Ik hang mijn jas op.
Ik doe mijn schoenen uit.
Ik trek pantoffels aan.
Ik ga naar de w.c.
Ik ga naar de woonkamer.
Ik ga zitten op de bank.
Ik pak de krant.
Ik lees de krant.
Ik drink wijn.
Ik heb honger.
Ik ga naar de keuken.
Ik maak eten.
Ik pak een bord.
Ik pak een mes.
Ik pak een vork.
Ik pak een lepel.
Ik pak een glas.
Ik ga naar de tafel.
Ik zit op een stoel.
Ik eet.
Ik heb dorst.
Ik drink water.
Ik eet een desert.
Ik ben klaar.
Ik heb geen honger meer.
Ik breng mijn bord naar de keuken.
Ik was mijn bord af.
Ik droog mijn bord af.
Ik ruim mijn bord op.
Ik ruim mijn mes op.
Ik ruim mijn vork op.
Ik ruim mijn lepel op.
Ik ruim mijn glas op.
Ik doe de televisie aan.
Ik kijk televisie.
Het is heel saai.
Ik doe de televisie uit.
Ik zet thee.
Ik pak een glas.
Ik schenk thee in.
Ik drink thee.
Ik lees een boek.
Ik ben moe.
Ik ben moe geworden.
Ik ben moe geworden van de hele dag.
Ik ben moe geworden van alles wat ik heb gedaan vandaag.
Ik wil nu slapen.
Ik ga naar mijn slaapkamer.
Ik poets mijn tanden.
Ik ga onder de douche.
Ik droog me af.
Ik trek mijn pyjama aan.
Ik ga naar bed.
Ik ga in bed liggen.
Ik ga onder de dekens liggen.
Ik leg mijn hoofd neer.
Ik leg mijn hoofd op het kussen.
Ik doe het licht uit.
Ik kan niet slapen.
Nu val ik in slaap.
Ik slaap.
Ik droom.
De wekker gaat af.
Ik word weer wakker.
Het is 7 uur.
Het is ochtend.
Het is 7 uur in de ochtend.
Ik doe de wekker uit.
Ik sta op.
Ik sta op uit bed.
Ik ga naar de badkamer.
Ik was me.
Ik poets mijn tanden.
Ik kam mijn haren.
Ik ga weer naar mijn slaapkamer.
Ik trek mijn pyjama uit.
Ik trek mijn broek aan.
Ik trek mijn trui aan.
Ik trek mijn sokken aan.
Ik ga naar beneden.
Ik maak koffie.
Ik fiets naar mijn werk.
"""

fp = open("my_daily_pattern.tex", "w")

for line in story.split("\n"):
    #print(line)
    line = line.strip()
    if len(line) < 3:
        continue
    tr = translator.translate(line, src="nl", dest="tr")
    en = translator.translate(line, src="nl", dest="en")
    res = "{}&\n{}&\n{}\\\\\n".format(line, en.text, tr.text)
    print(res)
    #fp.write(res)
