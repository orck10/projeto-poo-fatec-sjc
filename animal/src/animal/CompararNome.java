package animal;

import java.util.Comparator;
public class CompararNome implements Comparator<Animal> {
		@Override
		public int compare(Animal animal, Animal outroAnimal){
			return animal.nome.compareTo(outroAnimal.nome);
		}
}
