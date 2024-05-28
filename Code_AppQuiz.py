from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from collections import OrderedDict

root = Tk()
root.title("Заголовок окна квиза")
root.iconbitmap("pics/icon.ico")
root.geometry('700x700+610+50')
root['bg'] = '#8A6642'
root.resizable(width=False, height=False)

# Data for quiz
questions = [
    'Вопрос № 1: {Текст вопроса}?',
    'Вопрос № 2: {Текст вопроса}?',
    'Вопрос № 3: {Текст вопроса}?',
    'Вопрос № 4: {Текст вопроса}?',
    'Вопрос № 5: {Текст вопроса}?',
    'Вопрос № 6: {Текст вопроса}?',
    'Вопрос № 7: {Текст вопроса}?',
    'Вопрос № 8: {Текст вопроса}?',
    'Вопрос № 9: {Текст вопроса}?',
    'Вопрос № 10: {Текст вопроса}?',
    'Вопрос № 11: {Текст вопроса}?',
    'Вопрос № 12: {Текст вопроса}?',
    'Вопрос № 13: {Текст вопроса}?',
    'Вопрос № 14: {Текст вопроса}?',
    'Вопрос № 15: {Текст вопроса}?',
    'Вопрос № 16: {Текст вопроса}?',
    'Вопрос № 17: {Текст вопроса}?',
    'Вопрос № 18: {Текст вопроса}?',
    'Вопрос № 19: {Текст вопроса}?',
    'Вопрос № 20: {Текст вопроса}?'
    ]

a_options, a = OrderedDict(), 'a_options.txt'
b_options, b = OrderedDict(), 'b_options.txt'
c_options, c = OrderedDict(), 'c_options.txt'

def generator(dict_options, file_path):
    with open(file_path, 'r', encoding='utf-8') as simple_dict:
        simple_list = simple_dict.read().splitlines()
    for i in range(len(simple_list)):
        if i % 2 == 0:
            dict_options[simple_list[i]] = simple_list[i+1]
    dict_keys = list(dict_options.items())
    return dict_keys

a_keys = generator(a_options, a)
b_keys = generator(b_options, b)
c_keys = generator(c_options, c)

img_list = [
    'pics/1.png',
    'pics/2.png',
    'pics/3.png',
    'pics/4.png',
    'pics/5.png',
    'pics/6.png',
    'pics/7.png',
    'pics/8.png',
    'pics/9.png',
    'pics/10.png',
    'pics/11.png',
    'pics/12.png',
    'pics/13.png',
    'pics/14.png',
    'pics/15.png',
    'pics/16.png',
    'pics/17.png',
    'pics/18.png',
    'pics/19.png',
    'pics/20.png'
    ]

screen_counter = 0
quest_counter = 0
points = 0

def destroy_grid(*args):
    for i in args:
        i.pack_forget()

def welcome_screen():
    def start_game():
        destroy_grid(congrats,welcome,task,button_start)
        question_gen()

    congrats = Label(root,text='С Днем рождения, {Имя}!', font=('Helvetica', 20, 'bold'),background='#800000', fg='white')
    welcome = Label(root,text='Ну что, давай проверим, насколько хорошо ты разбираешься в собственной жизни.',font=('Helvetica', 20, 'bold'),background='#A95AEC', fg='white', wraplength=500)
    task = Label(root, text='За правильный ответ (он только один) ты увидишь "Правильно", за неправильный "Неправильно". Для горизонтального скролла зажимай Shift. От твоих результатов зависит итоговое обращение автора. Попытки не ограничены. Удачи!',font=('Helvetica', 20, 'bold'),background='#A95AEC', fg='white',wraplength=500)
    button_start = Button(root, text='Начать', width=15,height=1, font=('Helvetica', 20, 'bold'),bg='#800000',fg='white', command=lambda: start_game())
    
    congrats.pack(anchor='center', pady=30)
    welcome.pack(anchor='center', pady=20)
    task.pack(anchor='center', pady=40)
    button_start.pack(anchor='center', pady=20)

# Main function
def question_gen():
    def next_answer(x):
        global screen_counter
        global quest_counter
        destroy_grid(question,box_options,button_next,picture)
        if screen_counter % 2 == 0:
            screen_counter += 1
            quest_counter += 1
            answer_gen(x)
        else:
            screen_counter += 1
            quest_counter += 1
            question_gen()

    # creating a widgets
    question = Label(root,text=questions[quest_counter],font=('Helvetica', 18, 'bold'),background='#800000', fg='white', wraplength=700)
    options = [a_keys[quest_counter][0], b_keys[quest_counter][0], c_keys[quest_counter][0]]
    scrollbar = Scrollbar(root)
    box_options = Listbox(root,height=3,width=100,selectmode=SINGLE,bg='#A95AEC',font=('Helvetica', 18, 'bold'), selectbackground='#800000', fg='white', xscrollcommand=scrollbar.set)
    button_next = Button(root, text='Далее', width=10,height=1, font=('Helvetica', 25, 'bold'),bg='#800000',fg='white', command=lambda:next_answer(box_options.get(ANCHOR)) if len(box_options.get(ANCHOR)) > 0 else messagebox.showinfo(title='Ошибка', message='Пожалуйста, выбери вариант ответа'))
    for i in options:
        box_options.insert(END,i)

    # creating an image
    image = Image.open(img_list[quest_counter])

    if image.width == image.height:
        image = image.resize((380, 380))
        image = ImageTk.PhotoImage(image)
        picture = Label(root, image=image, width=350, height=350, bg='#8A6642')

    elif image.width + 20 == image.height:
        image = image.resize((round(image.width/image.height*350), 350))
        image = ImageTk.PhotoImage(image)
        picture = Label(root, image=image, width=round(image.width()/image.height()*350), height=350, bg='#8A6642')
    
    elif image.width < image.height:
        image = image.resize((round(image.width/image.height*450), 450))
        image = ImageTk.PhotoImage(image)
        picture = Label(root, image=image, width=350, height=400, bg='#8A6642')

    elif image.width < 440:
        image = image.resize((440, round(image.height/image.width*440)))
        image = ImageTk.PhotoImage(image)
        picture = Label(root, image=image, width=440, height=round(image.height()/image.width()*440), bg='#8A6642')

    else:
        image = image.resize((round(image.width/image.height*300), 300))
        image = ImageTk.PhotoImage(image)
        picture = Label(root, image=image, width=400, height=350, bg='#8A6642')
    
    picture.image = image

    # placing widgets
    question.pack(pady=20)   
    box_options.pack(padx=20, pady=20)   
    picture.pack(side=LEFT,padx=50)
    button_next.pack(side=RIGHT, padx=20)

