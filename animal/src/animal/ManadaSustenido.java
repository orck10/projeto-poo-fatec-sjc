package animal;

public class ManadaSustenido extends Manada{

	public ManadaSustenido() {
		super();
	}
	
	@Override
	public String estourar() {
		String msg = "";
		for (Animal a : animais){
			msg += a.fazerBarulho();
			msg += " # ";
		}
		return msg;
		
	}

}