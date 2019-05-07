#!/usr/bin/env python 
import pygame, sys, os, math
from random import randint
from pygame.locals import *
import time


class Window(object):
    win_width = 800
    win_height = 600
    half_win_width = win_width/2
    half_win_height = win_height/2
    def __init__(self):
        pass      

"game gobal variables"
clock = pygame.time.Clock()
screen = pygame.display.set_mode((Window.win_width,Window.win_height))
pygame.display.set_caption("rpg")
done = False

enemy_list = {}
#items_on_map = {}

snake_skin_image = pygame.image.load('/Users/lukevawter/Desktop/ActRPGImages/snake_skin.png')
cross_image = pygame.image.load('/Users/lukevawter/Desktop/ActRPGImages/cross.png')
cloth_image = pygame.image.load('/Users/lukevawter/Desktop/ActRPGImages/cloth.png')
potion_image = pygame.image.load('/Users/lukevawter/Desktop/ActRPGImages/potion.png')
RED = (255,   0,   0)
BLUE = (  0,   0, 255)
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
"end of game golobal variables"

#def draw_items():
    #for i in items_on_map:
        #screen.blit(pygame.image.load(items_on_map[i][0]+'.png'),(items_on_map[i][1], items_on_map[i][2]))


#DUNGEONS
class Dungeon(object):
    def __init__(self):
        self.tile_size = 50
        self.current_room = 11
        self.wall_list = {}
        self.block_list = {}
        self.master_wall_list = {}
        self.master_enemy_list = {}    
        self.items_on_map = {}
        self.item_count = 0
        
    def tile_fill(self):
        screen.blit(self.tile,(self.tileX,self.tileY))
        for x in range(self.tileX, self.tileX + 1000, 64):
            for y in range(self.tileY, self.tileY + 1000, 64):
                screen.blit(self.tile, (x, y))
        return x, y
        
    def wall_fill(self):
        #self.generate_walls(self)
        for key,val in self.master_wall_list.items():
            screen.blit(self.wall, val)
            
    def generate_walls(self):
        tileX = 0
        tileY = 0
        wall_count = 0
        for x in range(int(Window.win_width/2 / self.tile_size - 1)):   
            wall_count += 1
            self.wall_list.update({wall_count: [tileX, Window.win_height - self.tile_size]})
            wall_count += 1
            self.wall_list.update({wall_count: [tileX, 0]})
            tileX += self.tile_size
        tileX += self.tile_size * 2
        for x in range(int(Window.win_width/2 / self.tile_size - 1)):   
            wall_count += 1
            self.wall_list.update({wall_count: [tileX, Window.win_height - self.tile_size]})
            wall_count += 1
            self.wall_list.update({wall_count: [tileX, 0]})
            tileX += self.tile_size    
        for y in range(int(Window.win_height/2 / self.tile_size -1)):          
            wall_count += 1
            self.wall_list.update({wall_count: [Window.win_width - self.tile_size, tileY]})
            wall_count += 1
            self.wall_list.update({wall_count: [0, tileY]})
            tileY += self.tile_size
        tileY += self.tile_size * 2    
        for y in range(int(Window.win_height/2 / self.tile_size -1)):          
            wall_count += 1
            self.wall_list.update({wall_count: [Window.win_width - self.tile_size, tileY]})
            wall_count += 1
            self.wall_list.update({wall_count: [0, tileY]})
            tileY += self.tile_size
        self.generate_mwl()
        
            
    def generate_objects(self, level, room):
            self.blocks = self.OneOneblock_list
            for key,val in self.blocks.items():
                screen.blit(self.wall, val)
                
    def generate_mwl(self):
        self.master_wall_list.update(self.wall_list)
        self.master_wall_list.update(self.block_list)
    
    def draw_items(self):
        for i in self.items_on_map:
            screen.blit(pygame.image.load('/Users/lukevawter/Desktop/ActRPGImages/' + self.items_on_map[i][0]+'.png'),(self.items_on_map[i][1], self.items_on_map[i][2]))    
        
class Forest(Dungeon):
    def __init__(self):
        Dungeon.__init__(self)
        self.tile = pygame.image.load('/Users/lukevawter/Desktop/ActRPGImages/grass_tile.png')
        self.tileX = 0
        self.tileY = 0
        self.wall = pygame.image.load('/Users/lukevawter/Desktop/ActRPGImages/leaf_wall2.png') 
        self.block_list = {}   
        self.wall_list = {}
        self.master_wall_list = {}

class Desert(Dungeon):
      def __init__(self):
        Dungeon.__init__(self)
        self.tile = pygame.image.load('/Users/lukevawter/Desktop/ActRPGImages/desert_tile.png')
        self.tileX = 0
        self.tileY = 0
        self.wall = pygame.image.load('/Users/lukevawter/Desktop/ActRPGImages/rock_wallD2.png') 
        self.block_list = {}   
        self.wall_list = {}
        self.master_wall_list = {}
              
class OneOne(Forest):
    def __init__(self):
        Dungeon.__init__(self)
        Forest.__init__(self)
        self.block_list = {49:[0,250],50:[0,300],51:[350,0],52:[400,0],53:[400,250], 54:[350,250],\
        55:[400,300],56:[350,300]}
        self.master_wall_list = {}
 
class TwoOne(Forest):
     def __init__(self):
        Dungeon.__init__(self)
        Forest.__init__(self)
        self.block_list = {49:[750,250],50:[750,300],53:[400,250], 54:[350,250],\
        55:[400,300],56:[350,300],57:[350,0],58:[400,0]}
        self.master_wall_list = {}   
        #51:[350,550],52:[400,550],
class OneTwo(Forest):
     def __init__(self):
        Dungeon.__init__(self)
        Forest.__init__(self)
        self.block_list = {51:[350,550],52:[400,550],53:[400,250], 54:[350,250],\
        55:[400,300],56:[350,300],57:[0,250],58:[0,300]}
        self.master_wall_list = {}
        #49:[750,250],50:[750,300],
class TwoTwo(Desert):
     def __init__(self):
        Dungeon.__init__(self)
        Desert.__init__(self)
        self.block_list = {}
        self.master_wall_list = {} 
        #49:[750,250],50:[750,300],51:[350,550],52:[400,550]
class TwoThree(Desert):
     def __init__(self):
        Dungeon.__init__(self)
        Desert.__init__(self)
        self.block_list = {49:[750,250],50:[750,300],51:[350,550],52:[400,550]}
        self.master_wall_list = {} 
class ThreeTwo(Desert):
     def __init__(self):
        Dungeon.__init__(self)
        Desert.__init__(self)
        self.block_list = {49:[750,250],50:[750,300],51:[350,550],52:[400,550]}
        self.master_wall_list = {}
class ThreeThree(Desert):
     def __init__(self):
        Dungeon.__init__(self)
        Desert.__init__(self)
        self.block_list = {49:[750,250],50:[750,300],51:[350,550],52:[400,550]}
        self.master_wall_list = {}
#end DUNGEONS   

#CHARACTER
class Character(object):
    direction = 'down'
    def __init__(self): 
        self.pframe = ""
        self.playerX = 1
        self.playerY = 1
        self.health = 1
        self.health_max = 1
        #self.direction =  'down'
        self.frame = 0
        self.wall_hit = False
        
    def animate(self):
        if self.frame > len(self.frame_set) -1:
            self.frame = 0
        pframe = pygame.image.load(self.frame_set[self.frame])
        self.frame = (self.frame + 1) % len(self.frame_set)
        return pframe
        return frame
        
    def move(self, direction):
        if direction == 'down':
            self.frame_set = self.imagesD
            self.playerY += self.speed
            self.pframe = self.animate()
            self.direction = 'down'
            return self.frame_set
            return self.playerY
            return self.direction
        if direction == 'up':
            self.frame_set = self.imagesU
            self.playerY -= self.speed
            self.pframe = self.animate()
            self.direction = 'up'
            return self.frame_set
            return self.playerY
            return self.direction
        if direction == 'right':
            self.frame_set = self.imagesR
            self.playerX += self.speed
            self.pframe = self.animate()
            self.direction = 'right'
            return self.frame_set
            return self.playerX
            return self.direction
        if direction == 'left':
            self.frame_set = self.imagesL
            self.playerX -= self.speed
            self.pframe = self.animate()
            self.direction = 'left'
            return self.frame_set
            return self.playerX
            return self.direction
        for i in enemy_list:
            if self.id == i:
                enemy_list[i] = [self.playerX, self.playerY]
        return enemy_list
        
    def wall_check(self, dungeon):
        mwl = dungeon.master_wall_list
        for i in mwl:
            if self.direction == 'down':
                if mwl[i][1] -9 - self.playerY <= 40 and \
                mwl[i][1] -25 > self.playerY:
                    if self.playerX > mwl[i][0] -32 and self.playerX < \
                    mwl[i][0] + 32:
                        self.playerY -= self.speed
                        self.wall_hit = True 
                        #print(self.wall_hit)  
                        return self.playerY
                                  
            elif self.direction == 'right':
                if mwl[i][0] - 5 - self.playerX <= 40 and \
                 mwl[i][0] -20 > self.playerX:
                    if self.playerY > mwl[i][1] -32 and self.playerY < \
                    mwl[i][1] + 32:
                        self.playerX -= self.speed
                        self.wall_hit = True
                        #print(self.wall_hit)
                        return self.playerX 
                         
                                    
            elif self.direction == 'up':
                if self.playerY - mwl[i][1] + dungeon.tile_size - 40 <= \
                40 and mwl[i][1] - 50 < self.playerY:
                    if self.playerX > mwl[i][0] -32 and self.playerX < \
                    mwl[i][0] + 32:
                        self.playerY += self.speed
                        self.wall_hit = True
                        #print(self.wall_hit)
                        return self.playerY
                          

            elif self.direction == 'left':
                if self.playerX - mwl[i][0] + dungeon.tile_size - 40 <= \
                40 and mwl[i][0] - 50 < self.playerX:
                    if self.playerY > mwl[i][1] -32 and self.playerY < \
                    mwl[i][1] + 32:                        
                        self.playerX += self.speed
                        self.wall_hit = True
                        #print(self.wall_hit)
                        return self.playerX
                   
        #print str(dungeon)
        #print dungeon.master_wall_list
#end CHARACTER

