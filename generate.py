import os

TOPDIR = './python'

def generate_file_header(filename, filepath):
    return ('\\section{{{}}}\n'.format(filename) +
            r'\begin{lstlisting}[language=Python]' + '\n')

def generate_file_footer(filename):
    return r'\end{lstlisting}'

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
            codeblock = (generate_file_header(filename, d) +
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
