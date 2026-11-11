# Behave Features

Behave is a type of "Behavior Driven Development" framework.

What this means if that first we difine the behavior we would
like to see - in a reader friendly, systematic way - and the 
development follows from each step of that behavior. So a specific 
flow through a web app, say, for a login process, would be broken
down as a `scenario`, within a `feature file`, within the 
"features directory".

## Feature Steps

In Behave we are concerned with steps in 2 high-level ways:
1. Feature steps, defined in the feature file, and
2. Step functions, defined in ./steps/*_steps.py.

Here, we are concerned with **feature steps**.

### Given, When, Then

Each step has a step type of [ given | when | then ].
This is because BDD follows a system to keep it tidy, readable, and easily understood:

- Given: this is the circumstance we need to find ourselves in before we can test what we came here to test.
- When: the thing we *do* - the activity under test in a given moment.
- Then: the ***RESULT*** of a `When` step -- our validation that the action, or the expected result of the action, occurred as expected.

Example:

```behave
Feature: Admin workflows

    Scenario: Log in as the admin user
        Given we are logged in as the admin
        When we open the admin settings
        Then the admin settings are displayed
```

In the example above, we have a given feature step, a when feature step, and a then feature step. A then follows a when, and a when follows a given. With few exceptions, good BDD features will have only 1 given at the beginning and 1 Then at the end, with as many when steps as needed. Keep your features orderly to prevent difficult maintenance!

#### The 'Step' Step

There is one other type of feature step:
The generic `step` feature step.

This distinction is more important when used in step logic functions in `./steps/*`, but suffice to say that "step" steps can be used as any of the other types when written as a feature file step.

## Scenario Outlines

Whereas scenarios are defined with `Scenario: summative, descriptive text`, scenario outlines are defined with `Scenario Outline: summative, descriptive text with {variables}`, and are followed by a table of variations to use within that outline. The scenario runs once for each row in the table, except for the top row (which serves as column headers)

### Example

This scenario will run once for Bob and once for the Admin user:

```
Feature: user tests

  Scenario Outline: Run <number> tests as <name>
    Given we are logged in as <name>
    When we implement <number> tests
    Then <name> has run <number> tests
    | number | name  |
    | 5      | Bob   |
    | 7      | Admin |
```
:robot: