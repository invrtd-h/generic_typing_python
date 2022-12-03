from parser.ptnodes import *


class Visitor:
    def visit(self, node: PtNode) -> PtNode:
        return getattr(self, node.name)(node)