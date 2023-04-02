package Pull_Variante;

public class client {
    
    public static void main(String[] args) {
        station ws = new station();
        modul_LED signal = new modul_LED(ws);
       
        modul_Monitor m = new modul_Monitor(ws);
        ws.setHum(60.6f);
        ws.setTemp(35.9f);
    }

}
