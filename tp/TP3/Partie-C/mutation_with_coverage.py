import self as self
from fuzzingbook.Fuzzer import Fuzzer, RandomFuzzer
from fuzzingbook.MutationFuzzer import MutationFuzzer
from fuzzingbook.Coverage import Coverage
import random
import url_parser
import matplotlib.pyplot as plt
from num2words import num2words
random.seed(1954607)

class MyFuzzer(Fuzzer):
    """Produce random inputs."""

    def __init__(self) -> None:
        """ fournir un range pour les nombres"""
        self.min_value=float(-200000)
        self.max_value=float(200000)


    def fuzz(self) -> float:
        """ retourne un nombre aleatoire"""
        return random.uniform( self.min_value, self.max_value)



def calculate_cumulative_coverage(input_population, function):
    cumulative_coverage = []
    all_coverage = set()
    
    for inp in input_population:
        with Coverage() as cov:
            try:
                function(inp)
            except:
                # we ignore exceptions for the purpose of this code, but some exceptions may be interesting
                pass
        # set union
        all_coverage |= cov.coverage()
        cumulative_coverage.append(len(all_coverage))
    return cumulative_coverage

def plot(cumulative_coverage):
    plt.plot(cumulative_coverage)
    plt.title('Coverage')
    plt.xlabel('# of inputs')
    plt.ylabel('lines covered')


trials = 500

""" construction des 3 differents fuzzers """
fuzzer1= RandomFuzzer()
fuzzer2 = MutationFuzzer(seed = ["3452020"])
fuzzer3 = MyFuzzer()

""" prend en parametre un fuzzer et calcule son coverage cumulative"""
def computeCumulativeCoverage(fuzzer):
    input_set = []
    for i in range(0, trials):
        input_set.append(fuzzer.fuzz())
    cumulative_coverage = calculate_cumulative_coverage(input_set, num2words)
    return cumulative_coverage


plot(computeCumulativeCoverage(fuzzer1))
plot(computeCumulativeCoverage(fuzzer2))
plot(computeCumulativeCoverage(fuzzer3))

plt.show()
