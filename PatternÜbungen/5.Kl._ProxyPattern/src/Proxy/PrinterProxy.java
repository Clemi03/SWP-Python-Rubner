package Proxy;

public class PrinterProxy implements Printer {
	 private Printer swPrinter;
	   private Printer colorPrinter;
	   private Printer currentPrinter;
	   
	   public PrinterProxy() {
	      swPrinter = new SWPrinter();
	      colorPrinter = new ColorPrinter();
	      currentPrinter = swPrinter;
	   }
	   
	   public void switchToSW() {
	      currentPrinter = swPrinter;
	   }
	   
	   public void switchToColor() {
	      currentPrinter = colorPrinter;
	   }
	   
	   public void print(String text) {
	      currentPrinter.print(text);
	   }
	}

