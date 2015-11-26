package animal;

public class Animal implements Comparable<Animal>{
	public String nome;
	public String raca;
	public double peso;
	public int idade;
	
	public Animal(String nome, String raca, double peso, int idade) {
		super();
		this.nome = nome;
		this.raca = raca;
		this.peso = peso;
		this.idade = idade;
	}
	
	public String fazerBarulho(){
		return "Animal faz barulho";
	}
	
	@Override
	public String toString()
	{
		return "Nome: "+nome +" Raça: "+raca + " Peso: " + peso + " Idade: " + idade;
	}
	
	@Override
	public int compareTo(Animal o)
	{
		if(this.peso < o.peso)
			return -1;
		if(this.peso > o.peso)
			return 1;
		return 0;
	}

}

