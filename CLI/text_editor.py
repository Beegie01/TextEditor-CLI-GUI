import os

pkg = "C:\\Users\\Welcome\\Desktop\\MyFuncs"
if pkg not in os.sys.path:
    os.sys.path.append(pkg)

from fave_app_funcs import ask_next, file_path_inp

from myio_funcs import read_allfile_content

from text_editorOOP import EditorApp

# TEXT FILE EDITOR APP
editor = EditorApp()

EDITOR = True
while EDITOR:

    # open text file
    path, file, ext = file_path_inp()

    if path in ['', ' ']:
        path = None
    if file in ['', ' ']:
        file = None
    if ext in ['', ' ']:
        ext = None

    file_path = f"{path}\\{file}.{ext}"

    FOUND, text = read_allfile_content(path, file, ext)
    # no file was opened
    if not (FOUND):
        print(f"\nEnter a valid file name!")
        continue

    # store the original text
    editor.original_text = text

    # label each line
    editor.label_lines()
    print("\nLine labels assigned!")

    # select mode menu
    CURRENT_FILE = True
    while CURRENT_FILE:
        # user selects mode from options
        selected_mode = editor.add_or_edit()

        # inserting new lines
        if selected_mode == 'add':
            INSERTING = True
            while INSERTING:

                # display lines of file
                editor.view_file_text()

                editor.insert_lines()

                editor.save_changes(file_path)
                print("\n\nInserted row has been saved to system file!")

                # insert another row???
                prompt = "\nTo insert another line, enter 'y'\nTo stop, enter 'n'"
                if ask_next(prompt):
                    continue

                # insert mode turned off
                INSERTING = False

                # reselect mode with current file???
                prompt = "\nTo continue with the current file enter yes,\nTo stop working with current file, enter no"
                if ask_next(prompt):
                    continue

                # current mode off
                CURRENT_FILE = False

                # open another file or exit app???
                prompt = "\nTo open a different file, enter yes\nTo exit app, enter no"
                if not (ask_next(prompt)):
                    # exit the app
                    print("\n\nNow exiting TextEditorApp....")
                    EDITOR = False
                    quit()

                # open another file
                continue

        # update old rows/lines with new text
        else:

            UPDATING = True
            while UPDATING:

                # display lines of file
                editor.view_file_text()

                row_num, repl_text = editor.update_lines()

                # show user new result
                edited_text = [('line_' + str(row_num), repl_text)]
                old_text = [('line_' + str(row_num), editor.labelled_text['line_' + str(row_num)])]
                print(
                    "\n\nAt line_{line}:\n\nDo you want to update\nOld text:\n{old}\n\nWith \nNew text:\n{repl}".format(
                        repl=repl_text, old=old_text[0][1], line=row_num))

                # confirm whether to go ahead
                prompt = '\nTo save to file, enter yes\nTo continue without saving enter no'
                if not (ask_next(prompt)):
                    continue

                # replace old_text with repl_text
                editor.old_text.extend(old_text)
                editor.edited_text.extend(edited_text)
                editor.labelled_text['line_' + str(row_num)] = repl_text

                editor.save_changes(file_path)
                print(f"\n\n{editor.edited_text[0][0]} has been updated!")

                # update another row???
                prompt = "\nTo update another row, enter yes\nTo stop update, enter no"
                if ask_next(prompt):
                    continue

                # update mode turned off
                UPDATING = False

                # reselect mode with current file???
                prompt = "\nTo continue with the current file, enter yes,\nTo stop with the current file, enter no"
                if ask_next(prompt):
                    continue

                # current mode off
                CURRENT_FILE = False

                # open another file or exit app???
                prompt = "\nTo open a different file, enter yes\nTo exit app, enter no"
                if not (ask_next(prompt)):
                    # exit the app
                    print("\n\nNow exiting TextEditorApp....")
                    EDITOR = False
                    quit()

                # open another file
                continue