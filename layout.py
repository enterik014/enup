import questions
import tkinter as tk
from PIL import ImageTk, Image

class ENEMpopup():
    def __init__(self):
        self.win_width = 700
    
    def show(self, question: questions.Question):
        root = tk.Tk()
        root.title('ENEM popup')
        root.minsize(self.win_width, 0)
        self._gui = {}
        self._gui['root'] = root
        
        wraplength = self.win_width-10
        frame_context = tk.Frame(root, padx=10, pady=10)
        frame_context.grid(column=0, row=0)
        self._gui['frame_context'] = frame_context

        question_number = tk.Label(frame_context, text=f'Questão {question.number}', font=('Nunito', 14, 'bold'))
        question_number.pack(anchor='w')
        self._gui['question_number'] = question_number

        self._gui['context'] = []
        for i in question.context:
            text = i.get('text')
            label = None

            match i.get('type'):
                case 'title':
                    label = tk.Label(frame_context, text=text, font=('Nunito', 15, 'bold'))
                    label.pack(anchor='w')
                case 'text':
                    label = tk.Label(frame_context, wraplength=wraplength, text=text, font=('Nunito', 12))
                    label.pack()
                case 'source':
                    label = tk.Label(frame_context, wraplength=wraplength, text=text, font=('Nunito', 6))
                    label.pack(anchor='e')
                case 'image':
                    image = ImageTk.PhotoImage(Image.open(i.get('file_path')))
                    label = tk.Label(frame_context, image=image)
                    label.pack()
            
            self._gui['context'].append(label)
        
        statement = tk.Label(frame_context, text=question.statement, font=('Nunito', 12))
        statement.pack(anchor='w', pady=5)
        self._gui['statement'] = statement

        alternatives_frame = tk.Frame(root, padx=10, pady=10)
        alternatives_frame.grid(column=0, row=1, sticky='w')
        self._gui['altenatives_frame'] = alternatives_frame

        second_alternatives_frame = tk.Frame(root, padx=10, pady=10)
        second_alternatives_frame.grid(column=1, row=1, sticky='w')
        self._gui['second_alternatives_frame'] = second_alternatives_frame

        self._gui['alternatives'] = []
        for index in range(5):
            root.update_idletasks()
            print(root.winfo_width())

            alternative = question.alternatives[index]
            index += 1

            letter_path = f'images/{alternative['letter']}.png'
            letter_image = ImageTk.PhotoImage(Image.open(letter_path).resize((20, 20)))
            button = tk.Button(alternatives_frame, image=letter_image)
            button.grid(row=index)
            label = None
            question_image = None

            if alternative['text']:
                label = tk.Label(self._gui['altenatives_frame'], text=alternative.get('text'), font=('Nunito', 12), wraplength=wraplength)
                label.grid(row=index, column=2, sticky='w')

            if alternative['file_path']:
                question_image = ImageTk.PhotoImage(Image.open(alternative['file_path']))
                label = tk.Label(self._gui['altenatives_frame'], image=question_image)
                label.grid(row=index, column=2, sticky='w')

            self._gui['alternatives'].append({
                'letter_image': letter_image,
                'button': button,
                'question_image': question_image,
                'label': label
            })

        root.mainloop()