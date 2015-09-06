package animal;

public class Main {

	public static void main(String[] args) {
		Manada mana = new ManadaVirgula();
		Manada mana2 = new ManadaSustenido();
		
		mana.adicionarAnimal(new Gato("Persa", 7.5, 2));
		mana.adicionarAnimal(new Cachorro("Bull Dog", 15.4, 3));
		mana.adicionarAnimal(new Animal("Mangalarga", 150.0, 5));
		
		mana2.adicionarAnimal(new Gato("Ragdoll", 5.5, 2));
		mana2.adicionarAnimal(new Cachorro("Pastor Canadense", 15.4, 3));
		mana2.adicionarAnimal(new Animal("Shire", 160.0, 5));
		
		System.out.println(mana.estourar());
		
		System.out.println(mana2.estourar());
	}

}
