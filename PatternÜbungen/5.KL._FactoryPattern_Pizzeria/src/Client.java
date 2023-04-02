
public class Client {

	public static void main(String[] args) {
		Pizzeria berlinPizzeria = new PizzeriaBerlinFactory();
		Pizza berlinPizzeriaHawaii = berlinPizzeria.pizzaBekommen("Hawaii");
		
		//TODO: Fixen falsche eingabe
		Pizzeria hamburgPizzeria = new PizzeriaHamburgFactory();
		Pizza hamburgPizzeriaSalami = hamburgPizzeria.pizzaBekommen("Salami");
	}

}
