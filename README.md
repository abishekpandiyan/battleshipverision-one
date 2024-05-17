Introduction

The Battleship game implementation presented here demonstrates the use of object-oriented programming (OOP) principles and design patterns. The four main pillars of OOP—polymorphism, abstraction, inheritance, and encapsulation—are utilized to create a flexible and maintainable codebase. Additionally, two design patterns, Singleton and Factory Method, are incorporated to enhance the design. This summary provides an overview of the code, instructions on how to use it, and an analysis of its functionality.

How to Use the Code

Setup and Execution:
Ensure you have Python installed on your system.


Playing the Game:

The game will prompt you to enter the row and column for your guess.
Rows are numbered from 1 to 6, and columns are labeled from A to F.
Input the row number and column letter to make your guess.
The game will provide feedback on your guess, indicating whether you hit a ship or not.
The game continues until you either sink all the ships or run out of turns.


Analysis and Functional Overview

Encapsulation:

The Board class encapsulates the board's state and provides methods to interact with it.
The GameSettings singleton class encapsulates the game settings, ensuring a single source of truth for configuration.
Inheritance:

GameBoard and GuessBoard inherit from the Board class, reusing its properties and methods.

Abstraction:

The ShipPlacementStrategy class provides an abstract interface for different ship placement strategies.
The RandomShipPlacement class implements the abstract method to provide a specific ship placement strategy.

Polymorphism:

The ShipPlacementStrategy allows for different implementations of ship placement strategies, which can be used interchangeably in the BattleshipGame class.

Singleton Pattern:

The GameSettings class ensures only one instance of game settings is used, preventing configuration discrepancies.

Factory Method Pattern:

The game_factory function is a factory method that creates and returns an instance of BattleshipGame with a specific ship placement strategy.






