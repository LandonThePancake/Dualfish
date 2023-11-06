# Dualfish Interpreter

Written by LandonThePancake in Python v3.12.0<br><br>
<img src="dufilogolq.png" alt="dufi" width="250" height="250">

<h2>Info</h2>
Dualfish is an esoteric programming language heavily inspired by the language "deadfish". Dualfish aims to add more to deadfish, while having the goal of making it slightly more interesting <b>(whilst also making no god-damn sense)</b>.
It gets its name from having two INT registers to work with (unlike deadfish, which only has one), hence the name "<b><i>Dual</i></b>fish".
<br>
To get started writing code in dualfish, type 'help' into the interpreter to get a list of commands. You can also continue reading this readme for more detailed explanations.

<h2>Resources</h2>
- <a href="https://github.com/LandonThePancake/Dualfish/releases">The Live Interpreter (the main thing)</a>
<br>
- <a href="https://docs.google.com/spreadsheets/d/1gKh4uDy02_afG1-nugKlWfJaksBMk-j3rqJrQ4MQEzU/edit?usp=sharing">Num To Alph/Symbol Table (used to print text & symbols)</a>
<br>
- <a href="https://www.python.org/downloads/">Python 3.12.0 (not needed for the .exe builds)</a>

<h1>How to use dualfish</h1>
(If you want to run your code in .dufi files, type g into your interpreter and give it the file name. Keep in mind that dualfish ignores spaces and line breaks, so format it however you'd like.)
<br><br>
Dualfish has two INT registers that can be modified to your liking. You can switch between them with the "<" and ">" commands, and clear both of them with "r" (remember "r". it's very useful).<br>
We will start off with the functions that modify the value of said registers, and then move on to the other stuff.
<h2>Math Functions</h2>
Our first set of functions are used to add and subtract 1 from a register. "i" increments a register by 1 and "d" decrements a register. Simple.
<br><br>
<b>Incrementing a register</b>

~~~
INPUT: iii
(register 1 is now equal to 3)
~~~
<br>
<b>Decrementing a register</b>

~~~
INPUT: ddd
(register 1 is now equal to -3)
~~~
<br>
Next, we have "s" and "c", which squares and cubes a register respectively.
<br><br>
<b>Squaring a register</b>

~~~
INPUT: iiis
(register 1 is now equal to 9)
~~~
<br>
<b>Cubing a register</b>

~~~
INPUT: iiic
(register 1 is now equal to 27)
~~~
<br>
There is also a "*" function that multiplies our register by 2.
<br><br>
<b>Doubling a register</b>

~~~
INPUT: iii*
(register 1 is now equal to 6)
~~~
<h2>How to code efficiently with math functions</h2>
The thing that "s","c" and "*" have in common, is that they can all be used to make our code WAY more efficient.
Let's say we want register 1 to equal 26. Sure, we could just type "i" 26 times, or we could do something like this:<br><br>

~~~
INPUT: iii***ii
(register 1 is now equal to 26)
~~~
or:
~~~
INPUT: iiiiisi
(register 1 is now equal to 26)
~~~
or even:
~~~
INPUT: iiicd
(register 1 is now equal to 26)
~~~

Writing code like this is a much faster and better way to get what you want, and is <u><i>practically</i></u> required for when you are outputting out a word. Speaking of output, I think it's a good time to go over that.
<h2>How to output numbers</h2>
Number output is pretty easy in dualfish, I don't think I need to explain this one too much.
<br><br>
"o" outputs the value of your current register
<br>
"0" outputs the value of both registers side by side.
<br><br>
<b>Output with o</b>

~~~
INPUT: iii*do
OUTPUT: 5
~~~
<br>
<b>Output with 0</b>

~~~
INPUT: iii*d0
OUTPUT: [5, 0]
~~~
<h2>How to output letters and symbols</h2>
You're gonna need <b><a href="https://docs.google.com/spreadsheets/d/1gKh4uDy02_afG1-nugKlWfJaksBMk-j3rqJrQ4MQEzU/edit?usp=sharing">this.</a></b>
<br>
The "a" function outputs an alphabetical letter that corresponds to a registers current value. 
<br>So, 1 = a, 2 = b, 3 = c, etc.
<br>Its also worth noting that when you go past 26 (or z), you can find UPPERCASE letters. Just don't go past 52, because that will throw an error.
<br><br>
<b>Alphabet Output with a</b>
<br>

~~~
INPUT: ii**aia
OUTPUT: hi
~~~
<br>
"a" is also used to output symbols. If you use the "^" command, you will go into "symbol-mode", where you have access symbols instead of letters. Its also worth bringing up that "v" will bring you back to "alphabet-mode"
<br><br>
<b>Symbol Output with a</b>
<br>

~~~
INPUT: ^ii*ada
OUTPUT: @!
~~~
<h2>How to use the 2nd register</h2>
So this entire time, we've been talking in the context of using a single register, but using the 2nd register can be very useful in many situations, like outputting long text strings.
<br><br>
The ">" will switch the selected register to register 2, while "<" will switch it back to register 1

~~~
INPUT: ii>iiiio<o
OUTPUT: 42
~~~

<h2>Adding and subtracting registers</h2>
Now that we know how to assign values to each register, we can use "+" and "-" to add and subtract our registers together. The selected register is the one that will be added/subtracted from.
<br><br>
<b>Adding Registers</b>

~~~
INPUT: iiiii>ii<+0
OUTPUT: [7, 2]
(note that reg2 holds its value, even after adding it to reg1)
~~~
<br>
<b>Subtracting Registers</b>

~~~
INPUT: iiiii>ii<-0
OUTPUT: [3, 2]
(note that reg2 holds its value, even after subrtacting it from reg1)
~~~
<h2>Other functions and info</h2>
"r" resets BOTH registers back to 0. This can be used as a shortcut back to the starting point of the register.
<br><br>
<b>Resetting a register</b>
<br>

~~~
INPUT: iii*>ii*r0
Output: [0, 0]
~~~
<br>
"=" is used as the start and end of a comment, it's very useful when you are coding in a file instead of the interpreter
<br><br>
<b>Comments</b>
<br>

~~~
INPUT: iii>i<=dualfish is better than javascript=*0
Output: [6, 1]
~~~
<br>
The last function is the "e" function. it simply closes the application when called.
<br><br>
<b>Exiting The Interpreter</b>
<br>

~~~
INPUT: e
(closes the application)
~~~
<h2>That's all! (probably)</h2>
I'm almost done with this language, and only really need to add input and optimizations to call it done. Good luck learning this shit!
<br>
(Also I may remake this in C at some point, because I don't really think python is the right language for this.)
