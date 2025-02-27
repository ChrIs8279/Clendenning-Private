import java.util.Scanner;

public class Divisable {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		while(true){
			
				
			System.out.print ("enter a number you wish to find factors of: ");	
			int number = scanner.nextInt();
				
				if (number == 0) {
					break;
				}
					
				System.out.print("Factors of " + number + " from 1 - 9: ");	
				
			
				for (int i = 1; i <= 9; i++) {
					if (number % i == 0) {
						System.out.print(i + " ");
					}
			}
				System.out.println();
		}
	scanner.close();
	}
}