def brain_luck(code, input_):
    vars = {'tape': [0] * 30000, 'p': 0, 'input': list(input_), 'res': ''}
    py_code = []
    indent = 0
    for c in code:
        cur_indent = indent
        if c == '>': line = 'p += 1'
        elif c == '<': line = 'p -= 1'
        elif c == '+': line = 'tape[p] = (tape[p] + 1) % 256'
        elif c == '-': line = 'tape[p] = (tape[p] - 1) % 256'
        elif c == '.': line = 'res += chr(tape[p])'
        elif c == ',': line = 'tape[p] = ord(input.pop(0))'
        elif c == '[': line = 'while tape[p]:'; indent += 1
        elif c == ']': line = ''; indent -= 1
        py_code.append('\t' * cur_indent + line)
    exec('\n'.join(py_code), vars)
    return vars['res']
