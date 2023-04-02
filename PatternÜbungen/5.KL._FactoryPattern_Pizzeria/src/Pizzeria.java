
public abstract class Pizzeria {

	public Pizza pizzaBekommen(String name) {
		Pizza p = createPizza(name);
		
		p.backen();
		p.schneiden();
		p.verpacken();
		
		return p;
	}
	
	protected abstract Pizza createPizza(String name);
	
}
