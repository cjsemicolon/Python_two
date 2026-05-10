import java.util.Random;
import java.util.Scanner;

public class ArithematicApp {

    static Random random = new Random();
    static Scanner input = new Scanner(System.in);

    public static int[] generateQuestion() {

        int firstNumber = random.nextInt(20) + 1;
        int secondNumber = random.nextInt(20) + 1;

        if (secondNumber > firstNumber) {
            int temp = firstNumber;
            firstNumber = secondNumber;
            secondNumber = temp;
        }

        return new int[]{firstNumber, secondNumber};
    }

    public static boolean checkAnswer(int firstNumber, int secondNumber, int userAnswer) {

        int correctAnswer = firstNumber - secondNumber;

        return userAnswer == correctAnswer;
    }

    public static boolean askQuestion(int firstNumber, int secondNumber) {

        int attempts = 2;

        while (attempts > 0) {

            System.out.print("What is " + firstNumber + " - " + secondNumber + "? ");

            int answer = input.nextInt();

            if (checkAnswer(firstNumber, secondNumber, answer)) {
                System.out.println("Correct!");
                return true;
            }

            attempts--;

            if (attempts > 0) {
                System.out.println("Wrong answer. Try again.");
            }
        }

        System.out.println("Incorrect.");
        return false;
    }

    public static double calculateScore(int correctAnswers, int totalQuestions) {

        return ((double) correctAnswers / totalQuestions) * 100;
    }
}
