#final
import time
import random
import os
import sys 
import pygame
import threading


#print("\u001b[35mHi, coders. This is pink output.\u001b[0m"
os.system('cls')
#The Colors
purple = "\033[0;35m"
blue = "\033[0;34m"
green = "\033[0;32m"
red = "\033[0;31m"
yellow = "\033[0;33m"
white = "\033[0;37m"

# 音乐的路径
#def load_file():
    # 获取当前文件路径
current_path = os.path.abspath(__file__)
    # 获取当前文件的父目录
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
    # config.ini文件路径,获取当前目录的父目录的父目录与congig.ini拼接
config_file_path=os.path.join(os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".."),'config.ini')
#print('当前目录:' + current_path)
#print('当前父目录:' + father_path)
#print('config.ini路径:' + config_file_path)
#print ('-------------------------------------')

def music1():
    #print(current_path)
    a = current_path.replace('ENG_.py','Theme1.ogg' , 1)
   # print (a)
    file= a
# 初始化
    pygame.mixer.init()
# 加载音乐文件
    track = pygame.mixer.music.load(file)
# 开始播放音乐流
    pygame.mixer.music.play(-1)
    
    
    
def music2():
   # print(current_path)
    a = current_path.replace('ENG_.py','Theme5.ogg' , 1)
   # print (a)

    file= a
# 初始化
    pygame.mixer.init()
# 加载音乐文件
    track = pygame.mixer.music.load(file)
# 开始播放音乐流
    pygame.mixer.music.play(-1)
    
def music3():
    # print(current_path)
    a = current_path.replace('ENG_.py','Theme4.ogg' , 1)
   # print (a)

    file= a
# 初始化
    pygame.mixer.init()
# 加载音乐文件
    track = pygame.mixer.music.load(file)
# 开始播放音乐流
    pygame.mixer.music.play(-1)    
    
    
def music4():
    #print(current_path)
    a = current_path.replace('ENG_.py','Theme2.ogg' , 1)
   # print (a)
    file= a
# 初始化
    pygame.mixer.init()
# 加载音乐文件
    track = pygame.mixer.music.load(file)
# 开始播放音乐流
    pygame.mixer.music.play(-1)
    
    
    
def music5():
    # print(current_path)
    a = current_path.replace('ENG_.py','Gameover2.ogg' , 1)
   # print (a)

    file= a
# 初始化
    pygame.mixer.init()
# 加载音乐文件
    track = pygame.mixer.music.load(file)
# 开始播放音乐流
    pygame.mixer.music.play()  

def water_jump ():
  # print(current_path)
    a = current_path.replace('ENG_.py','water.mp3' , 1)
   # print (a)

    file= a
# 初始化
    pygame.mixer.init()
# 加载音乐文件
    track = pygame.mixer.music.load(file)
# 开始播放音乐流
    pygame.mixer.music.play() 
  
    

def drop():
   # print(current_path)
    a = current_path.replace('ENG_.py','drop.mp3' , 1)
   # print (a)

    file= a
# 初始化
    pygame.mixer.init()
# 加载音乐文件
    track = pygame.mixer.music.load(file)
# 开始播放音乐流
    pygame.mixer.music.play()  
    


def cheer ():
  # print(current_path)
    a = current_path.replace('ENG_.py','cheer.mp3' , 1)
   # print (a)
    
    file= a
# 初始化
    pygame.mixer.init()
# 加载音乐文件
    track = pygame.mixer.music.load(file)
# 开始播放音乐流
    pygame.mixer.music.play()  
    





def line():
  for i in range(100):
    print()

def pause():
  print()
  k = input()
  if k == '':
    return 0
  
  


def gamerules():
  print("Welcome to 'A Separate Peace' text adventure game. Every time you finish reading the line, press 'enter' to move on.")
  pause()
  print("Your goal is to help your main character make decisions and create your own story.")
  pause()
  print("Remember, each of your decision is significant and you are not allowed to go back and make decisions again.")
  pause()
  print('Every time you input instructions, please input valid strings. Otherwise the program cannot run successfully.')
  pause()
  print('Enjoy the game. Have fun!')
  line()
  

