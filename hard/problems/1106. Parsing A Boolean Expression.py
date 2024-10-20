class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def evaluate(expr: str) -> bool:
            if expr == "t":
                return True
            if expr == "f":
                return False

            if expr[0] == '!':
                return not evaluate(expr[2:-1])

            op = expr[0]
            sub_exprs = []
            count = 0
            start = 2

            for i in range(2, len(expr)):
                if expr[i] == '(':
                    count += 1
                elif expr[i] == ')':
                    count -= 1
                elif expr[i] == ',' and count == 0:
                    sub_exprs.append(expr[start:i])
                    start = i + 1

            sub_exprs.append(expr[start:-1])

            if op == '&':
                return all(evaluate(sub) for sub in sub_exprs)
            elif op == '|':
                return any(evaluate(sub) for sub in sub_exprs)

        return evaluate(expression)
