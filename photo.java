import java.awt.Robot;
import java.awt.event.KeyEvent;

public class photo{
	
	public photo(){

	}

	public static void main(String[] args){
		System.out.println("lol");
		try{
			Robot r = new Robot();
			r.keyPress(KeyEvent.VK_ENTER);
		}
		catch(Exception e){

		}
	}
}