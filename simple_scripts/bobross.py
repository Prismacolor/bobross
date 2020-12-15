import random

painting_colors = ['pale rose', 'magenta', 'alizarin crimson', 'red oxide', 'permanent red',
                   'indian yellow', 'yellow ochre', 'naples yellow',
                   'sage green', 'olive green', 'Hooker green', 'Jenkins green', 'terre vert hue',
                   'ultramarine', 'Prussian blue', 'Pthalo blue',
                   'violet', 'dioxazine purple',
                   'burnt sienna', 'raw sienna', 'burnt umber', 'Van Dyke brown',
                   'buff', 'titanium white']

tools = ['fan brush', 'mop brush', 'large pallette knife', 'filbert 0', 'filbert 2', 'filbert 4',
         'round shader', 'angle shader', 'spotter', 'dry brush', 'round brush 0', 'round brush 2',
         'small pallette knife', 'paint scraper', 'pallette spade']

canvas = ['small round', 'small square', 'small rectangle', 'taped border',
          'medium round', 'medium square', 'medium rectangle',
          'large square, large rectangle', 'utterly massive']


def main():
    palette = generate_colors()
    tools = get_tools()
    canvas = choose_canvas()

    print("Let's paint a neat little landscape today!")
    print("We're going to use a {0} canvas.".format(canvas))

    print("For tools, we're gonna use: ")
    print_line_by_line(tools)

    print("The colors you'll need today are: ")
    print_line_by_line(palette)


def generate_colors(num_colors=7):
    if num_colors <= 0:
        num_colors = 1

    palette = []
    colors_generated = 0

    while colors_generated < num_colors:
        color = random.choice(painting_colors)
        if color in palette:
            continue
        palette.append(color)
        colors_generated += 1

    return palette


def get_tools(num_tools=3):
    if num_tools <= 0:
        num_tools = 1

    kit = []
    tools_generated = 0

    while tools_generated < num_tools:
        tool = random.choice(tools)
        if tool in kit:
            continue
        kit.append(tool)
        tools_generated += 1

    return kit


def choose_canvas():
    my_canvas = random.choice(canvas)
    return my_canvas


def print_line_by_line(lines):
    for line in lines:
        print("\t- " + line)


if __name__ == "__main__":
    main()
