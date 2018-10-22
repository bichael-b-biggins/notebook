import os

TOPDIR = './python'

def generate_file_header(filename):
    return '\\section{{{}}}\n\\begin{{verbatim}}'.format(filename)

def generate_file_footer(filename):
    return '\\end{{verbatim}}'.format(filename)

def main():
    out = []
    for path, dirs, files in os.walk(TOPDIR):
        for filename in files:
            if not filename.endswith('.py'):
                continue
            d = os.path.join(path, filename)
            code = []
            with open(d) as f:
                for line in f:
                    # Remove newlines at end of lines.
                    line = line.rstrip()
                    if (line.lower().startswith('# todo') or
                        line.lower().startswith('##')):
                        continue
                    code.append(line)
            codeblock = (generate_file_header(filename) +
                         '\n'.join(code) +
                         generate_file_footer(filename))
            out.append(codeblock)
    total_content = '\n'.join(out)

    # Escape hash, as it is a special character in Tex.
    #total_content = total_content.replace('#', '\\#')
    with open('content_python.tex', 'w') as f:
        f.write(total_content)
    
if __name__ == '__main__':
    main()
