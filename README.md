# Dualfish Interpreter

Written by LandonThePancake in Python v3.12

<h2>Info</h2>
Dualfish is a esoteric programming language heavily inspired by another language named "deadfish". This language aims to add more to deadfish with the goal of making it slightly more interesting (whilst also making no god damn sense). 'Dual'fish gets its name from having two registers to work with instead of just one like deadfish. It really doesn't take rocket science to find out where the 'fish' part came from, so don't ask.
<br><br>
This is my first interpreter, and it definitely shows with how the code is structured, But im pretty proud of what i was able to pull off.

<h2>How to make something in Dualfish</h2>
<i>you can type 'help' in the interpreter for a list of functions</i><br><br>
So you wanna make something in Dualfish? Are you SURE you have nothing else you should be doing? No responsibilities to take care of? Alright then,
<br>
In Dualfish you have these things called "registers", two to be exact. Both of these hold a INT that start at 0 that can be modified to your liking. you can freely switch between these with the "<, >" commands, but I'll go over that a bit more later.
<h2>i and d</h2>
"i" stands for increment and adds 1 to the register, while "d" stands for decrement and subtracts 1 to the register.
<br><br>
<b>Increment</b>
  
~~~
Input: iiio
(register 1 will equal 3)
~~~
<br>
<b>Decrement</b>

~~~
Input: dddo
(register 1 will equal -3)
~~~

<h2>s and c</h2>
"s" stands for square, and squares the current register
"c" stands for cube, and cubes the current register
<br><br>
<b>Squaring</b>

~~~
Input: iiiiso
(register 1 will equal 16)
~~~
<br>
<b>Cubing</b>

~~~
Input: iiiico
(register 1 will equal 64)
~~~
<h2>o, and 0</h2>
"o" stands for output, and outputs the value of the selected register. "0" doesnt stand for anything, but will display the value of both registers.
<br><br>
<b>o</b>

~~~
Input: iiisdo
Output: 8
~~~
<br>
<b>0</b>

~~~
Input: iiisd0
Output: [8, 0]
~~~
<h2>a</h2>
<i>(you may need this: https://i.pinimg.com/736x/39/c7/11/39c71180679b0e5fa358fecc8d6c2682.jpg)</i><br>
"a" stands for alphabet, and is a bit more complicated than the other functions. It outputs an alphabetical letter, corresponding to a registers current INT value. So 1 = a, 2 = b, 3 = c, etc... Once you break past 26, you get to capital letters. So 27 = A, 28 = B, 29 = C etc... And past 52, it crashes the interpreter! (I'll fix it later)

~~~
Input: iiiiiiiiaia
Output: hi
~~~

<h2>< and ></h2>
"<" switches the current register to 1, and ">" sets it to register 2.

~~~
Input: iiii>iiiii0
Output: [4, 5]
~~~
<h2>*</h2>
"*" simply doubles the value of the current register

~~~
Input: iii*o
Output: 6
~~~

<h2>+ and -</h2>
"+" adds the value from the unselected register to the selected one, and "-" subtracts the value of the unselected register from the selected one. 
<br><br>
<b>Adding</b>

~~~
Input: ii>iiii+0
Output: [2, 6]
~~~
<br>
<b>Subtracting</b>

~~~
Input: >iiii<iiiii-0
Output: [1, 4]
~~~

<h2>f</h2>
"f" flips a registers positive and negative signs. It's also not in the help command for some reason. (I'll fix it later)

~~~
Input: iiifo
Output: -3
~~~

<h2>r</h2>
"r" resets the value of BOTH registers back to 0

~~~
Input: iiiii>iiiiir0
Output: [0, 0]
~~~

<h2>Hello World</h2>
I'm not really going to teach you how to pull off a hello world, because I would be here forever if I did. but rather I'll show you the smallest "hello world" program i've made so far so you can get an idea on how the code is structured.

~~~
Input: iic**iiarii*ia>iii*i<+aa>dddd<+a>dddaiiiciiiiiii<+ariiii**da>iii<+a>*<-arii*a
Output: Hello World
~~~
<h1>Whats to come?</h1>
I dont plan on expanding this language too much more, but I'd love to add a form of input, as well as a way to read dualfish files. But yeah, I think thats everything. Have fun!
