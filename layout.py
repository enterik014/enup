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
        self.root = root
        
        wraplength = self.win_width-10
        frame_context = tk.Frame(root, padx=10, pady=10)
        frame_context.grid(column=0, row=0)
        self.frame_context = frame_context

        question_number = tk.Label(frame_context, text=f'Questão {question.number}', font=('Nunito', 14, 'bold'))
        question_number.pack(anchor='w')
        self.question_number = question_number

        self.context = []
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
            
            self.context.append(label)
        
        statement = tk.Label(frame_context, text=question.statement, font=('Nunito', 12))
        statement.pack(anchor='w', pady=5)
        self.statement = statement

        alternatives_frame = tk.Frame(root, padx=10, pady=10)
        alternatives_frame.grid(column=0, row=1, sticky='w')
        self.altenatives_frame = alternatives_frame

        self.alternatives = []
        index = 0
        for letter in ['a', 'b', 'c', 'd', 'e']:
            path = f'images/{letter}.png'
            letter_image = ImageTk.PhotoImage(Image.open(path).resize((20, 20)))
            button = tk.Button(alternatives_frame, image=letter_image)
            button.grid(row=index)
            index += 1
            self.alternatives.append({
                'image': letter_image,
                'button': button
            })




        root.mainloop()