<!DOCTYPE html>
<html>
<head>
    <title>FC by YZFARGO</title>
    <style>
        body {
            font-family: Arial, bold;
            margin: 20px;
        }

        h1 {
            color: black;
            text-align: center;
            font-size: 28px;
        }

        .factorial-section {
            margin-bottom: 20px;
            padding: 20px;
            background-color: white;
            border-radius: 1px;
            text-align: center;
        }

        .factorial-section h2 {
            color: black;
            margin-top: 0;
            font-size: 24px;
        }

        .factorial-section p {
            margin-bottom: 20px;
            font-size: 20px;
        }

        .factorial-section form {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }

        .factorial-section input[type="number"] {
            padding: 8px;
            width: 150px;
            font-size: 18px;
        }

        .factorial-section button {
            padding: 10px 16px;
            background-color: pink;
            color: black;
            border: solid;
            border-radius: 1px;
            cursor: pointer;
            font-size: 18px;
        }

        .factorial-section button:hover {
            background-color: pink;
        }

        .result {
            font-weight: bold;
            font-size: 20px;
        }
    </style>
</head>
<body>
    <h1>FACTORIAL CALCULATOR</h1>

    <div class="factorial-section">
        
        <form method="POST">
            <input type="number" name="number" placeholder="yzfargo :3" required>
            <button type="submit">CALCULATE</button>
        </form>

        <?php
        function calculateFactorial($number) {
            $factorial = 1;

            if ($number >= 0) {
                for ($i = 1; $i <= $number; $i++) {
                    $factorial *= $i;
                }

                return $factorial;
            } else {
                return "Please enter a non-negative integer.";
            }
        }

        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $number = $_POST['number'];
            $result = calculateFactorial($number);
            echo '<p class="result">Factorial of ' . $number . ' is: ' . $result . '</p>';
        }
        ?>
    </div>
</body>
</html>
