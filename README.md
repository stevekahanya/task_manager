Task Management SystemA modular Python-based productivity application designed to help users track their tasks and monitor their completion progress.
This project demonstrates the use of packages, modules, and input validation using Python's datetime and math logic.
 Project StructureTo ensure the package imports work correctly, the project should be organized as follows:Plaintext.
├── main.py                 # Entry point of the application
└── task_manager/           # Package folder
    ├── __init__.py         # Required to treat the folder as a package
    ├── task_utils.py       # Core logic for task manipulation
    └── validation.py       # Input validation functions
 FeaturesTask Creation: Add tasks with a title, description, and due date.Data Validation:Ensures titles and descriptions are not empty.Validates that dates follow the YYYY-MM-DD format.Status Tracking: Mark specific tasks as "Complete" to update your workflow.Progress Monitoring: Calculates your completion percentage using the following logic:$$\text{Progress \%} = \left( \frac{\text{Completed Tasks}}{\text{Total Tasks}} \right) \times 100$$Pending View: Filter the list to show only tasks that still need attention.
Installation & Usage
1. PrerequisitesEnsure you have Python 3.6+ installed on your machine.
2. SetupCreate a folder for your project.Inside that folder, create the task_manager directory.Place task_utils.py, validation.py, and an empty __init__.py inside the task_manager folder.Place main.py in the root (outside the task_manager folder).
3. Running the AppExecute the following command in your terminal:Bashpython main.py
Module DescriptionsModuleResponsibilitymain.pyHandles the user interface (CLI) and menu loop.task_utils.pyManages the list of task dictionaries and performs calculations.validation.pyContains logic to check the integrity of user input.# task_manager
