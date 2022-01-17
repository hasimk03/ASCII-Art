from PIL import Image
from colorama import Fore,Back,Style 
import math
import subprocess 
import os

conversion = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$" #len = 65
char_matrix = []

def select_input_image():
    global im,pixels,file
    take_picture = input("Would you like your picture taken?\nEnter Yes or No\n")

    if take_picture == "Yes":
        command = 'imagesnap /Users/Hasim/Desktop/Python/your_picture.jpg'
        os.system(command)
        file = "your_picture.jpg"
    elif take_picture == "No": 
        file = input("Please enter a JPG or JPEG Image:")
        #file = "Test_Image.jpeg"
    else:
        print("Input is invalid. Please enter either 'Yes' or 'No'")
    

    im = Image.open(file)

    if (im.size[0] > 780):
        basewidth = 400
        img = Image.open(file)
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        img.save(file)



    pixels = im.load()
    print("Format:",im.format,"\nSize:",im.size,"\nMode:",im.mode)


def create_brightness_matrix(choice = 1): #user chooses which formula to use for creating brightness
    global brightness_value

    print("Please choose a formula to map RGB values to a brightness integer:")
    print("1: Average Formula     ->   brightness = (R + G + B)/3\n2: Lightness Formula   ->   brightness = [max(R,G,B) + min(R,G,B)]/2\n3: Luminosity Formula  ->   brightness = 0.21R + 0.72G + 0.07B")
    
    choice = input("\nPlease choose which formula you would like to use:\nEnter an integer between 1 and 3:")
    inverted = input("\nWould you like the image to be inverted?\nEnter Y for yes, and N for no: ")

    for i in range(im.size[0]):
        for j in range(im.size[1]):
            T = pixels[i,j] 
            if choice=="Average" or choice =="1":     #Average Formula
                brightness_value = round((T[0] + T[1] + T[2])/3) #creates brightness values
                if inverted == "Y": #inverts colors
                    pixels[i,j] = 255-brightness_value
                else:
                    pixels[i,j] = brightness_value

            elif choice=="Lightness" or choice=="2":     #Lightness Formula
                brightness_value = round((max(T[0],T[1],T[2]) + min(T[0],T[1],T[2]))/2)
                if inverted == "Y": #inverts colors
                    pixels[i,j] = 255-brightness_value
                else:
                    pixels[i,j] = brightness_value

            elif choice=="Luminosity" or choice =="3":     #Luminosity Formula
                brightness_value = round(0.21*T[0] + 0.72*T[1] + 0.07*T[2])
                if inverted == "Y": #inverts colors
                    pixels[i,j] = 255-brightness_value
                else:
                    pixels[i,j] = brightness_value

    #print("Inverted brightness =",pixels[0,0])

def create_ascii_conversion_table():
    i=0; j=0
    while i in range(60): #for first 60 elements -> each char maps to 4 brightness values
        char_matrix.append(conversion[i])
        char_matrix.append(conversion[i])
        char_matrix.append(conversion[i])
        char_matrix.append(conversion[i])
        i=i+1

    #For last 5 elements -> each char maps to 3 brightness values
    char_matrix.append(conversion[len(conversion)-5]); char_matrix.append(conversion[len(conversion)-5]); char_matrix.append(conversion[len(conversion)-5]); 
    char_matrix.append(conversion[len(conversion)-4]); char_matrix.append(conversion[len(conversion)-4]); char_matrix.append(conversion[len(conversion)-4]); 
    char_matrix.append(conversion[len(conversion)-3]); char_matrix.append(conversion[len(conversion)-3]); char_matrix.append(conversion[len(conversion)-3]); 
    char_matrix.append(conversion[len(conversion)-2]); char_matrix.append(conversion[len(conversion)-2]); char_matrix.append(conversion[len(conversion)-2]); 
    char_matrix.append(conversion[len(conversion)-1]); char_matrix.append(conversion[len(conversion)-1]); char_matrix.append(conversion[len(conversion)-1]); 
    char_matrix.append(conversion[len(conversion)-1]) #index 255


def intiailize_ascii_matrix():
    global ascii_matrix
    ascii_matrix = []

    for i in range(im.size[1]): #row
        ascii_row = []
        for j in range(im.size[0]): #val
            ascii_row.append(char_matrix[pixels[j,i][0]])
        ascii_matrix.append(ascii_row)
    

def print_ascii_matrix(change_color = 'N'): #add color feature
    change_color = input("Would you like to change the color of the art piece?\nEnter Y for yes and N for no: ")

    if change_color == 'Y':
        color = input("What color would you like the output to be? Enter one of the following:\nRed\nGreen\nYellow\nBlue\nWhite\nChoose a color:")
        print("COLOR===",color)
        if color == "Red":
            color = Fore.RED
        elif color == "Green":
            color = Fore.GREEN
        elif color == "Yellow":
            color = Fore.YELLOW
        elif color == "Blue":
            color = Fore.BLUE
        elif color == "White":
            color = Fore.WHITE
        else:
            print("You have entered an invalid choice: Image will be printed in black")

    for row in ascii_matrix:
        line = [v+v for v in row] #SIZE must be > 1287 x376
        if change_color == 'N':
            print("".join(line))
        else:
            print(color +"".join(line)) 

###create method to shrink the output ---> how?

def main():
    print("Start\n")
    select_input_image() 
    create_brightness_matrix()
    create_ascii_conversion_table()
    intiailize_ascii_matrix()
    print_ascii_matrix()


if __name__ == "__main__":
    main()