console.log("heyamram")
// alert("Helllo Creature!")
// prompt("Helllo")  same as pop up but it can take an input

/*
let a;          // here we only declare
let a = 26;     // here we declare and initialize(assigned value first time)
                    but we can't declare let twice only var can do
                    var added in window but let couldn't
a = 26;  

✅symble - unique immutable object
    let u1 = Symbol("uid");
    let u2 = Symbol("uid");          u1 === u2 -> False


✅dynamic typing - data ko change kr sakte hai becoz data type is dynamic

✅type coercion - one data tupy auto convert ho jayega.
    "2" + 1 = 21    (concatenation)
    "2" - 1 = 1

✅Truthy and falsy value;     check in console - !!0
    0
    false
    ""
    Null
    undifined
    NaN (not a number is actually a type of number)
    document.all

✅operator - arithmatic, comparion, logical, unary, ternary   
    ✳️Arithmetic operator 
        (+ - / * ** %) 

    ✳️comparison operator 
        ==  (only value check karta hai, not a strict comparision) 
        === (left and right equality check karta hai)
        12 == "12"   -> true
        12 === "12"  -> false

    ✳️logical operator - combine multiple condition
        && - and operator (one false = false)
        || - or operator (one true = true)
        ! - not operator (oposite - truthy or falsy)

    ✳️unary operator - used on a operand
        let a = "12"
         console.log(+a) -> "12" converted to a number
        let a = 12;
            ++a = 13  -> (pre increase)...just next value
            a++ = 12  -> (post increase ie. next time "a++"=13
            a++ = a  -> 13 + 12 = 25
            a-- = 12
            a-- = 10 -> 11 - 10 = 1

    ✳️ternary operator - shorthand for if...else
        12>13 ? console.log("is con is true then i ") : console.log("else me");
            # if codition is true then first part excuted if false then 2nd.
        in general :-
            condition ? valueifTrue : value if false

✅control flow - like at traffic signal
    ✳️if else else-if
        let marks = 78;
        if (marks >= 90){
            console.log("grade A")
        } else if (marks >= 74){
            console.log("grade B")
        } else{
            console.log("C");    
        }

    ✳️switch-case - one variable against many values
                - clean way to write long if-else lists
        let fruit = "apple"
        switch (fruit){
            case "banana":
                console.log("yellow")
                break;
            case "applle":
                console.log("red")
                break;
            default:
                console.log("unknown") 
        }

    ✳️early return pattern - exit early if some cindition fails.
        function checkAge(age) {
            if (age < 18) return "denied";
            else return "allowed"
        }

✌️Qn. Get user to input a number using prompt("Enter a number :- ")
    and check the is multiple of 5 or not.

    if (num % 5 === 0){
        console.log(num, "is multiple of 5")
    } else {
        console.loh(num, "is not multiple of 5")
    }
    let num = prompt("Enter your number :- ");


✌️Qn. Write a function getGrade(score) that:
        * takes astudent's marks (0 to 100)
        * returns the grade based on this logic
            90-100 = A+
            80-89 = A
            70-79 = B
            60-69 = c
            33-59 = D
            0-32 = fail           
Ans.
M1.
    function checkGrade(score){
        if (score >= 90 && score <= 100){
            return "grade A+"
        } else if (score >=80 && score < 90){
            return "grade A" 
        } else if (score >=70 && score < 80){
            return "grade B"
        } else if (score >=60 && score < 70){
            return "grade C"
        } else if (score >=33 && score < 60){
            return "grade D"
        } else if (score >=0 && score < 33){
            return "failed"
        }
    }
M2. - Earle return pattern
    function checkGrade(score){
        if (score >= 90 && score <= 100) return "A+";
        if (score >= 80 && score <= 89) return "A";
        if (score >= 70 && score <= 79) return "B";
        if (score >= 60 && score <= 69) return "C";
        if (score >= 33 && score <= 59) return "D";
        if (score >= 0 && score <= 32) return "FAIL";
        return "invalid marks ❌"   
    } 

✌️Q2. Create rock paper scisor (RPS) logic
Ans.
    function rps(user, computer){
        if (user === computer) return "draw";
        if (user === "rock" && computer === "scissor") return "user";
        if (user === "paper" && computer === "stone") return "user";
        if (user === "scissor" && computer === "paper") return "user";
        return "computer";
    }
    console.log(rps("scissor", "rock"));

🙋‍♂️✌️LOOPS the OG- for loop = kaha se -> kaha tak -> kaise jana hai
            - while loop = kaha se -> kaise jana hai -> kab rukna hai
            - do-while loop
            - break and continue
            - for-of - Arrays & Strings
            - forEach - arrays
            - for-in - Objects(and arrays if needed)

    ✳️ for loop - 
        for (let i = 1; i < 101; i++){
            console.log(i);
        }
        result - 1 to 100 printed in console.

    ✳️ while loop -
        start;
        while(end){
            code
            change
        }

        let i = 0
        while (i < 21){
            console.log(i);
            i++
        }

    ✳️ break and continue -
        for (let i = 1; i < 9; i++){
            if (i === 3) continue;
            console.log(i);  //skip 3 then continue            
        }

        for (let i = 1; i < 100; i++){
            console.log(i);
            if(i === 32) break  //used to search anythng in three list
        }
    ✳️ do-while loop - condition last me check hoti hai...
                     - one time to loop chalega
        let i = 1
        do {
            console.log("i =", i);
            i++;
        } while (i <= 5);   // 1 to 5 printed

    ✳️ for-of loop - array & String

        for(let char of "heyamram"){
            console.log(char);
        }

        let str = "heyamram"
        let count = 0
        for(let char of str){
            console.log("char = ", char);     // here it print heyamram
            count++
        }  
        console.log("count = ", count);   // here it print size = 8 

    ✳️ for-in loop - objects (and arrays if needed)

        let student = {
            name: "HeyAmRam",
            age: 29,
            cgpa: 9.2,
        }
        for(let key in student){
            console.log("key =", key,",value = ", student[key])
            console.log(key, student[key])
        }       
    
    
✌️Qn. Print 10 to 1
    for(let i = 10; i > 0; i--){
        console.log(i)
    }

    let i = 10;
    while (i > 0){
        console.log(i)
        i--;
    }
✌️Qn. calculate sum of 1 to 10
    let sum = 0
    for(let i = 1; i < 11; i++){
        sum = sum + i;       
    }
    console.log("sum = ",sum);

✌️Qn. Print even number between 1 to 20
    for (let i = 1; i < 21; i++ ){
        if (i % 2 === 0){
            console.log(i);
        }
    }

✌️Qn. Reverse a string using loop
    for (let i = "heyamram"; )

✌️Qn. Sum of all numbers in an array


✌️Qn. Guess number game -use while to ask until correct
    let gameNum = 33;
    let userNum = prompt("guess the number :-");
    while (userNum != gameNum){
        userNum = prompt("Oh sorry you entered wromg number...try again");
    }
    console.log("congratulations, you entered the right number");
    

✌️Qn. Print triangle using *


✅ String in js...
    let str = "heyamram"
        console.log(str.length)
        console.log(str[0], str[1], str[7])

✅ Template literal in JS - special string
    let sentance = `hello everyone myself Ram.Right now i am studying computer science.`
    console.log(sentance.length)

    \n -> next line
    \t -> tab space
    let str = "Revision\ntube"
    console.log(str)

    ✅string interpolation - to create string by doing substitution of placeholder.

    let object = {
        name: "Dhruv",
        class: "2nd",
        roll_no: 10,
    }
    console.log(`hello myself ${object.name}, roll number is ${object.roll_no} and studying in class ${object.class}`);

✅  str.toUpperCase
    str.toLowerCase
    str.trim
    str.slice(start, end?)
    str1.concat(str2)
    str.replace(searchVal, newVal)
    str.replaceall
    str.charAt(idx)

        let str = "hello Ram";           
        str = str.toUpperCase();        //string is immutable in js - we have to make copy
        console.log(str);   

        let str = "helloRam"
        console.log(str.slice(0,8));     //printed helloRam

        let str1 = "hey"
        let str2 = "amaRam" 
        console.log(str1.concat(str2));

        let str1 = "helllo worrld"
        console.log(str1.replace("worr", "go"))     //hello gold

✌️Qn. prompt the user to enter their full name and generate the username for them
      start username with @, followed by their fulllname and ending with the fullname length.
      like heyamram -> @heyamram8

    let fName = prompt("enter your full name :- ")
    let userName = "@" + fName + fName.length;
    console.log(userName)

✅ Arrays in js - store multiple value (num,str,obj,fun) in single variable
                - special type of object in which key is index but its inbuild 
    let marks = [89, 87, 93, 23, 56, 75];
    let fruits = ["guava", "apple", "pear", "chiku"]
    let info = ["ram", 29, delhi];   //we can store diff type of value but we don't preffer it

    string - immutable
    arrys - mutable

    marks[3] = 32   // updated index 3 : 23 with 32
    ✅ Iteration (looping) in array
        for(let idx = 0; idx < arr.length; idx++){          //we preffer i instead of idx
            my programme;
        }

        let marks = [89, 87, 93, 23, 56, 75];       // normal for
        for(let i = 0; i < marks.length; i++){
            console.log(marks[i])
        }

        let marks = [89, 87, 93, 23, 56, 75];       // for-of loop
        for(let num of marks){
            console,log(num)
        }

        let cities = ["patna", "delhi", "ludhiana", "goa"];
        for (let city of cities){
            console.log(city.toUpperCase());
        }

    ✳️ Iteration methods in array
        ➡️ map()
            


✌️Qn. for a given array with marks of students -> [85, 97, 44, 37, 76, 60]. find avg marks.
    ✳️-> normal for loop
    let marks = [85, 97, 44, 37, 76, 60]
    let sum = 0
    for (let i = 0; i < marks.length; i++){
        sum += marks[i]
    }
    console.log("avg = ", (sum/marks.length)) 

    ✳️-> for-of loop -> directly targetting value not through index.
    let marks = [85, 97, 44, 37, 76, 60]
    let sum = 0
    for(let i of marks){
        sum += i
    }
    console.log("avg = ", (sum/marks.length)) 

    ✳️-> Gave some respect
    let marks = [85, 97, 44, 37, 76, 60]
    let sum = 0
    for(let value of marks){
        sum += value
    }
    let avg = sum/marks.length;
    console.log(`the avg marks of the students = ${avg}`);

✌️Qn. For a given array with price of 5 items -> [250,645,300,900,50].
      all items have an offer of 10% off.
      change the array to store final price after applying offer.
    ✳️
    let items_price = [250,645,300,900,50];
    for(let i = 0; i < items_price.length; i++){
        let offer = items_price[i] / 10;
        items_price[i] -= offer;
    }
    console.log(items_price);

    ✳️
    let items_price = [250,645,300,900,50];
    let key = 0;
    for(let i of items_price){
       let offer = i / 10; 
       items_price[key] = items_price[key] - offer;
       console.log(`value after offer = ${items_price[key]}`)
       i++;
    }  



*/
  


