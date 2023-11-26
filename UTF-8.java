import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		System.out.println("Veuillez entrer quelque chose");
		String input = scanner.nextLine();
		scanner.close();
		for(int i = 0; i <= input.length(); i++) {
			char lettre = input.charAt(i); 
			int valeurAscii = (int) lettre; 
			String binary = Integer.toBinaryString(valeurAscii);  
			
			if(binary.length() <= 7) {
				System.out.println("0"+binary);
			}
			else if(binary.length() <= 11) {
				for(int j = 0; j <= (11-(binary.length()))+1; j++) {
					binary = "0" + binary;
				}
				System.out.println("110"+binary.substring(0, 5)+" 10"+binary.substring(5));
			}
			else if(binary.length() <= 16) {
				for(int k = 0; k <= (16-(binary.length()))+1; k++) {
					binary = "0" + binary;
				}
				System.out.println("1110"+binary.substring(0, 4)+" 10"+binary.substring(5,9)+" 10"+binary.substring(9));
			}
			else {
				for(int l = 0; l <= (21-binary.length())-1; l++) {
					binary = "0" + binary;
				}
				System.out.println("11110"+binary.substring(0, 3)+" 10"+binary.substring(4,8)+" 10"+binary.substring(8,14)+" 10"+binary.substring(14));
			}
		}
	}
}