def main():
  music3()
  gamerules()
  print('The story takes place in Devon School, the most prestigious high school in United States.')
  pause()
  print('You need to choose one of the main characters and help them make decisions.')
  pause()
  print('Here is the introduction of the two main character, Finny and Gene.')
  pause()
  print('Finny:')
  print('Atheletic, confident, kind, friendly, honest, handsome. He can always get himself out of trouble.')
  pause()
  print("Gene:")
  print('Intelligent, diligent. Always work hard to pursue glory. Like to compete with other people.',yellow)
  pause()
  

  

  while True:
    answer = input('Press 1 to choose Finny, press 2 to choose Gene, press 0 to quit the game.')
    print()
    if answer == '1':
      print(white,'Good job. Your character setup is done! Your character is Finny.')
      cheer()
      
      pause()
      music2()
      
      line()
      break
    elif answer == '2':
      print(white,'Good job. Your character setup is done! Your character is Gene.')
      
      cheer()
      pause()
      music1()
      line()
      break
    elif answer == '0':
      print(red,'Game Over',white)
      music5()
      return 0
    else:
      print('Please enter valid string')
      continue

   

  if answer == '2': #Gene
    print('Here our story starts...')
    pause()
    print('Finny is your roommate this semester. You hangs out with him every day. One day, Finny invites you to a tree near a river.')
    pause()
    print(yellow,'Finny points at the tree and says: We will make a suicide society, and the membership requirement is one jump out of this tree')
    pause()
    answer = input('Press 1 to agree, press 2 to deny.')
    line()
    if answer == '1':
      print(white,"'That is fine, that is okay', you said to Finny. Then you stand on a limb with Finny. As you are moving to the end of the limb, you lose your balance. Fortunately, Finny comes to grab your hand. ")
      pause()
      print('Since then, you and Finny are good friends.')
      pause()
      print("One day, you and Finny go to the swimming pool. Near the swimming pool, you find a bronze plaque marked with events for which the school kept records -- 50 yards, 100 yards, 220 yards. Under '100 Yards Free Style' there is 'A.Hopkins Parker --1940 -- 53.0 seconds'.")
      pause()
      print("'You mean that record has been up there the whole time we have been at Devon and nobody has busted it yet? That is an insult to the class.' Finny says.")
      pause()
      print('Therefore, Finny jumps into the pool and tries to break the record. You stand beside the pool and help him check the time on the stopwatch.')
      water_jump()
      pause()
      music4()
      print("After several turns in the pool, his hand touches the end and he looks up at you with a composed, interested expression. 'Well, how did I do', Finny asks.")
      pause()
      print('You look at your watch and tells him that he broke the record.')
      pause()
      print("'My God! So I really did it. You know what? I thought I was going to do it. It felts as though I had that stopwatch in my head and I could hear myself going just a little bit faster than A. Hopkins Parker.' Finny says")
      pause()
      print("'You must want everyone comes to see this.' you shout out. 'No, please do not say anything about it, to ...anyone. Will you?' Finny glances sharply at you.")
      pause()
      print("This incredible thing happened. Now you need to decide if you are going to tell everyone in school about the incident and to make him famous.",yellow)
      pause()
      while True:

        answer = input('Press 1 to tell everyone in the school, press 2 to keep it as a secret')
        line()
        if answer == '1':
          print(green,'You decide to spread the news to everyone. What you do not expect is the news does no good to Finny, many students come to see and to challenge Finny, with their doubt,surprise, and rivalry. Relationships in Devon are based on rivalry, and Finny is trapped in the swamp of fame that you give to him -- Phineas could get away with anything, but not this trouble.')
          pause()
          print(red,'Game over.',white)
          music5()
          return 0
        elif answer == '2':
          print(white,"His accomplishment takes root in your mind and grows rapidly in the darkness where you are forced to hide it. You know he is serious about it, so you do not tell anybody.")
          pause()
          
          
          break
        else:
          print('Please input valid string')
          continue
      
      # Finny and Gene go to the tree
      print("However, in the days you spend with Finny, you find a single sustaining thought that you and Phineas are even already and you gradually start to believe that Finny invited you to have fun because he does not want you to be even with him. The idea of 'Finny wants to compete with you' pops up to your mind ",yellow)
      pause()
      print("A day in late August, Finny asks you to go to the Super Suicide Society. You climb up the tree, right after Finny. Would you choose to bent your knees and jounce the limb and make him fall off from the tree because of your hatred to him?")
      pause()
      answer = input('Press 1 to jounce the limb, press 2 if you do not want to do it')
      line()
      

      #where is the choice answer == 2
      if answer == '2':

        num = random.randint(1,2)
        if num ==1:
          print(green,"You jump off the tree, as usual, so does Finny. Later in the week you two are punished by the school for breaking the school rule and illegally doing the tree jump. You break the rule, the rule breaks you.  ")
          pause()
          print(" But as always, Finny gets his out of the swirl but you are deeply trapped. You are not as perfect as Finny.")
          pause()
          print("When the mean idea comes to your mind you cannot control it and a fury swallows your mind -- that's unfair, you want revenge, you want to see Finny fail, you want him to suffer")
          pause()
          print('You are strongly influenced by your anger and start publicly compete with Finny, although Finny does not understand what happened to you, he feels you are not the friend he used to know.')
          pause()
          print('Since all your attention is focused on Finny, you loses your balance of study and life hence your academic marks start falling.')
          pause()
          print('In the coming years, your life is ruined by your own jealous of Finny.')
          print(red,'Game Over',white)
          music5()
          return 0

        elif num ==2:
          print(green,"Nothing happens, the SSS club goes normally every day later in the summer; You do not show any aggressive action to Finny, hence your 'Friendship' keeps well in Grade 11")
          print(red,'Game Over, but we have a random decision here so if you try again, there might be another result.',white)
          music5()
          return 0
        
       

      elif answer == '1':
        print(white,"You bent your knees. However, life is made up by uncertainties. Many things could happen after you bent your knees and jounce the limb. Therefore, you need to roll a die to determine the result.")
        pause()
        print("The rules is: if the number of the die is 1 or 2, Finny falls off and dies; if the number if 3 or 4, Finny falls off and hurts his leg; if the number if 5 or 6, Finny keeps the balance and does not fall off")
        pause()

        num = random.randint(1,6)

        print("The number you got was "+str(num))

        pause()

        if num == 1 or num == 2:
          print(green,"Finny dies: There is an awkward fall. Finny's head touches the ground first, then his neck bents an incredible angle with a sound of eggshell cracks. Finny is killed at 16 in the year of 1942. You are suspected by the school and you are arrested for suspected murder")
          drop()
          pause()
          print(red,'Game Over',white)
          music5()
          return 0
          pause()
          
        elif num == 3 or num == 4:
          print(green,'Finny hurts his leg: Finny tumbles sideways, breaks through the little branches below and hit the bank with a sickening, unnatural thud. His left leg is scattered and loses the ability to do any sports. You have done the same sin again to Finny.')
          drop()
          pause()
          print(red,'Game Over',white)
          music5()
          return 0
          pause()

        elif num == 5:
          print(green,"Finny does not fall off. Finny, his balance gone, swings his head around to look at me for an instant with extreme interest, and then he acts a weird gesture and rebalanced himself again, incredible.'Be careful pal? we are Super Suicide Society but we do not commit suicide! Now I will jump first and you follow up.' You are shocked by the evil that buried deep inside you, then you jump into the river, cold water calms you off. You had a peaceful summer later in the vacation.")

          print(red,'Game Over',white)
          music5()
          return 0
          
        else:
          print(green,"Finny does not fall off. Finny tumbles a couple of steps forward then swings his head around to see you with fury and dropped into the river so close to the bank.'Are you trying to murder me? I do not like this joke pal!' Although it is a summer night your body shakes hardly in the warm air, you know Finny knows it. He knows you. And you know the relationship, the friendship between you and Finny, is gone.")

          print(red,'Game Over',white)
          music5()
          return 0
     
          



    

    elif answer == '2':
      print()
      print(green,"''No!' You simply reply Finny. 'I need to study! Studying! You know, books, work. examinations.' Finny is shocked. 'I did not know you needed to study,' he said simply, 'I did not think you ever did. I thought it just came to you. Okay, hence you go to study en?")
      pause()
      print("That’s it. The summer goes peacefully and so does the next school year. On the graduation day, You become the head of the class, valedictorian, so you make a speech -- in Latin --and be the wonder of the school. Finny trains hard at the same time and is selected to represent the USA in the Summer Olympics in London in 1948.")
      print(red,'Game Over',white)
      music5()
      return 0
      
    

  #-----------------------------------------------------------
  
  elif answer == '1': #the player choose Finny
    print('Here our story starts...')
    pause()
    print('In this semester, your roommate is Gene.')
    pause()
    print('One day, when you are hanging out with Gene near a river. You find a tree by the river.')
    pause()
    print(yellow,'You come up with an idea of establishing a Super Suicide Society. The activity of this society is jumping out of the tree.')
    pause()
    answer = input('Would you like to tell Gene your plans and invite him to the club? Press 1 to tell him, press 2 if you do not want to tell him.')
    line()
    if answer == '1':
      print(white,'Gene agrees with and joins the society. Since then, you and Gene meet at the society every day.')
      pause()
      print('In the beginning, Gene does not dare to jump. But with your inspiration, Gene gradually begin to jump out of the tree.')
      pause()
      print('Because of this, you and Gene becomes best friends')
      pause()
      print('One day, you meet Gene at the school swimming pool.')
      pause()
      print("Gene points at a bronze plague and says:'Look at this plague, A.Hopkins Parker's held the record for years.")
      pause()
      print("'That is an insult to the class!', you yell.")
      pause()
      print('Then you take off your clothes and begin to challenge the record.')
      pause()
      print('After a while, you come out of the swimming pool and Gene is looking at you surprisingly.')
      pause()
      print("'You broke the record! Everyone in the school has to know this!', Gene says.")
      pause()
      print(yellow,'Now you need to decide if you are going to ask Gene to keep the secret.')
      pause()
      answer = input('Press 1 so that Gene will tell everyone in school, press 2 so that Gene will keep this as a secret.')
      line()
      if answer == '1': #tell everyone
        print(green,'Gene tells all people in Devon School. All the teachers, coaches come to witness how you break the record. Soon you become famous in the city')
        pause()
        print("The 'Swimming pool' incident brings you incredible fame and glory in Devon; satisfaction, happiness, and pride all quickly come to you. You lose the innocence you used to have.  ")
        pause()
        print('Then you gave up all the friends and relationships in Devon School to pursue honor and glory in swimming career.')
        pause()
        print(red,'Game Over',white)
        music5()
        return 0
      elif answer == '2':
        print(white,'As you wish, Gene keeps the secret and no one knows that you break the record. Life still goes the way it was.')
        pause()
        print('On a sunny afternoon, Gene tells you that he wants to be the valedictorian and give a speech in graduation.')
        pause()
        print(yellow,'As his best friend, there are several ways to respond to him.')
        pause()
        answer = input("Press 1 to say 'I will kill myself out of jealous.'; Press 2 to keep silence.")
        line()
        if answer == '1':
          print(white,'Then Gene says nothing. Later you and Gene go to the Super Suicide Society, but a subtle atmosphere emerges between you two guys.')
          pause()
          print('You climb up the tree, Gene follows behind you')
          pause()
          print(yellow,'When you are moving toward the end of the limb, it sways a little bit then you suddenly lose your balance, now you look back to Gene, would you like to grab Gene to save yourself from falling?')
          pause()
          answer = input('Press 1 to Grab him, press 2 fall off')
          line()
          if answer == '1':
            print(white,'No one know what will happen if you drag him.')
            pause()
            print('So the result is determined by a dice. If the dice point is 1,3 or 5, you fall off from the tree and die; If the point is 2 or 4, you catch Gene and survive; if the point is 6 both of you two fall.')
            num = random.randint(1,6)
            pause()
            print('You dice point is ' + str(num) + '.')
            if num == 1 or num == 3 or num == 5:
              print(green,'You fall off from the tree and you die.')
              drop()
              pause()
              print(red,'Game Over',white)
              music5()
              return 0
            elif num == 2 or num == 4:
              print(green,'You catch Gene and survived.')
              print(red,'Game Over',white)
              music5()
              return 0
            elif num ==6:
              print(green,"Gene does not expect you to act so fast.")
              pause()
              print("In the dark August night, two human shape object hit on the bank hardly and silence befalls.")
              print(red,'Game Over',white)
              music5()
              return 0
          elif answer == '2':
            print(green,'You fall off from the tree and your sports dream is broken.')
            drop()
            pause()
            print(red,'Game Over',white)
            music5()
            return 0
          
        elif answer == '2':
          print(green,'Since that day, Gene trys to figure out the meaning of that silence and more and more conflicts emerge between you and Gene in the rest of your student life in Devon School.')
          pause()
          print(red,'Game Over',white)
          music5()
          return 0
        

        

 
    elif answer == '2':
      print(green,'Since then, you and Gene do not have any connections. Both of you and Gene do own business. You begin to train hard in sports while Gene becomes the best student and gives a perfect speech in Latin on graduation day.')
      pause()
      print(red,'Game Over',white)
      music5()
      return 0
    
      

    






q = 1
while q == 1:
  print(white,'')
  main()
  q = int(input('Press 1 to play again, press 2 to quit'))

