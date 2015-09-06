package animal;

import java.util.ArrayList;
import java.util.List;

public abstract class Manada {
	
	List<Animal> animais = new ArrayList<Animal>();
	
	public abstract String estourar ();
	
	public void adicionarAnimal (Animal animal){
		this.animais.add(animal);
	}

}
