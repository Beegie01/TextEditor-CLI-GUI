import os, re

pkg = "C:\\Users\\Welcome\\Desktop\\MyFuncs"
if pkg not in os.sys.path:
    os.sys.path.append(pkg)

# print(os.sys.path)
from fave_app_funcs import num_inp, sentence_inp, ask_to_save, ask_next, file_path_inp


class EditorApp:

    def __init__(self):
        self.original_text = None   # for original text
        self.labelled_text =  None   # for original text with labelled lines
        self.old_text = []   # for discarded rows/lines
        self.inserted_text = []   # for inserted new rows/lines
        self.edited_text = []   # for replacement rows/lines


    def label_lines(self):
        '''
        gives a label to each line of text
        assigns the result to labelled text attribute
        '''
        # label each lines
        self.labelled_text = {'line_'+str(ind):line for ind,line in enumerate(self.original_text)}
        print("\nLine labels assigned!")



    def view_file_text(self):
        '''
        labels and displays each line contained in the file_text
        file_text is a list of strings
        each string corresponds to a line of text
        '''
        # display lines of file
        for label,text in self.labelled_text.items():
            print("{l}:\t{t}\n".format(t=text, l=label))


    def add_or_edit(self):
        '''
        '''
        acc_range = ['add', 'edit']
        prompt = "\n\nEnter 'edit' to replace a line of text\n\nEnter 'add' to insert more text\nEDIT/ADD LINE>\t"
        while True:
            inp = input(prompt)

            if inp.lower() not in acc_range:
                print("\nEntry is Out of Range!")
                continue
            return inp.lower()


    def insert_lines(self):
        '''
        '''
        while True:

            # user inputs the new text
            prompt = "\nEnter new text below\nInsert Text>\t"
            insr_text = sentence_inp(prompt)

            # determine the next line number
            # collecting the last lines
            line_ind = re.findall(r"\d+", ', '.join([label for label in self.labelled_text.keys()]))
            last_line = sorted([eval(ind) for ind in line_ind])[-1]

            print(f"\n{dict(['line_'+str(last_line+1), insr_text])} Entered!")
            prompt = "\nEnter yes to save inserted text\nOr no to discard insertion"
            if not(ask_next(prompt)):
                continue

            # insert text at next line number
            self.labelled_text['line_'+str(last_line+1)] = insr_text

            # store changes
            self.inserted_text.append(('line_'+str(last_line+1), insr_text))
            break

    def save_changes(self, file_path):
        '''
        '''
        with open(file_path, 'r+', encoding='utf8') as hand:
            hand.writelines([line for label,line in self.labelled_text.items()])

        print("\n\nChanges has been saved to system file!")
