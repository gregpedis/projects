import numpy as np
import os
import configparser as cp

config = cp.ConfigParser()
config.read('config.ini')

state_space = {}


def get_filenames():
    base = config['FOLDERS']['Base']
    dataset = config['FOLDERS']['Dataset']

    path = os.path.join(os.getcwd(), base, dataset)
    os.chdir(path)

    return [f for f in os.listdir() if f.endswith('.txt')]


def parse_file(fname):
    with open(fname, 'rt', encoding='utf8') as f:
        for title in f.readlines():
            parse_title(title)


def parse_title(title):
    words = title.split()
    for w1, w2 in enumerate_pairs(words):
        if w1 in state_space.keys():
            state_space[w1].append(w2)
        else:
            state_space[w1] = [w2]


def enumerate_pairs(words):
    for i in range(len(words)-1):
        yield (words[i], words[i+1])


def create_state_space():
    fnames = get_filenames()
    for fname in fnames:
        parse_file(fname)


if __name__ == "__main__":

    create_state_space()
    results = []

    tcount = int(config['COUNT']['Title'])
    wcount = int(config['COUNT']['Word'])

    for t in range(tcount):
        seeds = list(state_space.keys())
        first_word = np.random.choice(seeds)
        chain = [first_word]
        
        for i in range(wcount):
            if chain[-1] in state_space.keys():
                chain.append(np.random.choice(state_space[chain[-1]]))

        result = ' '.join(chain)
        results.append(result + '\n')

    with open('../filename.txt','wt+') as f:
        f.writelines(results)
    