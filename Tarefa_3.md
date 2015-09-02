package Animais;

public class Animal {
	public String raca;
	public double peso;
	public int idade;
	
	public Animal(String raca, double peso, int idade) {
		super();
		this.raca = raca;
		this.peso = peso;
		this.idade = idade;
	}
	

	public String fazerBarulho(){
		return "Animal faz barulho";
	}

}
