# ASCII-Art


Program takes an image as an input and recreates it using only characters. This process is known as ASCII art. By default the user enters a filename (jpg and jpeg supported), default size of (640 x 480) and the program outputs a sequence of characters, to the user's terminal, which (when zoomed out) is a re-creation of the supplied image. Many features have been added, allowing the user to invert the image, change the color, supply different size images and even use the built in camera to capture an image of the user and then re-create it as an ASCII art piece.

The link below explains ASCII art in more depth.

https://en.wikipedia.org/wiki/ASCII_art


The process works by using image processing libraries to analyze the RGB data of each pixel in a given image. Using this data, stored as a tuple in python, the program uses a basic algorithim to convert the RGB values into a brightness value, any value in the set [0,255] is a valid brightness value. The user can use one of three different algorithims to convert RGB  and a brightness value (the average formula, luminosiy formula and lightness formula are potential selections, the program uses the average formula by default). 

At this point we utilize a string of 65 character values, ordered by increasing brightness, where the latter characters are darker than the previous ones. The program uses these stored brightness values (one value for each pixel), and maps it to the equivalent character value. Finally we have converted each pixel to a character value, and now we are able to print the characters to the user's terminal. Prompts are given to the user, enabling them to choose which features they want to use

Features:
Multiple RGB-Brightness mapping algorithims
Multiple image sizes supported
Six different color outputs - changes the colors of the output characters
Image Inversion 
Real-time image capturing using the OS module - allows the user to take a selfie and use that as the input for the program.


Technologies used: VSC, Python