def answer_gen(x):
    global points
    global screen_counter
    def next_question():
        global screen_counter
        destroy_grid(answer,button_next)
        if screen_counter == 39:
            final_screen()
        else:
            screen_counter += 1
            question_gen()
    if x.startswith('а'):
        answer = Label(root, text=a_options[x],font=('Helvetica', 20, 'bold'),background='#A95AEC', fg='white', wraplength=500)
        if a_options[x].startswith('Правильно'):
            points += 1
    elif x.startswith('б'):
        answer = Label(root, text=b_options[x],font=('Helvetica', 20, 'bold'),background='#A95AEC', fg='white', wraplength=500)
        if b_options[x].startswith('Правильно'):
            points += 1
    elif x.startswith('в'):
        text=c_options[x]
        answer = Label(root, text=c_options[x],font=('Helvetica', 20, 'bold'),background='#A95AEC', fg='white', wraplength=500)
        if c_options[x].startswith('Правильно'):
            points += 1
    
    button_next = Button(root, text='Далее', width=10,height=1, font=('Helvetica', 25, 'bold'),bg='#800000',fg='white', command=lambda:next_question())
    answer.pack(anchor='center', pady=40)
    button_next.pack(side=RIGHT, padx=20)
    print(screen_counter, quest_counter, points)

def final_screen():
    global screen_counter, quest_counter, points
    def restart():
        destroy_grid(result,comment,button_finish,picture)
        question_gen()

    result = Label(root, text='Поздравляю, ты набрал(а) ' + str(points) + ' из 20 баллов',font=('Helvetica', 20, 'bold'),background='#800000', fg='white',width=35,height=2)
    
    comments_dict = {
        0:'{Текст обращения на 0 баллов}',
        1:'{Текст обращения на 1 балл}',
        2:'{Текст обращения на 2 балла}',
        3:'{Текст обращения на 3 балла}',
        4:'{Текст обращения на 4 балла}',
        5:'{Текст обращения на 5 баллов}',
        6:'{Текст обращения на 6 баллов}',
        7:'{Текст обращения на 7 баллов}',
        8:'{Текст обращения на 8 баллов}',
        9:'{Текст обращения на 9 баллов}',
        10:'{Текст обращения на 10 баллов}',
        11:'{Текст обращения на 11 баллов}',
        12:'{Текст обращения на 12 баллов}',
        13:'{Текст обращения на 13 баллов}',
        14:'{Текст обращения на 14 баллов}',
        15:'{Текст обращения на 15 баллов}',
        16:'{Текст обращения на 16 баллов}',
        17:'{Текст обращения на 17 баллов}',
        18:'{Текст обращения на 18 баллов}',
        19:'{Текст обращения на 19 баллов}'
    }
    
    if points == 20:
        comment = Label(root, text='{Текст обращения на 20 баллов}',font=('Helvetica', 20, 'bold'),background='#A95AEC', fg='white',width=35,height=2)
        image = Image.open('pics/final.png')
        image = image.resize((300, 400))
        image = ImageTk.PhotoImage(image)
        picture = Label(root, image=image, height=375,width=375, bg='#8a6642')
        picture.image = image
        button_finish = Button(root, text='Попробовать еще раз', width=20,height=1, font=('Helvetica', 20, 'bold'),bg='#800000',fg='white', command=lambda: restart())
        
        result.pack(anchor='center',ipady=5,pady=10)
        comment.pack(anchor='center')
        picture.pack(anchor='center', pady=20,padx=15)
        button_finish.pack(pady=20, padx=25)

    else:
        comment = Label(root, text=comments_dict[points],font=('Helvetica', 20, 'bold'),background='#A95AEC', fg='white',width=35,height=5, pady=10, wraplength=500)
        button_finish = Button(root, text='Попробовать еще раз', width=20,height=1, font=('Helvetica', 20, 'bold'),bg='#800000',fg='white',command=lambda: restart())
        result.pack(anchor='center',ipady=5,pady=10)
        comment.pack(anchor='center')
        picture = Label(text=None)
        button_finish.pack(anchor='s', pady=90, padx=25)
    
    screen_counter, quest_counter, points = 0, 0, 0

welcome_screen()

root.mainloop()