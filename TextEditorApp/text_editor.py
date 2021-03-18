# TEXT FILE EDITOR APP
import os, re

pkg = "C:\\Users\\Welcome\\Desktop\\MyFuncs"
if pkg not in os.sys.path:
    os.sys.path.append(pkg)

# print(os.sys.path)
from fave_app_funcs import num_inp, sentence_inp, ask_to_save, ask_next, file_path_inp
from myio_funcs import read_allfile_content


editor = EditorApp()

EDITOR =True
while EDITOR:

    # open text file
    path,file,ext = file_path_inp()

    file_path = f"{path}\\{file}.{ext}"

    FOUND,text = read_allfile_content(path,file,ext)
    if not(FOUND):
        print(f"\nEnter a valid file name!")
        break
    # store the original text
    editor.original_text = text

    # label each line
    editor.label_lines()

    # select mode menu
    MODE = True
    while MODE:
        # display lines of file
        editor.view_file_text()

        # user selects mode from options
        mode = editor.add_or_edit()

        if mode == 'add':
            INSERTING = True
            while INSERTING:
                editor.insert_lines()

                editor.save_changes(file_path)

                prompt = "\nTo insert another line, enter 'y'\nTo stop, enter 'n'
                if ask_next(prompt):
                    continue

                prompt = "\nTo continue with current file enter yes, to exit enter no"
                if not(ask_next(prompt)):
                    INSERTING = False
                    MODE = False
                    EDITOR = False
                    break

        else:

            # prompt user for line number of bad text
            print("\nWhat line do you want to change?")
            prompt = "\nEnter below:\nLineNumber>\t"

            # collecting the first and last lines
            line_ind = re.findall(r"\d+", ', '.join([label for label in labelled_lines.keys()]))
            first,last = sorted([eval(ind) for ind in line_ind])[0], sorted([eval(ind) for ind in line_ind])[-1]
            lim = (first,last+1)
            repl_line = num_inp(prompt,lim)

            # user inputs the new text
            prompt = "\nEnter replacement text below\nText>\t"
            repl_text = sentence_inp(prompt)

            # replace old_text with repl_text
            old_text = labelled_lines['line_'+str(repl_line)]
            labelled_lines['line_'+str(repl_line)] = repl_text

            # show user new result
            print("\n\nAt line_{line}:\n\n Replacing old text:\n{old}\n\nWith new text:\n{repl}".format(repl=repl_text, old=old_text, line=repl_line))

            # user chooses whether to save or discard changes made
            if ask_to_save():
                with open(dir_path+"\\"+'short_story.txt', 'r+', encoding='utf8') as h:
                    h.writelines([line for label,line in labelled_lines.items()])
                    h.seek(0)
                    r5 = h.read()

            if ask_next():
                continue

            EDITOR = False
