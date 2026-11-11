Feature: user tests

  Scenario Outline: Run <number> tests as <name>
    Given we are logged in as <name>
    When we implement <number> tests
    Then <name> has run <number> tests
    |number |name |
    | 5     |Bob  |