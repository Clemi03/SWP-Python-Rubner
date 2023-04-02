package Pull_Variante;

import java.util.ArrayList;
import java.util.List;

public class station implements Observable {

    private List<Observer> observerList = new ArrayList<>();

    private float temp;
    private float hum;    

    @Override
    public void addClient(Observer client) {
        this.observerList.add(client);
    }

    @Override
    public void deleteClient(Observer client) {
        this.observerList.remove(client);
    }

    @Override
    public void tellAll() {
        for (Observer observer : observerList){
            observer.update();
        }
    }

    	
    public double getHum() {
        return hum;
    }

    public void setHum(float hum) {
        this.hum = hum;
        this.tellAll();
    }
    
    
    public double getTemp() {
        return temp;
    }

    public void setTemp(float temp) {
        this.temp = temp;
        this.tellAll();
    }

  
}