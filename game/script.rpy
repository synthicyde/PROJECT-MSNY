# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#images
image devon = "devon_test.png"
image noved = "tset_noved.png"

#backgrounds
image bg_intro = "bg_intro.jpg"
image bg_outro = "bg_outro.png"

#characters
define devon = Character("Devon")
define nevod = Character("Nevod")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music "Synthicide.mp3" fadeout 1
    scene bg_intro

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show devon

    # These display lines of dialogue.

    devon "Hey! I see you downloaded the repository and figured out how to add it to Ren'Py!"
    devon "Who am I talking to here?"
    
    menu:
        "Troy":
            devon "Oh yeah, you're the project manager right?"
            jump choice_devon_done
        "Dev":
            devon "Oh, you're the coder."
            jump choice_devon_done
        "George":
            devon "The writer. How's the story coming along?"
            jump choice_devon_done
        "Shaina":
            devon "The muscian! Start on anything yet?"
            jump choice_devon_done
        "Devon":
            jump choice_devon
    
label choice_devon:

    devon "Oh, you write the dialogue."
    
    stop music fadeout 1
    
    devon "Wait, but I'm Devon! We can't BOTH be Devon."
    devon "Unless..."
    
    scene bg_outro
    play music "edycihtnys.mp3" fadeout 1
    show noved
    
    nevod ".GYRF FPSB RAPWQBQ YRD RQIIVFS MYRL VOMZ FHZIUGG ZLW UQIIUQ ZGMZ V"
    nevod ".SH IJASGPDUQ YRD AWVQRQ MH VHGBZ YRL SMEG JCC" 
    nevod ".IUHHVIUP ZPSI HCT CREHNIG YZDA L"
    nevod ".GYRF FPSB RAPWQBQ YRD RQIIVFS MYRL VOMZ FHZIUGG ZLW UQIIUQ ZGMZ V"
    nevod ".SH IJASGPDUQ YRD AWVQRQ MH VHGBZ YRL SMEG JCC" 
    nevod ".IUHHVIUP ZPSI HCT CREHNIG YZDA L"
    nevod ".GYRF FPSB RAPWQBQ YRD RQIIVFS MYRL VOMZ FHZIUGG ZLW UQIIUQ ZGMZ V"
    nevod ".SH IJASGPDUQ YRD AWVQRQ MH VHGBZ YRL SMEG JCC" 
    nevod ".IUHHVIUP ZPSI HCT CREHNIG YZDA L"
    nevod ".GYRF FPSB RAPWQBQ YRD RQIIVFS MYRL VOMZ FHZIUGG ZLW UQIIUQ ZGMZ V"
    nevod ".SH IJASGPDUQ YRD AWVQRQ MH VHGBZ YRL SMEG JCC" 
    nevod ".IUHHVIUP ZPSI HCT CREHNIG YZDA L"
    nevod ".GYRF FPSB RAPWQBQ YRD RQIIVFS MYRL VOMZ FHZIUGG ZLW UQIIUQ ZGMZ V"
    nevod ".SH IJASGPDUQ YRD AWVQRQ MH VHGBZ YRL SMEG JCC" 
    nevod ".IUHHVIUP ZPSI HCT CREHNIG YZDA L"
    
    jump choice_devon_done
    
label choice_devon_done:
    
    scene bg_intro
    play music "Synthicide.mp3" fadeout 1
    show devon
    
    devon "Anyways..."
    devon "This was just a test run."
    devon "I made this avatar of me using some software I got a while ago."
    devon "(They don't have male avatar's yet.)"
    devon "But really, I just made this as a start."
    devon "Start looking at Ren'Py's documentation and well get stuff started."
    devon "Talk to you soon!"
    
    return