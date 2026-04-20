def hanoi_solver(n):
    A = [i for i in range(n, 0, -1)]
    B = []
    C = []
    
    text = f"{A} {B} {C}\n"

    def solve(n, source, auxiliary, target):
        nonlocal text

        if n == 1:
            target.append(source.pop())
            text += f"{A} {B} {C}\n"
            return

        solve(n-1, source, target, auxiliary)

        target.append(source.pop())
        text += f"{A} {B} {C}\n"

        solve(n-1, auxiliary, source, target)

    solve(n, A, B, C)
    return text.strip()
