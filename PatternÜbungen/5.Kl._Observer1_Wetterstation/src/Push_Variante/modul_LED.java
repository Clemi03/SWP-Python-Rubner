package Push_Variante;



public class modul_LED implements Observer {
    private station ws;

    public modul_LED(station ws){
        this.ws = ws;
        this.ws.addClient(this);
    }

    
  
    @Override
    public void update(float temp, float hum) {
    	double newTemp = temp;
        double newHumidity = hum;
        
        
        
        if (newTemp <= 30.0f){
            System.out.println("LED_grün");
        }else{
            System.out.println("LED_rot");
        }
        if (newHumidity <= 60.0f){
            System.out.println("LED_grün");
        }else{
            System.out.println("LED_rot");
        }
    }
}