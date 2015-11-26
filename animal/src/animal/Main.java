package animal;

import java.util.Collections;

public class Main {

	public static void main(String[] args) {
		Manada mana = new ManadaVirgula();
		Manada mana2 = new ManadaSustenido();
		
		mana.adicionarAnimal(new Gato("Manda Chuva","Persa", 7.5, 2));
		mana.adicionarAnimal(new Cachorro("Xuxu","Bull Dog", 15.4, 3));
		mana.adicionarAnimal(new Animal("Batatinha","Mangalarga", 150.0, 5));
		
		mana2.adicionarAnimal(new Cachorro("Betovem","Pastor Canadense", 15.4, 3));
		mana2.adicionarAnimal(new Gato("Lecie","Ragdoll", 5.5, 2));
		mana2.adicionarAnimal(new Animal("Napoleão","Shire", 16.0, 5));
		
		System.out.println("\n Ordenar por peso\n");
		Collections.sort(mana2.animais);
		for(Animal a : mana2.animais)
		{
			System.out.println(a+"\n");
		}
		
		System.out.println("\n Ordenar por nome\n");
		CompararNome nomes = new CompararNome();
		Collections.sort(mana.animais,nomes);
		for(Animal a: mana.animais)
		{
			System.out.println(a+"\n");
		}
		
		System.out.println(mana.estourar());
		
		System.out.println(mana2.estourar());
	}

}

