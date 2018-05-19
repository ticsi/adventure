print('You are standing in the middle of a maze.')
print('Which way will you go?')
print('1 left')
print('2 right')

choice = input()
if choice == '1':
    print('You take a few steps to the left. '
          'Suddenly you hear a faint clicking sound, '
          'and in the next moment you are crushed to death '
          'by a huge, spikey rock. Game over.')

elif choice == '2':
    print('You see a distant light from the right end of the maze, '
          'so you decide to approach it. '
          'After a few minutes of walking, '
          'you come across a door that is slightly open. '
          'When you open it, you find yourself in an aincent stairway; '
          'the stairs lead both up and down.')
    print('Which way do you continue?')
    print('1 up')
    print('2 down')

    choice = input()
    if choice == '1':
        print('You start walking upwards. The stairs continue for so long that '
              'your feet start burning, but you don\'t stop. '
              'You slowly feel the air becoming warmer and clearer, '
              'and soon you reach a thick, wooden trapdoor, light shining '
              'trough its cracks. You push it open, and you find yourself in '
              'a calm, sunlit forest. A creek flows nearby and a path leads '
              'next to it, towards a distant settlement. You made it out.')

    elif choice == '2':
        print('You decide to go down. As you are descending, '
              'the air becomes colder and heavier, '
              'but you continue anyway. After a while, '
              'it becomes so dark that you can\'t even see your own hands.'
              'You hear a deep growl from below, and suddenly, '
              'you feel a huge mass darting in your direction. '
              'This is the last thing you experience in your life. Game over.')

    else:
        print('Error.')

else:
    print('Error.')
