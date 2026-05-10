public class Main {

    public static void main(String[] args) {

        int totalQuestions = 10;
        int correctAnswers = 0;

        System.out.println("Welcome to the Subtraction Quiz!");

        for (int question = 1; question <= totalQuestions; question++) {

            System.out.println("\nQuestion " + question);

            int[] numbers = ArithematicApp.generateQuestion();

            int firstNumber = numbers[0];
            int secondNumber = numbers[1];

            if (ArithematicApp.askQuestion(firstNumber, secondNumber)) {
                correctAnswers++;
            }
        }

        double finalScore = ArithematicApp.calculateScore(
                correctAnswers,
                totalQuestions
        );

        System.out.println("\nQuiz Finished!");
        System.out.println(
                "Correct Answers: " +
                correctAnswers +
                "/" +
                totalQuestions
        );

        System.out.println(
                "Final Score: " +
                finalScore +
                "%"
        );
    }
}
