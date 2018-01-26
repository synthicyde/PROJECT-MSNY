# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#images
image de = "devon_test.png"

#backgrounds
image bg_intro = "bg_intro.jpg"

#characters
define de = Character("Devon")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_intro

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show de

    # These display lines of dialogue.

    de "Hey! I see you downloaded the repository and figured out how to add it to Ren'Py!"
    de "Who am I talking to here?"
    
    menu:
        "Troy":
            de "Oh yeah, you're the project manager right?"
        "Dev":
            de "Oh, you're the coder."
        "George":
            de "The writer. How's the story coming along?"
        "Shaina":
            de "The muscian! Start on anything yet?"
    
    de "Anyways..."
    de "This was just a test run."
    de "I made this avatar of me using some software I got a while ago."
    de "(They don't have male avatar's yet.)"
    de "But really, I just made this as a start."
    de "Start looking at Ren'Py's documentation and well get stuff started."
    de "Talk to you soon!"
    
    return