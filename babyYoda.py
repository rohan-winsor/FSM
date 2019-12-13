from enum import Enum, unique
from random import randint
import time 


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

    def printState(self, list1):
        # print(list1)
        print(list1[1])
        # pass


if __name__ == "__main__":
    all_states = {1: [STATE.EAT, "Eating...."], 2: [STATE.SLEEP, "Sleeping..."], 3: [\
        STATE.FORCE, "Using Force..."], 4: [STATE.IDLE, "Cooing....."]}
    babyyoda = BabyYoda()
    count = 0
    while babyyoda.capactiy > 0:
        time.sleep(2)
        print("Health ::", babyyoda.capactiy)
        s = randint(1, 4)
        babyyoda.set_state(all_states[s][0])
        if babyyoda.get_state() == all_states[3][0]:
            babyyoda.useForce()
            babyyoda.printState(all_states[3])
        elif babyyoda.get_state() == all_states[2][0]:
            babyyoda.sleeping()
            babyyoda.printState((all_states[2]))
        elif babyyoda.get_state() == all_states[1][0]:
            babyyoda.eating()
            babyyoda.printState((all_states[1]))
        elif babyyoda.get_state() == all_states[4][0]:
            babyyoda.eating()
            babyyoda.printState((all_states[4]))
        else:
            break
        count += 1
    print("Number of Inter :",count)
