package Proxy;

public class Main {
	
	
 public static void main(String[] args) {
	 
	 Printer printer = new PrinterProxy();
	 ((PrinterProxy) printer).switchToColor();
	 printer.print("Page printed!");
	 ((PrinterProxy) printer).switchToSW();	 
	 printer.print("Page printed!");
}
}
