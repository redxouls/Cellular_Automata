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
After the installation, you have to keep all files(`main.py`, `pgset.py` and  `CA_func.py`).
To start the game, execute `main.py`

## Instuctions
![Game Screen](https://i.imgur.com/BSbVl4x.png)
### Step1: Input the "Width" and the "Heght" of the "Environment" in the terminal
### Step2: Click on the boxes to Place cells on the Environment
### Game Control Button:

`1. Red button:` Start and Resume the Cell
`2. Yellow button:` Reset the Environment
`3. Green button:` Exit the Game

## Function Explaination


### `main.py`
```python=
import pygame as pg
import time,os,pgset
import CA_func as c 
x = int(input("width"))
y = int(input("height"))
root,sub1,sub2,,reset,cell1,cell2
```

| Variables|Type| Usage |
| :--------: | :--------: | -------- |
|x|int|The maximum numbers of cells in one colum
|y|int|The maximum numbers of cells in one colum
|root|bool|Switch to the end the Game 
|sub1|bool|Switch for the [First Step](##Instuctions) is done
|sub2|bool|Switch for the [Second Step](##Instuctions) is done
|reset|bool|Switch for reseting the Environment
|cell1|list|The current generation of cell distribution
|cell2|list|The next generation of cell distribution
|temp|tuple|To store the output of cell()
|bg,screen|pygame object|Pygame Object to control the Gaming Screen
|clock|pygame object|Pygame Object to Control the screen's update speed 


### `CA_func.py`

```python=
def cell(x,y):
    return cell
```
Function: creating an two-dimensional array to store each cell's Life and Death (Death:0  Alive:1). 
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
Function: Computing the surrounding live cells to determine its Life and Death with the [Rules](#Rules)). 
```python=
def evolve(inc,x,y):
    return out
```
Function: Evolving the next generation from the current generation. 
### `pgset.py`
```python=
def Init(x,y):
    return bg,screen
```
Function: Initializing necessary pygame object with given `width` and `height`
```python=
def clicked(cell):
    return cell
```
Function: Check which cell is clicked and return changed `cell` list
```python=
def button(x,y,root,sub1,sub2,order,reset):
    return root,sub1,sub2,reset
```
Function: Determine which button is pressed and return a tuple of the boolean switches;therefore, start, stop, reset or exit the game



## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds


## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
