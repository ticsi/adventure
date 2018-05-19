gamebook = {
    0: (
        'You are standing in the middle of a maze. '
        'Which way will you go?',
        [
            ('left', 1),
            ('right', 2)
        ]
    ),

    1: (
        'You take a few steps to the left. '
        'Suddenly you hear a faint clicking sound, '
        'and in the next moment you are crushed to death '
        'by a huge, spikey rock. Game over.',
        []
    ),

    2: (
        'You see a distant light from the right end of the maze, '
        'so you decide to approach it. '
        'After a few minutes of walking, '
        'you come across a door that is slightly open. '
        'When you open it, you find yourself in an aincent stairway; '
        'spiral stairs lead both up and down. '
        'Which way do you continue?',
        [
            ('up', 3),
            ('down', 4),
            ('go back', 0)
        ]
    ),

    3: (
        'You start walking upwards. The stairs continue for so long that '
        'your feet start burning, but you don\'t stop. '
        'You slowly feel the air becoming warmer and clearer, '
        'and soon you reach a thick, wooden trapdoor, light shining '
        'trough its cracks. You push it open, and you find yourself in '
        'a calm, sunlit forest. A creek flows nearby and a path leads '
        'next to it, towards a distant settlement. You made it out.',
        []
    ),

    4: (
        'You decide to go down. As you are descending, '
        'the air becomes colder and heavier, '
        'but you continue anyway. After a while, '
        'it becomes so dark that you can\'t even see your own hands.'
        'You hear a deep growl from below, and suddenly, '
        'you feel a huge mass darting in your direction. '
        'This is the last thing you experience in your life. Game over.',
        []
    )
}


def print_options(options):
    for number, option in enumerate(options):
        print(f'{number + 1} {option[0]}')


def select_option(options):
    choice = input('Your choice: ')
    try:
        choice = int(choice) - 1
        return options[choice]
    except (ValueError, IndexError):
        return None


index = 0
while True:
    page = gamebook[index]
    story = page[0]
    print(story)
    print()
    options = page[1]

    print_options(options)

    if len(options) > 0:
        print()
        option = select_option(options)
        print()
        if (option is None):
            print('Error.')
            break
        else:
            index = option[1]
    else:
        break
