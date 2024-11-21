import pickle
from ancestry_pack import Ancestry
import os

class Saver:
    def __init__(self):
        self.path = 'ancestry_pack/ancestry_data/ancestry.pickle'

    def save(self, ancestry: Ancestry):
        with open(self.path, 'wb') as f:
            pickle.dump(ancestry, f)


class Loader:
    def __init__(self):
        self.path = 'ancestry_pack/ancestry_data/ancestry.pickle'

    def load(self) -> Ancestry:
        if not os.path.exists(self.path):
            with open(self.path, 'w') as f:
                pass
        with open(self.path, 'rb') as f:
            anc = pickle.load(f)
        return anc
