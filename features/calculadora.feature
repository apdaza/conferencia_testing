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

Scenario Outline: Get substraction total
  Given a <values> to substract
  When the calculator substract the values
  Then the <total> of substraction is correct

  Examples: values
  | values          | total |
  | 5,7             | -2    |
  | 5,3             | 2     |
  | 115,30          | 85    |

