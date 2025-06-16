import pandas as pd
from psychopy.gui import DlgFromDict
from psychopy.visual import Window, TextStim, ImageStim
from psychopy.core import Clock, quit, wait
from psychopy.event import Mouse
from psychopy.hardware.keyboard import Keyboard

### DIALOG BOX ROUTINE ###
exp_info = {'participant_nr': '', 'age': ''}
dlg = DlgFromDict(exp_info)

# If pressed Cancel, abort!
if not dlg.OK:
    quit()
else:
    # Quit when either the participant nr or age is not filled in
    if not exp_info['participant_nr'] or not exp_info['age']:
        quit()
        
    # Also quit in case of invalid participant nr or age
    if int(exp_info['participant_nr']) > 99 or int(exp_info['age']) < 18:
        quit()
    else:  # let's star the experiment!
        print(f"Started experiment for participant {exp_info['participant_nr']} "
                 f"with age {exp_info['age']}.")

# Initialize a fullscreen window with my monitor (HD format) size
# and my monitor specification called "samsung" from the monitor center
win = Window(size=(1920, 1080), fullscr=False, monitor='samsung')

# Also initialize a mouse, although we're not going to use it
mouse = Mouse(visible=True)

# Initialize a (global) clock
clock = Clock()

# Initialize Keyboard
kb = Keyboard()
kb.clearEvents()

### START BODY OF EXPERIMENT ###


### WELCOME ROUTINE ###
# Create a welcome screen and show for 2 seconds
welcome_txt_stim = TextStim(win, text="Welcome to this experiment!", color=(1, 0, -1), font='Calibri', height= 0.2)
welcome_txt_stim.draw()
win.flip()
wait(2.0)
win.flip()
wait(2.0)


win = Window(size=(1920, 1080), fullscr=False, monitor='samsung')

# Also initialize a mouse, although we're not going to use it
mouse = Mouse(visible=True)

# Initialize a (global) clock
clock = Clock()

# Initialize Keyboard
kb = Keyboard()
kb.clearEvents()

mood_txt = """ 
On a scale of 1-5, rate your current mood:
    1= Angry
    3= Neutral
    5= Happy

 """

# Show mood question and wait until response (return)
mood_txt = TextStim(win, mood_txt, alignText='left', height=0.085)
mood_txt.draw()
win.flip()

valid_mood_keys = ['1', '2', '3', '4', '5']
mood_response = None
while mood_response not in valid_mood_keys:
    keys = kb.getKeys()
    for key in keys:
        if key.name in valid_mood_keys:
            mood_response = key.name
            break
            
mood_rating = int(mood_response)

if mood_rating < 3:
    mood_image_file = 'angry.png'
elif mood_rating == 3:
    mood_image_file = 'neutral.png'
else:
    mood_image_file = 'happy.png'

mood_img = ImageStim(win, image=mood_image_file)
mood_img.size *= 0.8
mood_img.draw()
win.flip()
wait(3)

conditions_df = pd.read_excel('emo_conditions.xlsx')
conditions_df['participant_feeling'] = feeling_label

# Save updated DataFrame to a new Excel file (to prevent overwriting original)
conditions_df.to_excel('emo_conditions_updated.xlsx', index=False)

# CLOSE WINDOW AND END EXPERIMENT
win.close()
quit()







