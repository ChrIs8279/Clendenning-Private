public class EvenOrOdd {
	public static void main(String[] args) {
		
		System.out.print ("Even or Odd: Enter a number here: ");
			String input = System.console().readLine();
			
		int number = Integer.parseInt(input);
			
		if (number % 2 == 0) {
				System.out.println(number + " is an even number!!!");
			}else{
				System.out.println(number + " is an odd number!!!");
			}
		while (true){
			System.out.print ("0 to exit: Enter another number: ");
			String Second_input = System.console().readLine();
		
			int Another_Number = Integer.parseInt(Second_input);
			
			if (Another_Number == 0) {
				System.out.println("Goodbye, have a good day");
				break;
			}
		
			if (Another_Number % 2 == 0) {
				System.out.println(Another_Number + " is an even number!!!");
			}else{
				System.out.println(Another_Number + " is an odd number!!!");
			}
		}
	}
}