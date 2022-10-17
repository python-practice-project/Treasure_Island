# Treasure Island
print('''         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
ejm97  %%%%

       {}           {}
         \  _---_  /
          \/     \/
           |() ()|
            \ + /
ejm 96     / HHH  \
          /  \_/   \
        {}          {}
                           ___________
                ___________)%{}%%%%%%/
               /{}%%%%%%%%/%%/%%%%%%/
              /%%\% _---_/ \/%%%%%%/
             /%%%%\/    /()|%%%%%%/
            /%%%%%|()  /+ /%%%%%%/
           /%%%%%%%\ +/HH%%\%%%%/
          /%%%%%%/%HH/_/%%%\%%%/
 ejm97   /%%%%%%/%%\/%%%%%%{}%/
        /%%%%%{}%%%/
       /
      /
     /
    /
   /
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_1 = input("Type 'left' or 'right': ")
if choice_1 == "left":
    choice_2 = input("Type 'swim' or 'wait': ")
    if choice_2 == "wait":
        choice_3 = input("Which door? type 'Red', 'Blue', 'Yellow': ")
        if choice_3 == "Red":
            print("Burned by fire. Game Over.")
        elif choice_3 == "Blue":
            print("Eaten by beasts. Game Over.")
        elif choice_3 == "Yellow":
            print("You win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")