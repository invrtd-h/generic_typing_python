from preprocessor.preprocess import preprocess
from semantic.visitor import Visitor
import syntax.parser
from utils import logger

if __name__ == '__main__':
    f = open("input.txt", 'r')
    s = f.read()
    f.close()

    s = preprocess(s)

    x = syntax.parser.parser.parse(s)
    v = Visitor()
    v.visit(x)

    v.node.traverse(callback=logger.log)

    logger.write_on_file(filename='output.txt')