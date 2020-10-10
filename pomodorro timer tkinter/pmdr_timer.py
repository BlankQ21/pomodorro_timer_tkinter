#===========================================================
# imports
#===========================================================
from tkinter import*
from threading import Thread
from time import sleep
from winsound import*
from PIL import Image, ImageTk
from tkinter import messagebox as msg

#-------------------------------------------------
# Globals
#-------------------------------------------------

count = 0
num_cycles = 0



#-------------------------------------------------
# Initialize class Window
#-------------------------------------------------
    
class Window():
    
    def __init__(self):
        self.root = Tk()
        self.root.title('Pomodorro Timer')
        self.root.config( bg = 'orange2')               # background color
        self.root.geometry('300x300+650+250')           # 300mm x 300mm window, position at x:650px and y: 250px (Center Screen)
        self.root.resizable( False, False )             # lock the size of the window
        self.initUI()                                   # call the initUI(self) function
        self.root.iconbitmap('pmdricon.ico')          # Window Icon (placed after the initUI to prevent opening of another window)
        


#-------------------------------------------------
# Class Functions
#-------------------------------------------------

    # Button Click Functions
    #------------------------
    
    def start_click(self):                                      # Start Time Button Start Thread
        self.cycle_count()
        Thread(target = self.start_time).start()

    def rest_click(self):                                       # Start Time Button Start Thread
        Thread(target = self.rest_time).start()
        
    def long_rest_click(self):                                  # Start Time Button Start Thread
        Thread(target = self.long_rest_time).start()
        
        
        
    # Timer Functions
    #----------------

    def start_time(self):                                               # 25 Minute Work Timer
        time_left = 1500
        run = True
        
        while run:
            
            totalMin = time_left//60
            totalSec = time_left-(60*(totalMin))
            time_left-= 1
            
            if time_left >-1:
                timer_output = ((str(totalMin))+':'+(str(totalSec)))
                self.timer_lbl.config(text = timer_output)              # Configure Label Text
                self.start_btn.config(state ='disabled')                # Disable Start Button
                self.rest_btn.config(state ='disabled')                 # Disable Rest Button
                sleep(1)
                
            else:
                self.timer_lbl.config(text = 'Time\'s Up')              # Configure Label Text
                self.start_btn.config(state ='active')                  # Enable Start Button
                self.rest_btn.config(state ='active')                   # Enable Rest Button
                self.sfx()
                break
                
                
        
    def rest_time(self):                                                # 5 Minute Rest Timer
    
        time_left = 300
        run = True
        
        while run:
            
            totalMin = time_left//60
            totalSec = time_left-(60*(totalMin))
            time_left-= 1
            
            if time_left >-1:
                timer_output = ((str(totalMin))+':'+(str(totalSec)))
                self.timer_lbl.config(text = timer_output)              # Configure Label Text
                self.start_btn.config(state ='disabled')                # Disable Start Button
                self.rest_btn.config(state ='disabled')                 # Disable Rest Button
                sleep(1)
                
            else:
                self.timer_lbl.config(text = 'Work Time!')              # Configure Label Text
                self.start_btn.config(state ='active')                  # Enable Start Button
                self.rest_btn.config(state ='active')                   # Enable Rest Button
                self.sfx()
                break
                           
        
    def long_rest_time(self):                                           # 30 Minute Long Rest Timer
        time_left = 1800
        run = True
        
        while run:
            
            totalMin = time_left//60
            totalSec = time_left-(60*(totalMin))
            time_left-= 1
            
            if time_left >-1:
                timer_output = ((str(totalMin))+':'+(str(totalSec)))
                self.timer_lbl.config(text = timer_output)              # Configure Label Text
                self.start_btn.config(state ='disabled')                # Disable Start Button
                self.rest_btn.config(state ='disabled')                 # Disable Rest Button
                sleep(1)
                
            else:
                
                self.timer_lbl.config(text = 'Cycle Done!')             # Configure Label Text
                self.start_btn.config(state ='active',                  # Enable Start Button
                text ='Start', command = self.start_click)              
                self.rest_btn.config(state ='active')                   # Enable Rest Button
                self.count_lbl.config(text ='x0')                       # Reset Count
                self.cycles_done()                                      # Updates Cycles Done Label
                self.sfx()
                
                break
        
        
        


    def cycle_count(self):
        global count
        count += 1
        self.count_lbl.config(text = f'x{count}')
        
        if count == 4:
            count = 0
            self.start_btn.config(text ='Long Rest', command = self.long_rest_click)
            
    def cycles_done(self):
        global num_cycles
        num_cycles += 1
        self.cycle_count_lbl.config(text = num_cycles)           # f'string{integer} -- this code can combine a string and integer without needing the str() prefix
        
        
            
            
    def sfx(self):
        return PlaySound("dingsfx.wav", SND_FILENAME)

#-------------------------------------------------
# Class Widgets
#-------------------------------------------------
    def initUI(self):

        self.image = ImageTk.PhotoImage(Image.open('pmdricon2.png'))
        self.img_label = Label(image= self.image, bg = 'orange2')
        self.img_label.grid( column = 1, row =0, padx = 30, pady = 0, columnspan = 2,  sticky = 'E')
   
     
        # Labels
        #--------
        self.timer_lbl = Label(self.root, text='Timer Here',     # Main label that will show status and timer
        font = ('Helvetica, 32'), fg = 'green',  bg = 'orange2')
        self.timer_lbl.grid( column = 0, row =1, padx = 30, pady = 40, columnspan = 3, sticky = 'WE')
        
        self.count_lbl = Label(self.root, text = 'x0',    # Label that shows the number of pomodorro cycles completed
        font = ('Helvetica, 14'), fg = 'dark green',  bg = 'orange2')
        self.count_lbl.grid( column = 2, row = 0, padx = 0, pady = 5, sticky = 'E')

        self.cycle_count_lbl = Label(self.root, text = '0',    # Label that shows the number of pomodorro cycles completed
        font = ('Helvetica, 16'), fg = 'tan4',  bg = 'orange2')
        self.cycle_count_lbl.grid( column = 0, row = 0, padx = 5, pady = 5, sticky = 'W')


        
        
        # Buttons
        #--------
        self.start_btn = Button(self.root, text = 'Start', width = 19, command = self.start_click,
        font = ('Helvetica, 14'))
        self.start_btn.grid( column = 0, row = 2, padx = 40, pady = 3, sticky = 'WE', columnspan = 3)
        
        self.rest_btn = Button(self.root, text = 'Rest', width = 19, command = self.rest_click,
        font = ('Helvetica, 14'))
        self.rest_btn.grid( column = 0, row = 3, padx = 40, pady = 3, sticky = 'WE', columnspan = 3)

        
        


#===========================================================
# Start GUI
#===========================================================
win = Window()
win.root.mainloop()

# References:
# Timer Codes :timer code answer by Anshuman Bharadwaj, from:https:// stackoverflow.com/questions/30720665/countdown-timer-in-pygame
