import os

LANGS = [
    ('Python', '.py', './python'),
    ('C++', '.cc', './cpp'),
]

def generate_file_header(filename, filepath, lang):
    return ('\\section{{{}}}\n'.format(filepath) +
            r'\begin{lstlisting}[language=' + lang + ']\n')

def generate_file_footer(filename):
    return r'\end{lstlisting}'

def main():
    out = []
    for lang, ext, top_dir in LANGS:
        for path, dirs, files in os.walk(top_dir):
            for filename in files:
                if not filename.endswith(ext):
                    continue
                if filename.endswith('.test' + ext):
                    continue
                print(filename)
                d = os.path.join(path, filename)
                code = []
                with open(d) as f:
                    for line in f:
                        # Remove newlines at end of lines.
                        line = line.rstrip()
                        if (line.lower().startswith('# todo') or
                            line.lower().startswith('##')):
                            continue
                        if len(line) == 0:
                            continue
                        code.append(line)
                codeblock = (generate_file_header(filename, d, lang) +
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
