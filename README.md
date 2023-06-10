# [Where in the world is... Diego Santacarmen?!](https://pp3-diego-santacarmen.herokuapp.com/)

Where in the world is... Diego Santacarmen? is a command-line educational game that pays tribute to the 1985 classic ["Where in the world is Carmen Sandiego?"](https://en.wikipedia.org/wiki/Where_in_the_World_Is_Carmen_Sandiego%3F_(1985_video_game)#:~:text=Where%20in%20the%20World%20is%20Carmen%20Sandiego%3F%20is%20an%20educational,Facts%2C%20published%20by%20Pharos%20Books.).

The player will have to chase the thief while collecting clues and arrest the right suspect before time runs out.

[Play the game here!](https://pp3-diego-santacarmen.herokuapp.com/)

![Responsive Mockup](/assets/media/pp3_diego_santacarmen_resp.PNG)

## The game
The player is presented with the facts of the case and sent to the crime scene. There, they will have to interrogate the witnesses and follow the clues to either make an arrest, or travel to the next location where they will gather further clues. 

## Features

- ### __The Locations__

  - The player is placed in the first of 11 possible locations to visit, randomly selected as the victim city, where the crime has taken place. The object that is stolen does have a connection to the place, although it may not always seem very plausible.

    ![Screenshot of a case](/assets/media/case.PNG)
  
    ![Table of cities](/assets/media/cities.PNG)

  - During the game, the city where the player is currently located serves as the "screen" for that moment in the game. They present the options available to the player, and the player can, if they choose so, learn a little information about the city in question.

    ![Screenshot of a city screen](/assets/media/screen.PNG)

  - Additionally, the game keeps track of the places that have already been visited by the player and returns the information as a visual cue when deciding where to travel next.

    ![Screenshot of a travel screen](/assets/media/travel.PNG)


- ### __The Suspects__

  - Throughout the game, the player will collect clues that will help them figure out which of the usual suspect committed the crime.

    ![Table of suspects](/assets/media/suspects.PNG)
  
  - The player can choose to see the details in the individual suspect's file so they can match these with the clues collected and find the thief.

    ![Suspect details](/assets/media/suspect_details.PNG)

- ### __The clues__

  - In every city the player visits, they will be presented with 3 locations they can visit and interrogate witnesses. Of the 3 clues, 2 will point towards where the player needs to travel next, and 1 will give them information about the thief.

    ![Screenshot of locations](/assets/media/interrogation_locations.PNG)

  - Should the player need to, they can revisit the clues they have collected along the game and these are presented in order and with the name of the city where they were collected.

    ![Screenshot of clues](/assets/media/clues_capture.PNG)
  
  - __Watch out!__ If the player doesn't travel to the correct location, the clues they will receive from witnesses will be completely useless and they will have to travel back to the previous location, wasting precious time.

    ![Screenshot of bogus clue](/assets/media/bogus.PNG)
  
- ### __The Travel Sequence__

  - Once the player decides to travel, a basic animation of a dot travelling from the origin to the destination of the trip is presented, followed by a countdown displaying the time available for the player to catch the thief.

    ![Screenshot of travel](/assets/media/travel_1.PNG) 
    
    ![Screenshot of countdown](/assets/media/travel_2.PNG)

- ### __The Ending__

  - There are 3 possible scenarios in which the game may come to an end:
    1. The player runs out of time and the thief escapes:

    ![Screenshot out of time](/assets/media/out_of_time.PNG)

    2. The player arrests the incorrect suspect, allowing the thief to escape and thus, losing the game:

    ![Screenshot of incorrect suspect](/assets/media/wrong_suspect.PNG)

    3. The player arrests the thief, the stolen item is recovered and the player wins the game.

    ![Screenshot of thief caught](/assets/media/thief_caught.PNG)

  - As an additional feature, at the end of every game the player is presented with the option to start a new game, with a randomly selected thief, victim, etc. In the case of running a new game in this fashion, the game will skip the title sequence and remember the player's name:
    
    ![Screenshot of replay](/assets/media/replay.PNG)

## Under the Proverbial Hood

  - ### __Game Flowchart__

    > See below flowchart with the outline of the game logic:
    ![Game Flowchart](/assets/media/pp3_diego_santacarmen_flowchart.jpg)

 - ### __Helper Functions__
  The below minions have been defined to add to the visual appeal of the game:

  - clear()

    ```
    from os import system

    def clear():
        """
        Clears the terminal.
        See https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
        """
        system("clear")
    ```


  - t_print()
    ```
    def t_print(message):
    """
    Prints the passed string to the console, simulating a typewriter.
    """
    for char in message:
        sleep(0.05)
        print(char, end='', flush=True)
    ```


  - travel(origin, destination)
    ```
    def travel(origin, destination):
    """
    prints a sequence simulating the waiting time of a trip to the destination.
    """
    trip = [".         ", " .        ", "  .       ", "   .      ", "    .     ", "     .    ", "      .   ", "       .  ", "        . ", "         ."]
    for i in range(10):
        clear()
        print(f"{origin}{trip[i]}{destination}")
        sleep(0.3)
        cursor.hide()
    ```


## Future Development Opportunities

  - ### Here are some future implementations that were left for a further version:
    
    - __Rank promotion/demotion__: A reward-punishment logic can be implemented for every case resolution/failure so the player can ascend or fall in the ranks from traffic duty agent to Captain or Superintendent.

    - __Leaderboard__: building on the previous point, a leaderboard, could be implemented with the different players and their ranks.

    - __Coloured fonts/imagery__: as a visual improvement, colours can be implemented for the different sections/headings within the game, along with images/animations to be displayed.

## Testing and known issues

  - ### __Testing__

    - __PEP8__ The code has been submitted to the Code Institute PEP8 lint and all major issues were fixed. The ones that remain are due to strings being too long, or a character in a docstring that the lint recognizes erroneously as an escape character (L229). With regard to the strings length, it has been decided that they are to remain as is for design purposes.

      ![PEP8](/assets/media/pep8.PNG)

    - Every input request has been tested with blank and invalid inputs and they handle the data as expected.

    - The game has been tested both in the IDE's and heroku's terminals and they perform as expected.

  - ### __Known Issues__

    - An issue has been identified with the locations' descriptions' lengths. A function may be defined to parse through the individual strings and place line breaks in intervals so the text does not wrap breaking words.

    - When run on Heroku, the game title does is not cleared and users can scroll up in the terminal to see the game title. Since this does not disrupts the gameplay and remains almost inperceptible as an issue, ot has been decided to leave as-is.

  - ### __Bugs__
  No bugs have been found to remain in the code as presented.

## __Development and Version Control__

  - The chosen IDE for the development of the application was [Gitpod](https://www.gitpod.io/).

  - [GitHub](https://github.com) is the platform where the repository for "Where in the World is Diego Santacarmen" is hosted: [Jbocciadev Diego Santacarmen repository](https://github.com/jbocciadev/PP3_Diego_Santacarmen).

> Throughout development, the below commands were utilised to capture and store changes:
```
git add .
git commit -m "Message in quotation marks."
git push
```
>additionally
```
git pull
git stash
```

## __Deployment__
The application has been deployed to heroku. The steps taken were:

In heroku (https://dashboard.heroku.com/apps): 
    
  1. Open the "new" menu and click on "Create new app".
  2. Fill form fields with app name and region (Europe). Click on "Create app".
  3. In the "Settings" section, click on "Add buildpack" and add Python and NodeJS, __in that order__.
  4. In "Deployment method", select the GitHub option and provide the repository details. Click on "Connect".
  5. Click on "Enable Automatic Deploys" and finally, click on "Deploy Branch".


---------------########### CONTINUE HERE #########----------------

## Credits 

### Inspiration
- The first time I thought of building a web solution like Score! when, during an u-11 basketball match, the scoreboard was not working correctly and the audience had to keep track of the score by ourselves.

- It would be foolish of me not to mention [scorecount.com](https://scorecount.com/) and [rapidtables.com](https://www.rapidtables.com/tools/scoreboard.html). They were an obvious reference for me (*"If I hd known they existed before starting with this project, I would have probably built something else..."* :-D)

### Media
- The colour palette was extracted using [Coolors](https://coolors.co).
- The favicon was created using [Favicon](https://favicon.io).
- The icons used for social media links were sourced from [Fontawesome](https://fontawesome.com).

### Code
- [freeCodeCamp](https://www.freecodecamp.org/) were a huge help in understanding responsive design, relative dimensions, and were my first camp years ago.
- [Kevin Powell](https://www.kevinpowell.co/) CSS guru Kevin has changed the way I understand page layouts and keeps blowing my mind with his CSS videos on his [YouTube channel](https://youtube.com/kevinpowell). Hi 3-part "flexbox basics" playlist is a must-see for everyone (*"I wish I had seen this one before PP1"* XD).
- [W3Schools](https://www.w3schools.com/) were constantly open on my browser. My go-to HTML and CSS site. Of special importance was this [Article](https://www.w3schools.com/w3css/w3css_modal.asp). It is a small piece on the site, but it opened up a world pf possibilities.
- I cannot talk code without thanking Prof. David Malan and all the crew at HarvardX's [CS50X](https://cs50.harvard.edu/x/2023/)
- [stack __overflow__](https://stackoverflow.com/) if you code, you know ;-). This [article](https://stackoverflow.com/questions/1735230/can-i-add-a-custom-attribute-to-an-html-tag) was a life saver in my struggle against the HTML validator. Also [this](https://stackoverflow.com/questions/13551899/how-to-show-a-label-only-to-screen-readers-web-accessiblity) helped in adapting the page to screen readers without impacting on its layout.

### Other
- First and foremost, I owe gratitude to my family for dinners without me and days out I missed because I needed to sit and work on this project. Their support has always been unwavering.
- A masive thank you to my mentor, Spencer and his [5pence](https://5pence.net/) site.
- Thank you, thank you, thank you to the staff and colleagues at [Code Institute](https://codeinstitute.net). Course content, Tutoring sessions and (especially) Slack channels.