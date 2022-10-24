from fuzzingbook.MutationFuzzer import MutationFuzzer
import random
import url_parser

random.seed(1954607)
ranseed=1954607
seed = "https ://www.polymtl.ca/"
mutation_fuzzer = MutationFuzzer([seed])

valid_inputs = set()
trials = 40

print("the random seed %s\n" % ranseed)

for i in range(trials):
    inp = mutation_fuzzer.fuzz()
    print ("input " + inp)
    if url_parser.is_valid_url(inp):
        valid_inputs.add(inp) 

percentage_of_valid_url = (len(valid_inputs)/ trials)*100
        
        
print ("%s of the generated inputs are valid URLs" % percentage_of_valid_url)