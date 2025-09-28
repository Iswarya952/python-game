import java.util.*;
public class NumberGuessGame {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random rand = new Random();
        int number = rand.nextInt(100) ;
        int guess = 0, attempts = 0;

        System.out.println(" Welcome to Number Guessing Game!");
        System.out.println("I have chosen a number between 1 and 100. Try to guess it!");

        while (guess != number) {
            System.out.print("Enter your guess: ");
            guess = sc.nextInt();
            attempts++;

            if (guess < number) {
                System.out.println("Too low! Try again.");
            } else if (guess > number) {
                System.out.println("Too high! Try again.");
            } else {
                System.out.println(" Correct! You guessed it in " + attempts + " attempts.");
            }
        }
        sc.close();
    }
}
