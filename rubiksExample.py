from rubiks import *

exampleRubiks = rub = Rubiks(2)

rub.config[0][0][0] = color.orange
rub.config[0][0][1] = color.red
rub.config[0][1][0] = color.yellow
rub.config[0][1][1] = color.green

rub.config[1][0][0] = color.blue
rub.config[1][0][1] = color.orange
rub.config[1][1][0] = color.blue
rub.config[1][1][1] = color.green

rub.config[2][0][0] = color.red
rub.config[2][0][1] = color.yellow
rub.config[2][1][0] = color.red
rub.config[2][1][1] = color.orange

rub.config[3][0][0] = color.green
rub.config[3][0][1] = color.white
rub.config[3][1][0] = color.green
rub.config[3][1][1] = color.blue

rub.config[4][0][0] = color.white
rub.config[4][0][1] = color.white
rub.config[4][1][0] = color.white
rub.config[4][1][1] = color.orange

rub.config[5][0][0] = color.yellow
rub.config[5][0][1] = color.blue
rub.config[5][1][0] = color.yellow
rub.config[5][1][1] = color.red

rubB = RubiksBFS(rub)

print(rubB.runSingleBFS())
print()