#PLAYER                
class Player(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = "Luke"
        self.xp = 0
        self.lvl = 1
        self.pframe = pygame.image.load('/Users/lukevawter/Desktop/ActRPGImages/anjin_walk1.2.png')
        self.playerX = Window.half_win_width +100
        self.playerY = Window.half_win_height +100
        self.health = 50
        self.health_max = 50
        self.attack_power = 10
        self.xp_to_level = 100
        self.stamina =80
        self.stamina_max = 80
        self.current_room = [1,1]
        self.current_dungeon = 'Forest'
        self.id = 0
        self.exit_state = False
        self.item_pouch = {'potion':4, 'ammo':0, 'cloth':0, 'snake_skin':0, 'cross':0}
        self.equipment = {}
        self.euipment_equipped = {}
        self.menu_up = False
        
    imagesD = ['/Users/lukevawter/Desktop/ActRPGImages/anjin_walk1.2.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_walk2.2.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_walk3.2.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_walk4.2.png']
    imagesU = ['/Users/lukevawter/Desktop/ActRPGImages/anjin_walkb1.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_walkb2.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_walkb3.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_walkb4.png']
    imagesL = ['/Users/lukevawter/Desktop/ActRPGImages/anjin_walkl1.2.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_walkl2.2.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_walkl3.2.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_walkl4.2.png']
    imagesR = ['/Users/lukevawter/Desktop/ActRPGImages/anjin_walkr1.2.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_walkr2.2.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_walkr3.2.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_walkr4.2.png']
    imagesSD = ['/Users/lukevawter/Desktop/ActRPGImages/anjin_slash_ready.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_slashr.0.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_slash0.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_slash1.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_slash2.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_slash3.png']#'anjin_slashr.0.png'
    imagesSL = ['/Users/lukevawter/Desktop/ActRPGImages/anjin_slash_lready.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_slashu.0.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_slashl0.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_slashl1.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_slashl2.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_slashl3.png']
    imagesSR = ['/Users/lukevawter/Desktop/ActRPGImages/anjin_slash_rready.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_slashu.0.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_slashr0.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_slashr1.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_slashr2.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_slashr3.png']
    imagesSU = ['/Users/lukevawter/Desktop/ActRPGImages/anjin_slash_uready.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_slashl.0.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_slashu0.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_slashu1.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_slashu2.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_slashu3.png']
    imagesDD = ['/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_D1.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_D2.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_D3.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_D4.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_D5.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_D6.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_D7.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_D8.png']
    imagesDL = ['/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_L1.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_L2.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_L3.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_L4.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_L5.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_L6.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_L7.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_L8.png']
    imagesDR = ['/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_R1.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_R2.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_R3.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_R4.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_R5.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_R6.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_R7.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_R8.png']
    imagesDU = ['/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_U1.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_U2.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_U3.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_U4.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_U5.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_U6.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_U7.png', '/Users/lukevawter/Desktop/ActRPGImages/anjin_roll_U8.png']
    speed = 10
    frame_set = imagesD
           
    def HealthBar(self):
        max_health_bar = pygame.draw.rect(screen, WHITE, (10, 10, self.health_max, 5))
        health_bar = pygame.draw.rect(screen, RED, (10, 10, self.health, 5))
        if self.health <= 0:
            screen.fill(BLACK)
            pygame.time.wait(1000)
            self.playerX = Window.half_win_width +100 
            self.playerY = Window.half_win_height +100
            self.health = self.health_max
            self.current_room = [1,1]
            self.exit_state = True
            return self.playerX
            return self.playerY
            return self.health
            return self.current_room
            
    def XpBar(self):
        xp_to_level_bar = pygame.draw.rect(screen, WHITE, (10, 30, self.xp_to_level, 5))
        xp_bar = pygame.draw.rect(screen, BLUE, (10, 30, self.xp, 5)) 
    
    def StaminaBar(self):
        max_stamina_bar = pygame.draw.rect(screen, WHITE, (10, 20, self.stamina_max, 5))
        xp_bar = pygame.draw.rect(screen, ORANGE, (10, 20, self.stamina, 5))       
    
    def potions(self):
        if self.item_pouch['potion'] > 5:
            self.item_pouch['potion'] = 5    
        if self.item_pouch['potion'] == 5:
            screen.blit(potion_image, (50, 30))
        if self.item_pouch['potion'] >= 4:
            screen.blit(potion_image, (40, 30))
        if self.item_pouch['potion'] >= 3:
            screen.blit(potion_image, (30, 30))
        if self.item_pouch['potion'] >= 2:
            screen.blit(potion_image, (20, 30))
        if self.item_pouch['potion'] >= 1:
            screen.blit(potion_image, (10, 30))


             
    def use_potion(self):
        if self.item_pouch['potion'] > 0:
            if self.health_max - self.health >= 20:
                self.health += 20
                #self.item_pouch['potion'] -=1
            elif self.health_max - self.health < 20:
                self.health = self.health_max
            self.item_pouch['potion'] -=1
            #if self.health_max == self.health:
                #pass
       
        
    def attack(self,):
        speed_divider = 4
        attack_stamina_cost = 2
        can_attack = self.stamina - attack_stamina_cost
        if self.direction == 'down' and can_attack >= 0:
            self.frame_set = self.imagesSD
            self.playerY += self.speed/speed_divider
            self.pframe = self.animate()
            self.stamina -= attack_stamina_cost
            return self.stamina
            return self.frame_set
            return self.playerY
        if self.direction == 'up' and can_attack >= 0:
            self.frame_set = self.imagesSU
            self.playerY -= self.speed/speed_divider
            self.pframe = self.animate()
            self.stamina -= attack_stamina_cost
            return self.stamina
            return self.frame_set
            return self.playerY
        if self.direction == 'right' and can_attack >= 0:
            self.frame_set = self.imagesSR
            self.playerX += self.speed/speed_divider
            self.pframe = self.animate()
            self.stamina -= attack_stamina_cost
            return self.stamina
            return self.frame_set
            return self.playerX
        if self.direction == 'left' and can_attack >= 0:
            self.frame_set = self.imagesSL
            self.playerX -= self.speed/speed_divider
            self.pframe = self.animate()
            self.stamina -= attack_stamina_cost
            return self.stamina
            return self.frame_set
            return self.playerX
             
        

    def combat(self, enemy):
        ar = 50
        if self.direction == 'down' and pressed[pygame.K_c]:
            if self.playerY + 30 >= enemy.playerY and self.playerY <= enemy.playerY and\
            self.playerX <= enemy.playerX + ar/2 and self.playerX >= enemy.playerX - ar/2:
                enemy.playerY += 50
                enemy.health -= self.attack_power 
                return enemy.playerY
                return enemy.health    
                
        if self.direction == 'up' and pressed[pygame.K_c]:
            if self.playerY - 30 <= enemy.playerY and self.playerY >= enemy.playerY and\
            self.playerX <= enemy.playerX + ar/2 and self.playerX >= enemy.playerX - ar/2:
                enemy.playerY -= 50
                enemy.health -= self.attack_power 
                return enemy.playerY
                return enemy.health    

        if self.direction == 'left' and pressed[pygame.K_c]:
            if self.playerX - 30 <= enemy.playerX and self.playerX >= enemy.playerX and\
            self.playerY <= enemy.playerY + ar/2 and self.playerY >= enemy.playerY - ar/2:
                enemy.playerX -= 50
                enemy.health -= self.attack_power 
                return enemy.playerX
                return enemy.health   
                         
        if self.direction == 'right' and pressed[pygame.K_c]:
            if self.playerX + 30 >= enemy.playerX and self.playerX <= enemy.playerX and\
            self.playerY <= enemy.playerY + ar/2 and self.playerY >= enemy.playerY - ar/2:
                enemy.playerX += 50
                enemy.health -= self.attack_power 
                return enemy.playerX
                return enemy.health    
                
    def dodge(self):
        roll_multiplier = 2
        roll_stamina_cost = 1
        can_dodge = self.stamina - roll_stamina_cost
        for frames in Player.imagesDD:
            if self.direction == 'down' and can_dodge >= 0:
                self.frame_set = self.imagesDD
                self.playerY += self.speed * roll_multiplier
                self.pframe = self.animate()
                self.direction = 'down'
                self.stamina -= roll_stamina_cost
                return self.stamina
                return self.frame_set
                return self.playerY
                return self.direction
            if self.direction == 'up' and can_dodge >= 0:
                self.frame_set = self.imagesDU
                self.playerY -= self.speed * roll_multiplier
                self.pframe = self.animate()
                self.direction = 'up'
                self.stamina -= roll_stamina_cost
                return self.stamina
                return self.frame_set
                return self.playerY
                return self.direction
            if self.direction == 'right' and can_dodge >= 0:
                self.frame_set = self.imagesDR
                self.playerX += self.speed * roll_multiplier
                self.pframe = self.animate()
                self.direction = 'right'
                self.stamina -= roll_stamina_cost
                return self.stamina
                return self.frame_set
                return self.playerX
                return self.direction
            if self.direction == 'left' and can_dodge >= 0:
                self.frame_set = self.imagesDL
                self.playerX -= self.speed * roll_multiplier
                self.pframe = self.animate()
                self.direction = 'left'
                self.stamina -= roll_stamina_cost
                return self.stamina
                return self.frame_set
                return self.playerX
                return self.direction
                
    def stamina_recovery(self):
        if self.stamina <= self.stamina_max:
            self.stamina +=1

                
    def level_up(self):
	    self.health_max = self.health_max + 2
	    self.health = self.health_max
	    self.attack_power += 2
	    self.lvl = self.lvl + 1
	    self.xp = self.xp - self.xp_to_level
	    self.xp_to_level += 100
	    self.stamina_max += 2
	    print("You reached level %d. Your max health went up to %d. Your attack power went up to %d.\
        Your stamina went up to %d." % (self.lvl, self.health_max, self.attack_power, self.stamina_max))
	    return self.health_max
	    return self.health
	    return self.lvl
	    return self.xp
	    return self.attack_power
	    return self.xp_to_level
	    return self.stamina_max
		
    def lvl_check(self):
        if self.xp < self.xp_to_level:
            pass
        else:
            self.level_up()
            print("You have %d xp" % (self.xp))
		
    def exit_check(self):
        if self.playerY >= 550 and self.direction == 'down':
            screen.fill(BLACK)
            pygame.time.wait(1000)
            self.playerY = 50
            self.current_room[1] +=1
            #print self.current_room
            self.exit_state = True
            return self.playerY
        elif self.playerY <= -20 and self.direction == 'up':
            screen.fill(BLACK)
            pygame.time.wait(1000)
            self.playerY = 525
            self.current_room[1] -=1
            #print self.current_room
            self.exit_state = True
            return self.playerY
        elif self.playerX >= 750 and self.direction == 'right':
            screen.fill(BLACK)
            pygame.time.wait(1000)
            self.playerX = 50
            self.current_room[0] +=1
            #print self.current_room
            self.exit_state = True
            return self.playerX
        elif self.playerX <= -20 and self.direction == 'left':
            screen.fill(BLACK)
            pygame.time.wait(1000)
            self.playerX = 700
            self.current_room[0] -=1
            #print self.current_room
            self.exit_state = True
            return self.playerX
        else:
            self.exit_state = False

        return self.current_room
        
    def get_item(self, lvl):
        item_clear = []
        for i in lvl.items_on_map.keys():
            if self.playerX >= lvl.items_on_map[i][1] - 15 and \
            self.playerX <= lvl.items_on_map[i][1] +15 and self.playerY >= lvl.items_on_map[i][2] -15\
            and self.playerY <= lvl.items_on_map[i][2] +15:
                self.item_pouch[lvl.items_on_map[i][0]] +=1
                #item_clear.append(i)
                #print item_clear
                lvl.items_on_map.pop(i)
                #lvl.item_count -=1
        
            
#end PLAYER

#ENEMY                
class Enemy(Character):
    speed = 0
    enemy_count = 0
    def __init__(self):
        Character.__init__(self)
        self.alive =True
        self.defeated = False
        self.name = None
        Enemy.enemy_count += 1
 
#broken              
    def behavior(self, player):
        sw = 75
        sr = 150
        p_count = 0
        if self.playerX < player.playerX +sw and self.playerX > player.playerX -sw and\
        self.playerY < player.playerY +sr and self.playerY < player.playerY and\
        player.playerY - self.playerY >= player.playerX - self.playerX:
            self.direction = 'down'
            self.move('down')
            
            #print 'enemy'
            #print self.playerX
            #print self.playerY
            #print 'player'
            #print player.playerX
            #print player.playerY 
                    
        elif self.playerX < player.playerX +sw and self.playerX > player.playerX -sw and\
        self.playerY > player.playerY -sr and self.playerY > player.playerY and\
        self.playerY - player.playerY >= self.playerX - player.playerX:
            self.direction = 'up'
            self.move('up')
            
            #print 'enemy'
            #print self.playerX
            #print self.playerY
            #print 'player'
            #print player.playerX
            #print player.playerY 
                      
        elif self.playerY < player.playerY +sw and self.playerY > player.playerY -sw and\
        self.playerX < player.playerX +sr and self.playerX < player.playerX and\
        player.playerX - self.playerX >= player.playerY - self.playerY:
            self.direction = 'right'
            self.move('right')
            
            #print 'enemy'
            #print self.playerX
            #print self.playerY
            #print 'player'
            #print player.playerX
            #print player.playerY 
                          
        elif self.playerY < player.playerY +sw and self.playerY > player.playerY -sw and\
        self.playerX > player.playerX -sr and self.playerX > player.playerX and\
        self.playerX - player.playerX >= self.playerY - player.playerY:
            self.direction = 'left'
            self.move('left')
                        
            #print 'enemy'
            #print self.playerX
            #print self.playerY
            #print 'player'
            #print player.playerX
            #print player.playerY
        '''else:
            if p_count < Window.win_width / 2 / self.speed:
                self.direction = 'right'
                self.move('right')
                p_count += 1
            elif p_count > Window.win_width / 2 / self.speed and p_count < Window.win_width / self.speed:
                self.direction = 'left'
                self.move('left')
                p_count
            else: p_count = 0'''
                
        return self.playerX
        return self.playerY
        return self.direction
        '''differenceX = player.playerX - self.playerX  
        differenceY = player.playerY - self.playerY 
         
        if differenceX < sr and differenceX > - sr:
            if differenceY > 0:
                self.direction = 'down'
                self.move('down')     
            elif differenceY < 0:
                self.direction = 'up'
                self.move('up') 
        elif differenceY < sr and differenceY > - sr:  
            if differenceX > 0:
                self.direction = 'right'
                self.move('right')  
            elif differenceX < 0:
                self.direction = 'left'
                self.move('left')         
        return self.playerX
        return self.playerY
        return self.direction'''
#broken

    def enemy_collision(self, player):
        
        if self.direction == 'left':
            if self.playerX - 10 <= player.playerX and self.playerX >= player.playerX and\
            self.playerY <= player.playerY + 25 and self.playerY >= player.playerY - 25:
                player.playerX -= 50
                player.health -= 5            
        if self.direction == 'right':
            if self.playerX + 10 >= player.playerX and self.playerX <= player.playerX and\
            self.playerY <= player.playerY + 25 and self.playerY >= player.playerY - 25:
                player.playerX += 50
                player.health -= 5
        if self.direction == 'up':
            if self.playerY - 10 <= player.playerY and self.playerY >= player.playerY and\
            self.playerX <= player.playerX + 25 and self.playerX >= player.playerX - 25:
                player.playerY -= 50
                player.health -= 5      
        if self.direction == 'down':
            if self.playerY + 10 >= player.playerY and self.playerY <= player.playerY and\
            self.playerX <= player.playerX + 25 and self.playerX >= player.playerX - 25:
                player.playerY += 50
                player.health -= 5 
        
        return player.playerX
        return player.playerY
        return player.health 
        
    def E_HealthBar(self, player):
        max_health_bar = pygame.draw.rect(screen, WHITE, (self.playerX + 5, self.playerY -5, self.health_max, 5))
        health_bar = pygame.draw.rect(screen, RED, (self.playerX + 5, self.playerY -5, self.health, 5))
        if self.health <= 0:
            player.xp += 50
            self.alive = False
            self.defeated = True
            self.health = self.health_max
            if player.current_room == [1,1]:
                Enemy.drop_item(self,lvl1)
            if player.current_room == [2,1]:
                Enemy.drop_item(self,lvl2)
            if player.current_room == [1,2]:
                Enemy.drop_item(self,lvl3)
            if player.current_room == [2,2]:
                Enemy.drop_item(self,lvl4)

            return self.health
            return player.xp

    def spawn(self):
        if self.alive == True:
            screen.blit(self.pframe, (self.playerX, self.playerY))
        
    def revive(self, player):
        if player.exit_state == True:
            for i in enemy_list:
                if self.id == i:
                    if player.current_room[0] == self.room[0] and player.current_room[1] == self.room[1]:
                        if self.defeated == True:
                            self.alive = True
                            self.defeated = False
                        elif self.defeated == False:
                            self.alive = True
        #print "%s alive is %s and defeated is %s" %(str(self.id), str(self.alive), str(self.defeated))
        #print player.exit_state
        #player.exit_state = False
        
    def drop_item(self, lvl):
        item_chance = randint(0,100)
        #items_on_map = {}
        #item_count = 0
        for i in self.drop_rates:
            if item_chance >= self.drop_rates[i]:
                lvl.item_count +=1
                print('%s dropped' %(i))
                print(self.drop_rates[i])
                print("should be less than")
                print(item_chance)
                lvl.items_on_map.update({lvl.item_count:[i,self.playerX,self.playerY]})
                print(lvl.items_on_map)
                #return items_on_map
                #screen.blit(pygame.image.load(i+'.png'),(self.playerX, self.playerY))
            elif item_chance < self.drop_rates[i]:
                print('%s did not drop' %(i))
                print(item_chance)
    def path(self):
        if self.wall_hit == True:
            if self.direction == 'down':
                self.wall_hit = False
                #print('hit down')
                #self.direction = 'down'
            if self.direction == 'up':
                #print('hit up')
                self.wall_hit = False
                #self.direction = 'up'
            if self.direction == 'right':
                #print('hit right')  
                self.wall_hit = False
                #self.direction = 'right'
            if self.direction == 'left':
                #print ('hit left') 
                self.wall_hit = False
                #self.direction = 'left'
                   
    #def draw_items():
        #for i in items_on_map:
            #screen.blit(pygame.image.load(items_on_map[i][0]+'.png'),(items_on_map[i][1], items_on_map[i][2]))
#end ENEMY

#REPENTER
class Repenter(Enemy):
    def __init__(self, room, playerX, playerY):
        Enemy.__init__(self)
        self.pframe = pygame.image.load('/Users/lukevawter/Desktop/ActRPGImages/rep_D1.png')
        self.playerX = playerX
        self.playerY = playerY
        self.room = room
        self.health = 50
        self.health_max = 50 
        self.id = Enemy.enemy_count
        #print self.id
        self.defeated = False
        enemy_list.update({self.id: [self.playerX, self.playerY]})
        self.drop_rates = {'potion': 40, 'cloth': 20, 'cross':90}
    imagesD = ['/Users/lukevawter/Desktop/ActRPGImages/rep_D1.png', '/Users/lukevawter/Desktop/ActRPGImages/rep_D2.png']
    imagesU = ['/Users/lukevawter/Desktop/ActRPGImages/rep_U1.png', '/Users/lukevawter/Desktop/ActRPGImages/rep_U2.png']
    imagesL = ['/Users/lukevawter/Desktop/ActRPGImages/rep_L1.png', '/Users/lukevawter/Desktop/ActRPGImages/rep_L2.png']
    imagesR = ['/Users/lukevawter/Desktop/ActRPGImages/rep_R1.png', '/Users/lukevawter/Desktop/ActRPGImages/rep_R2.png']
    speed = 5
    frame_set = imagesD
#end REPENTER

#WORM
class Worm(Enemy):
    def __init__(self, room, playerX, playerY):
        Enemy.__init__(self)
        self.pframe = pygame.image.load('/Users/lukevawter/Desktop/ActRPGImages/wormD1.png')
        self.playerX = playerX
        self.playerY = playerY
        self.room = room
        self.health = 30
        self.health_max = 30 
        self.id = Enemy.enemy_count
        #print self.id
        self.defeated = False
        enemy_list.update({self.id: [self.playerX, self.playerY]})
        self.drop_rates = {'potion': 40, 'snake_skin': 20}
    imagesD = ['/Users/lukevawter/Desktop/ActRPGImages/wormD1.png','/Users/lukevawter/Desktop/ActRPGImages/wormD2.png']
    imagesU = ['/Users/lukevawter/Desktop/ActRPGImages/wormU1.png','/Users/lukevawter/Desktop/ActRPGImages/wormU2.png']
    imagesL = ['/Users/lukevawter/Desktop/ActRPGImages/wormL1.png','/Users/lukevawter/Desktop/ActRPGImages/wormL2.png']
    imagesR = ['/Users/lukevawter/Desktop/ActRPGImages/wormR1.png','/Users/lukevawter/Desktop/ActRPGImages/wormR2.png']
    speed = 8
    frame_set = imagesD
#end WORM

pygame.init()

dude1 = Player()

rep1 = Repenter([1,1], 200, 200)
rep2 = Repenter([1,1], 400, 100)
rep3 = Repenter([2,1], 500,200 )
rep4 = Repenter([1,2], 500, 400)
rep5 = Repenter([1,2], 200, 200)
worm1 = Worm([2,2], 400, 400)
worm2 = Worm([2,2], 200, 400)
worm3 = Worm([2,3], 500,400)
worm4 = Worm([2,3], 200,400)
#print enemy_list

lvl1 = OneOne()
lvl2 = TwoOne()
lvl3 = OneTwo()
lvl4 = TwoTwo()
lvl5 = TwoThree()


music =False

if music == True:
    pygame.mixer.music.load('/Users/lukevawter/Downloads/Fantasy Game Loop.wav')
    pygame.mixer.music.play(-1, 0.0)
    if done == True:
        pygame.mixer.music.stop()

while not done:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                Player.use_potion(dude1)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w\
             and dude1.menu_up == False:
                dude1.menu_up = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_w\
             and dude1.menu_up == True:
                dude1.menu_up = False

                
        pressed = pygame.key.get_pressed()
        
        
        if pressed[pygame.K_DOWN] and not pressed[pygame.K_c] and not pressed[pygame.K_x]:
            Player.move(dude1, 'down')
            Player.direction = 'down'
            
        elif pressed[pygame.K_UP] and not pressed[pygame.K_c] and not pressed[pygame.K_x]:
            Player.move(dude1, 'up')
            Player.direction = 'up'
            
        elif pressed[pygame.K_RIGHT] and not pressed[pygame.K_c] and not pressed[pygame.K_x]:
            Player.move(dude1, 'right')
            Player.direction = 'right'
            
        elif pressed[pygame.K_LEFT] and not pressed[pygame.K_c] and not pressed[pygame.K_x]:
            Player.move(dude1, 'left')
            Player.direction = 'left'
            
        elif pressed[pygame.K_c]:
            Player.attack(dude1)
            #Player.attack(dude1, rep2)
            #Player.attack(dude1, rep3)
            #Player.attack(dude1, rep4)


        elif pressed[pygame.K_x]:
                Player.dodge(dude1)
        else:
            Player.stamina_recovery(dude1)  
            
        #if pressed[pygame.K_z]:
            #Player.use_potion(dude1)

        if rep1.alive == True:
            Enemy.wall_check(rep1, lvl1)
            Enemy.behavior(rep1, dude1)
            Enemy.enemy_collision(rep1, dude1)
            Player.combat(dude1, rep1)
        if rep2.alive == True:
            Enemy.wall_check(rep2, lvl1)
            Enemy.behavior(rep2, dude1)
            Enemy.enemy_collision(rep2, dude1)
            Player.combat(dude1, rep2)
        if rep3.alive == True:
            Enemy.wall_check(rep3, lvl2)
            Enemy.behavior(rep3, dude1)
            Enemy.enemy_collision(rep3, dude1)
            Player.combat(dude1, rep3)
        if rep4.alive == True:
            Enemy.wall_check(rep4, lvl3)
            Enemy.behavior(rep4, dude1)
            Enemy.enemy_collision(rep4, dude1)
            Player.combat(dude1, rep4)
        if rep5.alive == True:
            Enemy.wall_check(rep5, lvl3)
            Enemy.behavior(rep5, dude1)
            Enemy.enemy_collision(rep5, dude1)
            Player.combat(dude1, rep5)
        if worm1.alive == True:
            Enemy.wall_check(worm1, lvl4)
            Enemy.behavior(worm1, dude1)
            Enemy.enemy_collision(worm1, dude1)
            Player.combat(dude1, worm1)
        if worm2.alive == True:
            Enemy.wall_check(worm2, lvl4)
            Enemy.behavior(worm2, dude1)
            Enemy.enemy_collision(worm2, dude1)
            Player.combat(dude1, worm2)
        if worm3.alive == True:
            Enemy.wall_check(worm3, lvl5)
            Enemy.behavior(worm3, dude1)
            Enemy.enemy_collision(worm3, dude1)
            Player.combat(dude1, worm3)
        if worm4.alive == True:
            Enemy.wall_check(worm4, lvl5)
            Enemy.behavior(worm4, dude1)
            Enemy.enemy_collision(worm4, dude1)
            Player.combat(dude1, worm4)          

        #if dude1.current_dungeon == 'Forest':
            Dungeon.tile_fill(lvl1)
            
        #if dude1.current_dungeon == 'Cave':
            #pass   
           
        if dude1.current_room == [1,1]:
            Dungeon.tile_fill(lvl1)
            Dungeon.draw_items(lvl1)
            Player.get_item(dude1, lvl1)
            Enemy.revive(rep1, dude1)
            Enemy.revive(rep2, dude1)
            #rep1.alive = True
            #rep2.alive = True
            OneOne.generate_walls(lvl1)
            OneOne.wall_fill(lvl1)
            Player.wall_check(dude1, lvl1)
            Enemy.path(rep1)
            Enemy.path(rep2)
        elif dude1.current_room != [1,1]:
            rep1.alive = False
            rep2.alive = False

        if dude1.current_room == [2,1]:
            Dungeon.tile_fill(lvl2)
            Dungeon.draw_items(lvl2)
            Player.get_item(dude1, lvl2)
            Enemy.revive(rep3, dude1)
            #rep3.alive = True
            TwoOne.generate_walls(lvl2)
            TwoOne.wall_fill(lvl2)
            Player.wall_check(dude1, lvl2)
            Enemy.path(rep3)
        elif dude1.current_room != [2,1]:
            rep3.alive = False
            #rep4.alive = False
            
        if dude1.current_room == [1,2]:
            Dungeon.tile_fill(lvl3)
            Dungeon.draw_items(lvl3)
            Player.get_item(dude1, lvl3)
            Enemy.revive(rep4, dude1)
            Enemy.revive(rep5, dude1)
            #rep4.alive = True
            OneTwo.generate_walls(lvl3)
            OneTwo.wall_fill(lvl3)
            Player.wall_check(dude1, lvl3)
            Enemy.path(rep4)
            Enemy.path(rep5)
        if dude1.current_room != [1,2]:
            rep4.alive = False
            rep5.alive = False
            #rep1.alive = False
            #rep2.alive = False
            
        if dude1.current_room == [2,2]:
            Dungeon.tile_fill(lvl4)
            Dungeon.draw_items(lvl4)
            Player.get_item(dude1, lvl4)
            Enemy.revive(worm1, dude1)
            Enemy.revive(worm2, dude1)
            TwoTwo.generate_walls(lvl4)
            TwoTwo.wall_fill(lvl4)
            Player.wall_check(dude1, lvl4)
            Enemy.path(worm1)
            Enemy.path(worm2)
        if dude1.current_room != [2,2]:
            worm1.alive = False
            worm2.alive = False

        if dude1.current_room == [2,3]:
            Dungeon.tile_fill(lvl5)
            Dungeon.draw_items(lvl5)
            Player.get_item(dude1, lvl5)
            Enemy.revive(worm3, dude1)
            Enemy.revive(worm4, dude1)
            TwoThree.generate_walls(lvl5)
            TwoThree.wall_fill(lvl5)
            Player.wall_check(dude1, lvl5)
            Enemy.path(worm3)
            Enemy.path(worm4)
        if dude1.current_room != [2,3]:
            worm3.alive = False
            worm4.alive = False
            
        Player.potions(dude1)
        screen.blit(dude1.pframe, (dude1.playerX, dude1.playerY))
        Enemy.spawn(rep1)
        Enemy.spawn(rep2)
        Enemy.spawn(rep3)
        Enemy.spawn(rep4)
        Enemy.spawn(rep5)
        Enemy.spawn(worm1)
        Enemy.spawn(worm2)
        Enemy.spawn(worm3)
        Enemy.spawn(worm4)

        #screen.blit(rep1.pframe, (rep1.playerX, rep1.playerY))
        #screen.blit(rep2.pframe, (rep2.playerX, rep2.playerY))
        #screen.blit(rep3.pframe, (rep3.playerX, rep3.playerY))
        #screen.blit(dude1.pframe, (dude1.playerX, dude1.playerY))
  
        
        Player.lvl_check(dude1)
        Player.exit_check(dude1)
        
        Player.HealthBar(dude1)
        Player.XpBar(dude1)
        Player.StaminaBar(dude1)
        if rep1.alive == True:
            Enemy.E_HealthBar(rep1, dude1)
        if rep2.alive == True:
            Enemy.E_HealthBar(rep2, dude1)
        if rep3.alive == True:
            Enemy.E_HealthBar(rep3, dude1)
        if rep4.alive == True:
            Enemy.E_HealthBar(rep4, dude1)
        if rep5.alive == True:
            Enemy.E_HealthBar(rep5, dude1)
        if worm1.alive == True:
            Enemy.E_HealthBar(worm1, dude1)
        if worm2.alive == True:
            Enemy.E_HealthBar(worm2, dude1)
        if worm3.alive == True:
            Enemy.E_HealthBar(worm3, dude1)
        if worm4.alive == True:
            Enemy.E_HealthBar(worm4, dude1)          
        #Dungeon.draw_items(lvl1)
        #Dungeon.draw_items(lvl2)
        #Dungeon.draw_items(lvl3)
        #Dungeon.draw_items(lvl4)
        
        if dude1.menu_up == True:
            print(dude1.item_pouch)
                        
        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)


    
'''for i in enemy_list:
    if self.name == i:
        print 'something'
        self.behavior(self, 
        self.enemy_collison'''     