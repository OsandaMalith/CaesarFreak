package ceasar;
import java.util.*;
/* Caesar Cipher programmed by Osanda Malith*/
public class ceasar {
	private static String LETTERS = new String("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
	private static Scanner s = new Scanner(System.in);
	
	public static void main(String[] args) {
		System.out.println("[+] Enter your msg: ");
		String msg = s.nextLine();
	
		System.out.println("1. Encrypt\n2. Decrypt\n3. Crack\n");
		int opt = s.nextInt();
		boolean choice;
		switch (opt) {
		case 1:
			choice = true;
			System.out.println(encDec(msg, choice));
			break;
		case 2:
			choice = false;
			System.out.println(encDec(msg, choice));
			break;
		case 3:
			crack(msg);
			break;
		default:
			System.err.println("Enter a 1 or 2");
		}		
	}
	
	private static String encDec(String msg, boolean choice) {
		System.out.println("[+] Enter your Key: "); 
		int key = s.nextInt();
		String trans = "";
		msg = msg.toUpperCase();
		char msg_array[] = msg.toCharArray();
		for (char a : msg_array) {
			if(LETTERS.indexOf(a) != -1) {
				int num = LETTERS.indexOf(a);
				if(choice) num += key;
				else num -= key;
				if (num >= LETTERS.length()) {
					num -= LETTERS.length();
				} else if (num < 0) num += LETTERS.length();
				try { trans += LETTERS.charAt(num); }
				catch (java.lang.StringIndexOutOfBoundsException e) { 
					System.out.println("[!] Enter a key between 0 and 25");
					System.exit(0);}
			} else trans += a;
		}
		return trans;
	}

	
	private static void crack(String msg) {
		msg = msg.toUpperCase();
		char msg_array[] = msg.toCharArray();
		for (int key = 0; key < LETTERS.length(); key++) {
			String trans = "";
			for (char a : msg_array) {
				if(LETTERS.indexOf(a) != -1) {
					int num = LETTERS.indexOf(a);
					num -= key; 
					if (num < 0) num += LETTERS.length();
					trans += LETTERS.charAt(num);
				} else trans += a;
			} 
			System.out.printf("[*] Key ~%d: %s\n", key, trans);
		}
	}
}
