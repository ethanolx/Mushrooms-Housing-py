# Mushrooms - Edible or Poisonous?

|               |   |                       |
|---------------|---|-----------------------|
|   Author      | : |   Ethan Tan Wee En    |
|   Admin No.   | : |   p2012085            |
|   Class       | : |   DAAA/2A/03          |
|   Language    | : |   Python (py)         |
|   Date        | : |   May 2021            |

## Setup

Pipenv is the package/dependency manager of choice

To create a virtual environment with all the required packages (in `.venv`):
1.  Install pipenv locally (using `pip install pipenv`)
2.  Create the virtual environment (using `pipenv install`)
3.  Activate the virtual environment (using `pipenv shell`)

An alternative is to use pip to install the required dependencies from `requirements.txt`

To connect the Jupyter notebook (`ai.ipynb`) to use the above virtual environment,
1.  Change kernel
2.  Select the `.venv` environment

To produce the output,
1.  Select `Run all cells` in ai.ipynb

## File Structure

```
CA1 ---- .venv (empty)
     |
     |-- data ---- agaricus-lepiota.data
     |         |-- agaricus-lepiota.names
     |         `-- kc_house_data.csv
     |
     |-- doc ---- CA1_Brief.pdf
     |        |-- classification-highlights.pptx
     |        |-- regression-highlights.pptx
     |        `-- technical-paper.docx
     |
     |-- models ---- best_clf_algo.p
     |           |-- best_clf_params.p
     |           |-- best_reg_algo.p
     |           |-- best_reg_params_2.p
     |           |-- best_reg_params.p
     |           |-- best_reg_trans.p
     |           |-- best_reg_y_trans.p
     |           |-- final_classifier.p
     |           `-- final_regressor.p
     |
     |-- utils ---- extraction.py
     |          `-- plotting.py
     |
     |-- ai.ipynb
     |-- Pipfile
     |-- Pipfile.lock
     |-- README.md
     `-- requirements.txt
```

# See Also

Part A Slides:  `doc/classification-highlights.pptx`
Part B Slides:  `doc/regression-highlights.pptx`
Part C Paper:   `doc/technical-paper.docx`