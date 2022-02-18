import java.util.Random;
import java.util.Scanner;

public class Magic8 {
    
    public static void main(String[] args) {
        Random rand = new Random();
        int upperExclusive = 5;
        boolean replay = true;
        
        welcomeMessage();
        while(replay) {
            userQuestionPrompt();
            int randomNum = rand.nextInt(upperExclusive);
            switch(randomNum) {
                case 0: advice00(); break;
                case 1: advice01(); break;
                case 2: advice02(); break;
                case 3: advice03(); break;
                case 4: advice04(); break;
                default: adviceDefault(); break;   
            }
            replay = replayQuestion();
        }
        goodbyeMessage();
    }
    
    
    
    // Messages / prompts
    // - - - - - - - - - -
    
    private static void welcomeMessage() {
        System.out.println(" ______________________________");
        System.out.println("|                              |");
        System.out.println("| Welcome to the Magic 8-Ball! |");
        System.out.println("|______________________________|");
        System.out.println("");
    }
    
    private static void userQuestionPrompt() {
        // Get user input
        Scanner sc = new Scanner(System.in);
        System.out.println("What would you like to ask?");
        System.out.print(">> ");
        String str = sc.nextLine();
        
        // Only proceed when user submits input
        while(str.length() < 1) {
            System.out.println("Sorry, I didn't quite hear you, please try again:\n");
            System.out.print(">> ");
            str = sc.nextLine();
        }
        System.out.println();
        System.out.println("\"" + str + "\", hmm...");
    }
    
    private static boolean replayQuestion() {
        Scanner sc = new Scanner(System.in);
        System.out.println();
        System.out.println("Would you like to ask another question? (Y/N):");
        
        while(true) {
            System.out.print(">> ");
            String str = sc.nextLine();
            String strUpper = str.toUpperCase();
            switch (strUpper) {
                case "Y":
                case "YES":
                    System.out.println();
                    System.out.println(" - - - - -");
                    System.out.println();
                    return true;
                case "N":
                case "NO":
                    return false;
                default:
                    System.out.println("Invalid input.");
                    break;
            }
        }
    }
    
    private static void goodbyeMessage() {
        System.out.println();
        System.out.println("Thank you for playing Magic 8-Ball!");
    }
    
    
    
    // Answer bank
    // - - - - - -
    
    private static void advice00() {
        System.out.println("It would be wise to do so!");
    }
    private static void advice01() {
        System.out.println("Sounds like a great idea!");
    }
    private static void advice02() {
        System.out.println("Definitely!");
    }
    private static void advice03() {
        System.out.println("Don't count on it!");
    }
    private static void advice04() {
        System.out.println("I wouldn't if I were you!");
    }
    private static void adviceDefault() {
        System.out.println("Maybe... that's a tough one!");
    }
}