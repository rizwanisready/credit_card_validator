# credit_card_validator
 validator
Check whether the entered credit card number is valid or not.
It must start with a , or .
It must contain exactly digits.
It must only consist of digits (-).
It may have digits in groups of , separated by one hyphen "-".
It must NOT use any other separator like ' ' , '_', etc.
It must NOT have or more consecutive repeated digits.
Valid Credit Card Numbers
4253625879615786
4424424424442444
5122-2368-7954-3214

Invalid Credit Card Numbers
42536258796157867       #17 digits in card number → Invalid 
4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
44244x4424442444        #Contains non digit characters → Invalid
0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid

Input:
Enter your credit card number: 4253625879615786

Output:
Valid
