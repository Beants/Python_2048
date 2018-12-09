# 类名：main
# 功能：主界面
# 时间：2018-5-1 晚
# 作者：beants

import os
import Calculate
import UI

# 注册UI组建 生成矩阵信息
ui = UI.UI()
calu = Calculate.Calculate()
calu.set_a_random(ui.game_matrix)
global GameOver
GameOver = False
while not GameOver:
    os.system('clear')
    ui.printUI()
    temp = input('\n请输入你的操作（上：w 下：s 左：a 右：d ）\n')
    print(temp)
    # print(ui.game_matrix)
    if temp == 'w':
        score = calu.up(ui.game_matrix)

    elif temp == 's':
        score =calu.down(ui.game_matrix)
    elif temp == 'd':
        calu.right(ui.game_matrix)
    elif temp == 'a':
        calu.left(ui.game_matrix)
    elif temp == 'q':
        break
    else:
        print('输入错误，请重新输入！')
    ui.set_score(score)

    gameover = calu.set_a_random(ui.game_matrix)

    if not gameover:
        break

print('GameOver!')
