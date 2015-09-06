package animal;

public class ManadaVirgula extends Manada{

	public ManadaVirgula() {
		super();
	}

	@Override
	public String estourar() {
		String msg = "";
		for (Animal a : animais){
			msg += a.fazerBarulho();
			msg += ",";
		}
		return msg;
		
	}

}