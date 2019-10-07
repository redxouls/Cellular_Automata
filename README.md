# Celluar Automata - Game of Live
## Introduction
The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.

The game is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves, or, for advanced players, by creating patterns with particular properties.          **--- excerpted from Wikipedia**
## Rules
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisite

Things you need to install beforehand and how to install them
```
Python3 
pip install pygame
```
### Executing
1. After the installation, you have to keep all files(including `main.py`, `pgset.py`,`CA_func.py`and `xxx.txt`).
2. *If you have a input file to load existing pattern, also keep the files in the same folder
3. To start the game, execute `main.py`

## Instuctions
![Game Screen](https://i.imgur.com/flfDALj.png)

### Step1: Input the file name (without the Filename Extension) you want to load.If no there is no input file please enter `0`
### Step2: According to the returned size of the input pattern,input the Initial position of this pattern
### Step3: Set the "Size" of a cell and "Width" and "Heght" of the "Environment" in the terminal
### The recommended composition of (csize,width,height) is (10,100,100) and (20,50,50)
### *Limint of the input will automatically set within 1920x1080 and 100x100
### Step4: Click on the boxes to place cells to the Environment
----
### Game Control Button:

#### `1. Red button:` Start ,Stop or Resume the Game operation 
#### `2. Yellow button:` Reset the Environment (while ruuning)
#### `3. Green button:` Exit the Game
#### `4. Blue Button:` Output the current pattern.(You'll beasked to enter a file name in the terminal)

## Function Explaination


### `main.py`
```python=
import pygame as pg
import time,os,pgset
import CA_func as c 

k = input("File name:")
x = int(input("width"))
y = int(input("height"))
initial_pos=[int(input("Initial x:")),int(input("Initial y:"))]
csize = int(input("cell size"))
root,sub1,sub2,,reset,cell1,cell2
```

| Variables|Type| Usage |
| :--------: | :--------: | -------- |
|x|int|The maximum numbers of cells in one colum
|y|int|The maximum numbers of cells in one colum
|root|bool|Switch to the end the Game 
|sub1|bool|On-Off Switch for the [First Step](##Instuctions)
|sub2|bool|On-Off Switch for the [Second Step](##Instuctions)
|reset|bool|Switch for reseting the Environment
|cell1|list|The current generation of cell distribution
|cell2|list|The next generation of cell distribution
|temp|tuple|To store the output of cell()
|bg,screen|pygame object|Pygame Object to control the Gaming Screen
|clock|pygame object|Pygame Object to Control the screen's update speed 
|k|str|Store the given file name for the pattern  
|initial_pos|list|Store the given "Initial Position"
|csize|int|Store the given Cell Size

### `CA_func.py`

```python=
def cell(x,y,k,initial_pos):
    return cell
```
***Function:*** It creat a two-dimensional array to store each cell's Life and Death with the given `x (width)` , `y(height)` , `k(pattern's filename)` and the `Initial_pos` of the pattern.

***Return:*** It will return the final cell patern with a 2-D array with 1 and 0.(Death:0  Alive:1). 
```python=
def alive(cell,xi,yi,x,y):
    if cell[x][y]==1:
        if count<2:
            return False
        elif count==2 or count<=3:
            return True
        elif count>3:
            return False
    else:
        if count == 3:
            return True
        else: 
            return False
```
***Function:*** The input` xi,yi`represent the coodirnate of the cell to evolve.Then it count the surrounding live cells to determine its Life(1) and Death(0) with the [Rules](#Rules)). 

***Return:*** A boolean value will be given.(Life:1 and Death:0)

```python=
def evolve(inc,x,y):
    return out
```
***Function:*** It take the current generation and evolve  next generation with `alive()` function. 

***Return:*** It ultmately return the evolves cell array.
### `pgset.py`
```python=
def Init(csize,x,y):
    return bg,screen
```
***Function:*** Initializing necessary pygame object with given `csize(cell size)` `x(width)` and `y(height)`.

***Return:*** It returns the pygame object `bg, screen` for the rest of the  operation.
```python=
def clicked(cell,x,y,csize):
    return cell
```
***Function:*** It checks which cell is clicked and modifies the current `cell` list accordingly.

***Return:*** It returns the modified `cell` array. 
```python=
def button(x,y,root,cell,sub1,sub2,order,reset,csize):
    return root,sub1,sub2,reset
```
***Function:*** It determines which button is pressed and modify the bollean switches;therefore, start, stop, resume, reset or exit the game.In addition, if the blue button is pressed, it will require a name for the saved pattern.

***Return:*** The output is a tuple where all the boolean switches stored.



## Running the tests
The Test file can be found either on my [github website](https://github.com/redxouls/Cellular_Automata) or from website [LifeWiki](https://www.conwaylife.com/wiki/Main_Page)

Explain how to run the automated tests for this system

### See more information on https://github.com/redxouls/Cellular_Automata

## Built With

* [Anaconda](https://www.anaconda.com/) - The environment used
* [pygame](https://www.pygame.org/news) - module used to visualize the game
* [LifeWiki](https://www.conwaylife.com/wiki/Main_Page) - Pattern Library for tests and references
