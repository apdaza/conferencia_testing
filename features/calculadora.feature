Feature: The calculator

Scenario Outline: Get sum total
  Given a <values> to sum
  When the calculator sums the values
  Then the <total> of sum is correct

  Examples: values
  | values         | total |
  | 5,7            | 12    |
  | 5,3            | 8     |
  | 15,33          | 48    |
  | 33,15          | 48    |
  | 23,10          | 33    |
  | 12,-4          | 8     |

Scenario Outline: Get substraction total
  Given a <values> to substract
  When the calculator substract the values
  Then the <total> of substraction is correct

  Examples: values
  | values          | total |
  | 5,7             | -2    |
  | 5,3             | 2     |
  | 115,30          | 85    |

Scenario Outline: Get times total
  Given a <values> to Multiply
  When the calculator multiply the values
  Then the <total> of multiply is correct

  Examples: values
  | values          | total |
  | 5,7             | 35    |
  | 5,3             | 15    |


Scenario Outline: Get divide total
  Given a <values> to Divide
  When the calculator divide the values
  Then the <total> of divide is correct

  Examples: values
  | values          | total |
  | 15,3            | 5     |
  | 15,2            | 7     |
  | 14,0            | None  |