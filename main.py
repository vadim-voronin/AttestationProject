from algorithm import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '-i',
    '–-input-data-path',
    type=str,
    defaul=None,
    help='путь до файла с метками'
)

parser.add_argument(
    '-n',
    '–-n-iterations',
    type=int,
    defaul=0,
    help='кол-во итераций Монте-Карло'
)

parser.add_argument(
    '-o',
    '–-output-pic-path',
    type=str,
    defaul=None,
    help='путь, куда сохранять картинку'
)

parser.add_argument(
    '-p',
    '–-probs',
    type=list,
    defaul=[],
    help='вероятности классов'
)


arg = parser.parse_args()
A = ProbsAlgo(arg.i, arg.p, arg.n)
A.plot_and_save_result(arg.o)