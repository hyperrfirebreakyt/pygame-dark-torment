#ISSA
#Ryan Wong, Aakar Panth, Amari Sealy
#Dark Torment
#


from gamelib import*

game = Game(1422,800,"Dark Torment")
bk = Image("image\\bk.png",game)
game.setBackground(bk)
bandage = Image("image\\bandage.png",game)
bandage.moveTo(70,730)
bandage.resizeBy(-80)
ammobox = Image("image\\ammo box.png",game)
ammobox.moveTo(550,730)
ammobox.resizeBy(-30)
shield = Image("image\\shield.png",game)
shield.resizeBy(-60)
shield.moveTo(100,650)
man = Image("image\\man.png",game)
man.moveTo(200,670)
man.resizeBy(-40)
title = Image("image\\start.png",game) 
title.moveTo(750,600)
title.resizeBy(-20)
bk2= Image("image\\jungle.png",game)
zombies = Image("image\\zombies.png",game)
howtoplay = Image("image\\howtoplay.png",game)
howtoplay.moveTo(200,700)
boss1 = Image("image\\boss1.png",game)
boss2 = Image("image\\boss2.png",game)
gun = Sound("image\\gun.wav",1)

zombies = []
for index in range(10):
    zombies.append(Animation("image\\zombies.png",1,game,1000,1407))
for index in range(10):
    x = randint(1000,1900)
    y = randint(670,670)
    s = randint(1,2)
    zombies[index].moveTo(x,y)
    zombies[index].setSpeed(-s,-90)
    zombies[index].resizeBy(-80)
    
ammo = []
for index in range(1):
    ammo.append(Animation("image\\ammo.png",4,game,200,200))
    
for index in range(1):
    x = randint(100,200)
    y = randint(100,200)
    ammo[index].moveTo(x,-y)
    ammo[index].setSpeed(-8,90)
    ammo[index].resizeBy(-70)
    
bullet = Animation("image\\bullet.png",1,game,400,400)
bullet.visible = False
bullet.resizeBy(-90)
zombie = Animation("image\\zombies.png",1,game,1000,1407)
zombie.visible = False


    
    
#title screen
while not game.over:
    game.processInput()
    bk.draw()
    title.draw()
    howtoplay.draw()
    if title.collidedWith(mouse) and mouse.LeftClick:
        game.over = True

        
    game.update(60)

game.over = False

#Level 1
while not game.over:
    game.processInput()
    game.scrollBackground("left",2)
    bk2.draw()
    man.draw()
    shield.draw()
    ammobox.draw()
    bandage.draw()
    bullet.move()
    
    game.drawText("Ammo: " + str(man.ammo),bk2.x-100,bk2.y-390)
    game.drawText("Health: " + str(man.health),bk2.x-700,bk2.y-390)
    for index in range(10):
        zombies[index].move()
        if zombies[index].collidedWith(man):
            man.health -= 1
    
    if man.collidedWith(ammobox):
        man.ammo += 30
    if man.collidedWith(ammobox) and man.ammo >99:
        man.ammo -= 0
        ammobox.visible = False
    if man.collidedWith(bandage) and man.health <2:
        man.health += 20
    if man.collidedWith(bandage) and man.health >99:
        man.health += 0

    if man.collidedWith(shield):
        shield.visible = False
        man.health += 100
    
    for index in range(10):
        if zombies[index].collidedWith(bullet):
            zombies[index].damage += 25
        if zombies[index].damage >100:
            zombies[index].visible = False
    
    if keys.Pressed[K_RIGHT]:
        man.x += 4
    if keys.Pressed[K_LEFT]:
        man.x -= 4
    
    if keys.Pressed[K_SPACE]:
        bullet.moveTo(man.x, man.y)
        bullet.setSpeed(8,-90)
        bullet.visible = True
        man.ammo -= 1
        gun.play()
  
    if man.health <1:
        game.over= True
    

    if bk2.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    
    game.update(60)

boss1 = []
for index in range(4):
    boss1.append(Image("image\\boss1.png",game))
for index in range(4):
    x = randint(1000,1900)
    y = randint(670,670)
    boss1[index].moveTo(x,y)
    boss1[index].setSpeed(-0.5,-90)
    boss1[index].resizeBy(-30)

ammo = []
for index in range(1):
    ammo.append(Animation("image\\ammo.png",4,game,200,200))
    
for index in range(1):
    x = randint(100,200)
    y = randint(100,200)
    ammo[index].moveTo(x,-y)
    ammo[index].setSpeed(-8,90)
    ammo[index].resizeBy(-70)
    
bullet = Animation("image\\bullet.png",1,game,400,400)
bullet.visible = False
bullet.resizeBy(-90)
#Level 2
game.over =  False
while not game.over and man.health > 1:
    game.processInput()
    game.scrollBackground("left",2)
    bk2.draw()
    
    #boss2.draw()
    ammobox.draw()
    bandage.draw()
    man.draw()
    game.drawText("Ammo: " + str(man.ammo),bk2.x-100,bk2.y-390)
    game.drawText("Health: " + str(man.health),bk2.x-700,bk2.y-390)
    for index in range(4):
        boss1[index].move()
        if boss1[index].collidedWith(man):
            man.health -= 60

    
    if man.collidedWith(ammobox):
        man.ammo += 30
    if man.collidedWith(ammobox) and man.ammo >99:
        man.ammo -= 0
        ammobox.visible = False
    if man.collidedWith(bandage) and man.health <2:
        man.health += 20
    if man.collidedWith(bandage) and man.health >99:
        man.health += 0

    if man.collidedWith(shield):
        shield.visible = False
        man.health += 100
    
    for index in range(10):
        if zombies[index].collidedWith(bullet):
            zombies[index].damage += 25
        if zombies[index].damage >100:
            zombies[index].visible = False
    
    if keys.Pressed[K_RIGHT]:
        man.x += 4
    if keys.Pressed[K_LEFT]:
        man.x -= 4
    
    if keys.Pressed[K_SPACE]:
        bullet.moveTo(man.x, man.y)
        bullet.setSpeed(8,-90)
        bullet.visible = True
        man.ammo -= 1
        gun.play()
  
    if man.health <1:
        game.over= True
    

    if bk2.collidedWith(mouse) and mouse.LeftClick:
        game.over = True

        
    game.update(60)
game.quit()
