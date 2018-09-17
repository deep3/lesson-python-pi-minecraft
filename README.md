
# Python coding lessons with Raspberry Pi & Minecraft

This package is to help teach beginners how to write python code and visualise the process using Minecraft on a Raspberry Pi. Follow the instructions to use code to create blocks in the game. Then expand to looping walls, buildings, cannons and more!

The focus of these lessons is to spark an interest in computer science by showing how simple code can affect a digital world. Minecraft is an excellent platform for visualising how loops and other technical actions operate.

These lessons have been built on top of the mcpi library **[https://github.com/martinohanlon/mcpi](https://github.com/martinohanlon/mcpi)** which comes bundled in Raspbian

Produced by [**Deep3**](https://deep3.co.uk/) as part of the [**NCSC Cyber Schools Hubs initive**](https://www.ncsc.gov.uk/information/cyber-schools-hubs).

# Requirements & Getting started

To use these lessons, you will need to have a Raspberry pi 2 or newer, running the latest Raspbian OS. This will provide you with a free copy of Minecraft Pi edition, Python 3, and mcpi read installed.

This guide is to detail the files included. Instructions for regular use can be found in the **Worksheet.pdf**

# Files

- **Python and Minecraft worksheet.pdf** : The step by step lesson guide to learn python, the Minecraft API, and how to build a house.

- **Minecraft Python API.pdf** : A printable version of the Minecraft Pi API. Used to support the worksheet see all the available commands and data values.

- **SETUP.sh** : This is the quick start script. This is to be used by those who want to run a class and follow the lesson steps directly.  It will;
	- create a folder to do your code in
	- copy in relevant libraries
	- launch an IDE and open a file in the correct place ready to code
	- launch Minecraft with an empty world. Once a Minecraft world is opened, it will be wiped and made immutable ready for the lesson steps.

- **completeExamples** : This folder contains finished python code that can be used for actions such as building a house or firing a cannon ball. These are intended to be used as a cheat sheet if you get stuck in the lesson.

- **deep3** : This folder contains library code used to hide some of the complexity of the code so it doesn’t need to be taken on in the lesson. In addition, they reset the Minecraft world, meaning each time you run your own code you can see the difference.

