const fs = require('fs');

// First we read the input file and convert it to an array of strings
const input = fs.readFileSync('./day2input.txt').toString().split('\n')

// Part 1

const passwordParser = passwords => {
    // We initialize a counter to keep track of the number of valid passwords
    let numValid = 0
    // Now we can take each line and parse it using regex
    passwords.forEach(line => {
        let [fullString, lowest, highest, char, password] = /(\d+)-(\d+) ([a-z]): (.*)/.exec(line)
        min = parseInt(lowest)
        max = parseInt(highest)
        // Convert password string to an array of letters
        password = [...password]
        // Calculate the number of times the relevant letter appears in the password
        numChar = password.filter(letter => letter === char).length
        // Check if it satisfies the password policy requirements
        if (numChar <= max && numChar >= min) {
            // If it does, increment our counter
            numValid++
        }
    })
    console.log(numValid)
}

passwordParser(input) // Output: 460 (correct!)

// Part 2
const passwordParser2 = passwords => {
    // We initialize a counter to keep track of the number of valid passwords
    let numValid = 0
    // Now we can take each line and parse it using regex
    passwords.forEach(line => {
        let [fullString, lowest, highest, char, password] = /(\d+)-(\d+) ([a-z]): (.*)/.exec(line)
        min = parseInt(lowest)
        max = parseInt(highest)
        let firstCharCorrect = false
        let secondCharCorrect = false
        // Check if characters at the given indices match the given letter
        if (password.charAt(min - 1) === char) {
            firstCharCorrect = true
        }
        if (password.charAt(max - 1) === char) {
            secondCharCorrect = true
        }
        if (firstCharCorrect !== secondCharCorrect) {
            // If they do, we increment our counter
            numValid++
        }
    })
    console.log(numValid)
}

passwordParser2(input) // Output: 251 (correct!)