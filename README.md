BattlePi
========

My BattlePi entry for the UoY 2013 competition

How To Use
========
Run main.py to run the code against a person / machine

Run iterate.py to iterate the code multiple times against predefined boards in boards.py

Some tests for pattern matching are in test_matrix.py

How It Works
========

Searching = When you're not sure where a boat is, and you're looking for a boat

Targetting = When you've got a hit from searching and you want to sink that ship

Searching
========

Looks at all the places the remaining boats could possibly fit and search at the most probable locations

Targetting
========

Tries to shoot a line then handles the situations of two, three & four horizontal and vertical manually (THIS ISN'T A GOOD WAY OF DOING THINGS!)
