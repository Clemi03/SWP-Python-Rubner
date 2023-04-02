package Pull_Variante;

public class modul_LED implements Observer {
    private station ws;

    public modul_LED(station ws){
        this.ws = ws;
        this.ws.addClient(this);
    }

    @Override
    public void update() {
        double newTemp = ws.getTemp();
        double newHumidity = ws.getHum();
        
        
        if (newTemp <= 35.0f){
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