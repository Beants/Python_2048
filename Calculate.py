# 类名：Calculate
# 功能：计算
# 时间：2018-5-1 晚
# 作者：beants
class Calculate:
    def __init__(self):
        pass

    def set_a_random(self, matrix):
        import random
        num_kong = 0
        list_kong = []

        for i in range(4):
            for j in range(4):
                if matrix[i][j] == 0:
                    list_kong.append([i, j])
                    num_kong += 1
        if num_kong == 0:
            return False
        num = random.randint(0, num_kong - 1)
        random_num = random.randint(1, 2) * 2

        matrix[list_kong[num][0]][list_kong[num][1]] = random_num
        return matrix

    def up(self, matrix):
        # 循环计算
        # 相加
        # 竖着的
        temp_score = 0
        for i in range(4):
            # 横着的
            for j in range(4):
                # 如果有数的这个位置在最上面一行
                if j == 0:
                    pass
                else:
                    # 如果两个数相等，则相加
                    if matrix[j][i] == matrix[j - 1][i] and matrix[j][i] is not 0:
                        matrix[j - 1][i] += matrix[j][i]
                        matrix[j][i] = 0
                        # 计算分数
                        temp_score += matrix[j - 1][i]

        for i in range(4):
            # 横着的
            for t in range(4):
                for j in range(4):
                    # 相加
                    # 如果J置在最上面一行
                    if j == 0:
                        pass
                    else:
                        # 向上移动
                        if matrix[j - 1][i] == 0 and matrix[j][i] != 0:
                            matrix[j - 1][i] = matrix[j][i]
                            matrix[j][i] = 0
                            # 向上移动之后还需要判断是不是继续相加

                            if matrix[j - 1][i] == matrix[j - 1 - 1][i] and matrix[j - 1][i] is not 0:
                                matrix[j - 1 - 1][i] += matrix[j - 1][i]
                                matrix[j - 1][i] = 0
                                # 计算分数
                                temp_score += matrix[j - 1 - 1][i]

        return temp_score

    def down(self, matrix):
        # 循环计算
        # 相加
        # 竖着的
        temp_score = 0
        for i in range(4):
            # 横着的
            for j in range(4):
                # 如果有数的这个位置在最上面一行
                if j == 3:
                    pass
                else:
                    # 如果两个数相等，则相加
                    if matrix[3 - j][i] == matrix[3 - j - 1][i] and matrix[3 - j][i] != 0:
                        matrix[3 - j][i] += matrix[3 - j - 1][i]
                        matrix[3 - j - 1][i] = 0
                        temp_score += matrix[3 - j][i]

        for i in range(4):
            # 横着的
            for t in range(4):
                for j in range(4):
                    # 相加
                    # 如果J置在最上面一行
                    if j == 3:
                        pass
                    else:
                        # 向下移动
                        if matrix[j + 1][i] == 0 and matrix[j][i] != 0:
                            matrix[j + 1][i] = matrix[j][i]
                            matrix[j][i] = 0
                            # +1 是因为元素交换了位置
                            if matrix[3 - j + 1][i] == matrix[3 - j - 1 + 1][i] and matrix[3 - j + 1][i] != 0:
                                matrix[3 - j + 1][i] += matrix[3 - j - 1 + 1][i]
                                matrix[3 - j - 1 + 1][i] = 0
                                temp_score += matrix[3 - j + 1][i]
        return temp_score

    def left(self, matrix):
        # 循环计算
        # 相加
        # 横着的
        temp_score = 0
        for j in range(4):
            # 竖着的
            for i in range(4):
                # 如果有数的这个位置在最上面一行
                if i == 0:
                    pass
                else:
                    # 如果两个数相等，则相加
                    if matrix[j][i] == matrix[j][i - 1] and matrix[j][i] != 0:
                        matrix[j][i - 1] += matrix[j][i]
                        matrix[j][i] = 0
                        temp_score += matrix[j][i - 1]

        for j in range(4):
            # 横着的
            for t in range(4):
                for i in range(4):
                    # 相加
                    # 如果I置在最上面一列
                    if i == 0:
                        pass
                    else:
                        # 向左移动
                        if matrix[j][i - 1] == 0 and matrix[j][i] != 0:
                            matrix[j][i - 1] = matrix[j][i]
                            matrix[j][i] = 0

                            if matrix[j][i - 1] == matrix[j][i - 1 - 1] and matrix[j][i - 1] != 0:
                                matrix[j][i - 1 - 1] += matrix[j][i - 1]
                                matrix[j][i - 1] = 0
                                temp_score += matrix[j][i - 1 - 1]
        return temp_score

    def right(self, matrix):
        # 循环计算
        # 相加
        # 横着的
        temp_score = 0
        for j in range(4):
            # 竖着的
            for i in range(4):
                # 如果有数的这个位置在最上面一行
                if i == 3:
                    pass
                else:
                    # 如果两个数相等，则相加
                    if matrix[j][3 - i] == matrix[j][3 - i - 1] and matrix[j][3 - i] != 0:
                        matrix[j][3 - i - 1] += matrix[j][3 - i]
                        matrix[j][3 - i] = 0
                        temp_score += matrix[j][3 - i - 1]

        for j in range(4):
            # 横着的
            for t in range(4):
                for i in range(4):
                    # 相加
                    # 如果I置在最上面一列
                    if i == 3:
                        pass
                    else:
                        # 向上移动
                        if matrix[j][i + 1] == 0 and matrix[j][i] != 0:
                            matrix[j][i + 1] = matrix[j][i]
                            matrix[j][i] = 0

                            if matrix[j][3 - i + 1] == matrix[j][3 - i - 1 + 1] and matrix[j][3 - i + 1] != 0:
                                matrix[j][3 - i - 1 + 1] += matrix[j][3 - i + 1]
                                matrix[j][3 - i + 1] = 0
                                temp_score += matrix[j][3 - i - 1 + 1]
        return temp_score


if __name__ == '__main__':
    temp = Calculate().up(matrix=[[0, 0, 0, 0], [4, 0, 0, 0], [2, 0, 0, 0], [2, 0, 0, 0]])
