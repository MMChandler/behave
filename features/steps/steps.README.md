# Behave Steps

Steps are the logic behind the easily readable feature files (../*.feature).
Each line in a feature file calls a function defined in the step files.

### For example:

"Given we have behave installed", as a feature step, corresponds to

```bdd
@given('we have behave installed')
```

in 'example_steps.py'.

---

## Reusable Step Functions

For steps that are potentially resuable across multiple features: 
1. Extract the logic into a separate function in `step_utilities.py` 
2. Write the step function in `common_steps.py`
3. Use the @step decorator to register it as a generic step rather 
   than specifying it as [given | when | then].
4. Import `common_steps.py` when slight variations on the same step are 
   needed in a feature-specific step file:

```python
from steps import common_steps as CS
.
.
.
@step("we do the thing")
def do_the_thing():
    CS.some_function_in_common_steps()
``` 
:robot: