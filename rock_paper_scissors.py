<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rock Paper Scissors</title>
    <style>
        body {
            font-family: sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f4f4f4;
        }

        .#game-container {
            text-align: center;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        button {
            padding: 10px 20px;
            margin: 5px;
            font-size: 16px;
            cursor: pointer;
        }

        #result {
            margin-top: 20px;
            font-weight: bold;
        }

        #score {
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div id="game-container">
        <h1>Rock Paper Scissors</h1>
        <button id="rock">Rock</button>
        <button id="paper">Paper</button>
        <button id="scissors">Scissors</button>
        <div id="result"></div>
        <div id="score">Player: 0, Computer: 0</div>
    </div>

    <script>
        const choices = ["rock", "paper", "scissors"];
        let playerScore = 0;
        let computerScore = 0;

        function getComputerChoice() {
            return choices[Math.floor(Math.random() * choices.length)];
        }

        function determineWinner(playerChoice, computerChoice) {
            if (playerChoice === computerChoice) {
                return "tie";
            } else if (
                (playerChoice === "rock" && computerChoice === "scissors") ||
                (playerChoice === "paper" && computerChoice === "rock") ||
                (playerChoice === "scissors" && computerChoice === "paper")
            ) {
                return "player";
            } else {
                return "computer";
            }
        }

        function updateScore() {
            document.getElementById("score").textContent = `Player: ${playerScore}, Computer: ${computerScore}`;
        }

        function playRound(playerChoice) {
            const computerChoice = getComputerChoice();
            const winner = determineWinner(playerChoice, computerChoice);
            const resultDiv = document.getElementById("result");

            resultDiv.textContent = `You chose ${playerChoice}, computer chose ${computerChoice}. `;

            if (winner === "player") {
                resultDiv.textContent += "You win!";
                playerScore++;
            } else if (winner === "computer") {
                resultDiv.textContent += "Computer wins!";
                computerScore++;
            } else {
                resultDiv.textContent += "It's a tie!";
            }

            updateScore();
        }

        document.getElementById("rock").addEventListener("click", () => playRound("rock"));
        document.getElementById("paper").addEventListener("click", () => playRound("paper"));
        document.getElementById("scissors").addEventListener("click", () => playRound("scissors"));

        updateScore(); // Initial score display.

    </script>
</body>
</html>