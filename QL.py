import _pickle
import Utils as U
import numpy as np


class State(object):
    def __init__(self, name: str = '', ID: int = 0):
        self.actions: list = []
        self.name = name
        self.ID = ID


class Action(object):
    def __init__(self, name: str = '', ID: int = 0):
        self.state: State = State()
        self.name = name
        self.ID = ID


class Rule(object):
    def __init__(self, qValue: float = 0.0, nextState: State = State()):
        self.qValue = qValue
        self.nextState = nextState


class QTable(object):
    def __init__(self, rules: list = []):
        self.rules: list = rules


class QLearn:

    def __init__(self,
                 states: list,
                 actions: list,
                 qTable: list or None = None,
                 initState: int = 0,
                 learningRate: float = 0.25,
                 discountFactor: float = 0.5):
        self.qTable = qTable
        self.states = states
        self.actions = actions
        self.initState = initState

        assert learningRate > 0 and learningRate < 1
        self.learningRate = learningRate

        assert discountFactor > 0 and discountFactor < 1
        self.discountFactor = discountFactor

        if qTable == [] or qTable == None:
            self.qTable = np.zeros([len(states), len(actions)])

    def posibleActions(self) -> list:
        pass

    def nextAction(self) -> Action:
        pass

    def Update(self, state: State, action: Action, RewardOrPunish: float, nextState: State,
               learningRate: float or None = None, discountFactor: float or None = None):
        assert (learningRate > 0 and learningRate < 1) or learningRate == None
        assert (
            discountFactor > 0 and discountFactor < 1) or discountFactor == None

        alpha = self.learningRate if learningRate == None else learningRate
        gamma = self.discountFactor if discountFactor == None else discountFactor

        def _next_state_max_qvalue() -> float:
            pass

        qValue = self.qTable[state.ID, action.ID].qValue
        self.qTable[state.ID, action.ID].qValue = \
            (1-alpha) * qValue + (RewardOrPunish + gamma * _next_state_max_qvalue())

        pass


if __name__ == "__main__":

    data = []
    with open('data.pkl') as f:
        data = _pickle.load(f)


    pass
