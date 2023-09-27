class CrossRiver:
    # 人 羊 狼 菜
    def __init__(self):
        self.visited = set()
        self.visited.add((0, 0, 0, 0,))
        self.movement = [(1, 0, 0, 0), (1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1), (-1, -1, 0, 0), (-1, 0, -1, 0),
                         (-1, 0, 0, -1), (-1, 0, 0, 0)]  # 必须由人带东西过去,且只能带一个

    def is_legal(self, new_state):
        if new_state[1] == new_state[2] and new_state[0] != new_state[1]:  # 狼吃羊,人不在
            return False
        elif new_state[1] == new_state[3] and new_state[0] != new_state[1]:
            return False
        for mystate in new_state:
            if mystate > 1 or mystate < 0:
                return False
        return True

    def is_not_visited(self, new_state):
        if new_state not in self.visited:
            return True
        else:
            return False

    def move(self, state):
        if state == (1, 1, 1, 1):
            # 找到了解决方案
            print("找到解决方案：", self.visited)
            return
        for moves in self.movement:
            new_state = tuple(state[i] + moves[i] for i in range(4))
            if self.is_legal(new_state) and self.is_not_visited(new_state):
                self.visited.add(new_state)
                self.move(new_state)
                self.visited.remove(new_state)


state = (0, 0, 0, 0,)
mycrossriver = CrossRiver()
mycrossriver.move(state)
