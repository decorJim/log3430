from fuzzingbook.Fuzzer import RandomFuzzer
import traceback # to get the stack trace
import random
import test_script
random.seed(1954607) # to fix the randomness

ranseed=1954607

random_fuzzer = RandomFuzzer()
trials = 100
for i in range(0, trials):
    inp = random_fuzzer.fuzz()
    print ("trial: %s \ninput: %s" % (i, inp))
    print ("le random seed: %s \n" % ranseed)
    try: 
        test_script.crash_if_too_long(inp)
    except ValueError:
        traceback.print_exc()
        break