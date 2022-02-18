let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:

function generateTarget() {
    let target = Math.floor(Math.random()*10);
    return target;
}

function compareGuesses(human, computer, target) {
    let humanDistance = getAbsoluteDistance(human, target);
    let computerDistance = getAbsoluteDistance(computer, target);
    return humanDistance <= computerDistance;
}

function updateScore(player) {
    switch(player) {
        case "human": humanScore++; break;
        case "computer": computerScore; break;
    }
}

function advanceRound() {
    currentRoundNumber++;
}

function getAbsoluteDistance(guess, target) {
    return Math.abs(target-guess);
}