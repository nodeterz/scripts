import yaml
import random
input_stream = open('posinp.yaml','r')
output_stream = open('posinp_out.yaml','w')
dict_list = list(yaml.load_all(input_stream))
print dict_list[0]['conf']['coord'][0][2]
for atom in dict_list[0]['conf']['coord']:
    for term in range(3):
        term = str(float(term) + random.random()*3)
output_stream.write('---\n')
yaml.dump(dict_list[0],output_stream)
