# Module to create widgets revealing exercise solutions.
# Example use in a notebook:
#
# import show_solutions
# show_solutions.show('week01_ex1')
#
# Shows an accordion menu to reveal/hide solutions tagged with 'week01_ex1'
# in the solutions script 'week0weektes1_solutions.txt'.

import ipywidgets as widgets
from IPython.display import display, Code, Markdown
import json, os

def parse_txt_solution(week, solution_id):
    try:
        solution_id = solution_id.strip("\n").strip()
        out_buffer = str()
        with open(os.path.join('common', 'hints_solutions', "week{:02d}_solutions.txt".format(week)), 'r') as j:
            start_read = False
            for line in j.readlines():
                if start_read:
                    if line.strip("\n").strip() == "{}_end".format(solution_id):
                        break
                    else:
                        out_buffer += line 
                if line.strip("\n").strip() == solution_id:
                    start_read = True
        return out_buffer
    except Exception:
        print("Could not find any solution for this question")

def parse_json(week, question):
    with open(os.path.join('common', 'hints_solutions', "week{:02d}_hints_solutions.json".format(week)), 'r') as j:
        data = json.loads(j.read())
        return data[question]
    
def generate_hint():
    return widgets.Output(layout={'border': '1px solid blue'})

def show(week, question):
    '''
    Displays solution to a particular question.
    
    Input:
    question (str): string of the form 'weekXX_exY'
    '''

    question_ans = parse_json(week, str(question))

    # Create output area for the solution
    hint_areas = []
    hint_titles = []
    sol_area = widgets.Output(layout={'border': '2px solid green'})

    # Set the data
    solution = parse_txt_solution(week, question_ans['solution'])
    if question_ans['typeCode'] == True:
        sol_area.append_display_data(Code(data=solution, language="python3"))
    else:
        sol_area.append_display_data(Markdown(data=solution))
    for hint_title, hint in question_ans['hints'].items():
        hint_titles.append(hint_title.capitalize())
        hint_area = generate_hint()
        hint_area.append_display_data(Markdown(data=hint))
        hint_areas.append(hint_area)

    # Create Hints Accordion
    hint_acc = widgets.Accordion(children=hint_areas, selected_index=None)
    for num, hint_title in enumerate(hint_titles):
        hint_acc.set_title(num, hint_title)
        
    # Create Solution Accordion
    solution_acc = widgets.Accordion(children=[sol_area], selected_index=None)
    solution_acc.set_title(0, 'Reveal Solution')

    # Create Tabs
    tab_nest = widgets.Tab()
    tab_nest.children = [hint_acc, solution_acc]
    tab_nest.set_title(0, 'Hints')
    tab_nest.set_title(1, 'Solution')

    display(tab_nest)

#show(week=1, question=1)