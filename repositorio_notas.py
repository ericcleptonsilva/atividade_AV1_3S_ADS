
import random

class RepoNotas:
    def gen_notas(self):
        nota = random.uniform(1, 10)
        return float('{:.1f}'.format(nota))
