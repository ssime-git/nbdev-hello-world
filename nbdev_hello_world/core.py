# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['question', 'option1', 'submit_button', 'foo', 'check_answer']

# %% ../nbs/00_core.ipynb 3
def foo(): pass

# %% ../nbs/00_core.ipynb 5
import ipywidgets as widgets

question = widgets.HTML(value="Quelle est la capitale de la France?")
option1 = widgets.RadioButtons(options=["Paris", "Londres", "Berlin"])
submit_button = widgets.Button(description="Soumettre")

def check_answer(button):
    if option1.value == "Paris":
        print("Bonne réponse!")
    else:
        print("Mauvaise réponse.")

submit_button.on_click(check_answer)

display(question, option1, submit_button)
