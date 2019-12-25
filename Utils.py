import _pickle
import numpy as np

import Utils as U


def UniqueValues(data: list, col: int) -> tuple:
    value, count = np.unique([_[col].strip() for _ in data], return_counts=True)
    return value.tolist(), count.tolist()


if __name__ == "__main__":

    data = []
    with open('data.pkl', 'rb') as f:
        data = _pickle.load(f)

    print(U.UniqueValues(data[1:], 1))
    print(U.UniqueValues(data[1:], 2))
    print(U.UniqueValues(data[1:], 5))
    print(U.UniqueValues(data[1:], 6))
    print(U.UniqueValues(data[1:], 7))

    pass
