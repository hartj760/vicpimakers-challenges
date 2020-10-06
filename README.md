# [VicPiMakers.ca](https://vicpimakers.ca) Coding Challenge
One of our [vicpimakers.ca](https://vicpimakers.ca) community members posed a fun
programming challenge to the group. The requirement is to build a program that takes
a list of integers as input and runs through a series of math and transformation
exercises to test your coding skills. Your choice of programming language.

Original Challenge: https://vicpimakers.ca/projects/programming-challenges/

I've posted this to GitHub to encourage our community to share their code.
Since we're officially in the month of
[Hacktoberfest](https://hacktoberfest.digitalocean.com/), I'm hoping we can
encourage a few brave souls to participate.  :-)

## Challenge Summary
The challenge consists of 1 input and 10 outputs. For the purpose of self-
evaluation, use the point system below:

| tests           | score    |
|:----------------|:---------|
| Output #1 - #5  | 3 points |
| Output #6 - #10 | 2 points |

### General Input
* 12, byte-size integers each ranging in value from 33 to 255 inclusive.

### Test Input
* 72,111,63,85,61,56,118,121,61,69,63,61

### Test Output
```
Output #1: 941 (sum)
Output #2: 78,5 (average of the 12 values leaving an integer quotient, remainder)
Output #3: 72,56,118 (even integers)
Output #4: 56,6 (smallest, position)
Output #5: 5,61,61,61,63,63 (#repeats, list)
Output #6: 18543 (value of new 16-bit integer)
** the 1st 2 elements of the input data (72,111) are used to define a new
   16-bit integer where 72 is the high byte and 111 the low byte
Output #7: 56,61,61,61,63,63,69,72,85,111,121 (sorted)
Output #8: Ho?U=8vy=E?=
** Hint: derived from Output #7
Output #9: HOUVYE (upper case)
Output#10: Key (1 <= key <= 26)
** “HOUVYE “(Output #9) is a coded word for “BIOPSY’ that has been encrypted
    using the Caesar Cipher. The Key unknown. Decipher “HOUVYE” to produce
    “BIOPSY’. Output #10 is the numerical value of Key.
```

### Notes
* The text enclosed in brackets or with leading "**" may be omitted.
* The outputs can be in any order.
* Data shown below is separated by commas. Any other delimiter can be used.
* Lightly edited from the original challenge for readability.

## Submissions To Date
| file              | requirements  | instructions            | notes                |
|:------------------|:--------------|:------------------------|:---------------------|
| jims_challenge.py | python3       | `$ python3 jims_challenge.py <list_of_integers>`<br/>Example:<br/> `$ python3 python/jims_challenge.py \` <br/> `"72,111,63,85,61,56,118,121,61,69,63,61"` | work in progress     |

## TODOs
* Add a general test runner.
* Add a python code example.
* Add CI support.
* Present this to the [vicpimakers.ca](https://vicpimakers.ca) community and
encourage submissions!
