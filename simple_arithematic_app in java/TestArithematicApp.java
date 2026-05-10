// FunctionsTest.java

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class TestArithematicApp {

    @Test
    public void testGenerateQuestionNoNegative() {

        int[] numbers =ArithematicApp.generateQuestion();

        assertTrue(numbers[0] >= numbers[1]);
    }

    @Test
    public void testCheckAnswerCorrect() {

        assertTrue(
                ArithematicApp.checkAnswer(10, 5, 5)
        );
    }

    @Test
    public void testCheckAnswerIncorrect() {

        assertFalse(
                ArithematicApp.checkAnswer(10, 5, 3)
        );
    }

    @Test
    public void testCalculateScore() {

        assertEquals(
                80.0,
                ArithematicApp.calculateScore(8, 10)
        );
    }

    @Test
    public void testCalculateScoreZero() {

        assertEquals(
                0.0,
                ArithematicApp.calculateScore(0, 10)
        );
    }
}
