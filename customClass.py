#Nathaniel Lopez Assignment 10.1: My Custom Class
#customClass.py
#The purpose of this script is to create a class based on an object

#pygame module needed for diplay and time module for demo purposes
import pygame
#AdventCalendar class
class AdventCalendar:
    #Class variable
    _total_days = 25
    #init which takes current day and file path where assets are stored
    def __init__(self, day = 1, assets = 'assets'):
        self._assets = assets
        self._day = day 
    #get day function which returns current day calendar is set to
    def get_day(self):
        return self._day
    #set day function which sets the current day
    def set_day(self,day):
        self._day = day
    #get assets function which returns where the file path is set to 
    def get_assets(self):
        return self._assets
    # set the assets file path 
    def set_assets(self,assets):
        self._assets = assets
    #view function which creates an actual viewable advent calendar
    def view(self):
        #initalize pygame
        pygame.init()
        #variables for plane
        x= 800
        y= 800
        white = (255,255,255)
        #make plane
        display_surface = pygame.display.set_mode((x,y))
        #fill plane with white
        display_surface.fill(white)
        #set caption of display window
        pygame.display.set_caption("Advent Calendar")
        #display image relevent to current day
        displayImage = self._assets + f'/{self._day}.jpg'
        #add image to the white plane
        while True:
            #display image relevent to current day
            displayImage = self._assets + f'/{self._day}.jpg'
            image = pygame.image.load(displayImage).convert_alpha()
            image = pygame.transform.scale(image, (x,y))
            display_surface.blit(image, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                pygame.display.update()

    #update day function which simply adds one making it the next day
    def update_day(self):
        self._day = self._day + 1 

#main containing demo program
def main():
        print("Hello and welcome to the Advent calendar demo")
        print("This demo will walk you through what the AdventCalendar class does")
        input("Please press enter when you are ready to proceed:")
        calendar = AdventCalendar()
        print("The first few methods I would like to talk about is the get and set for days")
        print("these change the current day the calendar is set to")
        print(f"for example calendar.get_day(): {calendar.get_day()}")
        print(f"Let's change that value to 5 with calendar.set_day(5)")
        calendar.set_day(5)
        print(f"We can also change the file directory using the asset get and set functions")
        print(f"If you want to just increment a day there is a update_day function")
        print(f"Lets call it so our current day will be set to 6")
        calendar.update_day()
        print(f"Finally there is the view() function")
        print(f"This prints the calendar for viewing as an image")
        input("press enter when you are ready to view")
        calendar.view()

        


if __name__ == "__main__":
    main()