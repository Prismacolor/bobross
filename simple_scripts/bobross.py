import random

painting_colors = ['pale rose', 'magenta', 'alizarin crimson', 'red oxide', 'permanent red',
                   'indian yellow', 'yellow ochre', 'naples yellow',
                   'sage green', 'olive green', 'Hooker green', 'Jenkins green', 'terre vert hue'
                   'ultramarine', 'Prussian blue', 'Pthalo blue',
                   'violet', 'dioxazine purple',
                   'burnt sienna', 'raw sienna', 'burnt umber', 'Van Dyke brown',
                   'buff', 'titanium white']

tools = ['fan brush', 'mop brush', 'large pallette knife', 'filbert 0', 'filbert 2', 'filbert 4'
         'round shader', 'angle shader', 'spotter', 'dry brush', 'round brush 0', 'round brush 2',
         'small pallette knife', 'paint scraper', 'pallette spade']

canvas = ['small round', 'small square', 'small rectangle', 'taped border',
          'medium round', 'medium square', 'medium rectangle',
          'large square, large rectangle', 'utterly massive']


def main():
    my_pallette = generate_colors()
    my_tools = get_tools()
    canvas = choose_canvas()

    print("Let's paint a neat little landscape today!")
    print("We're going to use a {0} canvas.".format(canvas))

    print("For tools, we're gonna use: ")
    print_line_by_line(my_tools)

    print("The colors you'll need today are: ")
    print_line_by_line(my_pallette)


def generate_colors():
    pallette = []
    numofcolors = 0

    while numofcolors < 7:
        pallette_color = random.choice(painting_colors)
        if pallette_color in pallette:
            continue
        pallette.append(pallette_color)
        numofcolors += 1

    return pallette


def get_tools():
    kit = []
    numoftools = 0

    while numoftools < 3:
        painting_tool = random.choice(tools)
        if painting_tool in kit:
            continue
        kit.append(painting_tool)
        numoftools += 1

    return kit


def choose_canvas():
    my_canvas = random.choice(canvas)

    return my_canvas


def print_line_by_line(somelist):
    for item in somelist:
        print(item)


if __name__ == "__main__":
    main()
