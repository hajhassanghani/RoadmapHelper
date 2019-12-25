import _pickle
import Utils as U
import numpy as np


class QLearn:
    def __init__(self,
                 states: list,
                 actions: list,
                 qTable: list or None = None,
                 currentState: int = 0,
                 learningRate: float = 0.25,
                 discountFactor: float = 0.25):
        self.qTable = qTable
        self.states = states
        self.actions = actions
        self.currentState = currentState

        assert learningRate > 0 and learningRate < 1
        self.learningRate = learningRate

        assert discountFactor > 0 and discountFactor < 1
        self.discountFactor = discountFactor

        if qTable == [] or qTable == None:
            self.qTable = np.zeros([len(states), len(actions)])

    def Update(self, nextState: int):
        alpha = self.learningRate
        gamma = self.discountFactor

        if not nextState == self.currentState:
            Reward = +1

            def _next_state_max_qvalue() -> float:
                return np.max(self.qTable[nextState, :])

            qValue = self.qTable[self.currentState, nextState]
            self.qTable[self.currentState, nextState] = \
                (1-alpha) * qValue + (Reward - gamma * _next_state_max_qvalue())

            self.currentState = nextState


if __name__ == "__main__":

    data = []
    with open('data.pkl', 'rb') as f:
        data = _pickle.load(f)

    GroupByPivot = U.GroupByPivot(data[1:], 7)

    states = list(GroupByPivot.keys())
    actions = list(GroupByPivot.values())

    ql = QLearn(states[:6], actions[:6])

    while True:
        q = int(input('Choose The Next Location: '))
        ql.Update(q)
        print(ql.qTable)

    pass
