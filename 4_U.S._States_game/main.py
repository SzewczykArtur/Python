import pandas
import turtle

screen = turtle.Screen()
screen.title('U. S. States Game')

img = 'blank_states_img.gif'
screen.addshape(img)
screen.setup(width=725, height=491)
turtle.shape(img)


# Get a x and y with clicking mouse on screen:
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv('50_states.csv')
counter = 0
game_is_on = True
state_list = data['state'].to_list()

all_ready_type = []

while game_is_on:
    answer_state = screen.textinput(title=f'{counter}/50 Guess the State', prompt="What's another state's name").title()
    if answer_state.capitalize() in all_ready_type:
        print('You are repeat!')
    elif answer_state in state_list:
        print('Correct')
        counter += 1
        all_ready_type.append(answer_state.capitalize())
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        x = state_data.iloc[0].x
        y = state_data.iloc[0].y
        t.goto(x, y)
        t.write(answer_state)
    elif counter == 50 or answer_state.lower() == 'end':
        game_is_on = False
        print('Game is over!')
    else:
        print('Wrong')

