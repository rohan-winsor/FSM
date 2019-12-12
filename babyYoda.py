from enum import Enum, unique
from random import randint

@unique
class STATE(Enum):
    AWAKE = 0
    SLEEP = 1
    EAT = 2
    FORCE = 3
    IDLE = 4


class Fsm:
    def __init__(self):
        self.state = STATE.AWAKE

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state


class BabyYoda(Fsm):
    def __init__(self):
        super().__init__()
        self.capactiy = 100

    def eating(self):
        if self.capactiy + 20 <= 100:
            self.capactiy += 20

    def useForce(self):
        self.capactiy -= 50

    def sleeping(self):
        if self.capactiy + 20 <= 100:
            self.capactiy += 20

    def printState(self):
        print(self.state)


if __name__ == "__main__":
    all_states = {1: STATE.EAT, 2: STATE.SLEEP, 3: STATE.FORCE, 4: STATE.IDLE}
    babyyoda = BabyYoda()
    count = 0
    while babyyoda.capactiy >= 0:
        print(babyyoda.capactiy)
        babyyoda.printState()
        s = randint(1,3)
        babyyoda.set_state(all_states[s])
        if babyyoda.get_state() == STATE.FORCE:
            babyyoda.useForce()
            babyyoda.printState()
        elif babyyoda.get_state() == STATE.SLEEP:
            babyyoda.sleeping()
            babyyoda.printState()
        elif babyyoda.get_state() == STATE.EAT:
            babyyoda.eating()
            babyyoda.printState()
        count += 1
    print(count)
