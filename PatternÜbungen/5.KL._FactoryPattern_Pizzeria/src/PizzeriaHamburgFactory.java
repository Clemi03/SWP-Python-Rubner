
class PizzeriaHamburgFactory extends Pizzeria{

	@Override
	protected Pizza createPizza(String name) {
		Pizza pizza = null;
		if(name.equals("Hawaii")) {
			pizza = new PizzaHawaii();
		}else if(name.equals("Salami")){
			pizza = new PizzaSalami();
		}else if(name.equals("Calzone")){
			pizza = new PizzaCalzone();
		}else if(name.equals("QuattroStagioni")){
			pizza = new PizzaQuattroStagioni();
		}else if(name.equals("HamburgHawaii")){
			pizza = new PizzaHamburgHawaii();
		}else {
			System.out.println("Ungültig!");
		}
		return pizza;
	}

}
