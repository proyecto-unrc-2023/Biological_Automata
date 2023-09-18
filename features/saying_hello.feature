Feature: Saying Hello

  Scenario: Run a simple test
    Given we have flask working
    When we hit the root path
    Then we see the Hello World regard